#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:42:32 2023

@author: vanshsoni
"""

import math
def quadratic_pos(a,b,c):
    quad_pos = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return quad_pos
    
def quadratic_neg(a,b,c):
    quad_neg = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return quad_neg
    


a = float(input("Please enter the coefficient A: \n"))
b = float(input("Please enter the coefficient B: \n"))
c = float(input("Please enter the coefficient C: \n"))

#this variable will check if complex root, 2 roots, or 1 root
discriminant = ((b**2) - (4 * a * c))


if a != 0 and b != 0 and discriminant == 0:
    print(f"The root is x = {quadratic_pos(a,b,c)}")
    
elif a != 0 and b != 0 and discriminant > 0:
    print(f"The roots are x = {quadratic_pos(a,b,c)} and x = {quadratic_neg(a,b,c)}")

elif a != 0 and b != 0 and discriminant < 0:
    discriminant1 = -b/2 * a
    disI = math.sqrt(abs(((b**2) - (4 * a * c))))/2
    pos = (str(discriminant1)+ " + " + str(disI) + "i")
    neg = (str(discriminant1)+ " - " + str(disI) + "i")
    print(f"The roots are x = {pos} and x = {neg}")
elif a == 0 and b != 0:
    linear = float(-c/b)
    print(f"The root is x = {linear}")
else:
    print("You entered an invalid combination of coefficients! ")

