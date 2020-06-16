# -*- coding: utf-8 -*-
"""
Created on Mon Apr 4 22:00:40 2020

@author: Onkar
"""

import math
import random
import numpy as np


import readData


def initWeights(wordList):
    weights = {'training_bias': 1.0}
    for word in wordList:
        weights[word] = random.random()
    
    return weights


# Extracts the vocabulary of all the words in a data set
# dataset = {docName1:{word1:freq, word2:freq, ... wordn:freq}, 
#           docName2:{word1:freq, word2:freq, wordn:freq} ...}
def getWordlist(data_set):
    wordList = []
    for document in data_set:
        for word in data_set[document]:
            if word not in wordList:
                wordList.append(word)
    return wordList


# Retrive class labels from the dict of dicts
def getClassLabels(dataset):
    class_labels = {}
    for document in dataset:
        class_labels[document] = dataset[document]['class_label']
        del[dataset[document]['class_label']]
    return class_labels


# get accuracy of the dataset
def getAccuracy(weights, dataset, class_labels):
    
    num_correct_guesses = 0    
    for document in dataset:
        guess = predict(weights, dataset[document])
        if guess == int(class_labels[document]):
            num_correct_guesses += 1

    accuracy = [num_correct_guesses, len(dataset), (float(num_correct_guesses) / float(len(dataset)) * 100.0)]
    
    return accuracy


# Used to get the current perceptron's output. 
# If > 0, then spam, else output ham.
def predict(weights, document):
    weight_sum = weights['training_bias']          
    for word in document:
        if word not in weights:
            weights[word] = 0.0
        weight_sum += float(weights[word]) * float(document[word])
    
    if weight_sum > 0:
        return 1
    return 0

# check if actual class label matches with the predicted one
def crossCheck(class_labels, document):
    if class_labels[document] == "1":
        return 1
    return 0


# update the weights vector based on whether the predicted output was same or 
# different from the actual output
def updateWeights(weights, learningRate, document, actual_result, perceptron_output):
    for word in document:
        weights[word] += float(learningRate) * float((actual_result - perceptron_output)) * float(document[word])
    return weights


# learns weights using the perceptron training rule
def train_weights(weights, learningRate, training_set, epochs, class_labels):

    # initialize past accuracy to negative infinity
    pastAccuracy = float("-inf")

    for epoch in range(epochs):
        
        # get accuracy of model at the biginging of each eteration
        accuracy = getAccuracy(weights, training_set, class_labels)
        print("Epoch: ", epoch, "\t Accuracy: ", accuracy[2])

        # if accuracy is greater than 90 and it is same as past accuracy then:
        # break out of the loop as we do not want to be stuct in infinite loop
        # with no change in weights
        if ((accuracy[2] > 90) and (accuracy[2] == pastAccuracy)):
            return weights, epoch
        
        # update pastAccuracy before calculating the predictions
        pastAccuracy = accuracy[2]

        # Go through all training instances and update weights
        for document in training_set:

            perceptron_output = predict(weights, training_set[document])

            target_value = crossCheck(class_labels, document)

            weights = updateWeights(weights, learningRate, training_set[document], target_value, perceptron_output)

    return weights, epoch


def main():

# =============================================================================
# I obtained best accuracy (94.3515% with stopwards and 94.7699% without) when 
#                           epoch = 16
#                           learning rate 0.22
# As I am initializing weights randomly, accuracy may vary a little
# Thus, I have set some margin in number of epochs    
# =============================================================================

    epochs = 20
    learningRate = 0.22

    # load training data
    train = readData.readData("./train", remove_stopwards = False)
    train_dataset = train.dataSet

    # Extract words from training dataset
    wordList = getWordlist(train_dataset)

    # extract doc['class_label'] from each document
    # this will be used to crosscheck predicted class with actual class
    class_labels =  getClassLabels(train_dataset)


    # list to store [No_of_Epochs, LeariningRate, AccuracyWithStopwards, AccuracyWithoutStopwards]
    combination = []

    # Initialize first weights randomly
    weights = initWeights(wordList)    
    # Learn weights using the training_set
    print("-------------------Training Model---------------------")
    weights, no_epochs = train_weights(weights, learningRate, train_dataset, epochs, class_labels)

    
    print("------------------------------------------------------")
    print("-------------------Testing Model----------------------")
    print("------------------------------------------------------")
    # load test data without removing stopwards
    test = readData.readData("./test", remove_stopwards = False)
    test_dataset = test.dataSet
    test_class_labels = getClassLabels(test_dataset)


    # Report accuracy
    accuracy_withStopwards = getAccuracy(weights, test_dataset, test_class_labels)
    print ("Test Dataset With Stopwards\nEmails classified correctly: %d/%d" % (accuracy_withStopwards[0], accuracy_withStopwards[1]))
    print ("Test Dataset Accuracy: %.4f%%" % accuracy_withStopwards[2])
    print("------------------------------------------------------")



    # load test data with removing stopwards
    test = readData.readData("./test", remove_stopwards = True)
    test_dataset = test.dataSet
    test_class_labels = getClassLabels(test_dataset)

    # Report accuracy
    accuracy_withoutStopwards = getAccuracy(weights, test_dataset, test_class_labels)
    print ("Test Dataset Without Stopwards\nEmails classified correctly: %d/%d" % (accuracy_withoutStopwards[0], accuracy_withoutStopwards[1]))
    print ("Test Dataset Accuracy: %.4f%%" % accuracy_withoutStopwards[2])
    print("------------------------------------------------------")
    
    
    combination.append(no_epochs)        
    combination.append(learningRate)
    combination.append(accuracy_withStopwards[2])
    combination.append(accuracy_withoutStopwards[2])


if __name__ == "__main__":
    main()

