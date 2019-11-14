from sys import argv

def allignStrings(string_x, string_y, c_insert, c_delete, c_sub):
	print("allignStrings")

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
	print("main")

	for i in range(1, len(args)):
		new_data = readFile(args[i])
		print(new_data, end="\n\n")

	return 0

if __name__ == '__main__':
	main(argv)