# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:36:36 2022

reddit: watching-watches
Formula to approximate the length of the filament on your spool
"""
import numpy as np
from colorama import Fore, Style
from math import floor

"""
How to use:
r1 := inner radius of spool
r2 := radius of midpoint to filament
b := width of the spool
d_f := diameter of filament
Type for example: 'lenght(50,71,45,1.75)' all units in mm in the command window
and press enter. The result will be in meters and gram.
"""
def length(r1,r2,b,d_f,density):
    L = 0
    n = (r2-r1)/d_f #number of layers
    rows = (b/d_f)-1 #number of rows minus one for safety reasons
    #rounds the numbers to a whole number:
    n = floor(n) #rounds down
    rows = floor(rows)
    A = np.pi*(d_f/2)**2 #area of filament cross section
    if(n >80): #with big spools you may need to change the 80 to a bigger number
        print("Number of Layers:",n,"is too big!")#prevents too much calculation
        
    else:
        for k in range(1,int(n)+1,1):
            l = 2*np.pi*(r1+d_f*k-d_f/2)*rows
            L += l
       
        V = 0.9*10**-3*L #sums the list and converts it to meters
        Vol = A*V #volume
        m = Vol*density #mass
        
        warnings = True # enable or disable warnings
        
        if(warnings == True):
            #this warns you when you may have entered wrong values
            if (r1>=r2):
                print(Fore.RED + 'r2 needs to be greater than r1:',V,'is not the lenght of your filament!')
                
            if (r1>b):
                print(Fore.RED + 'r1 = ',r1,' is greater than b = ',b,' are you sure you entered the right parameters?')
                
            if (d_f>3):
                print(Fore.RED + 'd_f = ',d_f,' is greater than 3 are you sure you entered the right parameters?')
                
            if (r1<=0 or r2 <= 0 or b<= 0 or d_f<= 0 or density<= 0):
                print(Fore.RED + 'Some values are smaller than 0 the calculation is wrong!') #(negative values)
            
        print(Style.RESET_ALL)    
        print(V,'[m]') 
        print(m,'[g]')
        print('density used:',density,'[g/cm^3]')
        print(n,'layers')
    
"""
Density:
  PLA 1.25
  PETG 1.24   
"""

#you can save the parameters of your spool in a function like this, so you only need to enter
#the data of r2
def Giantarm(r2,density):#1kg
    length(40,r2,53,1.75,density)
    
def Prima3d(r2,density):#750g
    length(52,r2,45,1.75,density)
    
def eSun(r2,density):
    length(95/2,r2,57,1.75,density)
    
