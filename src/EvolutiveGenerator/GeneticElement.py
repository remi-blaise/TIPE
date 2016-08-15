#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class GeneticElement:
	"""Carry the genetic information
	
	This is an abstract class to inherit.
	A genetic element carries one or several genetic informations or contains
	other genetic elements.
	It also brings the evolution logic of the element through the following
	object's methods:
		+mutate() -> GeneticElement
		+combine(GeneticElement) -> GeneticElement
		+generate(GeneticElement) -> GeneticElement
	And the following class method:
		+create() -> GeneticElement
	Evolution logic may typically use recursive process over the children.
	Evolution logic might be handled by an external EvolutionProcessor.
	"""
	
	
	def __init__(self, parent = None, children = [], cascade = True):
		"""Init the element
		
		Expects:
			parent to be a GeneticElement
			children to be an array of GeneticElement
			cascade to be a bool
		All are optional.
		Words "parent" and "children" refers to data trees concepts, not genetic's.
		
		If cascade is True (by default), append the element to parent's children list.
		"""
		
		self.parent = parent
		if cascade and parent:
			parent.children.append(self)
		self.children = children
	
	
	@classmethod
	def create(cls):
		"""Create a GeneticElement from void
		
		An essential element of the generation proccess.
		This is a class method which has to be implemented.
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	def isRoot(self):
		"""Has the element no parent"""
		
		return self.parent is None
	
	
	def isLeaf(self):
		"""Has the element no children"""
		
		return bool(len(self.children))
	
	
	def mutate(self):
		"""Make a mutated GeneticElement
		
		Operates genetic mutation to build a new GeneticElement.
		Has to be implemented.
		
		This is rather designed for internal use, see generate() instead.
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	def combine(self, partner):
		"""Form a new GeneticElement, combination of two ones
		
		Combine itself with an other GeneticElement to form an offspring.
		Has to be implemented.
		
		This is rather designed for internal use, see generate() instead.
		
		Expects:
			partner to be a GeneticElement
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	def generate(self, partner):
		"""Generate a new GeneticElement, final offspring of two ones
		
		Call combine() then mutate().
		
		Expects:
			partner to be a GeneticElement
		
		return GeneticElement
		"""
		
		return self.combine(partner).mutate()


if __name__ == '__main__':
	from copy import copy
	
	root = GeneticElement()
	child = GeneticElement(root)
	assert root.children[0] is child
