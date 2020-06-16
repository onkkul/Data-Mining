# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:39:48 2020

@author: Onkar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:51:12 2020

@author: Onkar
"""

import os
import numpy as np
import pandas as pd
# from nltk.stem.porter import *
# from nltk.stem.snowball import SnowballStemmer



class readData():
        
    def getFilenames(self, ham, spam):
        self.hamFiles = os.listdir(ham)   
        self.spamFiles = os.listdir(spam)


    def normalizeContents(self, fileContent):
        stemmer = SnowballStemmer("english", ignore_stopwords=True)
        
        print(fileContent)
        
    # read file contents and clean it
    def readFile(self, fileName):
        fileName = self.ham + fileName
        with open (fileName, "r+") as oneFile:
            flat_list=[word for line in oneFile for word in line.split()]
            print(flat_list)

            

            
    def loadWords(self):
        print(len(self.hamFiles))
        for eachFile in self.hamFiles[338:340]:
            print(eachFile)
            self.readFile(eachFile)

    

    def countFreq(self):
        folder = "/test_set.csv"
        test_data = self.getFilenames(folder)
        self.test_data = test_data


    def __init__(self, folder):
        self.ham = folder + "/ham/"
        self.spam = folder + "/spam/"
        self.getFilenames(self.ham, self.spam)
        # self.readFile()
        # self.countFreq()
        self.loadWords()
    
        
