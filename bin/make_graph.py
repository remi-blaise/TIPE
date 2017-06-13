#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from argparse import ArgumentParser
import matplotlib.pyplot as plt

parser = ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
parser.add_argument('param', type=str)
parser.add_argument('little', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as file:
    lines = file.readlines()
    del lines[0]
    results = [[int(i) for i in line[:-1].split(',')[1:]] for line in lines]

moyennes = [sum(gen)/len(gen) for gen in results]
maximums = [max(gen) for gen in results]

if args.little == 'little':
	plt.figure(figsize=(8, 3))

# Plot
plt.plot(range(len(results)), moyennes)
plt.plot(range(len(results)), maximums, 'r')
plt.ylabel('Scores' if args.param == 'score' else 'Distances')
plt.xlabel("Générations")
plt.legend([
	'Score moyen' if args.param == 'score' else 'Distance moyenne',
	'Score maximal' if args.param == 'score' else 'Distance maximale'
])
plt.title("Évolution des " + args.param + "s en fonction des générations")
plt.grid()

# Produce output
# plt.show()

if not args.little == 'little':
	plt.savefig(args.output_file + '.png')
else:
	plt.tight_layout()
	plt.savefig(args.output_file + '.little.png')
