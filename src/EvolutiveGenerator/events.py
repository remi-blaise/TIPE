#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments


class ProcessusEvent:
	"""A processus event"""
	
	@inject_arguments
	def __init__(self, processus_id):
		pass


class GenerationEvent(ProcessusEvent):
	"""A generation event"""
	
	@inject_arguments
	def __init__(self, processus_id, generation_id, population = None):
		pass


class SelectionEvent(GenerationEvent):
	"""A selection event"""
	
	@inject_arguments
	def __init__(self, grading, selection, *args, **kwargs):
		super().__init__(*args, **kwargs)


class GradingEvent(SelectionEvent):
	"""A grading event"""
	
	@inject_arguments
	def __init__(self, graduation = None, *args, **kwargs):
		GenerationEvent.__init__(self, *args, **kwargs)


class BreedingEvent(GenerationEvent):
	"""A breeding event"""
	
	@inject_arguments
	def __init__(self, offspring = None, *args, **kwargs):
		super().__init__(*args, **kwargs)
