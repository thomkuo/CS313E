#  File: Interval.py

#  Description: A basic interval class.

#  Student Name: Thomas Kuo

#  Student UT EID: tck574

#  Course Name: CS 313E

#  Unique Number: 52604

import sys

class IntegerInterval (object):
    # constructor with default values
    def __init__(self, beginning = 0, end = 0):
        self.beg = beginning
        self.end = end
    # creates a string representation of an Interval
    # returns a string in the form "Beginning: startTime, End: endTime"
    def __str__(self):
        string = "Beginning: " + str(self.beg) + ", End: " + str(self.end)
        return string

    # test for equality between two intervals
    # other is an interval object
    # returns a Boolean
    def __eq__(self, other):
        beg_condition = False
        end_condition = False
        if self.beg == other.beg:
            beg_condition = True
        if self.end == other.end:
            end_condition = True
        if beg_condition == True and end_condition == True:
            return True
        else:
            return False

    # returns the length of this interval
    # returns a boolean
    def __len__(self):
        return abs(self.beg - self.end)

    # determine if this interval overlaps with another
    # other is an interval object
    # returns a Boolean
    def overlap(self, other):
        if self.end == other.beg:
            return False
        if self.beg == other.end:
            return False
        if other.beg <= self.beg <= other.end:
            return True
        elif self.beg <= other.beg <= self.end:
            return True
        else:
            flag = False

        if other.beg <= self.end <= other.end:
            return True
        elif self.beg <= other.end <= self.end:
            return True
        else:
            flag = False
        return flag
    
    # determine the time in the intersection of this interval with another
    # other is an interval object
    # returns an Integer
    def intersection(self, other):
        if IntegerInterval.overlap(self, other) == False:
            return 0
        if other.beg <= self.beg <= other.end:
            bound1 = self.beg
        elif self.beg <= other.beg <= self.end:
            bound1 = other.beg
            
        if other.beg <= self.end <= other.end:
            bound2 = self.end
        elif self.beg <= other.end <= self.end:
            bound2 = other.end
        middle = IntegerInterval(bound1, bound2)
        output = IntegerInterval.__len__(middle)
        return output
    # determine the time in the union of this interval with another
    # other is an interval object
    # returns an Integer
    def union(self, other):
        A_len = IntegerInterval.__len__(self)
        B_len = IntegerInterval.__len__(other)
        intersection_len = IntegerInterval.intersection(self, other)
        return int(A_len) + int(B_len) - int(intersection_len)


# do NOT change main, it has been fully completed for you
def main():
    # read the two intervals
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line1 = line1.split(" ")
    line2 = line2.split(" ")

    interval1 = IntegerInterval(int(line1[0]), int(line1[1]))
    interval2 = IntegerInterval(int(line2[0]), int(line2[1]))

    # print the output
    print(interval1)
    print(interval2)
    print(len(interval1))
    print(len(interval2))
    print(interval1 == interval2)
    print(interval1.overlap(interval2))
    print(interval2.overlap(interval1))
    print(interval1.intersection(interval2))
    print(interval2.intersection(interval1))
    print(interval1.union(interval2))
    print(interval2.union(interval1))

if __name__ == "__main__":
    main()
