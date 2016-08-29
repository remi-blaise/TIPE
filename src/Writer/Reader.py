#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from json import loads
from re import fullmatch

from .JSONEncoder import JSONEncoder
from .Writer.PathManager import PathManager
from src.factories.IAFactory import IAFactory


class Reader:
	"""Read files
	
	This is a static class.
	
	Public API:
		processusExists(processus_id)
		getProcessusData(processus_id)
	"""
	
	
	@staticmethod
	def getPath(*args, **kwargs):
		PathManager.getPath(*args, **kwargs, read_only=True)
	
	
	@staticmethod
	def readJSON(path):
		loads(path.read_text())
	
	
	@staticmethod
	def readGrading(path):
		grading = []
		with path.open('r') as grading_file:
			for line in grading_file:
				try:
					graduation_tuple = fullmatch('([0-9]+): ([0-9]+)', line).group(1, 2)
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
	def getPopulation(self, processus_id, generation_id, generations):
		population = set()
		for ia_file in cls.getPath(processus_id, generations, None, generation_id).iterdir():
			population.add(IAFactory.hydrate(cls.readJSON(ia_file)))
		return population
	
	
	@classmethod
	def processusExists(cls, processus_id):
		path = cls.getPath(processus_id)
		if not path.parent.exists():
			return False
		return True
	
	
	@classmethod
	def getProcessusData(cls, processus_id):
		processus_params = cls.getProcessusParams(processus_id)
		
		getPath = lambda generation_id, file_name = None: cls.getPath(
			processus_id, processus_params['generations'], None, generation_id, file_name
		)
		
		# Get first inexistant generation
		generation_id = 0
		while getPath(generation_id).parent.exists():
			generation_id += 1
		
		# If none generation folder exist
		if generation_id == 0:
			return {'processus_id': processus_id, 'processus_params': processus_params}
		
		# Determine current generation and get its state
		# Generation state in (start, grading, selection, breeding, done)
		state = 'start'
		last_existing_state = cls.readJSON(getPath(generation_id - 1))['state']
		if last_existing_state != 'done':
			generation_id -= 1
			state = last_existing_state
		
		# Get relevant datas
		population = None
		grading = None
		selection = None
		
		if state in ('start', 'grading'):
			population = cls.getPopulation(
				processus_id, generation_id - 1, processus_params['generations']
			)
		if state == 'grading':
			grading = cls.readGrading(getPath(generation_id, 'grading'))
		if state == 'selection':
			grading = cls.readJSON(getPath(generation_id, 'final_grading'))
		if state == 'breeding':
			selection = cls.readJSON(getPath(generation_id, 'selection'))
		if state in ('breeding', 'done'):
			population = cls.getPopulation(
				processus_id, generation_id, processus_params['generations']
			)
		
		return {
			'processus_id': processus_id, 'processus_params': processus_params,
			'generation_id': generation_id, 'state': state,
			'population': population, 'grading': grading, 'selection': selection
		}
