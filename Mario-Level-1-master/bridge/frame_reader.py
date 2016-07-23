import pygame as pg
from lib.inject_arguments import injectArguments

from bridge.events.game_events import *


class FrameReader:
	"""Read the Frame event and make other game events"""
	
	@injectArguments
	def __init__(self, event_dispatcher):
		self.event_dispatcher.listen('game.frame', self.handle_frame)
		self.frame_count = 0
		self.frame = None
	
	@injectArguments
	def handle_frame(self, frame):
		self.frame_count += 1
		
		blocks = []
		for block_group in ['brick_group', 'coin_box_group', 'ground_group', 'pipe_group', 'step_group']:
			blocks.extend(frame.sprite_groups[block_group].sprites())
		viewport_sprite = ViewportSprite(frame.viewport)
		displayed_blocks = pg.sprite.spritecollide(viewport_sprite, blocks, False)
		
		#debug
		pg.display.set_caption("Displayed blocks = " + str(len(displayed_blocks)))
		
		# Make the events and dispatch
		for block in displayed_blocks:
			self.event_dispatcher.dispatch('game.block', Block(block.rect, frame.mario.rect))
			if self.frame_count == 1:
				print('game.block', Block(block.rect, frame.mario.rect))
		
		print('frame')


class ViewportSprite(pg.sprite.Sprite):
	"""A false sprite containing viewport"""
	
	def __init__(self, viewport_rect):
		pg.sprite.Sprite.__init__(self)
		self.rect = viewport_rect
