__author__ = 'justinarmstrong'

from .setup import setup
from .control import Control
from .states import main_menu,load_screen,level1
from . import constants as c


def main(config):
    """Add states to control here."""
    setup(config)
    
    control = Control(config)
    
    # Instanciation des States
    state_dict = {c.LEVEL1: level1.Level1(config, control.get_fps)}
    if config.show_game_frame:
        state_dict.update({
            c.MAIN_MENU: main_menu.Menu(config, control.get_fps),
            c.LOAD_SCREEN: load_screen.LoadScreen(config, control.get_fps),
            c.TIME_OUT: load_screen.TimeOut(config, control.get_fps),
            c.GAME_OVER: load_screen.GameOver(config, control.get_fps)
        })
    
    # Config du premier State
    if config.show_game_frame:
        control.setup_states(state_dict, c.MAIN_MENU)
    else:
        control.setup_states(state_dict, c.LEVEL1)
    
    # Doit renvoyer le persist
    return control.main()
