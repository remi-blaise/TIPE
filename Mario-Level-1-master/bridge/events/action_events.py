from lib.inject_arguments import injectArguments


class ActionEvent:
	"""Represents an input for the game"""
	
	@injectArguments
	def __init__(self, duration):
		self.key = self.__class__.key


class Jump(ActionEvent):
	key = 'jump'


class Left(ActionEvent):
	key = 'left'


class Right(ActionEvent):
	key = 'right'


class Down(ActionEvent):
	key = 'down'


class Fire(ActionEvent):
	key = 'action'
