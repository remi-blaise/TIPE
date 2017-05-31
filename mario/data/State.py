from lib.inject_arguments import inject_arguments
from . import constants as c


class _State(object):   # Classe abstraite pour les States
    """Abstract class for States"""
    
    @inject_arguments
    def __init__(self, config, get_fps):
        self.start_frame = 0.0
        self.current_frame = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}
    
    def start_game(self):
        """To be executed only once at the game launch"""
        self.persist = {
            c.COIN_TOTAL: 0, # Default persist
            c.SCORE: 0,
            c.LIVES: 3,
            c.TOP_SCORE: 0,
            c.CURRENT_FRAME: 0.0,
            c.LEVEL_STATE: None,
            c.CAMERA_START_X: 0,
            c.MARIO_DEAD: False,
            'time': 401 # Useless, overwrited on OverheadInfo's __init__
        }
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
