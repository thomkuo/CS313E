import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    expon = 1
    val = v
    #Checks to see when k**expon is less than v 
    #If it is bigger than v // k**expon is equal to 0
    while(k ** expon <= v):
       
        val += v // (k ** expon)
        
        expon += 1
   
    return(val)

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    val = 1
    #checks every integer value to see the minimum number of lines
    #until the more lines are written than required
    while (sum_series(val,k) < n):
        val += 1
    return(val)

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    minval = 1
    maxval = n
    mid = (minval + maxval) // 2
#If the midpoint is the correct answer than this while loops will break in the
#final iteration
    while(minval != mid):
        if(sum_series(mid, k) >= n):
#If the sum is greater than n than we need to decrease the max value so
#we replace the maxval with the mid value we just found
#bc we know the answer cannot be any higher than that integer
            maxval = mid
        elif(sum_series(mid, k) < n):
#if the sum of is less than N than we need to increase the min value so
#we replace the minval with the mid value we just found
            minval = mid
#Finds a new midpoint of the range
        mid = (minval + maxval) // 2
#Because integers are rounded down the midvalue could be too low so if its too
#low we just increase the value
    if(sum_series(mid, k) < n):
        return(mid + 1)
    return(mid)
    

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
