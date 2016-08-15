from lib.inject_arguments import injectArguments


class GameEvent:
	"""Represents an output from the game"""
	
	@injectArguments
	def __init__(self, current_frame):
		pass


class Frame(GameEvent):
	"""Emitted every frame"""
	
	@injectArguments
	def __init__(self, viewport, sprite_groups, mario, current_frame):
		pass


class DetectedComponent(GameEvent):
	"""Mario can see a component"""
	
	@injectArguments
	def __init__(self, rect, mario, current_frame):
		"""
		Attributes:
			rect 			Rect of the component
			mario 			Rect of Mario
			current_frame 	Current time
			
			Relative coordinates to Mario:
			left, top, right, bottom
		
		"""
		
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
