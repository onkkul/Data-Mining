# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


#function to calculate optimum threshold for selecting the principal components
def Calculation(dataset):
    
    pca = PCA()                                              #Create PCA model and pass data to it
    pca.fit(dataset) 
    pca.transform(dataset)
    variance = pca.explained_variance_ratio_* 100                 #This stores the variance contributions of each pc. *100 so that ratio is converted to percentage
    principalcomponents = 0
    for index in range(39):                                    #This for loop will return an index such that cummulative sum of variance till index is greater than 80%(index inclusive)
        if sum(variance[:index]) > 80:
            print("cumulative varience of dataset till ", index, "is: ", sum(variance[:index]))
            principalcomponents = index
            break
 
    return principalcomponents, variance

# function to display the results
def Visual(dataset1, result, variance1):
    
    plt.figure("Variation contribution of Principal Components")
    variance = list(variance1)
    
    tick = [1,10,38]
    
    plt.bar(x=range(1,11), height=variance[:10], label = "PC contributing 80.45% varience")
    plt.bar(x=range(11,len(variance)+1), height=variance[10:], label = "PC contributing remaining varience")
    plt.bar(x = tick, height = 0, tick_label = tick)
    
    plt.ylabel('Percentage of Variance')
    plt.xlabel('Principal Component no.')
    plt.legend()
    plt.show()

    plt.figure("PCA input - output datasets")
    plt.subplot(211)
    plt.title("PCA Original Dataset ")
    plt.plot(dataset1.T)
    plt.subplot(212)
    plt.title("PCA Projected-back Dataset")
    plt.plot(result.T)
    
    plt.show()
    plt.figure("Elbow")
    
    return


#function to project back the original data but with reduced dimentionality
def ProjectBack(Scaled_Dataset):

    principalcomponents, variance = Calculation(Scaled_Dataset)

    pca = PCA(n_components = principalcomponents)
    pca.fit(Scaled_Dataset)    
    reduced = pca.transform(Scaled_Dataset)
    
    print("PCA Reduced shape is: ", reduced.shape)
    #Project back reduced data to original featurespace
    project_back = pca.inverse_transform(reduced)
    
    Visual(Scaled_Dataset, project_back, variance)
    
    # Add the column for dates back in the reduced data
    first_col = np.zeros(shape = (527, 1))
    reduced = np.append(first_col, reduced, axis = 1)
    
    return reduced




