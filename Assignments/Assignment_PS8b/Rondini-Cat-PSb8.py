from sys import argv
import numpy as np

np.random.seed(0)

def quickSelect(A, left, right, split):
	print("hello")

def main(args):
	num_array = np.random.randint(int(args[1]), size=int(args[2]))
	for i in num_array:
		print(i)

if __name__ == '__main__':
	main(argv)