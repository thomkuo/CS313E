
#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Course Name: CS 313E

#  Unique Number: 86610


import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***
  def get_height(self):
# Add your code here!
    def height_helper(root):
      if root is None:
        return 0 
      else:
        left = height_helper(root.lchild)
        right = height_helper(root.rchild)
      output = max(left, right) + 1
      return output
    return height_helper(self.root)


  def get_level (self, level):
# Add your code here!
    nodes = []
    if self.root == None:
      return nodes
    self.level_helper(level, self.root, 0, nodes)
    return nodes

  def level_helper(self, level, node, current_level, nodes):
    theQueue = [[self.root, 0]]
    final_list = []
    while theQueue:
      nodeStuff = theQueue.pop(0)
      final_list.append(nodeStuff)
      if nodeStuff[0].lchild:
        theQueue.append([nodeStuff[0].lchild, nodeStuff[1]+1])
      if nodeStuff[0].rchild:
        theQueue.append([nodeStuff[0].rchild, nodeStuff[1]+1])
    if node is None:
      return
    elif current_level > level:
      return
    elif current_level == level:
      nodes.append(node)
    else:
      current_level +=1
      self.level_helper(level, node.lchild, current_level, nodes)
      self.level_helper(level, node.rchild, current_level, nodes)
    

  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
    left_sum = 0
    theQueue = [[self.root, 0]]
    final_list = []
    while theQueue:
      nodeStuff = theQueue.pop(0)
      final_list.append(nodeStuff)
    sum = 0
    while final_list:
      i = -1
      sum += final_list[-1][0].data
      while (len(final_list) >= -i) and (final_list[i][1] == final_list[-1][1]):
        i -= 1
      final_list = final_list[:i+1]
    for i in range(self.get_height()):
      left = self.get_level(i)[0].data
      left_sum += left
    return left_sum


# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_left_sum())

if __name__ == "__main__":
  main()
