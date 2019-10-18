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

def n_logn_count(list_of_nums):
	print()

def main(argv):
	# range_of_nums = int(input("Please enter how many numbers you would like to generate: "))
	list_of_nums = []

	for i in range(int(argv[1])): #Generate list of nums
		list_of_nums.append(i+1)

	random.shuffle(list_of_nums) #Shuffle nums
	

	n_squared_flips = bubbleSort(list_of_nums)
	print("There are %d flips in our list!" % (n_squared_flips))
	

if __name__ == '__main__':
	main(sys.argv)