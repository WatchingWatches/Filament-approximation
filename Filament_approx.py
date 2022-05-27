# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:36:36 2022

@author: bjans
reddit: watching watches
Formula to approximate the length and mass of the filament on your spool
"""
import numpy as np
density = 1.25 #Pla: 1.25 change the density to your material
"""
How to use:
r1 := inner radius of spool
r2 := radius of midpoint to filament
b := width of the spool
d_f := diameter of filament
Type for example: 'lenght(50,71,45,1.75)' all units in mm in the command window
and press enter. The result will be in meters.
"""
def lenght(r1,r2,b,d_f):
    L=[]  #creates empty list
    k = 1 #start point of the sum
    n = (r2-r1)/d_f #number of layers
    rows = (b/d_f) #number of rows
    #rounds the numbers to a whole number:
    round(n)
    round(rows)
    A = np.pi*(d_f/2)**2
    while k <= n:
        def f(x):
             l = 2*np.pi*(r1+d_f*x-d_f/2)*rows
             return l
        L.append(f(k))
        k+=1
    V = 0.9*10**-3*sum(L)
    Vol = A*V # volume of filament
    m = Vol*density #mass of filament(change the density to your material)
    print(V,'[m]')
    print(m,'[g]')
    if (r1>=r2):
        print('r2 needs to be greater than r1:',V,'is not the lenght of your filament')
