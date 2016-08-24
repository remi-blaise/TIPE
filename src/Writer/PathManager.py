#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from pathlib import Path
from os import getcwd
from re import fullmatch


class PathManager:
	"""Make all paths
	
	This is a static class.
	"""
	
	ROOT = Path(getcwd() + '/results/')
	
	
	@classmethod
	def newProcessusId(cls):
		path = Path(cls.ROOT)
		ids = [-1]
		
		for folder in path.iterdir():
			match = fullmatch('processus-(\d+)', folder)
			if match is not None:
				ids.append(int(match[1]))
		
		return max(ids) + 1
	
	
	@classmethod
	def getPath(cls,
		processus_id, generations, pop_length,
		generation_id = None, ia_id_or_selection_file = None
	):
		path = Path(cls.ROOT)
		
		# processus-00000/...
		if processus_id is not None:
			path /= 'processus-' + '{0:05d}'.format(processus_id)
		
		# processus-00000/generation-00/...
		if generation_id is not None:
			path /= 'generation-' + '{0:0{1}d}'.format(generation_id, generations)
			
			# processus-00000/generation-00/selection/...
			if ia_id_or_selection_file in ('grading', 'selection'):
				path /= ia_id_or_selection_file
			# processus-00000/generation-00/population/ia-000
			elif type(ia_id_or_selection_file) is int:
				path /= 'initial_pop' if generation_id == 0 else 'population'
				ia_id = ia_id_or_selection_file
				if ia_id is not None:
					path /= 'ia-' + '{0:0{1}d}'.format(ia_id, pop_length)
				else:
					raise ValueError('ia_id not given')
			# processus-00000/generation-00/generation
			elif ia_id_or_selection_file is None:
				path /= 'generation'
			else:
				raise ValueError('wrong ia_id_or_selection_file value')
		# processus-00000/processus
		else:
			path /= 'processus'
		
		cls.makeDir(path.parent)
		
		return path
	
	
	@staticmethod
	def makeDir(path):
		path.mkdir(parents=True, exist_ok=True)
