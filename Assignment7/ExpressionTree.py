#  File: ExpressionTree.py

#  Description:

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Partner Name: Mark Panjaitan

#  Partner UT EID: mpp854

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 10/23/2021

#  Date Last Modified: 10/26/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

#puts in objects as a stack
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        self.root = Node()
        stack = Stack()
        curr_node = self.root
        express = expr.split()
        for i in range(len(express)):
            token = express[i]
            #Creates left child, pushes current node onto the stack and makes it the lchild
            if token == "(":
                curr_node.lChild = Node()
                stack.push(curr_node)
                curr_node = curr_node.lChild
            #Pushes current data onto the stack and sets current to rchild
            elif token in operators:
                curr_node.data = token
                stack.push(curr_node)
                curr_node.rChild = Node()
                curr_node = curr_node.rChild
            #If the stack is not empty, make current node parent node
            elif token == ")":
                if stack.is_empty() is not True:
                    curr_node = stack.pop()
                else:
                    return
            else:
                if '.' in token:
                    curr_node.data = float(token)
                else:
                    curr_node.data = int(token)
                if stack.is_empty() is not True:
                    curr_node = stack.pop()

                    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    # function that is used to evaluate the input expression
    def evaluate(self, aNode):
        if aNode.data not in operators:
            return aNode.data
        
        elif aNode.rChild.data not in operators and aNode.lChild.data not in operators:
            #eval is used to take in the values string values and operate on it
            #then the number is returned
            not_in = float(eval(str(aNode.lChild.data) + aNode.data + str(aNode.rChild.data)))
            return not_in
        else:
            rec = float(eval(str(self.evaluate(aNode.lChild)) + aNode.data + str(self.evaluate(aNode.rChild))))
            return rec


    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation

    #helper function for pre_order_recur function
    def pre_order(self, aNode):
        #calls the recursive pre_order_recur function
        preorder = self.pre_order_recur(aNode, "")
        return preorder

#pre_order_recur function returns output for prefix expression
#example input:  (( 8 + 3 ) ∗( 7 −2 ) ) = 5 5 . 0
#example pre_order_recur output should be: ∗ + 8 3 −7 2

    def pre_order_recur(self, aNode, string):
    #if aNode is empty return a ""
    #once it is "" the recursive function stops running
        if aNode == None:
            return ""
        else:
            if aNode.data not in operators:
                #if period is in the string then we convert the number to a float
                #else this means the number is an integer
                if "." in str(aNode.data):
                    string = str(float(aNode.data)) + " "
                else:
                    string = str(int(aNode.data)) + " "
            else:
                string = aNode.data + ' '
#pre order recursive function runs by going on the left and right branches of the binary serach tree
            return string + self.pre_order_recur(aNode.lChild, string) + self.pre_order_recur(aNode.rChild, string)

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation/
    #post_order function is helper function for post_order_recur function
    def post_order(self, aNode):
        #calls the post_order_recur function
        postorder = self.post_order_recur(aNode, "")
        #should return organized postorder expression
        return postorder

    #recursive function thats used to print out the postfix expression
    def post_order_recur(self, aNode, string):
        #return blank value so the recursion ends
        if aNode == None:
            string = ""
            return string
        else:
            if aNode.data not in operators:
                #if period is in the string then we convert the number to a float
                #else this means the number is an integer
                if '.' in str(aNode.data):
                    string = str(float(aNode.data)) + " "
                else:
                    string = str(int(aNode.data)) + " "
            else:
                string = aNode.data + ' '
            #function returns recursively until the correct order and all values have been iterated
            #sends the recursive function to work on the left and right child
            return self.post_order_recur(aNode.lChild, string) + self.post_order_recur(aNode.rChild, string) + string
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
