#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from json import dumps

from .JSONEncoder import JSONEncoder
from src.Writer.PathManager import PathManager


class Writer:
	"""Write IA in files"""
	
	
	def onProcessusStart(self, event):
		self.__dict__.update(event.__dict__)
		
		infos = event.__dict__.copy()
		infos.pop('processus_id')
		self.writeJSON(infos, self.getPath())
	
	def onCreationStart(self, event):
		self.onGenerationStart(event)
	
	def onGenerationStart(self, event):
		self.writeState('start', event)
	
	def onCreationDone(self, event):
		self.onGenerationDone(event)
		for ia in event.population:
			self.writeJSON(ia, self.getPath(event.generation_id, ia.id))
	
	def onGenerationDone(self, event):
		self.writeState('done', event)
	
	def onGenerationSelectionStart(self, event):
		self.writeState('selection', event)
	
	def onGenerationSelectionGradingStart(self, event):
		self.writeState('grading', event)
	
	def onGenerationSelectionGradingProgress(self, event):
		with self.getPath(event.generation_id, 'grading').open('a') as grading_file:
			grading_file.write(
				'{}: {}'.format(event.ia.id, event.graduation)
			)
	
	def onGenerationSelectionDone(self, event):
		self.writeJSON(
			[(score, ia.id) for (score, ia) in event.grading],
			self.getPath(event.generation_id, 'final_grading')
		)
		self.writeJSON(
			[ia.id for ia in event.selection],
			self.getPath(event.generation_id, 'selection')
		)
	
	def onGenerationBreedingStart(self, event):
		self.writeState('breeding', event)
	
	def onGenerationBreedingProgress(self, event):
		self.writeJSON(event.offspring, self.getPath(event.generation_id, event.offspring.id))
		with self.getPath(event.generation_id, 'breeding').open('a') as breeding_file:
			breeding_file.write(
				'{} + {} -> {}\n'.format(event.parents[0].id, event.parents[1].id, event.offspring.id)
			)
	
	
	def getPath(self, *args, **kwargs):
		return PathManager.getPath(self.processus_id, self.generations, self.pop_length, *args, **kwargs)
	
	def write(self, text, path):
		path.write_text(text)
	
	def writeJSON(self, data, path):
		self.write(dumps(data, cls=JSONEncoder, sort_keys=True, indent=4), path)
	
	def writeState(self, state, event):
		self.writeJSON({'state': state}, self.getPath(event.generation_id))
