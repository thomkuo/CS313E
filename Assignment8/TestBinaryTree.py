
#  File: TestBinaryTree.py

#  Description:

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Partner Name: Mark Panjaitan

#  Partner UT EID: mpp854

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 11/01/2021

#  Date Last Modified: 11/02/2021


import sys

#Creates Queue to parse through the methods
class Queue(object):
  def __init__ (self):
    self.queue = []
  #Adds element at end of queue
  def enqueue (self, item):
    self.queue.append(item)
  #Removes element from queue
  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None
  #Checks if queue is empty
  def isEmpty (self):
    return (len (self.queue) == 0)
  #Finds size of queue
  def size (self):
    return len (self.queue)

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
        self.level = None


class Tree (object):
    # constructor
    def __init__(self):
        self.root = None

    # inserts data into l/r based on comparison with parent node
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if data < current.data:
                    current = current.lChild
                else:
                    current = current.rChild
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node



    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        if self.root == None and pNode.root == None:
            return True
        else:
            anode = self.root
            bnode = pNode.root
            #Helper function called to compare nodes
            return self.compareNodes(anode, bnode)
    
    def compareNodes(self, node1, node2):
    #If statements for different node comparison situations
      if node1 == None and node2 == None:
        return True
      if node1 == None and node2 != None:
        return False
      elif node1 != None and node2 == None:
        return False
      elif node1.data != node2.data:
        return False
      else:
        return self.compareNodes(node1.lChild, node2.lChild) and \
        self.compareNodes(node1.rChild, node2.rChild)

# Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        #List of nodes
        queue_list = []
        #Uses Queues to travers tree
        queue = Queue()
        queue.enqueue(self.root)
        #If empty returns the list
        if self.root == None:
            return queue_list
        else:
            self.root.level = 0
            #Loops the tree to find nodes in the same level
            while queue.isEmpty() != True:
                out_node = queue.dequeue()
                if out_node.level == level:
                    queue_list.append(out_node)
                if out_node.lChild is not None:
                    queue.enqueue(out_node.lChild)
                    out_node.lChild.level = out_node.level + 1
                if out_node.rChild is not None:
                    queue.enqueue(out_node.rChild)
                    out_node.rChild.level = out_node.level + 1
        return queue_list

    # Returns the height of the tree
    # should height include root? or root = 0, so height - 1?
    def get_height(self):
        #Variable to hold the height
        height = 0
        queue = Queue()
        queue.enqueue(self.root)
        #Returns if tree is empty
        if(self.root == None):
            return height
        else:
            self.root.level = 0
            height = 1
            #Loops the tree to find the height
            while queue.isEmpty() != True:
                out_node = queue.dequeue()
                if out_node.lChild is not None:
                    queue.enqueue(out_node.lChild)
                    out_node.lChild.level = out_node.level + 1
                    if out_node.lChild.level + 1 > height:
                        height = out_node.lChild.level + 1
                if out_node.rChild is not None:
                    queue.enqueue(out_node.rChild)
                    out_node.rChild.level = out_node.level + 1
                    if out_node.rChild.level + 1 > height:
                        height = out_node.rChild.level + 1
        return height

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        output = self.num_nodes_recur(self.root)
        return output
    #Helper function that helps passing in variables for recursion
    def num_nodes_recur(self, node):
        if node is None:
            return 0
        return 1 + self.num_nodes_recur(node.lChild) + self.num_nodes_recur(node.rChild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints


if __name__ == "__main__":
    main()