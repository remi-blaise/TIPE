#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class GeneratorManager:
	"""Manage Generator process
	
	Interact with the Generator during its process with the following methods:
		stop() Stop the Generator.
		pause() Stop the Generator and wait for resume().
		resume() Restart the Generator where it was when it paused.
	To see as a remote control of the Generator.
	"""
	
	
	def __init__(self):
		self.stopped = False
		self.processus_params = None
		self.waiting_for_stop = False
		self.process = None
	
	
	def onProcessusStop(self, event):
		if self.waiting_for_stop:
			self.processus_params = event.__dict__
			self.waiting_for_stop = False
	
	
	def start(self, processus_id, generations, pop_length = 500, proportion = .5, chance = 0):
		self.process(processus_id, generations, pop_length, proportion, chance)
	
	
	def stop(self):
		self.stopped = True
	
	
	def pause(self):
		self.stopped = True
		self.waiting_for_stop = True
	
	
	def resume(self):
		if (not self.stopped) or self.waiting_for_stop:
			raise RuntimeError("Try to resume Generator while it's not paused.")
		self.processus_params = None
		self.stopped = False
		self.process(**self.processus_params)
