from lib.inject_arguments import inject_arguments


class Config:
	"""Configuration of the game"""
	
	@inject_arguments
	def __init__(self, graphic_output = True, event_dispatcher = None, time = 401, debug = True, allow_control = False):
		self.show_game_frame = graphic_output # Jeu en accéléré, sans superflu # TODO: à mettre en argument indépendant
		self.allow_control = allow_control #not bool(event_dispatcher) # Active les controles
		self.fps = 60 if self.show_game_frame else 0
		self.show_fps = debug
		self.play_sound = self.show_game_frame # TODO: à mettre en argument
		
