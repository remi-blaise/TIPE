from math import floor
from random import gauss

def gauss_int(a, b):
    n = b + 1
    while n > b or n < a:
        n = floor(gauss(b, (b-a)))
    return n

if __name__ == '__main__':
	count = [0] * 39
	for i in range(1000000):
		count[gauss_int(0, 38)] += 1
	print(count)
