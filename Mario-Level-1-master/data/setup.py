__author__ = 'justinarmstrong'

"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg
from . import tools
from .import constants as c

ORIGINAL_CAPTION = c.ORIGINAL_CAPTION


os.environ['SDL_VIDEO_CENTERED'] = '1'                  # Centre la fenetre sur l'écran (param de SDL)
pg.init()                                               # Obligatoire
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])   # Autorise les events qu'on veut récupérer
pg.display.set_caption(c.ORIGINAL_CAPTION)              # Affiche le titre
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)             # Crée une fenetre de taille (800, 600) -> Surface
SCREEN_RECT = SCREEN.get_rect()                         # Récupère le rectangle correspondant à la fenetre entière


FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
MUSIC = tools.load_all_music(os.path.join("resources","music"))
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))


