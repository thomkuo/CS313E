#  File: BalanceFactor.py

#  Description: Determines the balance factor of a binary tree

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Course Name: CS 313E

#  Unique Number:

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Return the integer balance factor of a tree rooted at the given node.
def getHeight(node):
# # add your code here! 
    if node == None:
        return 0
    else:
        return max(getHeight(node.left), getHeight(node.right)) + 1

def balance_factor(node):
    lHeight = getHeight(node.left)
    rHeight = getHeight(node.right)
    balFact = rHeight-lHeight
    return balFact

# add your code here!

# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys


def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))


if __name__ == "__main__":
    main()
