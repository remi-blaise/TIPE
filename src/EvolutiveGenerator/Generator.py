#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import choice, sample
from math import ceil
from inspect import isfunction, ismethod
from re import match

from lib.eventdispatcher import EventDispatcher
from .events import *
from src.Writer.PathManager import PathManager


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
		generation.selection.start,
		generation.selection.done,
		generation.selection.grading.start,
		generation.selection.grading.process,
		generation.selection.grading.done,
		generation.breeding.start,
		generation.breeding.process,
		generation.breeding.done
	See events.py for informations carried by events.
	In particular, the population is available through creation.done and
	generation.start/done.
	"""
	
	
	def __init__(self, factory, graduator, listeners = []):
		"""Init
		
		Expects:
			factory to be a class inheriting of GeneticElementFactory
			graduator to be a instance inheriting of Graduator
			listeners to be a list of couples (event_name, listener)
		You can directly pass listeners instead of couples if the names of
		listeners follow the format 'onEventName'. For example, listener
		'onProcessusStart' will listen on 'processus.start'.
		If exists, factory.onProcessusStart method is automatically added to
		listeners.
		"""
		
		self.factory = factory
		self.graduator = graduator
		self.population = None
		self.selection = None
		self.processus_id = None
		self.generation_id = None
		
		self.dispatcher = EventDispatcher()
		if hasattr(factory, 'onProcessusStart'):
			listeners.append(factory.onProcessusStart)
		
		for listener in listeners:
			if type(listener) is tuple:
				self.dispatcher.listen(*listener)
			elif isfunction(listener) or ismethod(listener):
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
			else:
				raise ValueError('Bad listener value: {}'.format(listener))
	
	
	def dispatch(self, event_name):
		"""Shorthand to dispatch common events"""
		if event_name in ('processus.start', 'processus.done'):
			self.dispatcher.dispatch(event_name, ProcessusEvent(self.processus_id))
		elif event_name in (
			'creation.start', 'creation.done',
			'generation.start', 'generation.done'
		):
			self.dispatcher.dispatch(event_name, GenerationEvent(
				self.processus_id, self.generation_id, self.population
			))
		else:
			raise ValueError('Cannot dispatch {} events.'.format(event_name))
	
	def dispatchSelection(self, event_name, grading, selection):
		"""Shorthand to dispatch selection events"""
		self.dispatcher.dispatch('generation.selection.' + event_name, SelectionEvent(
			grading, selection, self.processus_id, self.generation_id
		))
	
	def dispatchGrading(self, event_name, graduation = None):
		"""Shorthand to dispatch grading events"""
		self.dispatcher.dispatch('generation.selection.grading.' + event_name, GradingEvent(
			graduation, self.processus_id, self.generation_id
		))
	
	def dispatchBreeding(self, event_name, offspring = None):
		"""Shorthand to dispatch breeding events"""
		self.dispatcher.dispatch('generation.breeding.' + event_name, BreedingEvent(
			offspring, self.processus_id, self.generation_id
		))
	
	
	def create(self, pop_length):
		"""Generate a whole initial population"""
		
		self.dispatch('creation.start')
		
		self.population = set([self.factory.create() for i in range(pop_length)])
		
		self.dispatch('creation.done')
	
	
	def select(self, proportion, chance):
		"""Operate the selection
		
		This is a basic system to be overcome.
		The selection is a subset of the population.
		
		Expects:
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		"""
		
		self.dispatchSelection('start', None, None)
		
		# Get a list of couple (score, individual) sorted by score
		graded_individuals = self.graduator.gradeAll(
			self.population, self.generation_id, self.dispatchGrading
		)
		# Get a list of individuals
		ordered_individuals = [c[1] for c in graded_individuals]
		
		# The number of individuals to select
		number = ceil(len(self.population) * proportion)
		# Among the [number] best individuals select number*(1-chance) ones
		selection = set(sample(
			ordered_individuals[:number],
			int(number*(1-chance))
		))
		# Complete selection with random individuals
		unused_individuals = self.population.difference(selection)
		while len(selection) < number:
			choiced = choice(unused_individuals)
			selection.add(choiced)
			unused_individuals.remove(choiced)
		
		self.dispatchSelection('done', graded_individuals, selection)
		
		self.selection = selection
	
	
	def breed(self, pop_length):
		"""Generate a new population based on selection
		
		This is a basic system to be overcome.
		"""
		
		self.dispatchBreeding('start')
		
		new_pop = set()
		
		while len(new_pop) < pop_length:
			parents = tuple([choice(list(self.selection)) for i in range(2)])
			offspring = self.factory.breed(*parents)
			new_pop.add(offspring)
			self.dispatchBreeding('progress', offspring)
		
		self.dispatchBreeding('done')
		
		self.population = new_pop
	
	
	def generate(self, pop_length, proportion, chance):
		"""Operate a generation"""
		
		self.generation_id += 1
		self.dispatch('generation.start')
		self.select(proportion, chance)
		self.breed(pop_length)
		self.dispatch('generation.done')
	
	
	def process(self, processus_id, generations, pop_length = 500, proportion = .5, chance = 0):
		"""Process multiple generations
		
		Expects:
			generations to be an int
			pop_length to be an int
			
			proportion to be a float between 0 and 1
			chance to be a float between 0 and 1
		
		Return the last generation
		"""
		
		self.processus_id = processus_id
		self.generation_id = 0
		self.dispatch('processus.start')
		
		self.create(pop_length)
		
		for i in range(generations):
			self.generate(pop_length, proportion, chance)
		
		self.dispatch('processus.done')
		
		self.processus_id = None
		self.generation_id = None
		
		return self.population
