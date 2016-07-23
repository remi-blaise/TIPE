class GameEvent:
	"""Represents an output from the game"""
	pass


class Frame(GameEvent):
	"""Emitted every frame"""
	
	def __init__(self, viewport, sprite_groups, mario):
		self.viewport = viewport
		self.sprite_groups = sprite_groups
		self.mario = mario


class DetectedComponent(GameEvent):
	"""Mario can see a component"""
	
	def __init__(self, rect, mario):
		"""
		Attributes:
			rect 	Rect of the component
			mario 	Rect of Mario
			
			Relative coordinates to Mario:
			left, top, right, bottom
		
		"""
		self.rect = rect
		self.mario = mario
		
		for i, edge in enumerate(('left', 'top', 'right', 'bottom')):
			value = getattr(rect, edge) - (mario.x if not i%2 else mario.y)
			setattr(self, edge, value)
	
	
	def __repr__(self):
		return self.__class__.__name__ + '({},{})'.format(self.left, self.top, self.right, self.bottom)


class Block(DetectedComponent):
	pass


class Enemy(DetectedComponent):
	pass


class Powerup(DetectedComponent):
	pass


class Coin(DetectedComponent):
	pass
