# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:49:53 2020

@author: Onkar
"""

import math
import numpy as np
import pandas as pd
import matplotlib as plt

import LoadData as ld


def calculateLog(integer):
    try:
        log = math.log2(integer)

    except ValueError:
        log = 0
    return log
    

def calculateVarience(dataset):

    varience = 1
    class_zero = 0
    class_one = 0
    labels = dataset[:, -1]
        
    total =  len(labels)
    class_zero = np.count_nonzero(labels == 0)
    class_one = np.count_nonzero(labels != 0)
    
    varience = (class_zero*class_one)/(total*total)
            
    return varience


def calculateEntropy(dataset):

    entropy = 1
    class_zero = 0
    class_one = 0
    
    labels = dataset[:, -1]
        
    total =  len(labels)
    class_zero = np.count_nonzero(labels == 0)
    class_one = np.count_nonzero(labels != 0)
   
    log_total = calculateLog(total)
    log_one = calculateLog(class_one)
    log_zero = calculateLog(class_zero)
    
    ratio_zero = 0
    ratio_one = 0

    ratio_zero = (class_zero/total)
    ratio_one = (class_one/total)
    
    entropy = -(ratio_zero*(log_zero - log_total)) -(ratio_one*(log_one - log_total))
            
    return entropy


def calculateGain(current_impurity, left, right):

    left_rows = np.shape(left)[0]
    right_rows = np.shape(right)[0]

    p = left_rows/(left_rows + right_rows)    
    gain = current_impurity - (p*calculateVarience(left) + (1-p)*calculateVarience(left))
    
    # print("current_Impurity = ", current_impurity, "gain = ", gain, "Entropy Left = ", calculateVarience(left), "Entropy right = ", calculateVarience(right))
    
    return gain