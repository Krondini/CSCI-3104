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
		new_entry = (input("Please enter a number: "))
		if (new_entry == ""): break

		input_arr.append(int(new_entry))

	answer = Q2b(input_arr, DP_table, len(input_arr) - 1)
	print("Total number of credits is: %d" % answer)


if __name__ == '__main__':
	main()