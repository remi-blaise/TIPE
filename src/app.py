#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from argparse import ArgumentParser
from math import inf

from lib.eventdispatcher import EventDispatcher
from mario.bridge.frame_reader import FrameReader
from mario.bridge.config import Config
from .EvolutiveGenerator.Generator import Generator
from .factories.IAFactory import IAFactory
from .graduators.IAGraduator import IAGraduator
from .Writer.Writer import Writer
from .Logger.FileLogger import FileLogger
from .Logger.ConsoleLogger import ConsoleLogger
from .Writer.PathManager import PathManager
from .Writer.Reader import Reader


def instanciateGenerator():
	event_dispatcher = EventDispatcher()
	FrameReader(event_dispatcher)
	return Generator(IAFactory, IAGraduator(event_dispatcher), [Writer(), FileLogger(), ConsoleLogger()],
		lambda state: True in [8470 <= score for score, individual in state.grading]
	)

def new(args):
	"""New processus"""
	population = instanciateGenerator().process(PathManager.newProcessusId(), args.generations, args.pop_length)

def resume(args):
	"""Resume a processus"""
	if not Reader.processusExists(args.processus_id):
		raise ValueError("Processus with id={} doesn't exist.".format(args.processus_id))
	population = instanciateGenerator().resume(Reader.getProcessusState(args.processus_id))

def play(args):
	"""Play the best individual of a processus' last generation"""
	if not Reader.processusExists(args.processus_id):
		raise ValueError("Processus with id={} doesn't exist.".format(args.processus_id))
	# Get IA
	ia = Reader.getBestIa(args.processus_id)
	print('The best AI is {}.'.format(ia.id))
	# Play IA
	event_dispatcher = EventDispatcher()
	FrameReader(event_dispatcher)
	score = IAGraduator(event_dispatcher).gradeIAWithConfig(ia, Config(True, event_dispatcher, time=10))


# Build parser
parser = ArgumentParser()
subparsers = parser.add_subparsers()

new_parser = subparsers.add_parser('new')
new_parser.add_argument('pop_length', type=int)
new_parser.add_argument('--generations', default=inf, type=int)
new_parser.set_defaults(command=new)

resume_parser = subparsers.add_parser('resume')
resume_parser.add_argument('processus_id', type=int)
resume_parser.set_defaults(command=resume)

play_parser = subparsers.add_parser('play')
play_parser.add_argument('processus_id', type=int)
play_parser.set_defaults(command=play)

# Parse arguments
args = parser.parse_args()
if hasattr(args, 'command'):
	args.command(args)
else:
	print('No command given, use --help')
