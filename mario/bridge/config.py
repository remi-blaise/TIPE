from lib.inject_arguments import inject_arguments


class Config:
	"""Configuration of the game"""
	
	@inject_arguments
	def __init__(self, graphic_output = True, event_dispatcher = None, debug = True):
		self.show_game_frame = graphic_output # Jeu en accéléré, sans superflu # TODO: à mettre en argument indépendant
		self.allow_control = True #not bool(event_dispatcher) # Active les controles # TODO: à mettre en argument indépendant
		self.fps = 60 if self.show_game_frame else 0
		self.show_fps = debug
