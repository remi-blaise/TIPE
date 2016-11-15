#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments


class GameOptimizer:
	@inject_arguments
	def __init__(self, event_dispatcher):
		self.event_dispatcher.listen('game.frame', self.onFrame)
		self.event_dispatcher.listen('action', self.onAction)
	
	
	def onFrame(self, frame):
		# Reset
		if frame.current_frame < 5:
			self.action_detected = False
			self.mario_x = 0
			self.last_mario_x_change = 0
		
		if self.mario_x != frame.mario.rect.x:
			self.last_mario_x_change = frame.current_frame
		if frame.current_frame > self.last_mario_x_change + 150:
			self.event_dispatcher.dispatch('stop')
		self.mario_x = frame.mario.rect.x
		
		if frame.current_frame > 10 and not self.action_detected:
			self.event_dispatcher.dispatch('stop')
	
	
	def onAction(self, event):
		self.action_detected = True
