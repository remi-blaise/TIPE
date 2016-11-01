#!/usr/bin/env python3

import set_dir

from launch import launch
from config import Config
from lib.eventdispatcher import EventDispatcher
from frame_reader import FrameReader

if __name__ == "__main__":
	event_dispatcher = EventDispatcher()
	reader = FrameReader(event_dispatcher)
	
	persist = launch(Config(True, event_dispatcher, allow_control=True))
	
	print(persist)
	print(persist['camera start x'] + reader.frame.mario.rect.x)
