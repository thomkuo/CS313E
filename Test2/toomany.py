#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Course Name: CS 313E

#  Unique Number: 52604

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
#Possible flowers number 1 to 9
#if the number of flowers in any count exceed the number of vases, there are too many of that type
	one = 0
	two = 0
	three = 0
	four = 0
	five = 0
	six = 0
	seven = 0
	eight = 0
	nine = 0
	count_list = []
	over_list = []
	for i in flower_list:
		if i == 1:
			one += 1
		if i == 2:
			two += 1
		if i == 3:
			three += 1
		if i == 4:
			four += 1
		if i == 5:
			five += 1
		if i == 6:
			six += 1
		if i == 7:
			seven += 1
		if i == 8:
			eight += 1
		if i == 9:
			nine += 1
	count_list.append(one)
	count_list.append(two)
	count_list.append(three)
	count_list.append(four)
	count_list.append(five)
	count_list.append(six)
	count_list.append(seven)
	count_list.append(eight)
	count_list.append(nine)
	flag1 = is_too_many(one, N)
	flag2 = is_too_many(two, N)
	flag3 = is_too_many(three, N)
	flag4 = is_too_many(four, N)
	flag5 = is_too_many(five, N)
	flag6 = is_too_many(six, N)
	flag7 = is_too_many(seven, N)
	flag8 = is_too_many(eight, N)
	flag9 = is_too_many(nine, N)
	if flag1 == True:
		over_list.append(1)
	if flag2 == True:
		over_list.append(2)
	if flag3 == True:
		over_list.append(3)
	if flag4 == True:
		over_list.append(4)
	if flag5 == True:
		over_list.append(5)
	if flag6 == True:
		over_list.append(6)
	if flag7 == True:
		over_list.append(7)
	if flag8 == True:
		over_list.append(8)
	if flag9 == True:
		over_list.append(9)
	return over_list
	
	
	
	
def is_too_many(input, N):
	if input > (N*2):
		return True





if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
