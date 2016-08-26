__author__ = 'justinarmstrong'

"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg
from .load_resources import *
from .import constants as c


def setup(config):
	global ORIGINAL_CAPTION, SCREEN, SCREEN_RECT, FONTS, GFX, MUSIC, SFX
	ORIGINAL_CAPTION = c.ORIGINAL_CAPTION

	os.environ['SDL_VIDEO_CENTERED'] = '1'				 	# Centre la fenetre sur l'écran (param de SDL)
	pg.init()											   	# Obligatoire
	if not config.play_sound:
		pg.mixer.quit()
	pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])   # Autorise les events qu'on veut récupérer
	pg.display.set_caption(c.ORIGINAL_CAPTION)			  	# Affiche le titre
	SCREEN = pg.display.set_mode(c.SCREEN_SIZE)		# Crée une fenetre de taille (800, 600) -> Surface
	SCREEN_RECT = SCREEN.get_rect()					# Récupère le rectangle correspondant à la fenetre entière
	
	if not config.graphic_output:
		pg.display.iconify()


	FONTS = load_all_fonts(os.path.join("mario", "resources", "fonts"))
	GFX   = load_all_gfx(os.path.join("mario", "resources", "graphics"))
	if config.play_sound:
		MUSIC = load_all_music(os.path.join("mario", "resources", "music"))
		SFX   = load_all_sfx(os.path.join("mario", "resources", "sound"))
	else:
		SFX = FakeDict()


class FakeSFX:
	def play(self):
		pass


class FakeDict:
	def __init__(self):
		self.item = FakeSFX()
	
	def __getitem__(self, index):
		return self.item
