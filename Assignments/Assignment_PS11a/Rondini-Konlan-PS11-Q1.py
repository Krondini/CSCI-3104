from sys import argv
from string import ascii_uppercase
from random import randint

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
		print(letter, sum_to_add)
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

	list_or_words = readFile(args[1])
	num_buckets = int(args[2])
	univ_random_int = randint(0, num_buckets)
	
	print(hash2(string_of_letters, dict_of_letters, num_buckets, univ_random_int))


if __name__ == '__main__':
	main(argv)