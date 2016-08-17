#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments

from src.EvolutiveGenerator.GeneticElement import GeneticElement


class IA(GeneticElement):
	"""An IA"""
	
	@inject_arguments
	def __init__(self, neurons=set()):
		"""Init the IA
		
		Expects:
			neurons to be a set of Neuron
		"""
		
		pass
