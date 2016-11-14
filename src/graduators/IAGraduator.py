#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments
from lib.inherit_docstring import inherit_docstring

from src.meta.ABCInheritableDocstringsMeta import ABCInheritableDocstringsMeta
from mario.bridge.config import Config
from mario.bridge.launch import launch
from src.EvolutiveGenerator.Graduator import Graduator


class IAGraduator(Graduator, metaclass=ABCInheritableDocstringsMeta):
	"""Graduate IA"""
	
	@inject_arguments
	def __init__(self, event_dispatcher):
		self.mario_x = 0
	
	
	def gradeIAWithConfig(self, ia, config):
		# Give the event_dispatcher to neurons
		for neuron in ia.neurons:
			neuron.event_dispatcher = self.event_dispatcher
		
		self.event_dispatcher.listen('game.frame', self.onFrame)
		
		# Launch game
		persist = launch(config)
		
		# Remove the event_dispatcher from neurons
		for neuron in ia.neurons:
			del neuron.event_dispatcher
		
		# Return the score
		return persist['camera start x'] + self.mario_x
	
	
	@inherit_docstring
	def grade(self, ia, generation_id):
		time = 1 + generation_id
		if time > 401:
			time = 401
		
		return self.gradeIAWithConfig(ia, Config(False, self.event_dispatcher, time))
	
	
	def onFrame(self, frame):
		self.mario_x = frame.mario.rect.x
