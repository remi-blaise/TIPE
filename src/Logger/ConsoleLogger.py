#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from shutil import get_terminal_size

from .AbstractLogger import AbstractLogger
from lib.inherit_docstring import inherit_docstring
from src.meta.ABCInheritableDocstringsMeta import ABCInheritableDocstringsMeta


class ConsoleLogger(AbstractLogger, metaclass=ABCInheritableDocstringsMeta):
	"""Log Generator events into a file"""
	
	def __init__(self):
		self.first_line = False
		self.last_line = False
	
	def onProcessusResume(self, event):
		self.first_line = True
		super().onProcessusResume(event)
	
	def onProcessusStart(self, event):
		self.first_line = True
		super().onProcessusStart(event)
	
	def onProcessusDone(self, event):
		self.last_line = True
		super().onProcessusDone(event)
	
	
	@inherit_docstring
	def write(self, msg):
		msg = '  ' + msg
		length = get_terminal_size()[0]
		msg = msg[:length]
		print(('\n' if not self.first_line else '') + msg, end=('' if not self.last_line else '\n'), flush=True)
		self.first_line = False
	
	
	@inherit_docstring
	def overwrite(self, msg):
		msg = '  ' + msg
		length = get_terminal_size()[0]
		msg = msg[:length]
		print('\r' + msg + (length-len(msg)) * ' ', end='', flush=True)
