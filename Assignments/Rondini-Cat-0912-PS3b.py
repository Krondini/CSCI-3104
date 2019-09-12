import sys
import random

def calcStops(k, lst_pods):
	print("Hello")

def main(args):
	
	lst_pods = []
	lst_pods.append(0)

	#Create variables for k and size of Pods list
	k = args[1] #This is the max distance our robot can go
	Pods_locs = int(args[2]) #Number of pod locations

	#We build the test list here
	while len(lst_pods) < Pods_locs:
		new_int = round(random.uniform(1, 10)*10)
		if(new_int not in lst_pods):
			lst_pods.append(new_int)


	#Sort into ascending order
	lst_pods.sort()

	print(lst_pods)

if __name__ == '__main__':
	main(sys.argv)