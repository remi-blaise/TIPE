from lib.inject_arguments import inject_arguments
import pygame as pg


class Keys:
    """Manage keys"""
    
    @inject_arguments
    def __init__(self, config):
        for key in ('action', 'jump', 'left', 'right', 'down', 'quit'):
            setattr(self, key, False)
        
        self.event_dispatcher = self.config.event_dispatcher
        if self.event_dispatcher:
            self.event_dispatcher.listen('action', self.handle_dispatched_event)
        
        self.pressed_keys = None
        self.dispatched_events = []
        self.dispatched_keys = set()
        
        self.keys = ('action', 'jump', 'left', 'right', 'down')
        self.pg_keybinding = {
            'action': pg.K_SPACE,
            'jump': pg.K_UP,
            'left': pg.K_LEFT,
            'right': pg.K_RIGHT,
            'down': pg.K_DOWN
        }
    
    @inject_arguments
    def get_keys(self, current_frame):
        if self.config.allow_control:
            self.get_keys_from_pg()
        if self.event_dispatcher:
            self.get_keys_from_dispatcher()
        # each key = pressed key or dispatched key
        for key in self.keys:
            setattr(self, key, self.pressed_keys and bool(self.pressed_keys[self.pg_keybinding[key]]))
        for key in self.dispatched_keys:
            setattr(self, key, True)
    
    def get_keys_from_pg(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit = True
            elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                self.pressed_keys = pg.key.get_pressed()
    
    def get_keys_from_dispatcher(self):
        self.dispatched_keys = set()
        for action in self.dispatched_events:
            if self.current_frame < action.start_frame + action.duration:
                self.dispatched_keys.add(action.key)
            else:
                self.dispatched_events.remove(action)
    
    def handle_dispatched_event(self, action):
        """Handle events dispatched by the event dispatcher"""
        
        def jumpInDispatchedEvents():
            for action in self.dispatched_events:
                if action.key == 'jump':
                    return True
            return False
        # Si on vient de sauter ou si un jump a déjà été émis (notamment ce tour-ci)
        if action.key == 'jump' and (self.jump or jumpInDispatchedEvents()):
            return False
        
        self.dispatched_events.append(action)
