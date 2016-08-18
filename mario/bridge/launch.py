def launch(config):
	"""Usual launch"""
	import pygame as pg
	from mario.data.main import main
	import cProfile


	persist = main(config)
	print('debug')
	# pg.quit() # Can freeze pygame: to delete and use the same pygame each time
	print('debug2')
	
	return persist
