#!/usr/bin/env python3

import set_dir

import sys

from launch import launch
from config import Config
from lib.eventdispatcher import EventDispatcher
from frame_reader import FrameReader
from simple_ia import IA


if __name__ == "__main__":
	print("start")
	event_dispatcher = EventDispatcher()
	reader = FrameReader(event_dispatcher)
	ia = IA(event_dispatcher)
	
	persist = launch(Config(False, event_dispatcher, allow_control=True))
	
	print(persist)
	print(persist['camera start x'] + reader.frame.mario.rect.x)
