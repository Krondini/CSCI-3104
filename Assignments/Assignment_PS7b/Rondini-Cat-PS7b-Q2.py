import random
import sys
import matplotlib
import matplotlib.pyplot as plt

def bubbleSort(list_of_nums):
	
	num_flips = 0
	
	for i in range(len(list_of_nums)):
		for j in range(0, len(list_of_nums)-i-1):
			if list_of_nums[j] > list_of_nums[j+1]:
				num_flips += 1
				list_of_nums[j], list_of_nums[j+1] = list_of_nums[j+1], list_of_nums[j]

	return num_flips

def partition(A, left, right):
	low = (left-1) #Marker for lower boundary
	pivot = A[right] #Pivot element

	for i in range(left, right):
		if A[i] < pivot: #Element belongs in lower boundary
			low += 1 #Elongate lower bound
			A[low], A[i] = A[i], A[low] #Swap

	A[low+1], A[right] = A[right], A[low+1] #Swap final elements
	return (low+1) #Return the boundary marker

def quickSort(list_of_nums, left, right, num_flips):
	if (left<right): #Check for base case
		q = partition(list_of_nums, left, right) 
		num_flips = quickSort(list_of_nums, left, q-1, num_flips) #Call on left side
		num_flips = quickSort(list_of_nums, q+1, right, num_flips) #Call on right side

	return num_flips+1 #Increment counter


def main(argv):
	# range_of_nums = int(input("Please enter how many numbers you would like to generate: "))
	list_of_nums = []
	list_of_square_inputs = []
	list_of_square_flips = []
	list_of_lgn_inputs = []
	list_of_lgn_flips = []

	for j in range(1, 12):
		for i in range(2**j): #Generate list of nums
			list_of_nums.append(i+1)

		list_of_square_inputs.append(i)
		list_of_lgn_inputs.append(i)

		random.shuffle(list_of_nums) #Shuffle nums
		

		n_squared_flips = bubbleSort(list_of_nums)
		print("There are %d flips in our list!" % (n_squared_flips))
		list_of_square_flips.append(n_squared_flips)

		random.shuffle(list_of_nums)


		n_lgn_flips = quickSort(list_of_nums, 0, len(list_of_nums)-1, 0)
		print("There are %d flips in our list!" % (n_lgn_flips))
		print()
		list_of_lgn_flips.append(n_lgn_flips)

	fig1, n_lgn = plt.subplots()
	fig2, n_squared = plt.subplots()

	n_lgn.plot(list_of_lgn_inputs, list_of_lgn_flips)
	n_lgn.set(xlabel="Size of inputs (2^n)", ylabel="Number of flips", title="Quick Sort")

	n_squared.plot(list_of_square_inputs, list_of_square_flips)
	n_squared.set(xlabel="Size of inputs (2^n)", ylabel="Number of flips", title="Bubble Sort")


	fig1.savefig("BubbleSort.png")
	fig2.savefig("QuickSort.png")

	plt.show()




if __name__ == '__main__':
	main(sys.argv)