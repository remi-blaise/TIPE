#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import inherit_docstring
from random import randint, random, choice, sample
from math import ceil

from src.meta.ABCInheritableDocstringsMeta import ABCInheritableDocstringsMeta
from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.IA import IA
from src.factories.NeuronFactory import NeuronFactory


class IAFactory(GeneticElementFactory, metaclass=ABCInheritableDocstringsMeta):
	"""IA factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return IA
	
	
	@staticmethod
	@inherit_docstring
	def create():
		neurons = set()
		for i in range(3 + randint(0, 3)):
			neurons.add(NeuronFactory.create())
		return IA(neurons)
	
	
	@staticmethod
	@inherit_docstring
	def mutate(element):
		if random() < .2:
			element.neurons.add(NeuronFactory.create())
		if random() < .1:
			element.neurons.remove(choice(list(element.neurons)))
		for neuron in element.neurons:
			if random() < .2:
				NeuronFactory.mutate(neuron)
	
	
	@staticmethod
	@inherit_docstring
	def combine(element1, element2):
		neurons = set()
		for half in (element1.neurons, element2.neurons):
			neurons.update(
				sample(element1.neurons, ceil(len(element1.neurons) / 2))
			)
		return IA(neurons)
