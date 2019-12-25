# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import numpy as np
import pandas as pd


def loadData():
    
    print("Loadind data...")
    dataSet = pd.read_csv("water-treatment.data", header = None)
    dataSet = np.array(dataSet)
    
    #load file containing statastical metadata(mena, sd, min, max etc) of given dataset
    metadata =  "metadata.csv"    
    metadata = pd.read_csv(metadata, header = None)
    metadata = np.array(metadata)

    return dataSet, metadata


def cleanData():
    
    dataSet, metadata = loadData()
    
    print("Cleaning data...")
    for column in range(1, 39):
        for row in range(527):
            #replace '?' with mean
            if (dataSet[row][column] == "?"):
                dataSet[row][column] = float(metadata[column][4])
            
            #convert integer and/or str data to float
            else:
                dataSet[row][column] = float(dataSet[row][column])

            #calculate z score normalization
            dataSet[row][column] = (dataSet[row][column] - float(metadata[column][4]))/float(metadata[column][5])
            dataSet[row][column] = float(format(dataSet[row][column], ".4f"))

    return dataSet


def removeDate():
    
    print("Removing date")
    cleanedDataSet = cleanData()
    scaled_dataset = np.ndarray(shape = (527, 38))
    
    for row in range(527):
        for column in range(1, 39):
            scaled_dataset[row][column - 1] = cleanedDataSet[row][column]
            
    return scaled_dataset