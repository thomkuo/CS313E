#  File: maximum_profit.py

#  Description: This program uses a circular linked list to solve the Josephus problem

#  Student Name: Thomas Kuo
 
#  Student UT EID: tck574
 
#  Partner Name: Mark Panjaitan
 
#  Partner UT EID: mpp854
 
#  Course Name: CS 313E
 
#  Unique Number: 52604
 
#  Date Created: 11/25/2021
 
#  Date Last Modified:11/25/2021

import sys

# Add Your functions here
def max_prof(budget, houses, prices, increase):
    #Creates a list that holds the true profit earned from flipping the houses
    profit = []
    for i in range(houses):
        roi = float(increase[i])*float(prices[i])
        profit.append(roi)
    
    #Creates an array of zeroes used for dynamic programming
    dp_array = []
    for y in range(houses + 1):
        temp = []
        for x in range(budget + 1):
            temp.append(0)
        dp_array.append(temp)

    #Populates dp_array with values to find maximum possible profit from flipping the houses listed in the subset
    for y in range(houses + 1):
        for x in range(budget + 1):
            #Fills top row and first column with zeroes
            if y == 0 or x == 0:
                dp_array[y][x] = 0
            #Uses tabulation dp approach to fill out dp_array with maximum possible profits
            elif prices[y-1] <= x:
                dp_array[y][x] = max(profit[y-1] + dp_array[y-1][x-prices[y-1]], dp_array[y-1][x])
            else:
                dp_array[y][x] = dp_array[y-1][x]
 
    return (float(dp_array[houses][budget]))/100
 
# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)
 
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} 
    # (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])

# Add your implementation here .... 
    result =  max_prof(money, num_houses, prices, increase)

# Add your functions and call them to generate the result. 

    print(result)

main()
