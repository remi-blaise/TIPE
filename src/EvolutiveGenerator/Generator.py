#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import choice, sample


class Generator:
	"""Handle the generation proccess
	
	The generator, at the heart of the generation process, has three charges:
		- create a population of individuals
		- operate the selection, based on individuals' performances
		- generate a new population, based on the selection
	Individuals are represented by root GeneticElement instances.
	Use a Graduator to grade performances.
	Extending it is strongly adviced.
	"""
	
	
	def __init__(self, factory, graduator):
		"""Init
		
		Expects:
			factory to be a class inheriting of GeneticElementFactory
			graduator to be a instance inheriting of Graduator
		"""
		
		self.factory = factory
		self.graduator = graduator
		self.population = None
		self.selection = None
	
	
	def create(self, length):
		"""Generate a whole initial population"""
		
		self.population = set([factory.create() for i in range(length)])
	
	
	def select(self, proportion, chance):
		"""Operate the selection
		
		This is a basic system to be overcome.
		The selection is a subset of the population.
		
		Expects:
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		"""
		
		# Get an OrderedDict of char sorted by score
		ordered_char = self.graduator.gradeAll(self.population)
		
		# The number of char to select
		number = int(len(self.population) * proportion)
		# Among the [number] best individuals select number*(1-chance) ones
		selection = set(sample(
			list(ordered_char.values())[:number],
			int(number*(1-chance))
		))
		# Complete selection with random char
		unused_char = self.population.difference(selection)
		while len(selection) < number:
			choiced = choice(unused_char)
			selection.add(choiced)
			unused_char.remove(choiced)
		
		self.selection = selection
	
	
	def generate(self, length):
		"""Generate a new population based on selection
		
		This is a basic system to be overcome.
		"""
		
		new_pop = set()
		
		while len(new_pop) < length:
			parents = tuple([choice(self.selection) for i in range(2)])
			new_pop.add(parents[0].generate(parents[1]))
		
		self.population = new_pop
	
	
	def run(self, length, proportion, chance):
		"""Operate a run"""
		
		self.select(proportion, chance)
		self.generate(length)
	
	
	def process(self, number, length = 500, proportion = .5, chance = 0):
		"""Process multiple runs
		
		Expects:
			number to be an int
			length to be an int
			
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		
		Return the last generation
		"""
		
		self.create(length)
		
		for i in range(number):
			self.run(length, proportion, chance)
		
		return self.population
