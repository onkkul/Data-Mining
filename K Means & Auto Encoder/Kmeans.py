# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import math
import copy
import pickle
import random
import hashlib
import numpy as np
import pandas as pd

# Select initial centroids
def initial_centroids(k, cleanedDataSet):
    
    row, column = np.shape(cleanedDataSet)
    
    print("Would you like to use the same intial centroids that were used while generating the result file?")
    setDefault = input("1. Yes, I want to cross-check results\n2. No, Select randomly\n(1/2) : ")
    
    if (setDefault == '1'):
        default_centroids = pd.read_csv("Default_initialCentroids.csv", header = None)
        all_centroids = np.array(default_centroids)
    
    else:
        print("Calculating initial ", k," centroids...")
        all_centroids = np.ndarray(shape = (k,column))
        sampling = list(random.sample(range(527), k))
        
        for each in range(0, k):
            all_centroids[each][0] = each
            for x in range(1, column):
                all_centroids[each][x] = cleanedDataSet[sampling[each]][x]
        # np.savetxt("randomCentroids.csv", all_centroids,fmt='%.3f', delimiter = ',')   
    
    return all_centroids


def calculateCentroids(k, all_clusters, cleanedDataset):
    
    # Create an array to store new centriods
    row, column = np.shape(cleanedDataset)
    new_centroids = np.ndarray(shape = (k,column))
    
    for cluster_index, cluster in enumerate(all_clusters):
        temp_dataframe = []
        new_centroids[cluster_index][0] = cluster_index

        for member in cluster:
            temp_dataframe.append(list(cleanedDataset[member][1::]))

        temp_dataframe = np.array(temp_dataframe)
        mean = np.mean(temp_dataframe, axis = 0)
        for mean_feature in range(1, column):
              new_centroids[cluster_index][mean_feature] = mean[mean_feature - 1]
              new_centroids[cluster_index][mean_feature] = float(format(new_centroids[cluster_index][mean_feature], ".4f"))
        
    return new_centroids


# function to check if previous clustering results
# are same as this clustering result (comparing hash of both)
def isSame(clusters_old, clusters_new):
    old_hash = hashlib.md5(pickle.dumps(clusters_old)).hexdigest()
    new_hash = hashlib.md5(pickle.dumps(clusters_new)).hexdigest()
    if (old_hash == new_hash):
        return True
    else:
        return False
     

def kmeans(k, cleanedDataSet):
    
    # Select initial k centroids
    centroids = initial_centroids(k, cleanedDataSet)
        
    # Initialize k clusters
    final_clusters = []
    for x in range(k):
        cluster = list()
        final_clusters.append(cluster)
    
    # Create a list to store previous clustering result
    previous_clusters = []


# =============================================================================
#                           MAIN CLUSTERING
# =============================================================================

    iteration = 0
    while(isSame(previous_clusters, final_clusters) == False):
        iteration += 1
        print("iteration: ", iteration)
        
        # Create a copy of previous clustering result and
        # Clear the final_clusters list to store the new clustering
        previous_clusters = copy.deepcopy(final_clusters)
        for x in range(k):
            final_clusters[x].clear()
        
        # Calculate mean square difference for each datapoint from each centroid
        for row in range(0,527):
            # Create a list to store distance of each sample from each centroid
            euclidian_distance = list()
            a = cleanedDataSet[row][1:]
            
            for x in range(k):
                b = centroids[x][1:]
                dist = math.sqrt(sum([(x - y) ** 2 for x, y in zip(a, b)]))
                dist = float(format(dist, ".4f"))
                euclidian_distance.append(dist)
            
            # Find the closest cluster based in the distance calculated
            cluster_index = euclidian_distance.index(min(euclidian_distance))
            
            # Assign sample to that cluster
            final_clusters[cluster_index].append(row)
        
        centroids = calculateCentroids(k, final_clusters, cleanedDataSet)

    # Calculate final centroids
    centroids = calculateCentroids(k, final_clusters, cleanedDataSet)
    return final_clusters, centroids


def writeResults(final_clusters, final_centroids, Choice):

    if (Choice == 2):
        print("writing results to 'WithOut_PCA_OutPut.data'")
        filename = "OutPut_WithOut_PCA_.data"
    else:
        print("writing results to 'With_PCA_OutPut.data'")
        filename = "OutPut_with_PCA_.data"
    
    
    # Store final centroids
    np.savetxt("finalCentroids.csv", final_centroids,fmt='%.3f', delimiter = ',')
     
    result = {}
    renamed = {}
    new_name = 0
    samples = list(range(527))
    
    print("\n----Final Clustering Results ----","\nindex\t", "size")
    # Creating a dict s.t. {sample:cluster}
    for cluster_index, cluster in enumerate(final_clusters):
        count = 0
        for member in cluster:
            count += 1
            result[member] = cluster_index
        print(cluster_index + 1, "\t", count)

    print("\n---- Renaming Results ----")
    # Renaming clusters s.t. sample 0 in cluster 0
    with open(filename, "w+") as writeResult:
        for each in samples:
            if (result[each] not in renamed.keys()):
                renamed[result[each]] = new_name
                print(result[each]+1, " renamed to ", new_name+1)
                result[each] = new_name
                new_name +=1
            else:
                result[each] = renamed[result[each]]
            
            writeResult.write(str(each + 1))
            writeResult.write("\t\t")
            writeResult.write(str(result[each]+1))
            writeResult.write("\n")    

    return