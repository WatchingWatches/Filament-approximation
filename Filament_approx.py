# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:36:36 2022

@author: bjans
reddit: watching-watches
Formula to approximate the length and mass of the filament on your spool
Please note: this is only a approximation this only works accurate if the spool is wound properly
"""
import numpy as np
from colorama import Fore, Style

density = 1.27 #Pla 1.25; PETG 1.27 enter the value for density here
"""
How to use:
r1 := inner radius of spool
r2 := radius of midpoint to filament
b := width of the spool
d_f := diameter of filament
Type for example: 'lenght(50,71,45,1.75)' all units in mm in the command window
and press enter. The result will be in meters and gram.
"""
def length(r1,r2,b,d_f):
    L=[]
    k = 1 #start point of the sum
    n = (r2-r1)/d_f #number of layers
    rows = (b/d_f) #number of rows
    #rounds the numbers to a whole number:
    round(n)
    round(rows)
    A = np.pi*(d_f/2)**2 #area of filament cross section
    while k <= n:
        def f(x):
             l = 2*np.pi*(r1+d_f*x-d_f/2)*rows
             return l
        L.append(f(k)) #writes lists with length of each layer
        k+=1
    V = 0.9*10**-3*sum(L) #sums the list and konverts it to meters
    Vol = A*V #volium
    m = Vol*density #mass
    #this warns you when you may have entered wrong values
    if (r1>=r2):
        print(Fore.RED + 'r2 needs to be greater than r1:',V,'is not the lenght of your filament')
        
    if (r1>b):
        print(Fore.RED + 'r1 is greater than b are you sure you entered the right parameters?')
        
    if (d_f>3):
        print(Fore.RED + 'd_f is greater than 3 are you sure you entered the right parameters?')
        
    print(Style.RESET_ALL) #the values will not be red
    print(V,'[m]')
    print('density used:',density,'[g/cm^3]')
    print(m,'[g]')
    
#you can save the parameters of your spool in a function like this, so you only need to enter
#the data of r2 when using it again
def Giantarm(r2):#1kg
    length(30,r2,53,1.75)
    
