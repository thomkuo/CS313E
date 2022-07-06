# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 01:13:49 2021

@author: markp
"""
# -*- coding: utf-8 -*-

#  File: Josephus.py

#  Description: This program uses a circular linked list to solve the Josephus problem

#  Student Name: Mark Panjaitan
 
#  Student UT EID: mpp854
 
#  Partner Name: Thomas Kuo
 
#  Partner UT EID: tck574
 
#  Course Name: CS 313E
 
#  Unique Number: 52604
 
#  Date Created: 10/14/2021
 
#  Date Last Modified:10/19/2021
import sys
class Link(object):
  # intializes variables 
  def __init__(self, data):
    self.data = data
    self.next = None

  # string
  def __str__(self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__(self): 
    self.head = None 
    self.last = None 
		
  # Insert an element (value) in the list
  def insert(self, data):
    new = Link(data)
    # if nothing is there, insert an element
    if self.head == None:
      self.head = new 
      self.last = new
    self.last.next = new
    self.last = new
    self.last.next = self.head

  # Find the Link with the given data (value)  
  # or return None if the data is not there
  def find(self, data):
    current = self.head
    while current != self.last:
      if current.data == data:
        return current
      current = current.next 
  # If data not there returns none
    if self.last.data == data:
      return self.last
    return None

  # delete current node and then move current so that it points to next node
  def deleteList(self):
      # initialize the current node
      current = self.head
      self.last.next = None
      while current:
          prev = current.next  # move next node
          # delete the current node
          del current.data
          # set current equals prev node
          current = prev
      return

  def getCount(self):
      count = 1
      current = self.head
      while current.next != self.head:
          current = current.next
          count +=1
      return(count)
  def EmptyChecker(self):
    return self.head.next is None
# Find the Link with the given data (value)  
# or return None if the data is not there
  def delete(self, data):
    if self.EmptyChecker() == True:
      return(None)

    if self.getCount() == 1:
      current = self.head
      x = current.next
      self.deleteList()
      return(x)

    # uses try block
    
    try:
      current = self.head
      while current != self.last:
        if current.next == self.last and current.next.data == data:
          self.last = current
          break
        elif current.next.data == data:
          break
        current = current.next
      else:
        if current.next.data != data or current.next == None:
          return None
        else:
          self.head = current.next.next
      deleted_link = current.next
      current.next = current.next.next
      return deleted_link
    # If data not there returns none
    except Exception as err:
      return(None)
  # Delete the nth Link starting from the Link start  
  # Return the data of the deleted Link AND return the  
  # next Link after the deleted Link in that order
  def delete_after(self, start, n):

    if self.EmptyChecker() == True:
      return(None)
    # Get to start
    if self.getCount() == 1:
      current = self.head
      x = current.data
      self.deleteList()
      print(x)
      return(None)
    current = self.head
    while current.data != start:
      current = current.next
    
    # get to link to delete
    i = 1
    while i != n:
      i += 1
      current = current.next

    # Delete link
    deleted_link = current
    self.delete(current.data)
    print(deleted_link)
    try:
      if current.next:
        return current.next
    except AttributeError:
      return(None)
    


  # Return a string representation of a Circular List
  def __str__(self):
    line =[]
    cur = self.head
    if cur.next == None:
      return(str(line))
    try:
        current = self.head
        while current.next != self.head:
            line.append((current.data))
            current = current.next
        line.append((current.data))
        return str(line)
    except AttributeError:
        return(str(line))
        
    

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int(line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int(line)

  # your code
  circle = CircularList()
  # Add to circle
  for i in range(1, num_soldiers + 1):
    circle.insert(i)

  for i in range(num_soldiers+1):
        try:
            start_count = circle.delete_after(start_count, elim_num)
            
            start_count = start_count.data
        except AttributeError as err:
            break
      
        
          
if __name__ == "__main__":  
  main()