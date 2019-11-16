from sys import argv
from os import system

def allignStrings(string_x, string_y, c_insert, c_delete, c_sub):
	# print("allignStrings")
	length = 0
	orig_c_sub = c_sub

	if(len(string_x) > len(string_y)):
		length = len(string_x)
	else:
		length = len(string_y)

	S = []
	for i in range(length+2):
		sublist = []
		for j in range(length+2):
			sublist.append(0)
		S.append(sublist)

	S[0][1] = '_'
	for i in range(2, len(S[0])):
		try:
			S[0][i] = string_x[i-2]
			S[1][i] = i-1
		except IndexError:
			S[0][i] = '_'
			S[1][i] = S[i-1][1]

	S[1][0] = '_'
	for i in range(2, len(S)):
		try:
			S[i][0] = string_y[i-2]
			S[i][1] = i-1
		except IndexError:
			S[i][0] = '_'
			S[i][1] = S[i-1][1]

	for i in range(2, len(S[0])):
		for j in range(2, length+2):
			if S[0][j] == S[i][0]:
				c_sub = 0
			else:
				c_sub = orig_c_sub
			S[i][j] = min(S[i-1][j] + c_delete, S[i][j-1] + c_insert, S[i-1][j-1] + c_sub)

	return S


def extractAllignment(S_matrix, string_x, string_y, c_insert, c_delete, c_sub):
	print("extractAllignment")


def commonSubstrings(string_x, int_L, opt_edits):
	print("commonSubstrings")


def readFile(filename):

	list_of_words = []
	fo = open(filename, 'r')

	for line in fo:
		line = line.strip().split()
		list_of_words.append(line)

	return list_of_words


def main(args):
	# print("main")

	file1 = args[1] #Read in file 1 for Plagerism Detector
	file2 = args[2] #Read in file 2 for Plagerism Detector

	string_x = input("Please enter your first string: ")
	string_y = input("Please enter your second string: ")
	c_insert = int(input("Please enter the cost of an insert: "))
	c_delete = int(input("Please enter the cost of a delete: "))
	c_sub = int(input("Please enter the cost of a substitute: "))
	S = allignStrings(string_x, string_y, c_insert, c_delete, c_sub)

	# system("clear") #Clear screen

	# for i in range(1, len(S[0])):
	# 	S[0][i] = string_x[i-1]
	#
	# for i in range(1, len(S)):
	# 	S[i][0] = string_y[i-1]

	for i in range(len(S)):
		print(S[i])


	return 0

if __name__ == '__main__':
	main(argv)
