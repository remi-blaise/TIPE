#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.inherit_docstring import InheritableDocstrings, inherit_docstring
from random import choice, randint

from mario.data.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.EvolutiveGenerator.GeneticElementFactory import GeneticElementFactory
from src.entities.GameEventData import GameEventData


class GameEventDataFactory(GeneticElementFactory, metaclass=InheritableDocstrings):
	"""GameEventData factory"""
	
	@property
	@inherit_docstring
	def genetic_element_class(self):
		return GameEventData
	
	GAME_EVENT_NAMES = ('game.block', 'game.enemy')
	
	MIN_X = -int(SCREEN_WIDTH / 2) # max left
	MAX_X = SCREEN_WIDTH # max right
	MIN_Y = -GROUND_HEIGHT # max top
	MAX_Y = SCREEN_HEIGHT # max bottom
	
	
	@classmethod
	@inherit_docstring
	def create(cls):
		return GameEventData(cls.createEventName(), cls.createCoor())
	
	@classmethod
	@inherit_docstring
	def mutate(cls, element):
		if randint(0, 1):
			element.event_name = cls.createEventName()
		else:
			element.coor = mutateCoor(element.coor)
	
	
	@classmethod
	def createEventName(cls):
		return choice(cls.GAME_EVENT_NAMES)
	
	@classmethod
	def createCoor(cls):
		return {
			'x': randint(cls.MIN_X, cls.MAX_X),
			'y': randint(cls.MIN_Y, cls.MAX_Y)
		}
	
	@classmethod
	def mutateCoor(cls, coor):
		coor.x += randint(-100, 100)
		coor.y += randint(-100, 100)
		
		coor.x = cls.MIN_X if coor.x < cls.MIN_X
		coor.x = cls.MAX_X if coor.x > cls.MAX_X
		coor.y = cls.MIN_Y if coor.y < cls.MIN_Y
		coor.y = cls.MAX_Y if coor.y > cls.MAX_Y
		return coor
