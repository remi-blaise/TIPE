#!/usr/bin/env python3

import sys

from launch import launch
from config import Config
from eventdispatcher import EventDispatcher
from frame_reader import FrameReader
from simple_ia import IA


if __name__ == "__main__":
	print("start")
	event_dispatcher = EventDispatcher()
	reader = FrameReader(event_dispatcher)
	ia = IA(event_dispatcher)
	
	persist = launch(Config(False, event_dispatcher))
	
	print(persist)
	print("done")
	print(str(reader.frame_count) + " frames")
