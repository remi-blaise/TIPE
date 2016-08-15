__author__ = 'justinarmstrong'

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c


def main(config):
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION, config)
    
    # Instanciation des States
    state_dict = {c.LEVEL1: level1.Level1(config, run_it.get_fps)}
    if config.show_game_frame:
        state_dict.update({
            c.MAIN_MENU: main_menu.Menu(config, run_it.get_fps),
            c.LOAD_SCREEN: load_screen.LoadScreen(config, run_it.get_fps),
            c.TIME_OUT: load_screen.TimeOut(config, run_it.get_fps),
            c.GAME_OVER: load_screen.GameOver(config, run_it.get_fps)
        })
    
    # Config du premier State
    if config.show_game_frame:
        run_it.setup_states(state_dict, c.MAIN_MENU)
    else:
        run_it.setup_states(state_dict, c.LEVEL1)
    
    # Doit renvoyer le persist
    return run_it.main()
