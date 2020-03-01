# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:21:08 2020

@author: Onkar
"""

import sys
import math
import string
import numpy as np
import pandas as pd
import matplotlib as plt

import LoadData as ld
import statics as st


# Stores best split column number/ name at an intermediate node
# Also stores references to the left and right child
class Decision_Node:

    # holds refrerence to child classes and the feature name/number on which currennt node is split
    def __init__(self, question, leftBranch, rightBranch):
        self.question = question
        self.leftBranch = leftBranch
        self.rightBranch = rightBranch


# stores leaf node and also calculates {label:count}
# for all samples that reached this leaf node
class Leaf:

    def countResult(self, rows):
        result = {}
        labels = rows[:, -1]
        result[0] = np.count_nonzero(labels == 0)
        result[1] = np.count_nonzero(labels != 0)
        
        return result

    def __init__(self, rows):
        self.predictions = self.countResult(rows)
        if(self.predictions[0] > self.predictions[1]):
            self.dominant = 0
        else:
            self.dominant = 1


# to predict the result of test, validation
def predict(sample, node):

    # Check if it is a leaf node
    if isinstance(node, Leaf):
        return node.dominant

    # if value of feature (column) stored in node.question 
    # for sample is 0, go to left, else right
    if sample[node.question] == 0:
        return predict(sample, node.leftBranch)
    else:
        return predict(sample, node.rightBranch)


def splitDataset(dataset, col):
    
    n_samples = np.shape(dataset)[0]
    leftchild = []
    rightchild = []
    for row in range(n_samples):
        if dataset[row][col] == 0:
            leftchild.append(dataset[row])
        else:
            rightchild.append(dataset[row])
    
    leftchild = np.array(leftchild)
    rightchild = np.array(rightchild)
    return leftchild, rightchild


def findBestSplit(dataset, features, heuristic):

    best_gain = 0  # keep track of the best information gain
    best_feature = None  # keep train of the feature / value that produced it
    
    if (heuristic == "H1"):
        current_impurity = st.calculateEntropy(dataset)
    else:
        current_impurity = st.calculateVarience(dataset)


    n_features = len(dataset[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        if col in features:
            # skip feature if it is already processed
            continue
        else:
            leftchild, rightchild = splitDataset(dataset, col)
        
            # Skip this split if it doesn't divide the dataset.
            if len(leftchild) == 0 or len(rightchild) == 0:
                continue

            # Calculate the information gain from this split
            gain = st.calculateGain(current_impurity, leftchild, rightchild)

            if gain > best_gain:
                best_gain, best_feature = gain, col

    return best_gain, best_feature


def buildTree(dataset, features, heuristic):

    if (heuristic == "H1"):
        curr_gain = st.calculateEntropy(dataset)
    else:
        curr_gain = st.calculateVarience(dataset)

    if curr_gain == 0:
        return Leaf(dataset)
        # return cls.isLeaf = True
    
    bestGain, bestFeature = findBestSplit(dataset, features, heuristic)
    
    if bestFeature != None:
        features.append(bestFeature)
    
    if bestGain == 0:
        # return cls.isLeaf = True
        return Leaf(dataset)
    else:
        leftChild, rightChild = splitDataset(dataset, bestFeature)
        leftBranch = buildTree(leftChild, features, heuristic)
        rightBranch = buildTree(rightChild, features, heuristic)

    return Decision_Node(bestFeature, leftBranch, rightBranch)
    

def print_tree(node, feature_names, spacing="|"):

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.dominant)
        return

    # Print the question at this node
    print (spacing, "X"+feature_names[node.question], '= 0:')
    print_tree(node.leftBranch, feature_names, spacing + "    |")


    print (spacing, "X"+feature_names[node.question], '= 1:')
    print_tree(node.rightBranch, feature_names, spacing + "    |")


def printAccuracy(testSet, mytree1, mytree2):
    
    correct = 0
    incorrect = 0
    for sample in range(len(testSet)):
        actual_result = testSet[sample][-1]
        row = testSet[sample][:21]
        pred_result = predict(row, mytree1)
        # print(pred_result)5
        if (actual_result == pred_result):
            correct +=1
        else:
            incorrect +=1
    print("Accuracy of training set with Huristics H1 = ", correct/len(testSet))
    
    correct = 0
    incorrect = 0
    for sample in range(len(testSet)):
        actual_result = testSet[sample][-1]
        row = testSet[sample][:21]
        pred_result = predict(row, mytree2)
        # print(pred_result)5
        if (actual_result == pred_result):
            correct +=1
        else:
            incorrect +=1
    print("Accuracy of training set with Huristics H2 = ", correct/len(testSet))
    

if __name__ == "__main__":
    
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

    trainingSet = str(sys.argv[1])
    validationSet = str(sys.argv[2])
    testSet = str(sys.argv[3])
    toPrint = str(sys.argv[4])
    huristic = str(sys.argv[5])

    trainingSet = pd.read_csv(trainingSet)
    trainingSet = np.array(trainingSet)
    
    validationSet = pd.read_csv(validationSet)
    validationSet = np.array(validationSet)

    testSet = pd.read_csv(testSet)
    testSet = np.array(testSet)

    features_H1 = []
    mytree_H1 = buildTree(trainingSet, features_H1, "H1")
    
    features_H2 = []
    mytree_H2 = buildTree(trainingSet, features_H2, "H2")
    
    
    printAccuracy(testSet, mytree_H1, mytree_H2)
    
    if toPrint == "yes":
        feature_names = list(string.ascii_uppercase)
        del[feature_names[21:]]
        del[feature_names[0]]
        if huristic == "H1":
            print_tree(mytree_H1, feature_names)
        else:
            print_tree(mytree_H2, feature_names)
        
    

