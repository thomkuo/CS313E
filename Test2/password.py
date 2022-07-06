#  File: password.py

#  Description: Rotates a linked list to the left (counter-clockwise) ``r_step'' steps ``times'' times

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 52604

import sys

class Link (object):
    # do not change this constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last (self, data):
        newLink = Link(data)
        current = self.first

        if current == None:
            self.first = newLink
            return

        while current.next != None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # COMPLETE THIS FUNCTION
    # return a new linked list that results from the rotation
    # do not change this linked list
    def rotate(self, r_step, times):
        rotations = self.num_links() + r_step
        copy = self.copy_list()
        curr = copy.first
        if curr == None:
            return None
        for i in range(rotations * times):
            if curr.next != None:
                curr = curr.next
            else:
                curr = copy.first
        rotated = LinkedList()
        for i in range(copy.num_links()):
            rotated.insert_last(curr.data)
            if curr.next != None:
                curr = curr.next
            else:
                curr = copy.first
        return rotated



# DO NOT CHANGE MAIN
def main():
    ll = LinkedList()

    data = list(map(int, input().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    r_step, times = list(map(int, input().split()))

    rotated = ll.rotate(r_step, times)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)

if __name__ == "__main__":
    main()
