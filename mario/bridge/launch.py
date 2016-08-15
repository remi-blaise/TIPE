"""Set parent directory as root directory"""
import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
main_dir = os.path.dirname(parent_dir)
os.chdir(main_dir) 			# Set main dir for resources
sys.path.append(main_dir)	# Set main dir for import paths


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
