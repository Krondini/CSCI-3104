from sys import argv
import time
import os

M = [1, 1]

def Pell(n):
	if(n == 0) or (n == 1):
		return 1

	else:
		return((2*Pell(n-1)) + Pell(n-2))


def memoPell(n):
	if(n == 0) or(n == 1):
		return 1


	try:
		if M[n] != None:
			return M[n]

	except IndexError:
		return ((2*memoPell(n-1)) + memoPell(n-2))

def bottomUpPell(n, P):
	for i in range(2, n):
		P.append(2*P[i-1] + P[i-2])

	print(P)
	return P[-1]

def constantSpacePell(n):
	Pell_0 = 1
	Pell_1 = 1
	next_Pell = 0
	for i in range(2, n):
		next_Pell = (2*Pell_0 + Pell_1)
		Pell_0 = Pell_1
		Pell_1 = next_Pell
		print("The current Pell number is: %d" % next_Pell)

	return next_Pell

def main(args):
	num_Pells = int(args[1])
	start = time.time() #Begin timing

	# print(bottomUpPell(num_Pells, M))

	print(constantSpacePell(num_Pells))
	# for i in range(num_Pells + 1): #Generate Pell numbers
	# 	nth_Pell = memoPell(i)
	# 	M.append(nth_Pell)
	# 	print("The %dth Pell number is: %d" % (i, nth_Pell))


	# os.system("clear") #Clear screen
	

	# print("The %dth Pell number is: %d" % (num_Pells, M[-1]))
	end = time.time() #End timing
	total = end - start #Calculate timing
	print("Total time to calculate the first %d Pell numbers was: " % (num_Pells), end=" ")
	print(total, end=" ")
	print("seconds")

if __name__ == '__main__':
	main(argv)