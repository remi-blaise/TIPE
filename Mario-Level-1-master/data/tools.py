__author__ = 'justinarmstrong'

from lib.inject_arguments import injectArguments
import os
import pygame as pg
from . import constants as c


class Control(object):
    """Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to States as needed. Logic for flipping
    States is also found here."""
    
    @injectArguments
    def __init__(self, caption, config):
        self.screen = pg.display.get_surface() # Represents the image
        self.done = False
        self.clock = pg.time.Clock()        # La clock fournie par pg
        self.fps = config.fps
        self.show_fps = config.show_fps
        self.current_frame = 0.0
        self.keys = Keys(self.config)
        self.state_dict = {}                # Dict des States
        self.state_name = None              # Nom du State actuel
        self.state = None                   # State actuel
    
    def setup_states(self, state_dict, start_state):    # Initialise
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
        self.state.start_game()
    
    def update(self):   # Update les infos de cet objet, met fin au jeu si besoin, passe les infos au State
        # self.current_time = pg.time.get_ticks() # Return the number of millisconds since pygame.init() was called.
        self.current_frame += 1
        
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_frame)
        # 2e Interaction avec le State : update propagé à tous les components
    
    def flip_state(self):   # Passe d'un State à un autre, basé sur state.next
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_frame, persist)
        self.state.previous = previous
    
    def event_loop(self):   # Écoute les events de pg
        self.keys.get_keys()
        self.done = self.keys.quit

    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)
    
    def main(self):
        """Main loop for entire program"""
        while not self.done:
            self.event_loop()           # Récup les events
            self.update()               # Update le jeu (passe les infos du jeu au State)
            pg.display.update()         # Update l'image
            self.clock.tick(self.fps)   # Gère la fin de la frame :
                                            # calcule combien de temps s'est écoulé depuis le début de la frame
                                            # puis l'allonge de sorte à respecter le framerate (fps)
            # if self.show_fps: # (anecdotique)
            #     fps = self.clock.get_fps()
            #     with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
            #     pg.display.set_caption(with_fps)
        
        return self.state.persist


class Keys:
    """Manage keys"""
    
    @injectArguments
    def __init__(self, config):
        for key in ('action', 'jump', 'left', 'right', 'down', 'quit'):
            setattr(self, key, False)
        
        self.event_dispatcher = self.config.event_dispatcher
        if self.event_dispatcher:
            self.event_dispatcher.listen('action', self.handle_dispatched_event)
        
        self.pressed_keys = None
        self.dispatched_events = []
        
        self.pg_keybinding = {
            'action':pg.K_SPACE,
            'jump':pg.K_UP,
            'left':pg.K_LEFT,
            'right':pg.K_RIGHT,
            'down':pg.K_DOWN
        }
        
        self.get_keys()
    
    def get_keys(self):
        if self.config.allow_control:
            self.get_keys_from_pg()
        if self.event_dispatcher:
            self.get_keys_from_dispatcher()
    
    def get_keys_from_pg(self):
        self.pressed_keys = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit = True
            elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                self.pressed_keys = pg.key.get_pressed()
        
        if self.pressed_keys is not None:
            for key in ('action', 'jump', 'left', 'right', 'down'):
                setattr(self, key, bool(self.pressed_keys[ self.pg_keybinding[key] ]))
    
    def get_keys_from_dispatcher(self):
        for key in self.dispatched_events:
            setattr(self, key, True)
        self.dispatched_events = []
    
    def handle_dispatched_event(self, action):
        """Handle events dispatched by the event dispatcher"""
        self.dispatched_events.append(action.key)


class _State(object):   # Classe abstraite pour les States
    """Abstract class for States"""
    
    @injectArguments
    def __init__(self, config):
        self.start_frame = 0.0
        self.current_frame = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}
    
    def start_game(self):
        """To be executed only once at the game launch"""
        self.persist = {c.COIN_TOTAL: 0, # Default persist
                   c.SCORE: 0,
                   c.LIVES: 3,
                   c.TOP_SCORE: 0,
                   c.CURRENT_FRAME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_START_X: 0,
                   c.MARIO_DEAD: False}
        if not self.config.show_game_frame:
            self.persist[c.LIVES] = 1
        self.startup(0.0, self.persist)

    # def get_event(self, event):
    #     pass

    def startup(self, current_frame, persistant):
        self.persist = persistant
        self.start_frame = current_frame

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_frame):
        pass



def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_fonts(directory, accept=('.ttf')):
    return load_all_music(directory, accept)


def load_all_sfx(directory, accept=('.wav','.mpe','.ogg','.mdi')):  # SFX = Spécial EFFECTS = sounds
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects











