import random
import sys
import matplotlib.pyplot as plt

def countFlips(n):
	arr = []
	for i in range(n):
		arr.append(i+1)
	
	# print(arr) Used for testing
	random.shuffle(arr)
	# print(arr) Used for testing 

	flips = 0
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if(arr[i] > arr[j]):
				flips += 1	
			

	return flips

def main(argv):
	sizeArr = 2
	arrN = []
	arrFlip = []
	while(sizeArr < 2**12):
		flips = countFlips(sizeArr)
		arrN.append(sizeArr)
		arrFlip.append(flips)
		print("\nNumber of flips for size %d is: %d" % (sizeArr, flips))	
		sizeArr *= 2
	fig = plt.figure()
	ax = plt.axes()
	plt.plot(arrN, arrFlip)
	plt.title("Number of Flips for Size n")
	plt.xlabel("Size of Array")
	plt.ylabel("Number of Flips")
	plt.show()
	#We can see that it takes roughly n/2 flips for an array of size n



if __name__ == '__main__':
	main(sys.argv)