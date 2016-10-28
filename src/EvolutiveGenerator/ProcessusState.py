#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


class ProcessusState:
	"""Store processus state data"""
	
	def __init__(self):
		"""
		Parameters:
			processus_id
			generations, pop_length
			proportion, chance
		
		State data:
			Data 			Description 					Updated before
			---------------|-------------------------------|----------------------------
			event_name 		The emitted event name 			*
			population 		The population 					creation.done, breeding.done
			generation_id 	The generation id 				generation.start
			individual 		The graded individual 			grading.progress
			graduation 		Graduation of the individual 	grading.progress
			grading 		The grading 					grading.stop
			selection 		The selection 					selection.done
			offspring 		The offspring 					breeding.progress
			parents 		Parents of the offspring 		breeding.progress
		
		Pay attention, data is READ-WRITE!
		"""
		
		## Parameters
		self.processus_id = None
		self.generations = None
		self.pop_length = None
		self.proportion = None
		self.chance = None
		
		## State data
		self.event_name = None
		# generation
		self.generation_id = None
		# grading
		self.individual = None #progress
		self.graduation = None #progress
		self.grading = None
		# selection
		self.selection = None
		# breeding
		self.offspring = None #progress
		self.parents = None #progress
		self.population = None
