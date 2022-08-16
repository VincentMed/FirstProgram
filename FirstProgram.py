# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:08:35 2022

@author: be
"""

'''
compute the sum of the first 100 integers. In GitHub account, open a repo
called "FirstProgram". Complete assignment, push to GitHub account.

'''

import numpy as np

list100 = np.linspace(1, 100, 100)

#print(list100)

sum100 = sum(list100)

# format to remove the decimal

print('sum of first 100 numbers is : {:.0f}'.format(sum100))

''' -------------------------------- '''

otherSum = 0

for i in range(101): 
    otherSum = otherSum + i
    
print('otherSum = {}'.format(otherSum))