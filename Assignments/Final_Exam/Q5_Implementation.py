def sumsUp(M, n, list_of_nums, total):

	if total == 0: return True

	try:
		return M[n-1][total]

	except Exception:
		M[n-1][total] = sumsUp(M, n-2, list_of_nums, total) or sumsUp(M, n-2, list_of_nums, total-list_of_nums[n-1])


def main():

	M = []
	list_of_nums = []
	new_num = 0
	total = int(input("Please enter what you want to sum up to: "))
	while new_num != -1:
		new_num = input("Please enter a number to add: ")
		try:
			list_of_nums.append(int(new_num))
		except Exception as e:
			new_num = -1

	# print(list_of_nums)
	labels = []
	for i in range(total+1):
		labels.append(i)
	# M.append(row)
	
	for i in range(len(list_of_nums)):
		row = []
		for j in range(total):
			row.append(False)
		M.append(row)

	for i in range(len(M)): M[i][0] = True

	print(labels)
	for row in M:
		print(row)

	result = sumsUp(M, len(list_of_nums), list_of_nums, total)
	for row in M:
		print(row)	
	print("Final Result is: %r" % result)

if __name__ == '__main__':
	main()