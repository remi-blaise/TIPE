#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from argparse import ArgumentParser

from lib.eventdispatcher import EventDispatcher
from mario.bridge.frame_reader import FrameReader
from .EvolutiveGenerator.Generator import Generator
from .factories.IAFactory import IAFactory
from .graduators.IAGraduator import IAGraduator
from .Writer.Writer import Writer
from .Logger.FileLogger import FileLogger
from .Logger.ConsoleLogger import ConsoleLogger
from .Writer.PathManager import PathManager
from .Writer.Reader import Reader


event_dispatcher = EventDispatcher()
reader = FrameReader(event_dispatcher)
generator = Generator(IAFactory, IAGraduator(event_dispatcher), [Writer(), FileLogger(), ConsoleLogger()])

def new(args):
	"""New processus"""
	population = generator.process(PathManager.newProcessusId(), args.generations, args.pop_length)

def resume(args):
	"""Resume a processus"""
	if not Reader.processusExists(args.processus_id):
		raise ValueError("Processus with id={} doesn't exist.".format(args.processus_id))
	population = generator.resume(Reader.getProcessusState(args.processus_id))

def play(args):
	"""Play the best individual of a processus' last generation"""
	pass


# Build parser
parser = ArgumentParser()
subparsers = parser.add_subparsers()

new_parser = subparsers.add_parser('new')
new_parser.add_argument('generations', type=int)
new_parser.add_argument('pop_length', type=int)
new_parser.set_defaults(command=new)

resume_parser = subparsers.add_parser('resume')
resume_parser.add_argument('processus_id', type=int)
resume_parser.set_defaults(command=resume)

play_parser = subparsers.add_parser('play')
play_parser.set_defaults(command=play)

# Parse arguments
args = parser.parse_args()
args.command(args)
