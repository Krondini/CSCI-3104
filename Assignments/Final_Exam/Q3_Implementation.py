'''
Author: Cat Rondini
Start Date: 12/5/19
'''
from random import randint

def EPIC(M, list_of_nums, left, right, n, p1_score):

	if left == right: return 0
	left = left+1 if (min(list_of_nums[left], list_of_nums[right]) == list_of_nums[left]) else left
	right = right-1 if (min(list_of_nums[left], list_of_nums[right]) == list_of_nums[right]) else right

	if M[n] != 0: return M[n]
		
	else:

		M[n] = min(p1_score + EPIC(M, list_of_nums, left+1, right-1, left+1, list_of_nums[left]), p1_score + EPIC(M, list_of_nums, left+1, right-1, right-1, list_of_nums[right])) 
		# print(M[n])
		return M[n]


def main():
	
	M = []
	num_cards = int(input("Please enter how many cards you would like to use for this game: "))
	for i in range(num_cards): M.append(0)

	list_of_nums = []
	for i in range(num_cards): list_of_nums.append(randint(0, 100))
	print(list_of_nums)

	result = EPIC(M, list_of_nums, 0, len(list_of_nums)-1, 0, 0)
	print("Your result is: %d" % result)
if __name__ == '__main__':
	main()