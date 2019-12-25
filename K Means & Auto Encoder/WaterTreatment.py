# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import CleanData
import DecideK
import PCA
import Kmeans
import AutoEncoder
import sklearn.metrics as mse
import numpy as np

default_K = 8
default_reducedK = 7
choice = 0

while choice < 6:
    print("\n1. Find Optimal Value of K for both normal and reduced data")
    print("2. Perform clustering over normal data")
    print("3. Perform clustering over reduced data")
    print("4. Display Autoencoder results")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if (choice == 1):
        dataset = CleanData.removeDate()
        Calculated_K, calculated_reducedK = DecideK.findK(dataset)
        print("\nOptimum values using Elbow Method are: ")
        print("For normal data: ", Calculated_K, " For reduced data: ", calculated_reducedK, "\n")
    
    elif (choice == 2):
        dataset = CleanData.cleanData()
        final_clusters, final_centroids = Kmeans.kmeans(default_K, dataset)
        Kmeans.writeResults(final_clusters, final_centroids, 2)
    
    elif (choice == 3):
        dataset = CleanData.removeDate()
        reduced = PCA.ProjectBack(dataset)
        
        # For calculation of MSE
        # mean = np.mean(reduced, axis = 0)
        # a = np.array(reduced[0][::])
        # print(mse.explained_variance_score(mean, a, sample_weight=None, multioutput='uniform_average'))      


        final_clusters, final_centroids = Kmeans.kmeans(default_reducedK, reduced)
        Kmeans.writeResults(final_clusters, final_centroids, 3)
    
    elif(choice == 4):
        dataset = CleanData.removeDate()
        Encoded = AutoEncoder.encode(dataset)
        
        #for calculation of MSE
        # mean = np.mean(Encoded, axis = 0)
        # a = np.array(Encoded[0][::])
        # print(mse.explained_variance_score(mean, a, sample_weight=None, multioutput='uniform_average')) 
        
    elif(choice == 5):
        choice = 10
    
    else:
        print("I will pretend I didn't see that...\n")
        choice = 0
