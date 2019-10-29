from random import randint
from sys import argv
from math import sqrt
import numpy as np
import csv

def generateItems(num_items, max_weight):
	
	list_items = []

	for i in range(num_items):
		list_items.append((randint(1, (max_weight)//2), randint(1, 100)))

	return list_items

def main(args):

	num_items = int(args[1])
	max_weight = int(args[2])

	list_items = generateItems(num_items, max_weight)
	array_of_items = np.array(list_items)
	array_of_items.sort(axis=0)
	print(array_of_items)

	with open("Q1_Excel_Sheet.csv", 'w', newline='') as csvfile:
		line = csv.writer(csvfile)
		for i in range(len(array_of_items)):
			line.writerows([array_of_items[i]])
			# line.writerows(array_of_items[1])

	csvfile.close()

if __name__ == '__main__':
	main(argv)