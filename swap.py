import math
def swap_list(input):
	length = len(input)

	a = []
	a[0: middle] = input[0:middle]
	a[middle-1] = input[-1]
	a[middle:] = input[middle:]
	a[-1] = input[middle-1]
	return a
print(swap_list([1,2,3,4]))	
