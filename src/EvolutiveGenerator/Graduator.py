#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from abc import ABCMeta, abstractmethod
from collections import OrderedDict


class Graduator(metaclass=ABCMeta):
	"""Graduate individuals
	
	This is an abstract class to inherit.
	Assess individual's performances and assign them a score.
	The Graduator a to see as a bridge between the Generator and the software.
	It is designed to use the software to make evolute individuals.
	IT IS THE NATURE.
	Individuals are represented by root GeneticElement instances.
	"""
	
	
	@abstractmethod
	def grade(self, individual):
		"""Assign a score to a individual
		
		Has to be implemented.
		
		Expects:
			individual to be an GeneticElement
		
		return int or any sortable object The score
		"""
		
		raise NotImplementedError
	
	
	@abstractmethod
	def gradeAll(self, individuals):
		"""Return an OrderedDict of GeneticElement individuals
		
		Individuals are sorted by score as key in natural order.
		
		Expects:
			individuals to be a list of GeneticElement
		
		return OrderedDict
		"""
		
		unorderedChar = {}
		for char in individuals:
			unorderedChar[self.grade(char)] = char
		
		return OrderedDict(sorted(unorderedChar.items(), key=itemgetter(0), reverse=True))
