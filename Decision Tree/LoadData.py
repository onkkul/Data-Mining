# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:51:12 2020

@author: Onkar
"""

import numpy as np
import pandas as pd


class loadData():
        
    def readCSV(self, filename):
        filename = self.filepath+filename
        dataset = pd.read_csv(filename)
        dataset = np.array(dataset)
        return dataset
    
    
    def readTrainingD(self):
        filename = "/training_set.csv"
        training_data = self.readCSV(filename)        
        self.training_data = training_data

        
        
    def readTestD(self):
        filename = "/test_set.csv"
        test_data = self.readCSV(filename)
        self.test_data = test_data


    def readValidationD(self):
        filename = "/validation_set.csv"
        validation_data = self.readCSV(filename)
        self.validation_data = validation_data


    def __init__(self, folder):
        self.filepath = folder
        print(self.filepath, "Loading....")
        self.readTrainingD()
        self.readTestD()
        self.readValidationD()
        
        print(self.filepath, ": all 3 sets loaded")
        
