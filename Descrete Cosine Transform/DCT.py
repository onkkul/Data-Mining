# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:23:06 2019

@author: Onkar
"""

# =============================================================================
# This script takes input of 1000x100 CSV files WITHOUT headers.
# Please modify input data or use the CSV files provided with script.
# =============================================================================

import copy
import math
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



def loadData(filename):
	
	dataset = pd.read_csv(filename, header = None) 	 	 	
	dataset = np.array(dataset)
	return dataset


#function to calculate Mean Square Deviation of a datapoint.
#This metric is used to determine variance contributed by a feature in further references
def MSD(dataset, means):
	
	for row in range(1000):
		for column in range(0,100):
			diff = dataset[row][column] - means[column]
			sq_diff = diff**2
			dataset[row][column] = sq_diff/100

	return dataset


#function to truncate feature space such that only features
#that contribute to 80% of Mean Square Deviation are retained
def Truncation(variance, dataset):
		
	final_dataset = list()
	significant = list() 	#A list of list such that each member list contains
							# indices of significant features for that vector
	
	
	#this loop calculates significance of a featue in vector and
	#stores its index if cumulative significance upto that index is > 80%
	dush = list()
	dushdush = list()
	for row in range(1000):				
		significant_columns = list()	
		tmp = list(variance[row])
		tmp.sort()
		tmp.reverse()
		total = sum(tmp)
		
		for x in range(len(tmp)):
			if sum(tmp[:x])/total > 0.8:
				dush.append(x)
				dushdush.append(row)
				print(row, x)
				del(tmp[x:])
				break
		
		for column in range(100):
			if variance[row][column] in tmp:
				significant_columns.append(column)
		significant.append(significant_columns)
	print(min(dush), max(dush))
	print("######################################################3")
	#This loop uses indices calculated in previous loop
	# to load the significant feature values in a new numpy array 
	for row in range(1000):
		final_row = list()
		for column in significant[row]:
			final_row.append(dataset[row][column])
		final_dataset.append(final_row)

	final_dataset = np.array(final_dataset)
	return final_dataset
	

#main DCT function
def DCT(dataset):
	
	transformed = copy.deepcopy(dataset)
	for row in range(1000):
		for column in range(100):
			k = 100
			if column == 0:
				alpha = math.sqrt(1/k)
			else:
				alpha = math.sqrt(2/k)		
				
			transformed[row][column] = alpha*(dataset[row][column]*math.cos((2*row + 1)*(column*math.pi)/(2*k)))
	
	means = list(np.mean(transformed, axis = 0))
	
	#calling mean square daviation function to get varience matrix
	square_deviation = MSD(transformed, means)

	reduced_dataset = Truncation(square_deviation, transformed)
	
	#plot power curve of a random sample
	index = random.randint(0,999)
	pre_transition = list(transformed[index])
	pre_transition.sort()
	pre_transition.reverse()
	post_transition = list(reduced_dataset[index])
	post_transition.sort()
	post_transition.reverse()
	plt.figure("DCT power curve")
	plt.title("DCT Power curve of Dataset1 & Dataset2")
	x = len(post_transition)-1
	y = post_transition[-1]
	plt.annotate(x, (x,y))
	plt.plot(post_transition, label = "80% varience of row #"+str(index))
	plt.plot(pre_transition, label = "remaining variance of row#"+ str(index), alpha = 0.5)
	plt.legend()

	plt.show()

	return reduced_dataset, transformed


def Visual(original1, transformed1, reduced_dataset1, original2, transformed2, reduced_dataset2):

	#Data transformation graphs of DataSet 1
	plt.figure("DCT transition graphs of DataSet 1")
	
	plt.subplot(311)
	plt.title("Unprocessed Dataset 1")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in original1:
		plt.plot(x)

	plt.subplot(312)
	plt.title("DCT transformed")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in Transformed1:
		plt.plot(x)
		
	plt.subplot(313)
	plt.title("Final reduced matrix")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in reduced_dataset1:
		plt.plot(x)
	
	#Data transformation graphs of DataSet 2
	plt.figure("DCT transition graphs of DataSet 2")
	
	plt.subplot(311)
	plt.title("Unprocessed Dataset 2")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in original2:
		plt.plot(x)

	plt.subplot(312)
	plt.title("DCT transformed")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in Transformed2:
		plt.plot(x)
		
	plt.subplot(313)
	plt.title("Final reduced matrix")
	plt.ylabel("feature component value ->")
	plt.xlabel("<- no. of feature components ->")
	for x in reduced_dataset2:
		plt.plot(x)
		
	plt.show()


print("Enter absolute file paths without inverted comma")
FirstFile = input("\n Enter absolute file path of first CSV file: \n")	#PLease provide absolute path
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_1.csv
SecondFile = input("Enter absolute file path of second CSV file: \n")
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_2.csv


DataSet1 = loadData(FirstFile)
Reduced_Dataset1 ,Transformed1 = DCT(DataSet1)


DataSet2 = loadData(SecondFile)
Reduced_Dataset2 ,Transformed2 = DCT(DataSet2)


Visual(DataSet1, Transformed1, Reduced_Dataset1, DataSet2, Transformed2, Reduced_Dataset2)


