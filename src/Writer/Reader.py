#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from json import loads
from re import fullmatch

from .JSONEncoder import JSONEncoder
from .PathManager import PathManager
from src.factories.IAFactory import IAFactory
from src.EvolutiveGenerator.ProcessusState import ProcessusState
from src.EvolutiveGenerator.event_names import *


class Reader:
	"""Read files
	
	This is a static class.
	
	Public API:
		processusExists(processus_id)
		getProcessusState(processus_id)
	"""
	
	
	@staticmethod
	def getPath(*args, **kwargs):
		return PathManager.getPath(*args, **kwargs, read_only=True)
	
	
	@staticmethod
	def readJSON(path):
		return loads(path.read_text())
	
	
	@staticmethod
	def readGrading(path):
		grading = []
		with path.open('r') as grading_file:
			for line in grading_file:
				try:
					graduation_tuple = fullmatch('([0-9]+): ([0-9]+)\n', line).group(1, 2)
					grading.append(graduation_tuple)
				except AttributeError:
					raise ValueError("The given grading file doesn't match the right format.")
		return grading
	
	
	@classmethod
	def getProcessusParams(cls, processus_id):
		path = cls.getPath(processus_id)
		if not path.parent.exists():
			raise ValueError("Processus {} doesn't exists.".format(processus_id))
		if not path.exists():
			raise ValueError("Processus {} doesn't have processus.json file.".format(processus_id))
		
		return cls.readJSON(path)
	
	
	@classmethod
	def getPopulation(cls, processus_id, generation_id, generations):
		population = set()
		for ia_file in (
			cls.getPath(processus_id, generations, None, generation_id).parent
			/ ('population' if generation_id > 0 else 'initial_pop')
		).iterdir():
			population.add(IAFactory.hydrate(cls.readJSON(ia_file)))
		return population
	
	
	@classmethod
	def processusExists(cls, processus_id):
		path = cls.getPath(processus_id)
		if not path.parent.exists():
			return False
		return True
	
	
	@classmethod
	def getProcessusState(cls, processus_id):
		'''
		for state.event_name in (
			PROCESSUS.START,
			CREATION.START,
			CREATION.DONE,
			GENERATION.START,
			GRADING.START,
			GRADING.PROGRESS,
			GRADING.DONE,
			SELECTION.START,
			SELECTION.DONE,
			BREEDING.START,
			BREEDING.PROGRESS,
			BREEDING.DONE,
			GENERATION.DONE,
			PROCESSUS.DONE
		)
		'''
		
		state = ProcessusState()
		state.processus_id = processus_id
		state.__dict__.update(cls.getProcessusParams(processus_id))
		
		getPath = lambda generation_id, file_name = None: cls.getPath(
			processus_id, state.generations, None, generation_id, file_name
		)
		
		# Get first inexistant generation
		generation_id = 0
		while getPath(generation_id).parent.exists():
			generation_id += 1
		
		# If none generation folder exist
		if generation_id == 0:
			state.event_name = PROCESSUS.START
			return state
		
		state.generation_id = generation_id - 1
		del generation_id
		
		# Get event_name
		state.event_name = cls.readJSON(getPath(state.generation_id))['event_name']
		
		if state.event_name in (CREATION.DONE, BREEDING.DONE, GENERATION.DONE, PROCESSUS.DONE):
			state.population = cls.getPopulation(state.processus_id, state.generation_id, state.generations)
		else:
			state.population = cls.getPopulation(state.processus_id, state.generation_id - 1, state.generations)
		
		if state.event_name in (GRADING.PROGRESS):
			state.grading = cls.readGrading(getPath(state.generation_id, 'grading'))
		elif state.event_name in (GRADING.DONE, SELECTION.START):
			grading = cls.readJSON(getPath(state.generation_id, 'final_grading'))
		else:
			pass
		
		if state.event_name in (SELECTION.DONE, BREEDING.START, BREEDING.PROGRESS):
			state.selection = cls.readJSON(getPath(state.generation_id, 'selection'))
		else:
			pass
		
		return state
