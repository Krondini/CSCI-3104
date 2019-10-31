import numpy as np
import sys
from random import randint

'''
Takes in two parameters
	list_tuples = list of tuples in the form (item_value, item_weight)
	max_weight = the maximum weight our knapsack can carry

First check if an item's weight is greater than the max_weight

Returns filled in array of item values
'''
def knapsack(list_tuples, max_weight):
	curr_element = list_tuples[0] #Current element is the first item
	if curr_element[1] < max_weight: #We can fit item in our knapsack
		return max(knapsack(list_tuples[1:], max_weight), curr_element[0] + knapsack(list_tuples[1:], max_weight- curr_element[1]))

	else: #Current item's weight is too large for knapsack
		return knapsack(list_tuples[1:], max_weight)


def main(argv):
	rows = int(input("Please enter the width of your array: "))
	cols = int(input("Please enter the height of your array: ")) + 1

	global_arr = []
	for row in range(rows):
		curr_row = []
		for col in range(cols):
			curr_row.append(0)
		global_arr.append(curr_row)

	for row in global_arr:
		print(row)



	# max_val = knapsack(global_arr, cols)
	# print(max_val)


if __name__ == '__main__':
	main(sys.argv)