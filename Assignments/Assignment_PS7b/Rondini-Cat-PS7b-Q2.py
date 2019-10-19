import random
import sys


def bubbleSort(list_of_nums):
	
	num_flips = 0
	
	for i in range(len(list_of_nums)):
		for j in range(0, len(list_of_nums)-i-1):
			if list_of_nums[j] > list_of_nums[j+1]:
				num_flips += 1
				list_of_nums[j], list_of_nums[j+1] = list_of_nums[j+1], list_of_nums[j]

	return num_flips

def partition(A, left, right):
	low = (left-1)
	pivot = A[right]

	for i in range(left, right):
		if A[i] < pivot:
			low += 1
			A[low], A[i] = A[i], A[low]

	A[low+1], A[right] = A[right], A[i+1]
	return (i+1)

def quickSort(list_of_nums, left, right):
	if (left<right):
		q = partition(list_of_nums, left, right)
		quickSort(list_of_nums, left, q-1)
		quickSort(list_of_nums, q+1, right)

def main(argv):
	# range_of_nums = int(input("Please enter how many numbers you would like to generate: "))
	list_of_nums = []

	for i in range(int(argv[1])): #Generate list of nums
		list_of_nums.append(i+1)

	random.shuffle(list_of_nums) #Shuffle nums
	

	n_squared_flips = bubbleSort(list_of_nums)
	print("There are %d flips in our list!" % (n_squared_flips))
	print()

	random.shuffle(list_of_nums)
	print(list_of_nums)
	print()

	quickSort(list_of_nums, 0, len(list_of_nums)-1)
	print(list_of_nums)

if __name__ == '__main__':
	main(sys.argv)