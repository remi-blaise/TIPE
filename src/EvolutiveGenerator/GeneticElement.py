#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from abc import ABCMeta


class GeneticElement(metaclass=ABCMeta):
	"""Carry the genetic information
	
	This is an abstract class to inherit.
	A genetic element carries one or several genetic informations or contains
	other genetic elements.
	
	Evolution logic is handled by an external GeneticElementFactory.
	"""
	
	pass
