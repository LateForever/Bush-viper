# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:46:16 2023

@author: Albert
"""

inpt = int(input())

def everOrOdd(n):
    
    if n == 0 or n == 1:
        return "odd"
    
    b = bin(n)[2:][-1]
    
    if int(b) == 1:
        return "odd"

    return "even"
    

print(everOrOdd(inpt))