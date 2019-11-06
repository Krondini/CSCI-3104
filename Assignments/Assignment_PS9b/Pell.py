from sys import argv
import time

M = []

def Pell(n):
	if(n == 0) or(n == 1):
		return n
	try:
		if M[n] != None:
			return M[n]
	except IndexError:
		return ((2*Pell(n-1)) + Pell(n-2))

def main(args):
	num_Pells = int(args[1])
	start = time.time()

	for i in range(num_Pells + 1):
		nth_Pell = Pell(i)
		M.append(nth_Pell)
		# print("The %dth Pell number is: %d" % (i, nth_Pell))
	print("The %dth Pell number is: %d" % (num_Pells, M[-1]))
	end = time.time()
	total = end - start
	print("Total time to calculate the first %d Pell numbers was: " % (num_Pells), end=" ")
	print(total, end=" ")
	print("seconds")

if __name__ == '__main__':
	main(argv)