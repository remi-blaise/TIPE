#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from src.EvolutiveGenerator.GeneratorManager import GeneratorManager as BaseManager
from .PathManager import PathManager
from .Reader import Reader


class GeneratorManager(BaseManager):
	"""Manage Generator process
	
	"""
	
	
	def startNew(self, *args, **kwargs):
		"""Start Generator with a new processus id"""
		self.start(PathManager.newProcessusId(), *args, **kwargs)
	
	
	def restart(self, processus_id):
		"""Resume a previously stopped processus"""
		self.stopped = True
		processus_data = Reader.getProcessusData(processus_id)
		self.
		self.processus_params = processus_data['processus_params']
		self.processus_params.update({'processus_id': processus_id, 'state': processus_data['state']})
		self.resume()
