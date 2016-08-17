#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import InheritableDocstrings, inherit_docstring

from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.IA import IA


class IAFactory(GeneticElementFactory, metaclass=InheritableDocstrings):
	"""IA factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return IA
	
	
	@staticmethod
	@inherit_docstring
	def create():
		raise NotImplementedError
	
	
	@staticmethod
	@inherit_docstring
	def mutate(element):
		raise NotImplementedError
	
	
	@staticmethod
	@inherit_docstring
	def combine(element1, element2):
		raise NotImplementedError
