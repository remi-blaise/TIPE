#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from abc import ABCMeta
from lib.inherit_docstring import InheritableDocstrings


class ABCInheritableDocstringsMeta(InheritableDocstrings, ABCMeta):
	pass
