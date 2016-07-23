#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import choice, sample


class Generator:
	"""Handle the generation proccess
	
	The generator, at the heart of the generation process, has three charges:
		- create a group of characters
		- operate the selection, based on characters' performances
		- generate a new  group, based on the selection
	Characters are represented by root GeneticElement instances.
	Use Graduator to grade performances.
	Extending it is strongly adviced.
	"""
	
	
	def __init__(self, character_class, graduator):
		"""Init
		
		Expects:
			character_class to be a class inheriting of GeneticElement
			graduator to be a instance inheriting of Graduator
		"""
		
		self.character_class = character_class
		self.graduator = graduator
		self.group = None
		self.selection = None
	
	
	def create(self, number = 500):
		"""Generate a whole initial group"""
		
		self.group = set([character_class.create() for i in range(number)])
	
	
	def select(self, proportion = .5, chance = 0):
		"""Operate the selection
		
		This is a basic system to be overcome.
		The selection is a subset of the group.
		
		Expects:
			proportion to be an int between 0 and 1
			chance to be an int between 0 and 1
		"""
		
		# Get an OrderedDict of char sorted by score
		orderedChar = self.graduator.grade_all(self.group)
		
		# The number of char to select
		number = int(len(self.group) * proportion)
		# In the number best characters select number*(1-chance) ones
		selection = set(sample(list(orderedChar.values())[-number], int(number*(1-chance))))
		# Complete selection with random char
		unusedChar = self.group.difference(selection)
		while len(selection) < number:
			choiced = choice(unusedChar)
			selection.add(choiced)
			unusedChar.remove(choiced)
		
		
	
	
	def generate(self, number = 500):
		"""Generate a new group based on selection
		
		This is a basic system to be overcome.
		"""
		
		pass
	
	
	def run(self):
		"""Operate a run"""
		
		pass
