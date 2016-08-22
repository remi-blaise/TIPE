__author__ = 'justinarmstrong'

from .. import setup, State
from .. import constants as c
from .. import game_sound
from ..components import info


class LoadScreen(State._State):
    def startup(self, current_frame, persist):
        self.start_frame = current_frame
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state, self.config, self.get_fps)
        self.sound_manager = game_sound.Sound(self.overhead_info, self.get_fps)


    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL1

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.LOAD_SCREEN


    def update(self, surface, keys, current_frame):
        """Updates the loading screen"""
        if (current_frame - self.start_frame) < 2.400*self.get_fps:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_frame - self.start_frame) < 2.600*self.get_fps:
            surface.fill(c.BLACK)

        elif (current_frame - self.start_frame) < 2.635*self.get_fps:
            surface.fill((106, 150, 252))

        else:
            self.done = True




class GameOver(LoadScreen):
    """A loading screen with Game Over"""

    def set_next_state(self):
        """Sets next state"""
        return c.MAIN_MENU

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.GAME_OVER

    def update(self, surface, keys, current_frame):
        self.current_frame = current_frame
        self.sound_manager.update(self.persist, None)

        if (self.current_frame - self.start_frame) < 7.000*self.get_fps:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_frame - self.start_frame) < 7.200*self.get_fps:
            surface.fill(c.BLACK)
        elif (self.current_frame - self.start_frame) < 7.235*self.get_fps:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):
    """Loading Screen with Time Out"""

    def set_next_state(self):
        """Sets next state"""
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """Sets the state to send to the overhead info object"""
        return c.TIME_OUT

    def update(self, surface, keys, current_frame):
        self.current_frame = current_frame

        if (self.current_frame - self.start_frame) < 2.400*self.get_fps:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True









