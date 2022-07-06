# File: Anagrams.py
# Description: A program to group strings into anagram families
# Student Name: Thomas Kuo
# Student UT EID: tck574
# Course Name: CS 313E
# Unique Number: 52604
# Output: True or False

def are_anagrams(str1, str2):
    s1 = "".join(sorted(str1))
    s2 = "".join(sorted(str2))
    if s1 == s2:
        return True
    else:
        return False

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    groups = []
    count = 1
    for i in lst:
        key = "".join(sorted(i))
        if key not in groups:
            groups.append(key)
    for j in groups:
        if not are_anagrams(i,j):
            count += 1
    return count

def main():    
# read the number of strings in the list    
    num_strs = int(input())    
    # add the input strings into a list    
    lst = []    
    for i in range(num_strs):        
        lst += [input()]    
    # compute the number of anagram families    
    num_families = anagram_families(lst)    
    # print the number of anagram families    
    print(num_families)

if __name__ == "__main__":    
    main()