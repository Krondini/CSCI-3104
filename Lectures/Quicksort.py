import random
import sys

def quicksort(Arr, left_bound, right_bound):
	if(left_bound < right_bound):
		pivot = partition(Arr, left_bound, right_bound)
		quicksort(Arr, left_bound, pivot-1)
		quicksort(Arr, pivot+1, right_bound)
	return

def partition(Arr, left_bound, right_bound):
	pivot = Arr[right_bound]
	i = left_bound - 1
	for j in range(left_bound, right_bound):
		if(Arr[j] < pivot):
			i += 1
			temp = Arr[i]
			Arr[i] = Arr[j]
			Arr[j] = temp
			# print(Arr)
	
	temp = Arr[i]
	Arr[i] = Arr[right_bound]
	Arr[right_bound] = temp
	return(i+1)

def main(argv):
	test_arr = [] #Establish array to be sorted
	for i in range(int(argv[1])):
		test_arr.append(random.randint(1, 100))

	print("Unsorted list: ", end="")
	print(test_arr)


	quicksort(test_arr, 0, len(test_arr)-1) #List is sorted
	print("Sorted list: ", end="")
	print(test_arr) 

	return 0

if __name__ == '__main__':
	main(sys.argv)