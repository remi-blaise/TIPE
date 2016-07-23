from lib.inject_arguments import injectArguments


class Config:
	"""Configuration of the game"""
	
	@injectArguments
	def __init__(self, graphic_output = True, event_dispatcher = None, debug = True):
		self.show_game_frame = graphic_output # Jeu en accéléré, sans superflu # TODO: à mettre en argument indépendant
		self.allow_control = True #not bool(event_dispatcher) # Active les controles # TODO: à mettre en argument indépendant
		self.fps = 62.5 if self.show_game_frame else 0
		self.show_fps = debug
