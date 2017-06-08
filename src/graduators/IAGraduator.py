#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from math import ceil

from lib.inject_arguments import inject_arguments
from lib.inherit_docstring import inherit_docstring

from src.meta.ABCInheritableDocstringsMeta import ABCInheritableDocstringsMeta
from mario.bridge.config import Config
from mario.bridge.launch import launch
from src.EvolutiveGenerator.Graduator import Graduator
from src.entities.Result import Result


class IAGraduator(Graduator, metaclass=ABCInheritableDocstringsMeta):
	"""Graduate IA"""

	@inject_arguments
	def __init__(self, event_dispatcher, show = False):
		self.mario_x = 0
		self.max_y = 0


	def gradeIAWithConfig(self, ia, config):
		# Init
		self.mario_x = 0
		self.max_y = 0

		# Give the event_dispatcher to neurons
		for neuron in ia.neurons:
			neuron.event_dispatcher = self.event_dispatcher

		self.event_dispatcher.listen('game.frame', self.onFrame)

		# Launch game
		persist = launch(config)

		# Remove the event_dispatcher from neurons
		for neuron in ia.neurons:
			del neuron.event_dispatcher

		# Make the result
		result = Result(persist['camera start x'] + self.mario_x, self.max_y)

		# Return the score
		return result


	@inherit_docstring
	def grade(self, ia, generation_id):
		time = 1 + ceil(generation_id / 2)
		if time > 401:
			time = 401

		return self.gradeIAWithConfig(ia, Config(self.show, self.event_dispatcher, time))


	def onFrame(self, frame):
		self.mario_x = frame.mario.rect.x
		self.max_y = max(self.max_y, frame.mario.rect.y)
