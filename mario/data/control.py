__author__ = 'justinarmstrong'

from lib.inject_arguments import inject_arguments
from . import setup
import pygame as pg
from .keys import Keys


class Control(object):
    """Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to States as needed. Logic for flipping
    States is also found here."""
    
    @inject_arguments
    def __init__(self, config):
        self.screen = pg.display.get_surface() # Represents the image
        self.done = False
        self.clock = pg.time.Clock()        # La clock fournie par pg
        self.fps = config.fps
        self.get_fps = 60
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
        # get_fps = self.clock.get_fps()
        # if get_fps:
        #     self.get_fps = get_fps
        
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
        self.keys.get_keys(self.current_frame)
        self.done = self.keys.quit

    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(setup.ORIGINAL_CAPTION)
    
    def main(self):
        """Main loop for entire program"""
        while not self.done:
            self.event_loop()           # Récup les events
            self.update()               # Update le jeu (passe les infos du jeu au State)
            pg.display.update()         # Update l'image
            self.clock.tick(self.fps)   # Gère la fin de la frame :
                                            # calcule combien de temps s'est écoulé depuis le début de la frame
                                            # puis l'allonge de sorte à respecter le framerate (fps)
            if self.show_fps: # (anecdotique)
                caption = pg.display.get_caption()[0]
                if not 'FPS' in caption:
                    with_fps = caption + " - {} FPS".format(int(self.get_fps))
                    pg.display.set_caption(with_fps)
        
        return self.state.persist


