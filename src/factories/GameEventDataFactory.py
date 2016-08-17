#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import InheritableDocstrings, inherit_docstring

from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.GameEventData import GameEventData


class GameEventDataFactory(GeneticElementFactory, metaclass=InheritableDocstrings):
	"""GameEventData factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return GameEventData
	
	
	@staticmethod
	@inherit_docstring
	def create():
		raise NotImplementedError
	
	
	@staticmethod
	@inherit_docstring
	def mutate(element):
		raise NotImplementedError
