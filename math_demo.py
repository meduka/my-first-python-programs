#THis program demonstrates how to use the math module.
#
#Manuela Cano
#August 30, 2017

import math

#the math module has constants

print(math.pi)
print(math.e)

#the math module also has built in functions

print(math.sqrt(2))
print(math.sin(0.5))


#this program contains functions that evalute formalas used in geometry

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r ** 2
    return a

#function calls

print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))


def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(x, b, h):
    a = ((x + b)/2) * h
    return a 

def rectpris_volume(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = (math.pi * r ** 2) * (h/3)
    return v

def sphere_volume(r):
    v = (4/3) * math.pi * r ** 3
    return v

def rectpris_surface_area(w, h, l):
    sa = 2 * (w * l + h * l + h * w)
    return sa

def sphere_surface_area(r):
    sa = 4 * math.pi * r ** 2
    return sa

def right_tri_hyp(a, b):
    hyp = a ** 2 + b **2
    return math.sqrt(hyp)
    

print(parallelogram_area(2,3))

print(trapezoid_area(2, 3, 4))

print(rectpris_volume(2,3,4))

print(cone_volume(5,7))

print(sphere_volume(3))

print(rectpris_surface_area(2, 5, 6))

print(sphere_surface_area(3))

print(right_tri_hyp(20,20))
