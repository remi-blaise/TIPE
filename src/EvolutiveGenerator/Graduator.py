#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from abc import ABCMeta, abstractmethod
from operator import itemgetter


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
	def grade(self, individual, generation_id):
		"""Assign a score to a individual
		
		Has to be implemented.
		
		Expects:
			individual to be an GeneticElement
		
		return int or any sortable object The score
		"""
		
		raise NotImplementedError
	
	
	def gradeAll(self, individuals, generation_id, dispatch):
		"""Assign a score to each individual
		
		Individuals are sorted by score as key in natural order.
		
		Expects:
			individuals to be a list of GeneticElement
		
		Return a list of couple (score, GeneticElement) sorted by score by desc
		"""
		
		dispatch('start')
		
		graded_individuals = []
		for individual in individuals:
			graduation = self.grade(individual, generation_id)
			graded_individuals.append((graduation, individual))
			dispatch('progress', individual, graduation)
		
		dispatch('done')
		
		graded_individuals.sort(key=itemgetter(0), reverse=True)
		
		return graded_individuals
