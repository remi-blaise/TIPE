#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class GeneticElement:
	"""A genetic element
	
	This is an abstract class to inherit.
	A genetic element brings one or several genetic informations or contains
	other genetic elements.
	It also brings the evolution logic of the element through the following
	methods:
		+mutate() -> GeneticElement
		+combine(GeneticElement) -> GeneticElement
		+generate(GeneticElement) -> GeneticElement
	Evolution logic may typically use recursive process over the children.
	"""
	
	
	def __init__(self, children = [], parent = None):
		"""Inits the element
		
		Expects:
			children to be an array of GeneticElement
			parent to be a GeneticElement
		Both are optional.
		"""
		
		self.parent = parent
		self.children = children
	
	
	def isRoot(self):
		"""Has the element no parent"""
		
		return self.parent is None
	
	
	def isLeaf(self):
		"""Has the element no children"""
		
		return bool(len(self.children))
	
	
	def mutate(self):
		"""Makes a mutated GeneticElement
		
		Operates genetic mutation to build a new GeneticElement.
		Has to be implemented.
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	def combine(self, partner):
		"""Forms a new GeneticElement, combination of two ones
		
		Combine itself with an other GeneticElement to form an offspring.
		Has to be implemented.
		
		Expects:
			partner to be a GeneticElement
		
		return GeneticElement
		"""
		
		raise NotImplementedError
	
	
	def generate(self, partner):
		"""Generate a new GeneticElement, final offspring of two ones
		
		Call combine() then mutate()
		
		Expects:
			partner to be a GeneticElement
		
		return GeneticElement
		"""
		
		return self.combine(partner).mutate()

