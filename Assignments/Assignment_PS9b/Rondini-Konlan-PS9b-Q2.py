from random import randint

def Q2bPartC(input_arr, n):
	
	best_solution_1 = 0 #Best solution if you take the n-1 best case
	best_solution_2 = 0	#Best solution if you take the n-2 best case

	best_total_solution = 0

	for i in range(0, n+1):
		if (i%2 == 0): #Even cases
			best_solution_1 += input_arr[i]

		else: #Odd cases
			best_solution_2 += input_arr[i]

		best_total_solution = max(best_solution_1, best_solution_2)

	return best_total_solution

def Q2b(input_arr, DP_table, n):
	
	if (n < 0):
		return 0

	try:
		return DP_table[n]

	except IndexError:
		new_entry = max(Q2b(input_arr, DP_table, n-1), input_arr[n] + Q2b(input_arr, DP_table, n-2))
		DP_table.append(new_entry)
		return DP_table[n]

def main():
	
	input_arr = []
	DP_table = []

	while True: #Imput elements
		new_entry = (input("Please enter a number, enter nothing to stop: "))
		if (new_entry == ""): break

		input_arr.append(int(new_entry))
	
	# num_credits = int(input("Please enter how many classes are possible: "))
	# for i in range(num_credits):
	# 	input_arr.append(randint(1, 10))


	# print(input_arr)	

	answer = Q2bPartC(input_arr, len(input_arr) - 1)
	# answer = Q2b(input_arr, DP_table, len(input_arr) - 1)
	print("Total number of credits is: %d" % answer)


if __name__ == '__main__':
	main()