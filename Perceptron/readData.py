# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:00:35 2020

@author: Onkar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:39:48 2020

@author: Onkar
"""


import os
import string
import numpy as np
import pandas as pd
from collections import Counter
from nltk.stem.snowball import SnowballStemmer

import encyclopedia


class parser():
    
    # convert words "I'd" to "I would". refrer encyclopedia.py for complete list
    def cleanAppostrophe(self, words):
        index = 0
        while index < len(words):
            if words[index] == "'":
                words[index-1] = words[index-1] + words[index] + words[index+1]
                if words[index-1] in encyclopedia.appos.keys():
                    replace = encyclopedia.appos[words[index-1]].split()
                    words[index-1] = replace[0]
                    words[index] = replace[1]
                    del[words[index+1]]
                else:
                    del[words[index+1]]
                    del[words[index]]
            index += 1
        return words


    # remove all punctuation marks
    def removePunctuation(self, words):
        table = str.maketrans('', '', string.punctuation)
        removed = [w.translate(table) for w in words]       
        return removed


    # remove stopwards. refrer encyclopedia.py for complete list
    def removeStopwards(self, frequencies):
        for key in list(frequencies.keys()):
            if key in encyclopedia.stopwards:
                del frequencies[key]
        return frequencies


    # perfrom stemming
    def getStemwords(self, words):
        stemmer = SnowballStemmer("english")
        for index in range(len(words)):
            words[index] = stemmer.stem(words[index])
        return words


    # count frequencies of each word such that {word1:freq, word2:freq}
    def countFreq(self, words):
        frequencies = Counter(words)
        frequencies = dict(frequencies)
        
        # delete all keys of integer type
        for key in list(frequencies.keys()):
            if not key.isalpha():
                del frequencies[key]
        return frequencies


    # clean the contents of file
    def getFreq(self, fileContent):
        fileContent = str.lower(fileContent)
        words = fileContent.split()
        words = self.cleanAppostrophe(words)
        words = self.removePunctuation(words)
        words = self.getStemwords(words)

        frequencies = self.countFreq(words)
        if self.remove_stopwards == True:
            frequencies = self.removeStopwards(frequencies)

        return frequencies
    
    def __init__(self, stopwards):
        self.remove_stopwards = stopwards



class readData():

    def getFilenames(self):
        self.hamFiles, self.spamFiles = os.listdir(self.ham), os.listdir(self.spam)
        return self.hamFiles, self.spamFiles

        
    # read file content
    def readFile(self, folder, fileName):
        fileName = folder + fileName
        with open (fileName, "r+") as oneFile:
            content = oneFile.read()
        return content        


    # create a dict such that {doc1:{word1:freq,word2:freq,...}, doc2:{word1:} ...}
    def shapeMatrix(self):
        # above mentioned dict
        dataSet = {}
        Parser = parser(self.remove_stopwards)

        hamFiles, spamFiles = self.getFilenames()
        
        for eachHamfile in hamFiles:
            content = self.readFile(self.ham, eachHamfile)
            frequencies = Parser.getFreq(content)
            frequencies["class_label"] = "0"
            dataSet[eachHamfile] = frequencies

        for eachSpamfile in spamFiles:
            content = self.readFile(self.spam, eachSpamfile)
            frequencies = Parser.getFreq(content)
            frequencies["class_label"] = "1"
            dataSet[eachSpamfile] = frequencies
        
        return dataSet
            
            
    # form a matrix such as 
    # | docID | word1 | word2 | ... | ham/spam
    # | 1     |   2   |   4   |  7  | ham
    def createDTM(self):
        
        dataSet = self.shapeMatrix()
        self.dataSet = dataSet
        
        # convert the dictionary of dictionaries into above mentioned matrix
        # dataSet = pd.DataFrame.from_dict(dataSet, orient='index')
        # dataSet.sort_index(axis = 1, inplace=True)
        
        # # make the class_label column last
        # features = list(dataSet.columns)
        # del[features[features.index("class_label")]]
        # features.append("class_label")
        # dataSet = dataSet[features]

        # # fill empty values with 0
        # dataSet.fillna(0, inplace = True)

        # # self.dataSet = dataSet
        # self.features = np.array(self.dataSet.iloc[:, 0:-1])
        # self.feature_names = np.array(self.dataSet.columns)
        # self.labels = np.array(self.dataSet.iloc[:,-1])
        # self.dataSet = np.array(self.dataSet)

        # # store the dataframe in csv file. why?? Who knows!!!
        # dataSet.to_csv("Dataset.csv")
        # feature_names = pd.DataFrame(dataSet.columns)
        # feature_names.to_csv("Features.csv")


    def __init__(self, folder, remove_stopwards):
        self.remove_stopwards = remove_stopwards
        self.ham = folder + "/ham/"
        self.spam = folder + "/spam/"
        # print("loading... ", self.ham, self.spam)
        
        self.createDTM()
