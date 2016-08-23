#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import sys

from mario.bridge.eventdispatcher import EventDispatcher
from mario.bridge.frame_reader import FrameReader
from src.EvolutiveGenerator.Generator import Generator
from src.factories.IAFactory import IAFactory
from src.graduators.IAGraduator import IAGraduator


event_dispatcher = EventDispatcher()
reader = FrameReader(event_dispatcher)
generator = Generator(IAFactory, IAGraduator(event_dispatcher))

population = generator.process(5, 10)

print(population)
