from sys import argv
import math
import random

def quickSelect(Arr, left, right, k):

	middle = ((right - left)//2) #Find the midpoint of the array

	if k == middle: #Base case
		return Arr[middle] 

	elif(k < middle): #Item we care about is less than the pivot
		return quickSelect(Arr, middle, right, k)

	else: #Item we care about is greater than the pivot
		return quickSelect(Arr, left, middle, k)


def calcIndex(N):
	print("Hello")

def main(argv):
	lst = [1, 2, 3, 4, 5]
	lst2 = []
	for i in range(10):
		lst2.append(random.randint(0, 100))

	lst2.sort()
	print(quickSelect(lst, 0, len(lst)-1, 3))
	print()
	print(quickSelect(lst2, 0, len(lst)-1, 4))


if __name__ == '__main__':
	main(argv)