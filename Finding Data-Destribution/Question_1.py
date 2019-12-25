# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:27:19 2019

@author: Onkar Kulkarni
"""

# =============================================================================
# This script takes input of 1000x100 CSV files WITHOUT headers.
# Please modify input data or use the CSV files provided with script.
# =============================================================================

import random
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from matplotlib import pyplot as plt


def loadData(filename):
	
	dataset = pd.read_csv(filename, header = None) 	 	 	
	dataset = np.array(dataset) 							
	
	return dataset


#Randomly selecting 10 distinct row indices for dataset1 and load in subset
def randomSelection(dataset):
	
	row_indices = (random.sample(range(1000),10))
	row_indices.sort()

	subset = list()
	for each_row in row_indices: 			#Add those randomly selescted rows to a subset data
		subset.append(dataset[each_row])
	np.array(subset)
	
	return subset, row_indices	


#graphical disply of distribution
def visual(subset1, row_indices1, subset2, row_indices2):

	plt.figure("DataSet Distributions")
	
	plt.subplot(211)
	plt.title('Q1 - Uniform (Dataset 1)')
	plt.ylabel('<-- Value of each Vector Components -->')
	plt.xlabel('<-- Vectors -->')
	for row in range(5): 	#change to 10 if you wish to see all the 10 samples
		sns.distplot(subset1[row], hist = True, kde = False, kde_kws = {'linewidth': 1}, label = "row #"+str(row_indices1[row]))
			   
	plt.subplot(212)
	plt.title('Q1 - Gaussian (Dataset 2)')
	plt.ylabel('<-- Value of each Vector Components -->')
	plt.xlabel('<-- Vectors -->')
	for row in range(10):
		sns.distplot(subset2[row], hist = False, kde = True, kde_kws = {'linewidth': 3}, label = "row #"+str(row_indices2[row]))
	
	plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
	plt.show()


#calculate distribution parameters of dataset
def DistributionParameters(subset, index):
	parameters = list()
	for row in range(10):
		per_row = list()
		per_row.append(index[row]) 						#Row no
		per_row.append(np.mean(subset[row]))			#Mean
		per_row.append(np.median(subset[row]))			#Median
		per_row.append(stats.mode(subset[row])) 		#Mode
		per_row.append(np.std(subset[row])) 			#Std deviation
		per_row.append(np.var(subset[row])) 			#varience
		per_row.append(min(subset[row])) 				#min
		per_row.append(max(subset[row])) 				#max
		per_row.append(np.percentile(subset[row], 25)) 	#First Quartile
		per_row.append(np.percentile(subset[row], 75)) 	#Third Quartile
		per_row.append(stats.iqr(subset[row])) 			#Interquartile Range
		parameters.append(per_row)
	
	parameters = pd.DataFrame(parameters, columns = ['Row #', 'Mean', 'Median', 'Mode', 'Std', 'Variance', 'Min', 'Max', 'Quart 1', 'Quart 2', 'IQ Range'])
	print("Distribution Parameters are: \n", parameters)

	return parameters


print("Enter absolute file paths without inverted comma")
FirstFile = input("\n Enter absolute file path of first CSV file: \n")	#PLease provide absolute path
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_1.csv
SecondFile = input("Enter absolute file path of second CSV file: \n")
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_2.csv


DataSet1 = loadData(FirstFile)
SubSet1, Indices1 = randomSelection(DataSet1)
Parameters1 = DistributionParameters(SubSet1, Indices1) 	#this contains all the destribution parameters for dataset 1


DataSet2 = loadData(SecondFile)
SubSet2, Indices2 = randomSelection(DataSet2)
Parameters2 = DistributionParameters(SubSet2, Indices2) 	#this contains all the destribution parameters for dataset 2


visual(SubSet1, Indices1, SubSet2, Indices2)

