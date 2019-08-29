import sys
import csv

def insertionSort(arr):
	
	key = arr[0]



def main(argv):

	try:
		if(argv[1]):
			with open(argv[1]) as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				for row in csv_reader:
					for element in row:
						element = int(element)

				insertionSort(argv[1])

			close(csv_file)

	except Exception as e:
		raise e


if __name__ == '__main__':
	main(sys.argv)