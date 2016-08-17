#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments

from src.EvolutiveGenerator.GeneticElement import GeneticElement


class ActionEventData(GeneticElement):
	"""An action event data, part of a neuron"""
	
	@inject_arguments
	def __init__(self, action_class, duration):
		pass
	
	
	def buildAction(self, event):
		return self.action_class(self.duration, event.current_frame)
