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
		cls.makeDir(path)
		ids = [-1]
		
		for folder in path.iterdir():
			match = fullmatch('processus-(\d+)', folder.name)
			if match is not None:
				ids.append(int(match.group(1)))
		
		return max(ids) + 1
	
	
	@classmethod
	def getPath(cls,
		processus_id, generations = None,
		generation_id = None, ia_id_or_file = None, read_only = False
	):
		path = Path(cls.ROOT)
		
		# processus-00000/
		path /= 'processus-' + '{0:05d}'.format(processus_id)
		
		# processus-00000/generation-00/...
		if generation_id is not None:
			generations = generations if type(generations) is int else '00000'
			path /= 'generation-' + '{0:0{1}d}'.format(generation_id, len(str(generations)))
			
			# processus-00000/generation-00/selection/...
			if ia_id_or_file in ('grading', 'final_grading', 'selection'):
				path /= 'selection/' + ia_id_or_file
			# processus-00000/generation-00/population/ia-000
			elif type(ia_id_or_file) is int:
				path /= 'initial_pop' if generation_id == 0 else 'population'
				ia_id = ia_id_or_file
				if ia_id is not None:
					path /= 'ia-{}.json'.format(ia_id)
				else:
					raise ValueError('ia_id not given')
			# processus-00000/generation-00/breeding
			elif ia_id_or_file == 'breeding':
				path /= 'breeding'
			# processus-00000/generation-00/generation
			elif ia_id_or_file is None:
				path /= 'generation'
			else:
				raise ValueError('wrong ia_id_or_file value')
		# processus-00000/processus
		else:
			path /= 'processus'
		
		if (
			path.name in ('generation', 'processus', 'final_grading', 'selection')
			or path.parent.name == 'population'
		):
			path = path.with_suffix('.json')
		
		if not read_only:
			cls.makeDir(path.parent)
		
		return path
	
	
	@staticmethod
	def makeDir(path):
		path.mkdir(parents=True, exist_ok=True)
