#  File: Cipher.py

#  Description: Rotates a matrix either 90 degrees clockwise or counterclockwise

#  Student Name: Mark Panjaitan

#  Student UT EID: mpp854

#  Partner Name: Thomas Kuo

#  Partner UT EID: tck574

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 9/07/2021

#  Date Last Modified: 9/13/2021

import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

#For decryption create an empty matrix and fill in the asterisks
def initialize_matrix(dim):
    matrix_list = []
    for x in range(0,dim):
        interior_list = []
        for y in range(0,dim):
            interior_list.append("0")
        matrix_list.append(interior_list)
    return(matrix_list)
# Returns the dimension size of the thing
def dimension_array(strng):
    lengthofArr = len(strng)
    sqrt = math.sqrt(lengthofArr)
    k = math.ceil(sqrt) 
    return(k)
#adds asterisk for decryption
def decryption_asterisk(matrix, dim, ast_amount):
    z = 0
    for x in range(0, dim):
        for y in range(dim-1, -1, -1):
            if z == ast_amount:
                break
            z += 1
            matrix[y][x] = "*"
        if z == ast_amount:
            break
def asterisk_adder(length, size):
    #size is the dimensions of the array 
    #square the variable size to find how many places there are in the matrix
    size_square = size * size
    #Do size_square - length to find how many more asterisk are needed to fill the matrix
    amount = size_square - length
    return(amount)
#The below function fills in the values of an input string into the decryption matrix
#For context, the matrix being input into here is a matrix that has placed any needed asterisks in the right location
#The function takes in a matrix, the dimension of the matrix, and string_form which is the original input string
def fill_in_decryption(matrix, dim, string_form):
    a = 0
    #for each position in the matrix check to see if it is equal to "*"
    for x in range(0,dim):
        for y in range(0,dim):
            #If the position's value is equal to "*" skip that position
            if matrix[x][y] == "*":
                continue
            #if not then for that position put in one character from the input string for that position
            matrix[x][y] = string_form[a]
            #a is increased by a value of 1 so for the next loop it inputs the next character in the string
            a += 1
    #return a filled matrix that has the asterisks and original input string in it
    return(matrix)
#takes in a matrix and returns a string
def final_string(matrix):
    final = []
    # converts matrix into a 1D list
    for x in matrix:
        for y in x:
            final.append(y)
   # takes the 1D list and converts it into a string
    final_string = ''.join(final)
    return(final_string)

#Splits the word into a 1D list
def split(word):
    return [letter for letter in word]

def encrypt ( strng ):
    #If list is all numbers in converts from int or float into string type
    strng = str(strng)
    #Finds the length of the inputted string
    original_len = len(strng)
    #finds the size of the array (dimensions)
    size = dimension_array(strng)
    # creates a new string that places asterisks at the end of the string to make the string length a perfect square
    strng = strng + (asterisk_adder(original_len, size)*"*") 
    
    # converts the string into a 1D list
    stringVersion = split(strng)
  
    #Creates lambda function to create a 2d array
    ArrCreator = lambda string, size: [string[i:i+size] for i in range(0,len(string), size)]
    #Create a second empty matrix to put in the rotated values
    new_matrix = initialize_matrix(size)
    #Creates a 2D list of the stringVersion
    original_message = ArrCreator(stringVersion, size)
    #Finds length of the 2D list of string version
    length = len(original_message)
    #For each position in the new matrix it replaces with the rotated value from the 2D matrix of stringVersion
    for row in range(0,length):
        for col in range(0,length):
            #moving from left to right the new_matrix list holds the rotated value from the original message
            new_matrix[row][col] = original_message[(length-1) - col][row] 
    #creates the end_string thaat will be reurned
    end_string = final_string(new_matrix)
    #Searches through the string and removes any leftover asterisks 
    end_string = end_string.replace("*", "")
            
    return(end_string)

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    string_form = str(strng)
    strlen = len(string_form)
    size = dimension_array(string_form)
    #create empty matrix
    original_string_matrix = initialize_matrix(size)
    #count amount of asterisks needed
    ast_amount = asterisk_adder(strlen, size)
    # add asterisks to the initial matrix at the right locations
    decryption_asterisk(original_string_matrix, size, ast_amount)

    #Fill in the above matrix with the values from string_form
    fill_in_decryption(original_string_matrix, size, string_form)
    #store the length of the matrix for later use
    length = len(original_string_matrix)
    #Create new matrix to put new values in
    new_matrix = initialize_matrix(size)
    #For each position in the new_matrix put in the rotated value of the original_string_matrix
    for row in range(0,length):
        for col in range(0,length):
            new_matrix[row][col] = original_string_matrix[col][(length-1)-row]

    #creates the end_string thaat will be reurned
    end_string = final_string(new_matrix)
    #Searches through the string and removes any leftover asterisks 
    end_string = end_string.replace("*", "")
    return(end_string)

def main():
  # read the strings P and Q from standard input
  pstring = str(sys.stdin.readline().strip("\n"))
  qstring = str((sys.stdin.readline().strip("\n")))
  # encrypt the string P
  # print the encrypted string of P
  print(encrypt(pstring))
  # decrypt the string Q
  # print the decrypted string of Q
  print(decrypt(qstring))
  
if __name__ == "__main__":
    main()


