from random import randint

def Q2bPartC(input_arr, n):
	
	if (n < 0):
		return 0

	else:
		return max(Q2bPartC(input_arr, n-1), input_arr[n] + Q2bPartC(input_arr, n-2))

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
	while True:
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