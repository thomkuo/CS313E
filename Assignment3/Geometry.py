# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:08:32 2021

@author: markp
"""
# Geometry.py
#  Description: Creates different classes of geometric objects:
# Cube, Sphere, Point, Cylinder. Run comparison tests between objects
 
#  Student Name: Mark Panjaitan
 
#  Student UT EID: mpp854
 
#  Partner Name: Thomas Kuo
 
#  Partner UT EID: tck574
 
#  Course Name: CS 313E
 
#  Unique Number: 52604
 
#  Date Created: 09/16/2021
 
#  Date Last Modified:09/21/2021
import sys
import math
 
class Point (object):
   # constructor with default values
   def __init__ (self, x = 0, y = 0, z = 0):
       self.x = x
       self.y = y
       self.z = z
      
   # create a string representation of a Point
   # returns a string of the form (x, y, z)
   def __str__ (self):
       string = "(" + str(float(self.x)) + ", " + str(float(self.y)) \
           + ", " + str(float(self.z)) + ")"
       return string
 
      
 
   # get distance to another Point object
   # other is a Point object
   # returns the distance as a floating point number
   def distance (self, other):
      x = ((self.x - other.x)** 2) +  ((self.y - other.y)**2) + \
          ((self.z - other.z)**2)
      distance = math.sqrt(x)
      return(distance)
 
   # test for equality between two points
   # other is a Point object
   # returns a Boolean
   def __eq__ (self, other):
       diff = 1.0e-8
       if ((abs(self.x-other.x)< diff) and (abs(self.y-other.y)<diff) and \
           (abs(self.z-other.z)<diff)):
           return True
       return False
class Sphere (object):
   # constructor with default values
   def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
       self.radius = radius
       self.x = x
       self.y = y
       self.z = z
       self.center = Point(x,y,z)
 
       self.x_max = self.x + self.radius
       self.x_min = self.x - self.radius
      
       self.z_max = self.z + self.radius
       self.z_min = self.z - self.radius
      
       self.y_max = self.y + self.radius
       self.y_min = self.z - self.radius
      
   # returns string representation of a Sphere of the form:
   # Center: (x, y, z), Radius: value
   def __str__ (self):
       string = "Center: (" + str(float(self.x)) + ", " + str(float(self.y)) \
           + ", " + str(float(self.z ))+ "), Radius: " + \
               str(float(self.radius))
      
       return string
   # compute surface area of Sphere
   # returns a floating point number
   def area (self):
       area = 4 * math.pi * ((self.radius)**2)
       return(area)
      
   # compute volume of a Sphere
   # returns a floating point number
   def volume (self):
       volume = (4/3)*math.pi*(self.radius ** 3)
       return(volume)
      
 
   # determines if a Point is strictly inside the Sphere
   # p is Point object
   # returns a Boolean
   def is_inside_point (self, p):
       distance = p.distance(self.center)
       return(distance < self.radius)
      
      
   # determine if another Sphere is strictly inside this Sphere
   # other is a Sphere object
   # returns a Boolean
   def is_inside_sphere (self, other):
       distance = other.center.distance(self.center)
       return((distance + other.radius) < self.radius) 
     
     
   # determine if a Cube is strictly inside this Sphere
   # determine if the eight corners of the Cube are strictly
   # inside the Sphere
   # a_cube is a Cube object
   # returns a Boolean
   def is_inside_cube (self, a_cube):
       side = self.radius * math.sqrt(2)
       cube_inscribed = Cube(self.x,self.y,self.z,side)
       if cube_inscribed.is_inside_cube(a_cube):
           return(True)
       return(False)
      
      
   # determine if a Cylinder is strictly inside this Sphere
   # a_cyl is a Cylinder object
   # returns a Boolean
   def is_inside_cyl (self, a_cyl):
       stack = []
       point_a = Point(a_cyl.x-(a_cyl.radius),a_cyl.y,a_cyl.z+(a_cyl.height/2))
       point_b = Point(a_cyl.x-(a_cyl.radius),a_cyl.y,a_cyl.z-(a_cyl.height/2))
       point_c = Point(a_cyl.x+(a_cyl.radius),a_cyl.y,a_cyl.z+(a_cyl.height/2))
       point_d = Point(a_cyl.x+(a_cyl.radius),a_cyl.y,a_cyl.z-(a_cyl.height/2))
       point_e = Point(a_cyl.x,a_cyl.y+(a_cyl.radius),a_cyl.z+(a_cyl.height/2))
       point_f = Point(a_cyl.x,a_cyl.y+(a_cyl.radius),a_cyl.z-(a_cyl.height/2))
       point_g = Point(a_cyl.x,a_cyl.y-(a_cyl.radius),a_cyl.z+(a_cyl.height/2))
       point_h = Point(a_cyl.x,a_cyl.y-(a_cyl.radius),a_cyl.z-(a_cyl.height/2))
       stack.append(point_a)
       stack.append(point_b)
       stack.append(point_c)
       stack.append(point_d)
       stack.append(point_e)
       stack.append(point_f)
       stack.append(point_g)
       stack.append(point_h)
       counter = 0
       for i in stack:
           if self.is_inside_point(i):
               continue
           else:
               counter += 1
       if counter > 0:
           return False
       else:
           return True
 
      
   # determine if another Sphere intersects this Sphere
   # other is a Sphere object
   # two spheres intersect if they are not strictly inside
   # or not strictly outside each other
   # returns a Boolean
   def does_intersect_sphere (self, a_sphere):
       if a_sphere.x_max < self.x_max and a_sphere.x_min > self.x_min:
           if a_sphere.y_max < self.y_max and a_sphere.y_min > self.x_min:
               if a_sphere.z_max < self.z_max and a_sphere.z_min > self.z_min:
                   return(False)
       if a_sphere.center.distance(self.center) > \
           a_sphere.radius + self.radius:
           return(False)
       return(True)
      
 
   # determine if a Cube intersects this Sphere
   # the Cube and Sphere intersect if they are not
   # strictly inside or not strictly outside the other
   # a_cube is a Cube object
   # returns a Boolean
   def does_intersect_cube (self, a_cube):
       if self.is_inside_cube(a_cube):
           return False
       cube_side = a_cube.side
       stack = []
       point_a = Point(a_cube.x-(cube_side/2),a_cube.y-(cube_side/2), \
                       a_cube.z+(cube_side/2))
       point_b = Point(a_cube.x-(cube_side/2),a_cube.y-(cube_side/2),\
                       a_cube.z-(cube_side/2))
       point_c = Point(a_cube.x+(cube_side/2),a_cube.y-(cube_side/2),\
                       a_cube.z+(cube_side/2))
       point_d = Point(a_cube.x+(cube_side/2),a_cube.y-(cube_side/2),\
                       a_cube.z-(cube_side/2))
       point_e = Point(a_cube.x-(cube_side/2),a_cube.y+(cube_side/2),\
                       a_cube.z+(cube_side/2))
       point_f = Point(a_cube.x-(cube_side/2),a_cube.y+(cube_side/2),\
                       a_cube.z-(cube_side/2))
       point_g = Point(a_cube.x+(cube_side/2),a_cube.y+(cube_side/2),\
                       a_cube.z+(cube_side/2))
       point_h = Point(a_cube.x+(cube_side/2),a_cube.y+(cube_side/2),\
                       a_cube.z-(cube_side/2))
       stack.append(point_a)
       stack.append(point_b)
       stack.append(point_c)
       stack.append(point_d)
       stack.append(point_e)
       stack.append(point_f)
       stack.append(point_g)
       stack.append(point_h)
       for i in stack:
           if self.is_inside_point(i):
               return True
       return False
 
  
   # return the largest Cube object that is circumscribed
   # by this Sphere
   # all eight corners of the Cube are on the Sphere
   # returns a Cube object
   def circumscribe_cube(self):
       return(Cube(self.x,self.y,self.z,self.radius*2/math.sqrt(3)))
         
class Cube (object):
   # Cube is defined by its center (which is a Point object)
   # and side. The faces of the Cube are parallel to x-y, y-z,
   # and x-z planes.
   def __init__ (self, x = 0, y = 0, z = 0, side = 1):
       d = side/2
       self.x = x
       self.y = y
       self.z = z
       self.center = Point(x,y,z)
       self.side = side
      
      
       self.x_max = self.x + d
       self.x_min = self.x - d
       self.y_max = self.y + d
       self.y_min = self.y - d
       self.z_max = self.z + d
       self.z_min = self.z - d
      
       self.point1 = Point(self.x - d, self.y + d, self.z + d)
       self.point2 = Point(self.x + d, self.y + d, self.z + d)
       self.point3 = Point(self.x - d, self.y - d, self.z + d)
       self.point4 = Point(self.x + d, self.y - d, self.z + d)
      
       self.point5 = Point(self.x - d, self.y + d, self.z - d)
       self.point6 = Point(self.x + d, self.y + d, self.z - d)
       self.point7 = Point(self.x - d, self.y - d, self.z - d)
       self.point8 = Point(self.x + d, self.y - d, self.z - d)
      
   def Cube_Vertex(self):
       d = self.side * .5
       for x in range(0,2):
           for y in range(0,2):
               for z in range(0,2):
                   if z == 0:
                       self.z += d
                   elif z == 1:
                       self.z += -1*d
       return(str(self.z))  
    
   # string representation of a Cube of the form:
   # Center: (x, y, z), Side: value
   def __str__ (self):
       string = "Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + \
           ", " + str(float(self.z) )+ "), Side: " + str(float(self.side))
       return(string)
      
   # compute the total surface area of Cube (all 6 sides)
   # returns a floating point number
   def area (self):
       x = (self.side ** 2) * 6
       return(x)
   # compute volume of a Cube
   # returns a floating point number
   def volume (self):
       y = self.side ** 3
       return(y)
      
   # determines if a Point is strictly inside this Cube
   # p is a point object
   # returns a Boolean
   def is_inside_point (self, p):
       if self.x_max >= p.x and self.x_min <= p.x and \
           self.y_max >= p.y and self.y_min <= p.y and \
               self.z_max  >= p.z and self.z_min <= p.z:
           return(True)
       return(False)
      
  
  
   # determine if a Sphere is strictly inside this Cube
   # a_sphere is a Sphere object
   # returns a Boolean
   def is_inside_sphere (self, a_sphere):
       cube_sph = Cube(a_sphere.x,a_sphere.y,a_sphere.z)
       return(self.is_inside_cube(cube_sph))
      
    
   # determine if another Cube is strictly inside this Cube
   # other is a Cube object
   # returns a Boolean
   def is_inside_cube (self, other):
       if self.x_max > other.x_max and self.x_min < other.x_min:
           if self.y_max > other.y_max and self.y_min < other.y_min:
               if self.z_max > other.z_max and self.z_min < other.z_min:
                   return(True)
       return(False)
   # determine if a Cylinder is strictly inside this Cube
   # a_cyl is a Cylinder object
   # returns a Boolean
   def is_inside_cylinder (self, a_cyl):
       side = a_cyl.radius * 2
       cyl_square = Square(a_cyl.x, a_cyl.y,side)
       cube_square = Square(self.x, self.y, self.side)
       if cube_square.inside_Square(cyl_square):
           if self.z_max > a_cyl.z_max and self.z_min < a_cyl.z_min:
               return(True)
       return(False)           
      
          
   # determine if another Cube intersects this Cube
   # two Cube objects intersect if they are not strictly
   # inside and not strictly outside each other
   # other is a Cube object
   # returns a Boolean
   def does_intersect_cube (self, other):
       side = other.side
       if not self.is_inside_cube(other):
           if not(abs(self.x_max - other.x_max) > side) \
               and not(abs(self.y_max -other.y_max)) > side and not \
                   (abs(self.z_max - other.z_max)) > side:
               return(True)
       return(False)
   # determine the volume of intersection if this Cube
   # intersects with another Cube
   # other is a Cube object
   # returns a floating point number
   def intersection_volume (self, other):
       if self.does_intersect_cube(other):
           dx = min(self.x_max,other.x_max) - max(self.y_min,other.y_min)
           dy = min(self.y_max,other.y_max) - max(self.y_min,other.y_min)
           dz = min(self.z_max,other.z_max) - max(self.z_min,other.z_min)
           overlap = dx * dy * dz
           return(overlap)
       else:
          return(0)
   # return the largest Sphere object that is inscribed
   # by this Cube
   # Sphere object is inside the Cube and the faces of the
   # Cube are tangential planes of the Sphere
   # returns a Sphere object
   def inscribe_sphere (self):
       r = self.side/2
       x = Sphere(self.x,self.y, self.z, r)
       return(x)
      
class Cylinder (object):
   # Cylinder is defined by its center (which is a Point object),
   # radius and height. The main axis of the Cylinder is along the
   # z-axis and height is measured along this axis
   def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
       self.center = Point(x,y,z)
       self.x = x
       self.y = y
       self.z = z
       self.radius = radius
       self.height = height
       h = self.height / 2
      
       self.x_max = self.x + self.radius
       self.x_min = self.x - self.radius
      
       self.y_max = self.y + self.radius
       self.y_min = self.y - self.radius
      
       self.z_max = self.z + h
       self.z_min = self.z - h
      
      
   # returns a string representation of a Cylinder of the form:
   # Center: (x, y, z), Radius: value, Height: value
   def __str__ (self):
       string = "Center: (" + str(float(self.x)) + ", " + str(float(self.y)) \
           + ", " + str(float(self.z ))+ "), Radius: " + \
               str(float(self.radius)) + ", Height: " + \
                   str(float(self.height))
       return(string)
   # compute surface area of Cylinder
   # returns a floating point number
   def area (self):
       area = (2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius **2))
       return(area)
   # compute volume of a Cylinder
   # returns a floating point number
   def volume (self):
       volume = math.pi * (self.radius **2) * self.height
       return(volume)
   # determine if a Point is strictly inside this Cylinder
   # p is a Point object
   # returns a Boolean
   def is_inside_point (self, p):
       p_point = TwoDimPoint(p.x, p.y)
       cyl_center_point = TwoDimPoint(self.x, self.y)
       if cyl_center_point.distance(p_point) < self.radius:
           if self.z_max > p.z and self.z_min < p.z:
               return(True)
       return(False)
      
   # determine if a Sphere is strictly inside this Cylinder
   # a_sphere is a Sphere object
   # returns a Boolean
   def is_inside_sphere (self, a_sphere):
       if a_sphere.x_max < self.x_max and a_sphere.x_min > self.x_min:
           if a_sphere.y_max < self.y_max and a_sphere.y_min > self.x_min:
               if a_sphere.z_max < self.z_max and a_sphere.z_min > self.z_min:
                   return(True)
       return(False)
      
   # determine if a Cube is strictly inside this Cylinder
   # determine if all eight corners of the Cube are inside
   # the Cylinder
   # a_cube is a Cube object
   # returns a Boolean
   def is_inside_cube (self, a_cube):
       side = self.radius * math.sqrt(2)
       cyl_square = Square(self.x,self.y,side)
       cube_square = Square(a_cube.x, a_cube.y,a_cube.side)
       if cyl_square.inside_Square(cube_square):
           if a_cube.z_max <= self.z_max and a_cube.z_min >= self.z_min:
               return(True)
       return(False)
 
   # determine if another Cylinder is strictly inside this Cylinder
   # other is Cylinder object
   # returns a Boolean
   def is_inside_cylinder (self, other):
       factor_1 = abs(self.x-other.x)+other.radius < self.radius
       factor_2 = abs(self.y-other.y) + other.radius < self.radius
       factor_3 = abs(self.z - other.z) + other.height/2 < self.height/2
       if factor_1 and factor_2 and factor_3:
           return True
       else:
           return False
      
   def is_outside_cylinder(self, other):
       factor_4 = abs(self.x-other.x)>self.radius + other.radius
       factor_5 = abs(self.y-other.y) > self.radius + other.radius
       factor_6 = abs(self.z - other.z) > self.height/2 + other.height/2
       if factor_4 or factor_5 or factor_6:
           return True
       else:
           return False
 
   # determine if another Cylinder intersects this Cylinder
   # two Cylinder object intersect if they are not strictly
   # inside and not strictly outside each other
   # other is a Cylinder object
   # returns a Boolean
   def does_intersect_cylinder (self, other):
       if not self.is_outside_cylinder(other) and not \
           self.is_inside_cylinder(other):
           return True
       else:
           return False
 
class Square(object):
  
   def __init__(self,x,y,side):
       self.x = x
       self.y = y
       self.side = side
       s = self.side/2
       self.x_max = self.x + s
       self.x_min = self.x - s
       self.y_max = self.y + s
       self.y_min = self.y - s
   def inside_Square(self,other):
       if self.x_max >= other.x_max and self.x_min <= other.x_min:
           if self.y_max >= other.y_max and self.y_min <= other.y_min:
               return(True)
       return(False)
class Circle(object):
   def __init__(self,x,y,radius):
       self.x = x
       self.y = y
       self.radius = radius
   def point_inside_circle(self,point):
       distance = point.distance(self.center)
       return(distance < self.radius)
 
  
class TwoDimPoint(object):
   def __init__(self,x,y):
       self.x = x
       self.y = y
   def distance(self,other):
       distance = math.hypot((max(self.x,other.x) - min(self.x,other.x)), \
                             (max(self.y,other.y) - min(self.y,other.y)))
       return(distance)
def main():
   # read data from standard input
 
   # read the coordinates of the first Point p
   read_p = sys.stdin.readline().strip().split(" ")
   # create a Point object
   p = Point(float(read_p[0]) ,float(read_p[1]), float(read_p[2]) )
   # read the coordinates of the second Point q
 
   read_q = sys.stdin.readline().strip("\n").split(" ")
 
   # create a Point object
   q = Point (float(read_q[0]) , float(read_q[1]), float(read_q[2]) )
   # read the coordinates of the center and radius of sphereA
   read_sphereA = sys.stdin.readline().strip("\n").split(" ")
   # create a Sphere object
   sphereA = Sphere(float(read_sphereA[0]),float(read_sphereA[1]),float(read_sphereA[2]),float(read_sphereA[3]))
   # read the coordinates of the center and radius of sphereB
   read_sphereB = sys.stdin.readline().strip("\n").split(" ")
  
   # create a Sphere object
   sphereB = Sphere(float(read_sphereB[0]),float(read_sphereB[1]),float(read_sphereB[2]),float(read_sphereB[3]))
   # read the coordinates of the center and side of cubeA
   read_cubeA = sys.stdin.readline().strip("\n").split(" ")
   # create a Cube object
   cubeA = Cube(float(read_cubeA[0]),float(read_cubeA[1]),float(read_cubeA[2]),float(read_cubeA[3]))
   # read the coordinates of the center and side of cubeB
   read_cubeB = sys.stdin.readline().strip("\n").split(" ")
   # create a Cube object
   cubeB = Cube(float(read_cubeB[0]),float(read_cubeB[1]),float(read_cubeB[2]),float(read_cubeB[3]))
   # read the coordinates of the center, radius and height of cylA
   read_cylA = sys.stdin.readline().strip("\n").split(" ")
   # create a Cylinder object
   cylA = Cylinder(float(read_cylA[0]),float(read_cylA[1]), float(read_cylA[2]),float(read_cylA[3]),float(read_cylA[4]))
   # read the coordinates of the center, radius and height of cylB
   read_cylB = sys.stdin.readline().strip("\n").split(" ")
   # create a Cylinder object
   cylB = Cylinder(float(read_cylB[0]),float(read_cylB[1]),float(read_cylB[2]),float(read_cylB[3]),float(read_cylB[4]))
 
   origin = Point(0,0,0)
   # print if the distance of p from the origin is greater
   # than the distance of q from the origin
   if p.distance(origin) > q.distance(origin):
       print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
   else:
       print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")
   # print if Point p is inside sphereA
   if sphereA.is_inside_point(p):
       print("Point p is inside sphereA")
   else:
       print("Point p is not inside sphereA")
 
   # print if sphereB is inside sphereA
   if sphereA.is_inside_sphere(sphereB):
       print("sphereB is inside sphereA")
   else:
       print("sphereB is not inside sphereA")
   # print if cubeA is inside sphereA
   if sphereA.is_inside_cube(cubeA):
       print("cubeA is inside sphereA")
   else:
       print("cubeA is not inside sphereA")
   # print if cylA is inside sphereA
   if sphereA.is_inside_cyl(cylA):
       print("cylA is inside sphereA")
   else:
       print("cylA is not inside sphereA")
   # print if sphereA intersects with sphereB
   if sphereA.does_intersect_sphere(sphereB):
       print("sphereA does intersect sphereB")
   else:
       print("sphereA does not intersect sphereB")
   # print if cubeB intersects with sphereB
   if sphereB.does_intersect_cube(cubeB):
       print("cubeB does intersect sphereB")
   else:
       print("cubeB does not intersect sphereB")
   # print if the volume of the largest Cube that is circumscribed
   # by sphereA is greater than the volume of cylA'
   x = sphereA.circumscribe_cube()
   if x.volume() > cylA.volume():
       print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
   else:
       print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")
   # print if Point p is inside cubeA
   if cubeA.is_inside_point(p):
       print("Point p is inside cubeA")
   else:
       print("Point p is not inside cubeA")
   # print if sphereA is inside cubeA
   if cubeA.is_inside_sphere(sphereA):
       print("sphereA is inside cubeA")
   else:
       print("sphereA is not inside cubeA")
 
   # print if cubeB is inside cubeA
   if cubeA.is_inside_cube(cubeB):
       print("cubeB is inside cubeA")
   else:
       print("cubeB is not inside cubeA")
 
   # print if cylA is inside cubeA
   if cubeA.is_inside_cylinder(cylA):
       print("cylA is inside cubeA")
   else:
       print("cylA is not inside cubeA")
      
   # print if cubeA intersects with cubeB
 
   if cubeA.does_intersect_cube(cubeB):
       print("cubeA does intersect cubeB")
   else:
       print("cubeA does not intersect cubeB")
   # print if the intersection volume of cubeA and cubeB
   # is greater than the volume of sphereA
   if float(cubeA.intersection_volume(cubeB)) > float(sphereA.volume()):
       print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
   else:
       print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")
 
   # print if the surface area of the largest Sphere object inscribed
   # by cubeA is greater than the surface area of cylA
   x =cubeA.inscribe_sphere()
   if x.area() > cylA.area():
       print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
   else:
       print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")
   # print if Point p is inside cylA
   if cylA.is_inside_point(p):
       print("Point p is inside cylA")
   else:
       print("Point p is not inside cylA")
   # print if sphereA is inside cylA
   if cylA.is_inside_sphere(sphereA):
       print("sphereA is inside cylA")
   else:
       print("sphereA is not inside cylA")
      
   # print if cubeA is inside cylA
   if cylA.is_inside_cube(cubeA):
       print("cubeA is inside cylA")
   else:
       print("cubeA is not inside cylA")
   # print if cylB is inside cylA
   if cylA.is_inside_cylinder(cylB):
       print("cylB is inside cylA")
   else:
       print("cylB is not inside cylA")
   # print if cylB intersects with cylA
   if cylA.does_intersect_cylinder(cylB):
       print("cylB does intersect cylA")
   else:
       print("cylB does not intersect cylA")
if __name__ == "__main__":
 main()
 
 
 

