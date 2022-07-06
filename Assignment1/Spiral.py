#  File: Spiral.py

#  Description: Creates 2d array of Ulam's spiral and finds adjacent values of target number

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Partner Name: Mark Panjaitan

#  Partner UT EID: mpp854

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 9/01/2021

#  Date Last Modified: 9/06/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
import sys

#function identifies what numbers that need to be searched for in the matrix
def list_number():
    x = sys.stdin.readlines()
    num_list = []
    for y in x:
        y = y.strip("\n")
        y = int(y)
        num_list.append(y)
    return(num_list)
#function intilializes the matrix with the dimension that is read
def initialize_matrix(dim):
    matrix_list = []
    for x in range(0,dim):
        interior_list = []
        for y in range(0,dim):
            interior_list.append(0)
        matrix_list.append(interior_list)
    return(matrix_list)

#Creates the spiral of numbers
def create_spiral(n):
    # initializes the matrix with size n
    matrix = initialize_matrix(n)
    #Middle var takes the integer value of n/2 to identify the middle coordinates of the 2d spiral array
    middle = int(n/2)
    counter = 1
    start_col = middle
    start_row = middle
    #sets the middle values of the array as 1
    matrix[start_row][start_col] = counter
    #intializes starting location of matrix
    current_row = start_row
    current_col = start_col
    
    
    rdchange = 1
    
    #Checks to see if the amount of changes is less then/equal to n
    while rdchange <= n:
        #Top row end pattern code(Fills up the top row values)
        if rdchange == n:
            counted1 = 0
            while counted1 < rdchange-1:
                counter += 1
                current_col += 1
                matrix[current_row][current_col] = counter
                counted1 += 1
            break
        #If rdchange value is not even then numbers go right then down
        if rdchange % 2 != 0:
            counted1 = 0
            counted2 = 0
            #makes the numbers of counter print rightwards
            while counted1 < rdchange:
                counter += 1
                current_col += 1
                matrix[current_row][current_col] = counter
                counted1 += 1
            #makes the numbers of counter print downwards
            while counted2 < rdchange:
                counter += 1
                current_row += 1
                matrix[current_row][current_col] = counter
                counted2 += 1 
        #If rdchange is even then numbers go left then up
        if rdchange % 2 == 0:
            counted3 = 0
            counted4 = 0
            #makes the numbers of counter print leftwards
            while counted3 < rdchange:
                counter += 1
                current_col -= 1
                matrix[current_row][current_col] = counter
                counted3 += 1            #makes the numbers of counter print leftwards
                #makes the numbers of counter print upwards
            while counted4 < rdchange:
                counter += 1
                current_row -= 1
                matrix[current_row][current_col] = counter
                counted4 +=1

        rdchange +=1
    return(matrix)
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

#Function searches through the spiral and adds adjacent numbers
def sum_adjacent_numbers(spiral, n):
    grid_length = len(spiral)
    #Creates sum value
    sum = 0
    #Searches for value n in the spiral
    for row in range(grid_length):
        for col in range(grid_length):
            #Once the spiral coordinates are found it triggers an if function
            if spiral[row][col] == n:
                #Nested for loop tracks the values around the coordinates of value n
                for rinc in range(-1,2):
                    for cinc in range (-1,2):
                        #In bounds checker ensures there is no error
                        if not in_bounds(spiral, row+rinc, col+cinc) or (rinc == 0 and cinc == 0):
                            continue
                        #Sum value is created by adding each value around the coordinates of n
                        sum += spiral[row+rinc][col+cinc]
    return(sum)

#In bounds function checks if the coordinates inputted exist in the spiral
def in_bounds(grid, row, col):
    length = len(grid)
    if row < 0 or row >= length or col >= length or col < 0:
        return False
    return True

def main():
# read the input file
    n = int(sys.stdin.readline())
# create the spiral
    if n % 2 == 0:
        n += 1
    list1 = list_number()
    matrix = create_spiral(n)
# add the adjacent numbers
# print the result
    for x in list1:
        print(sum_adjacent_numbers(matrix, x))


if __name__ == "__main__":
    main()