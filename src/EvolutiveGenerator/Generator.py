#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import choice, sample
from math import ceil
from inspect import isfunction, ismethod
from re import match

from lib.eventdispatcher import EventDispatcher
from .ProcessusState import ProcessusState
from .event_names import *


class Generator:
	"""Handle the generation proccess
	
	The generator, at the heart of the generation process, has three charges:
		- create a population of individuals
		- select a subset of the population, based on their performances
		- breed individuals of the selection to form a new population
	Individuals are represented by root GeneticElement instances.
	Use a Graduator to grade performances.
	Extending it is strongly adviced.
	
	The generator dispatches several events through its internal dispatcher:
		processus.start,
		processus.done,
		creation.start,
		creation.done,
		generation.start,
		generation.done,
		grading.start,
		grading.process,
		grading.done,
		selection.start,
		selection.done,
		breeding.start,
		breeding.process,
		breeding.done
	See events.py for informations carried by events.
	In particular, the population is available through creation.done and
	generation.start/done.
	"""
	
	
	def __init__(self, factory, graduator, listeners = []):
		"""Init
		
		Expects:
			factory to be a class inheriting of GeneticElementFactory
			graduator to be a instance inheriting of Graduator
			listeners to be a list of listeners (see below)
		Listeners can be:
			- couples (event_name, listener)
			- tuples (event_name, listener, priority)
			- functions and methods if their names follow the format
			  'onEventName'. For example, listener 'onProcessusStart' will
			  listen on 'processus.start'.
			- objects: every method following the format above is added to
			listeners.
		factory and graduator are automatically added to listeners.
		Priorities has to be strictly smaller than 1000.
		"""
		
		self.factory = factory
		self.graduator = graduator
		
		self.state = ProcessusState()
		
		self.dispatcher = EventDispatcher()
		listeners.append(factory)
		listeners.append(graduator)
		
		listeners.extend([
			(PROCESSUS.START, self.create, 1000),
			(CREATION.DONE, self.initGeneration, 1000),
			(GENERATION.START, self.grade, 1000),
			(GRADING.DONE, self.select, 1000),
			(SELECTION.DONE, self.breed, 1000),
			(BREEDING.DONE, self.endGeneration, 1000),
		])
		
		# Get all objects' methods
		listenersMethods = listeners.copy()
		for listener in listeners:
			if not (type(listener) is tuple or isfunction(listener) or ismethod(listener)):
				listenersMethods.remove(listener)
				for method in [method for method in dir(listener) if ismethod(getattr(listener, method))]:
					if match('on([A-Z]\w+)', method):
						listenersMethods.append(getattr(listener, method))
		
		# Inscribe all listeners
		for listener in listenersMethods:
			if type(listener) is tuple:
				self.dispatcher.listen(*listener)
			else:
				# Parse method names to get event names
				m = match('on([A-Z]\w+)', listener.__name__)
				if m:
					event_name = ''
					camel_event_name = m.group(1)
					while True:
						m = match('([A-Z][a-z0-9_]+)(\w*)', camel_event_name)
						if not m:
							break
						if event_name:
							event_name += '.'
						event_name += m.group(1).lower()
						camel_event_name = m.group(2)
					self.dispatcher.listen(event_name, listener)
				else:
					raise ValueError('The given listener do not follow the format onEventName.')
	
	
	def dispatch(self, event_name):
		self.state.event_name = event_name
		self.dispatcher.dispatch(event_name, self.state)
	
	def dispatchGrading(self, individual, graduation):
		"""Shorthand to dispatch grading events"""
		self.state.individual = individual
		self.state.graduation = graduation
		self.dispatch(GRADING.PROGRESS)
	
	
	def initProcessus(self):
		self.dispatch(PROCESSUS.START)
	
	def endProcessus(self):
		self.dispatch(PROCESSUS.DONE)
	
	def initGeneration(self, state):
		state.generation_id += 1
		self.dispatch(GENERATION.START)
	
	def endGeneration(self, state):
		self.dispatch(GENERATION.DONE)
		if state.generation_id < state.generations:
			self.initGeneration(state)
		else:
			self.endProcessus()
	
	
	def create(self, state):
		"""Generate a whole initial population"""
		
		state.generation_id = 0
		self.dispatch(CREATION.START)
		
		state.population = set([self.factory.create() for i in range(state.pop_length)])
		
		self.dispatch(CREATION.DONE)
	
	
	def grade(self, state):
		"""Grade all individuals"""
		
		self.dispatch(GRADING.START)
		
		# Get a list of couple (score, individual) sorted by score
		state.grading = self.graduator.gradeAll(
			state.population, state.generation_id, self.dispatchGrading
		)
		self.dispatch(GRADING.DONE)
	
	
	def select(self, state):
		"""Operate the selection
		
		This is a basic system to be overcome.
		The selection is a subset of the population.
		"""
		
		self.dispatch(SELECTION.START)
		
		# Get a list of individuals
		ordered_individuals = [c[1] for c in state.grading]
		
		# The number of individuals to select
		selection_length = ceil(len(state.population) * state.proportion)
		# Among the [selection_length] best individuals select selection_length*(1-state.chance) ones
		selection = set(sample(
			ordered_individuals[:selection_length],
			int(selection_length * (1 - state.chance))
		))
		# Complete selection with random individuals
		unused_individuals = state.population.difference(selection)
		while len(selection) < selection_length:
			choiced = choice(unused_individuals)
			selection.add(choiced)
			unused_individuals.remove(choiced)
		
		state.selection = selection
		self.dispatch(SELECTION.DONE)
	
	
	def breed(self, state):
		"""Generate a new population based on selection
		
		This is a basic system to be overcome.
		"""
		
		self.dispatch(BREEDING.START)
		
		new_pop = set()
		
		while len(new_pop) < state.pop_length:
			parents = tuple([choice(list(state.selection)) for i in range(2)])
			offspring = self.factory.breed(*parents)
			new_pop.add(offspring)
			
			state.offspring = offspring
			state.parents = parents
			self.dispatch(BREEDING.PROGRESS)
		
		state.population = new_pop
		
		self.dispatch(BREEDING.DONE)
	
	
	def process(self, processus_id, generations, pop_length = 500, proportion = .5, chance = 0):
		"""Process multiple generations
		
		Expects:
			generations to be an int
			pop_length to be an int
			
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		
		Return the last generation
		"""
		
		self.state.processus_id = processus_id
		self.state.generations = generations
		self.state.pop_length = pop_length
		self.state.proportion = proportion
		self.state.chance = chance
		
		self.initProcessus()
		
		return self.state.population