from sys import argv
from string import ascii_uppercase
from random import randint, shuffle
from os import system
import matplotlib.pyplot as plt

def hash1(string_of_letters, dict_of_letters, num_buckets):

	index_sum = 0
	for letter in string_of_letters:
		index_sum += retIndex(letter, dict_of_letters)

	index_sum %= num_buckets


	return index_sum

def hash2(string_of_letters, dict_of_letters, num_buckets, random_int):
	
	index_sum = 0
	for letter in string_of_letters:
		sum_to_add = retIndex(letter, dict_of_letters) * random_int
		index_sum += sum_to_add

	index_sum %= num_buckets


	return index_sum	

def retIndex(letter, dict_of_letters):

	if letter not in ascii_uppercase: 
		letter = letter.upper()

	
	return dict_of_letters.get(letter)


def readFile(filename):

	fo = open(filename, 'r')

	words = []
	for line in fo:
		line = line.strip().split()
		words.append(line)

	return words

def main(args):
	
	dict_of_letters = {}
	counter = 1
	for letter in ascii_uppercase:
		dict_of_letters[letter] = counter
		counter += 1

	lines_from_file = readFile(args[1])
	num_buckets = int(args[2])
	univ_random_int = randint(0, num_buckets)

	print("File has %d lines" % len(lines_from_file))

	list_of_names = []

	for i in range(len(lines_from_file)): list_of_names.append(lines_from_file[i][0])
	
	shuffle(list_of_names)

	#Pick half of the names
	random_names = []
	for i in range(len(list_of_names)//2): random_names.append(list_of_names[i])


	#Histogram of hash1
	list_from_hash1 = []
	for i in range(len(random_names)):
		new_index = hash1(random_names[i], dict_of_letters, num_buckets)
		list_from_hash1.append(new_index)
		print(list_from_hash1[i])

	plt.hist(list_from_hash1, color="orange")
	plt.xlabel("Bucket Location")
	plt.ylabel("Length of Chain")
	plt.title("1st Hash Function")
	plt.savefig("Hash1.png")
	plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	#Histogram of hash2
	list_from_hash2 = []
	for i in range(len(random_names)):
		new_index = hash2(random_names[i], dict_of_letters, num_buckets, univ_random_int)
		list_from_hash2.append(new_index)
		print(list_from_hash2[i])

	plt.hist(list_from_hash2, color="green")
	plt.xlabel("Bucket Location")
	plt.ylabel("Length of Chain")
	plt.title("2nd Hash Function")
	plt.savefig("Hash2.png")
	plt.show()
	return 0

if __name__ == '__main__':
	main(argv)