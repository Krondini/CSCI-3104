import sys
import random

def calcStops(k, lst_pods):
	stop_pods = []
	curr_loc = lst_pods[0] #Placeholder for robot's current location
	remaining_dist = k
	for i in range(len(lst_pods) - 1): #Checking possibily of completion
		if(lst_pods[i+1] - lst_pods[i]) > k:
			return "Cannot complete route!"
	
	for i in range(len(lst_pods)):
		if(remaining_dist - lst_pods[i]) < 0:
			stop_pods.append(lst_pods[i-1])
			remaining_dist = k
		remaining_dist -= lst_pods[i]

	return stop_pods

def main(args):
	
	lst_pods = []
	lst_pods.append(0)

	#Create variables for k and size of Pods list
	k = int(args[1]) #This is the max distance our robot can go
	Pods_locs = int(args[2]) #Number of pod locations

	#We build the test list here
	while len(lst_pods) < Pods_locs:
		new_int = round(random.uniform(1, 5)*10)
		if(new_int not in lst_pods):
			lst_pods.append(new_int)


	#Sort into ascending order
	lst_pods.sort()
	print(lst_pods) # Used for testing

	result = calcStops(k, lst_pods)

	print(result)

if __name__ == '__main__':
	main(sys.argv)