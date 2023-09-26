#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vansh Soni
# Section: 514
# Assignment: 2.11 Lab
# Date: 25 08 2023
"""
Created on Fri Sep 22 15:36:17 2023

@author: vanshsoni
"""
import math

#this function defines the equation that is needed to use with the variables
def equation(x_user, x_initial, y_initial, x1,y1):
    #i split the exponent part for readability
    m = (math.log(y1/y_initial) / (math.log(x1/x_initial)))
    y = (y_initial) * (((x_user)/(x_initial)) ** m)
    
    return y

x_user = float(input("Enter the excess temperature: "))
#The float allows string to be converted to num

#checks if user_score between 1 and 5
if(1 <= x_user <= 5):
    #uses the points between A and B
    x_0 = 1.3 #point A
    y_0 = 1000
    x1 = 5 #Point B
    y1 = 7000
    print(f"The surface heat flux is approximately {equation(x_user,x_0,y_0,x1,y1):.0f} W/m^2")
elif(5 < x_user <= 30):
    #uses the points between B and C
    x_0 = 5 #Point B
    y_0 = 7000
    x1 =30
    y1 = 1500000 #Point C
    print(f"The surface heat flux is approximately {equation(x_user,x_0,y_0,x1,y1):.0f} W/m^2")
elif(30 < x_user <= 120):
    #uses the points between C and D
    x_0 = 30 #point C
    y_0 = 1500000
    x1 =120#Point D
    y1 = 25000
    print(f"The surface heat flux is approximately {equation(x_user,x_0,y_0,x1,y1):.0f} W/m^2")
elif(120 < x_user <= 1200):
    #uses the points between D and E
    x_0 = 120#Point D
    y_0 = 25000
    x1 =1200 #Point E
    y1 = 1500000
    print(f"The surface heat flux is approximately {equation(x_user,x_0,y_0,x1,y1):.0f} W/m^2")
else:
    #if any other value is given then the fllux is not available
    print("Surface heat flux is not available")
    
    
