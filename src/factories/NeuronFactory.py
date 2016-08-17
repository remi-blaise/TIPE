#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import InheritableDocstrings, inherit_docstring
from random import randint

from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.Neuron import Neuron
from GameEventDataFactory import GameEventDataFactory
from ActionEventDataFactory import ActionEventDataFactory


class NeuronFactory(GeneticElementFactory, metaclass=InheritableDocstrings):
	"""Neuron factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return Neuron
	
	
	@staticmethod
	@inherit_docstring
	def create():
		return Neuron(GameEventDataFactory.create(), ActionEventDataFactory.create())
	
	
	@staticmethod
	@inherit_docstring
	def mutate(element):
		if randint(0, 1):
			GameEventDataFactory.mutate(element.game_event_data)
		else:
			ActionEventDataFactory.mutate(element.action_event_data)
