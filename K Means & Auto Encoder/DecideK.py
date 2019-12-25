# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import PCA
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer


def findK(reducedDataset):

    PCA_DataSet = PCA.ProjectBack(reducedDataset)
    
    
    # Calculate K for given dataset
    kmeans = KMeans(init='k-means++', n_init=10, max_iter=600, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='full')
    visualizer = KElbowVisualizer(kmeans, k=(1,20), timings = False)
    visualizer.fit(reducedDataset)        # Fit the data to the visualizer
    visualizer.show()
    
    K = visualizer.elbow_value_

    #calculate K for reduced dataset
    
    # kmeans = KMeans(init='k-means++', n_init=10, max_iter=600, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='full')
    # visualizer = KElbowVisualizer(kmeans, k=(1,15), timings = False)
    # visualizer.fit(PCA_DataSet)        # Fit the data to the visualizer
    # visualizer.show()
    # reducedK = visualizer.elbow_value_
    
    reducedK = 0

    return K, reducedK