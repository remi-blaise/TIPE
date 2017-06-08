#!/usr/bin/python3
# -*-coding:Utf-8 -*

from lib.inject_arguments import inject_arguments


class Result:
	"""Contain all informations to atribute a score to IA"""

	@inject_arguments
	def __init__(self, max_x, max_y):
		self.score = max_x + max_y
		self.percent = max_x / 8470


	def __le__(self, value):
		return self.score <= value.score

	def __lt__(self, value):
		return self.score < value.score

	def reprJSON(self):
		return self.__dict__


if __name__ == '__main__':
	r1 = Result(800, 100)
	r2 = Result(800, 50)
	print(r1 < r2)
	print(r1 <= r2)
	print(r1 == r2)
	print(r1 > r2)
	print(r1 >= r2)
