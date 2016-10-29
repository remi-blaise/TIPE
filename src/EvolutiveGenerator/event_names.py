#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments


class EventNameFactory:
	@inject_arguments
	def __init__(self, parent_name, progress = False):
		pass
	
	@property
	def START(self):
		return self.parent_name + '.start'
	
	@property
	def DONE(self):
		return self.parent_name + '.done'
	
	@property
	def PROGRESS(self):
		if self.progress:
			return self.parent_name + '.progress'
		else:
			raise ValueError(self.parent_name + '.progress event name does not exists.')


for parent_name in ['processus', 'creation', 'generation', 'selection']:
	exec("{1} = EventNameFactory('{0}')".format(parent_name, parent_name.upper()))

for parent_name in ['grading', 'breeding']:
	exec("{1} = EventNameFactory('{0}', True)".format(parent_name, parent_name.upper()))

PROCESSUS.RESUME = 'processus.resume'

assert SELECTION.DONE == 'selection.done'
