#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from .AbstractLogger import AbstractLogger
from lib.inherit_docstring import inherit_docstring
from src.meta.ABCInheritableDocstringsMeta import ABCInheritableDocstringsMeta
from src.Writer.PathManager import PathManager


class FileLogger(AbstractLogger, metaclass=ABCInheritableDocstringsMeta):
	"""Log Generator events into a file"""
	
	
	def onProcessusResume(self, event):
		self.processus_id = event.processus_id
	
	def onProcessusStart(self, event):
		self.onProcessusResume(event)
		super().onProcessusStart(event)
	
	
	@inherit_docstring
	def write(self, msg):
		with PathManager.getPath(self.processus_id).with_name('log').open('a') as f:
			f.write(msg + '\n')
	
	
	@inherit_docstring
	def overwrite(self, msg):
		with PathManager.getPath(self.processus_id).with_name('log').open('r') as f:
			lines = f.readlines()
		with PathManager.getPath(self.processus_id).with_name('log').open('w') as f:
			f.writelines([item for item in lines[:-1]])
			f.write(msg + '\n')
