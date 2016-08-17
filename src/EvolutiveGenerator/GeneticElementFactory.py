#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from abc import ABCMeta, abstractmethod


class GeneticElementFactory(metaclass=ABCMeta):
	"""Handle the evolution logic of a GeneticElement
	
	This is an abstract class to inherit.
	This is a static class.
	It brings the evolution logic of the GeneticElement through the following
	class methods:
		+create() -> GeneticElement
		+mutate(GeneticElement) -> GeneticElement
		+combine(GeneticElement, GeneticElement) -> GeneticElement
		+generate(GeneticElement, GeneticElement) -> GeneticElement
	Evolution logic may typically use recursive process over children of elements.
	"""
	
	@property
	@abstractmethod
	def genetic_element_class(self):
		"""The GeneticElement based class"""
		
		raise NotImplementedError
	
	
	@staticmethod
	@abstractmethod
	def create(parent = None, children = [], cascade = True):
		"""Create a GeneticElement from void
		
		An essential element of the generation proccess.
		This is a static method which has to be implemented.
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	@staticmethod
	@abstractmethod
	def mutate(element):
		"""Make a mutated GeneticElement
		
		Operates genetic mutation to build a new GeneticElement.
		Has to be implemented.
		
		This is rather designed for internal use, see generate() instead.
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	@staticmethod
	def combine(element1, element2):
		"""Form a new GeneticElement, combination of two ones
		
		Combine two GeneticElement to form an offspring.
		Has to be implemented.
		
		This is rather designed for internal use, see generate() instead.
		
		Expects:
			element1, element2 to be GeneticElement's
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	@classmethod
	def generate(cls, element1, element2):
		"""Generate a new GeneticElement, final offspring of two ones
		
		Call combine() then mutate().
		
		Expects:
			element1, element2 to be a GeneticElement's
		
		return GeneticElement
		"""
		
		return cls.mutate(cls.combine(element1, element2))
