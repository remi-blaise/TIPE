#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from collections import OrderedDict


class Graduator:
	"""Graduate characters
	
	This is an abstract class to inherit.
	Assess character's performances and assign them a score.
	The Graduator a to see as a bridge between the Generator and the software.
	It is designed to use the software to make evolute characters.
	IT IS THE NATURE.
	Characters are represented by root GeneticElement instances.
	"""
	
	
	def grade(self, character):
		"""Assign a score to a character
		
		Has to be implemented.
		
		Expects:
			character to be an GeneticElement
		
		return int or any sortable object The score
		"""
		
		raise NotImplementedError
	
	
	def gradeAll(self, characters):
		"""Return an OrderedDict of GeneticElement characters
		
		Characters are sorted by score as key in natural order.
		
		Expects:
			characters to be a list of GeneticElement
		
		return OrderedDict
		"""
		
		unorderedChar = {}
		for char in characters:
			unorderedChar[self.grade(char)] = char
		
		return OrderedDict(sorted(unorderedChar.items(), key=itemgetter(0), reverse=True))
