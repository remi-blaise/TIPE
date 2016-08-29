#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments


class ProcessusEvent:
	"""A processus event"""
	
	@inject_arguments
	def __init__(self, processus_id, generations = None, pop_length = None, proportion = None, chance = None):
		pass


class ProcessusStopEvent(ProcessusEvent):
	"""A processus stop event"""
	
	@inject_arguments
	def __init__(self, state, *args, **kwargs):
		super().__init__(*args, **kwargs)


class GenerationEvent(ProcessusEvent):
	"""A generation event"""
	
	@inject_arguments
	def __init__(self, generation_id, population = None):
		pass


class SelectionEvent(GenerationEvent):
	"""A selection event"""
	
	@inject_arguments
	def __init__(self, grading, selection, *args, **kwargs):
		super().__init__(*args, **kwargs)


class GradingEvent(SelectionEvent):
	"""A grading event"""
	
	@inject_arguments
	def __init__(self, ia = None, graduation = None, *args, **kwargs):
		GenerationEvent.__init__(self, *args, **kwargs)


class BreedingEvent(GenerationEvent):
	"""A breeding event"""
	
	@inject_arguments
	def __init__(self, offspring = None, parents = None, *args, **kwargs):
		super().__init__(*args, **kwargs)
