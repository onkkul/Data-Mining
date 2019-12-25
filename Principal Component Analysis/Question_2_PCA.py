# -*- coding: utf-8 -*-
"""
Created on Thu Oct 6 11:56:50 2019

@author: Onkar Kulkarni
"""

# =============================================================================
# This script takes input of 1000x100 CSV files WITHOUT headers.
# Please modify input data or use the CSV files provided with script.
# =============================================================================

import numpy as np
import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def loadData(filename):
	
	dataset = pd.read_csv(filename, header = None) 	 	 	
	dataset = np.array(dataset) 							
	scaled_dataset = preprocessing.scale(dataset) 		#scale the dataset to 0 mean and unit variance
	
	return scaled_dataset


#function to calculate optimum threshold for selecting the principal components
def Calculation(dataset):
	
	pca = PCA() 												#Create PCA model and pass data to it
	pca.fit(dataset)	
	pca.transform(dataset)
	variance = pca.explained_variance_ratio_* 100 				#This stores the variance contributions of each pc. *100 so that ratio is converted to percentage
	principalcomponents = 0
	for index in range(100):									#This for loop will return an index such that cummulative sum of variance till index is greater than 80%(index inclusive)
		if sum(variance[:index]) > 80:
			print("cumulative varience of dataset 1 till ", index, "is: ", sum(variance[:index]))
			principalcomponents = index
			break
		
	return principalcomponents, variance


#function to project back the original data but with reduced dimentionality
def ProjectBack(dataset, principalcomponents):
	
	pca = PCA(n_components = principalcomponents)
	pca.fit(dataset)	
	transformed = pca.transform(dataset)
	resultant = pca.inverse_transform(transformed)
	
	return resultant



def Visual(dataset1, result1, variance1, dataset2, result2, variance2):
	
	plt.figure("Variation contribution of Principal Components")

	plt.subplot(211)
	plt.title('Variation contribution of Principal Components for DataSet 1')	
	variance = list(variance1)
	tick = [1,50,100]
	
	plt.bar(x=range(1,51), height=variance[:50], label = "PC contributing 80.10% varience")
	plt.bar(x=range(51,len(variance)+1), height=variance[50:], label = "PC contributing remaining varience")
	plt.bar(x = tick, height = 0, tick_label = tick)
	
	plt.ylabel('Percentage of Variance')
	plt.xlabel('Principal Component no.')
	plt.legend()

	plt.subplot(212)
	plt.title('Variation contribution of Principal Components for Dataset 2')
	variance = list(variance2)
	tick = [1,47,100]
	
	plt.bar(x=range(1,48), height=variance[:47], label = "PC contributing 80.07% varience")
	plt.bar(x=range(48,len(variance)+1), height=variance[47:], label = "PC contributing remaining varience")
	plt.bar(x = tick, height = 0, tick_label = tick)
	
	plt.ylabel('Percentage of Variance')
	plt.xlabel('Principal Component no.')
	plt.legend()
	
	plt.figure("PCA input - output datasets")
	
	plt.subplot(221)
	plt.title("PCA Original Dataset 1")
	plt.plot(dataset1.T)
	plt.subplot(222)
	plt.title("PCA Dataset 1 Using Reduced Dimensions PCA")
	plt.plot(result1.T)
	plt.subplot(223)
	plt.title("PCA Original Dataset 2")
	plt.plot(dataset2.T)
	plt.subplot(224)
	plt.title("PCA Dataset 2 Using Reduced Dimensions PCA")
	plt.plot(result2.T)
	
	plt.show()


print("Enter absolute file paths without inverted comma")
FirstFile = input("\n Enter absolute file path of first CSV file: \n")	#PLease provide absolute path
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_1.csv
SecondFile = input("Enter absolute file path of second CSV file: \n")
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_2.csv

Scaled_Dataset1 = loadData(FirstFile)
PrincipalComponents1, Variance1 = Calculation(Scaled_Dataset1)
Result1 = ProjectBack(Scaled_Dataset1, PrincipalComponents1)


Scaled_Dataset2 = loadData(SecondFile)
PrincipalComponents2, Variance2 = Calculation(Scaled_Dataset2)
Result2 = ProjectBack(Scaled_Dataset2, PrincipalComponents2)

Visual(Scaled_Dataset1, Result1, Variance1, Scaled_Dataset2, Result2, Variance2)

