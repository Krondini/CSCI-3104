import sys

def isMcNugget(n):
	if n == 0:
		return True
	elif n < 0:
		return False

	return isMcNugget(n-6) or isMcNugget(n-9) or isMcNugget(n-20)

if __name__ == '__main__':
	print(isMcNugget(sys.argv))