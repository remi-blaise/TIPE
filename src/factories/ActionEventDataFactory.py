#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import InheritableDocstrings, inherit_docstring
from random import choice, randint

from mario.bridge.events.action_events import Jump, Left, Right, Down, Fire
from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.ActionEventData import ActionEventData


class ActionEventDataFactory(GeneticElementFactory, metaclass=InheritableDocstrings):
	"""ActionEventData factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return ActionEventData
	
	ACTION_CLASSES = (Jump, Left, Right, Down, Fire)
	
	
	@classmethod
	@inherit_docstring
	def create(cls):
		return ActionEventData(cls.createActionClass(), cls.createDuration())
	
	@staticmethod
	@inherit_docstring
	def mutate(element):
		raise NotImplementedError
	
	
	@classmethod
	def createActionClass(cls):
		return choice(cls.ACTION_CLASSES)
	
	@staticmethod
	def createDuration():
		return randint(2, 30)
