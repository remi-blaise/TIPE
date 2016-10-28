#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from lib.eventdispatcher import EventDispatcher
from mario.bridge.frame_reader import FrameReader
from .EvolutiveGenerator.Generator import Generator
from .factories.IAFactory import IAFactory
from .graduators.IAGraduator import IAGraduator
from .Writer.Writer import Writer
from .Logger.FileLogger import FileLogger
from .Logger.ConsoleLogger import ConsoleLogger
from .Writer.PathManager import PathManager


event_dispatcher = EventDispatcher()
reader = FrameReader(event_dispatcher)
generator = Generator(IAFactory, IAGraduator(event_dispatcher), [Writer(), FileLogger(), ConsoleLogger()])

population = generator.process(PathManager.newProcessusId(), 1, 10)

# print(population)
