# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:27:05 2019

@author: Onkar
"""

# =============================================================================
# This script takes input of 1000x100 CSV files WITHOUT headers.
# Please modify input data or use the CSV files provided with script.
# =============================================================================

import random
import numpy as np
import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot as plt
from sklearn.decomposition import FastICA


def loadData(filename):
	
	dataset = pd.read_csv(filename, header = None) 	 	 	
	dataset = np.array(dataset) 							
	scaled_dataset = preprocessing.scale(dataset) 		#scale the dataset to 0 mean and unit variance
	
	return scaled_dataset


def MSD(dataset, means):
	
	for row in range(1000):
		for column in range(0,100):
			diff = dataset[row][column] - means[column]
			sq_diff = diff**2
			dataset[row][column] = sq_diff/100

	return dataset


def Calculation(dataset):
	
	ica = FastICA(n_components=100)	
	result = ica.fit_transform(dataset)
	means = list(np.mean(result, axis = 0))
	square_deviation = MSD(result, means)
	
	index = random.randint(0,999)
	power_curve = list(square_deviation[index])
	power_curve.sort()
	power_curve.reverse()
	plt.figure("ICA power curve")
	plt.title("ICA Power curve of Dataset1 & Dataset2")
	plt.plot(power_curve, label = "row #"+str(index))
	plt.legend()
	plt.show()
	
	independent_components = list()
	for row in range(1000):
		variation = list(square_deviation[row])
		variation.sort()
		variation.reverse()
		total = sum(variation)
		for column in range(100):									#This for loop will return an index such that cummulative sum of variance till index is greater than 80%(index inclusive)
			if ((sum(variation[:column])/total)*100) > 80:
				independent_components.append(column)
				break
			
	return result, independent_components


def Visual(scaled_dataset1, result1, independent_components1, ic_value1, scaled_dataset2, result2, independent_components2, ic_value2):
	plt.figure("No of independent component")

	plt.subplot(211)
	plt.title('Independent Component for DataSet 1')	
	plt.ylabel('Independent Component no.')
	plt.xlabel('Row no.')
	plt.plot(independent_components1, 'c.', label = "Mean Component = "+str(ic_value1))
	plt.legend()

	plt.subplot(212)
	plt.title('Independent Component for Dataset 2')
	plt.ylabel('Independent Component no.')
	plt.xlabel('<-- Row no. -->')
	plt.plot(independent_components2, "r*", label = "Mean Component = "+str(ic_value2))
	plt.legend()
	
	plt.show()
	
	plt.figure("ICA input - output datasets")
	plt.subplot(221)
	plt.title("ICA Original Dataset 1")
	plt.plot(scaled_dataset1.T)
	plt.subplot(222)
	plt.title(" ICA Independent Components of Dataset 1")
	plt.plot(result1.T)
	plt.subplot(223)
	plt.title("ICA Original Dataset 2")
	plt.plot(scaled_dataset1.T)
	plt.subplot(224)
	plt.title("ICA Independent Components of Dataset 2")
	plt.plot(result2.T)
	
	plt.show()
	
	
def ProjectBack(dataset, ic_value):
	
	ica = FastICA(n_components=ic_value)
	transformed = ica.fit_transform(dataset)
	resultant = ica.inverse_transform(transformed)
	
	return resultant


print("Enter absolute file paths without inverted comma")
FirstFile = input("\n Enter absolute file path of first CSV file: \n")	#PLease provide absolute path
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_1.csv
SecondFile = input("Enter absolute file path of second CSV file: \n")
# D:/Academic/PostGraduate/Data Mining/assignment1/DataSet_2.csv

	
Scaled_Dataset1 = loadData(FirstFile)
Transformed1, Independent_Components1 = Calculation(Scaled_Dataset1)
IC_Value1 = int(np.mean(Independent_Components1))
Result1 = ProjectBack(Transformed1, IC_Value1)

print(IC_Value1, " is mean of Independent_Components for dataset1 shared by", Independent_Components1.count(IC_Value1), " vectors.",) #


Scaled_Dataset2 = loadData(SecondFile)
Transformed2, Independent_Components2 = Calculation(Scaled_Dataset2)
IC_Value2 = int(np.mean(Independent_Components2))
Result2 = ProjectBack(Transformed2, IC_Value2)

print(IC_Value2, " is mean of Independent_Components for dataset2 shared by", Independent_Components2.count(IC_Value2), " vectors.",) #


Visual(Scaled_Dataset1, Result1, Independent_Components1, IC_Value1, Scaled_Dataset2, Result2, Independent_Components2, IC_Value2)


