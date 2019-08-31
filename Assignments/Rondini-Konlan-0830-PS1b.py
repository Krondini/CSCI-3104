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
		if(arr[i] > i+1):
			flips += 1

	return flips

def makePlot(n, numFlips):
	print("Hello")
	
	plt.show()

def main(argv):
	sizeArr = 2
	arrN = []
	arrFlip = []
	while(sizeArr < 2**20):
		flips = countFlips(sizeArr)
		arrN.append(sizeArr)
		arrFlip.append(flips)
		print("\nNumber of flips for size %d is: %d" % (sizeArr, flips))	
		sizeArr *= 2
	fig = plt.figure()
	ax = plt.axes()
	#We can see that it takes roughly n/2 flips for an array of size n



if __name__ == '__main__':
	main(sys.argv)