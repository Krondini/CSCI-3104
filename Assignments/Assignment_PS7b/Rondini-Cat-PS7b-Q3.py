'''
# Takes in a list and its bounds as parameters
# Function will split the list in half recursively 
# in order to search for the maximum h-index 
# Will return the maximum h-index of the list
'''
def calcIndex(N, left, right):
	
	median = len(N)//2

	if (len(N)%2) == 0: #Even number of elements, adjust median
		median -= 1

	if N[median+1] >= median+2: #h-index is larger than the median
		return calcIndex(N, median+1, right)	

	elif(N[median] >= median+1):
		return median + 1

	else:
		return calcIndex(N, left, median-1)

def main():
	
	lst = [7, 6, 4, 3, 1, 0] #Even elements test

	print(lst)
	print(calcIndex(lst, 0, len(lst)-1))

	lst2 = [6, 5, 3, 1, 0] #Odd elements test
	print(lst2)
	print(calcIndex(lst2, 0, len(lst2)-1))

if __name__ == '__main__':
	main()