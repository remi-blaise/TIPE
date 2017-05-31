#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments
from lib.XMLRepr import XMLRepr

from src.EvolutiveGenerator.GeneticElement import GeneticElement


class GameEventData(GeneticElement, XMLRepr):
	"""An game event data, part of a neuron"""
	
	@inject_arguments
	def __init__(self, event_name, coor):
		pass
	
	
	def checkCoor(self, event):
		return self.coor['x'] >= event.left and self.coor['x'] <= event.right \
			and self.coor['y'] >= event.top and self.coor['y'] <= event.bottom
	
	
	def reprJSON(self):
		return self.__dict__
	
	def __repr__(self):
		return super().__repr__(
			attributes=['event_name', 'coor'],
			__dict__={'event_name': self.event_name, 'coor': (self.coor['x'], self.coor['y'])}
		)
