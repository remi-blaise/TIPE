def launch(config):
	"""Usual launch"""
	import pygame as pg
	from mario.data.main import main
	import cProfile


	persist = main(config)
	# print('program done')
	# Pb 1: Can freeze pygame
	# Possibly resolved with Objective 1.1
	# Pb 2: Seems to resurrect each done Pygame on init
	# Can possibly be resolved with Objective 2.6
	# temp: to delete and use the same pygame each time
	# pg.quit()
	# print('pygame done')
	
	return persist
