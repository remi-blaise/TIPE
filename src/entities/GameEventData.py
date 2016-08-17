#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments

from src.EvolutiveGenerator.GeneticElement import GeneticElement


class GameEventData(GeneticElement):
	"""An game event data, part of a neuron"""
	
	@inject_arguments
	def __init__(self, event_name, coor):
		pass
	
	
	def checkCoor(self, event):
		return self.coor['x'] >= event.left and self.coor['x'] <= event.right \
			and self.coor['y'] >= event.top and self.coor['y'] <= event.bottom
