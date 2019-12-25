# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:00:20 2019

@author: Onkar Kulkarni
"""

import numpy as np # linear algebra
from keras.models import Model
from keras.layers import Input, Dense
from matplotlib import pyplot as plt


def splitData(dataSet):
    
    train = np.ndarray(shape = (450, 38))
    for row in range(450):
        for column in range(38):
            train[row][column] = dataSet[row][column]

    test = np.ndarray(shape = (77, 38))
    for row in range(450, 527):
        for column in range(38):
            test[row - 450][column] = dataSet[row][column]
            
    print('CleanData data shape', dataSet.shape)
    print('Train data shape', train.shape)
    print('Test data shape', test.shape)
    
    return train, test, dataSet

def writeResults(encoded_data):
    # Store final centroids
    np.savetxt("Encoded_Dataset.data", encoded_data,fmt='%.3f', delimiter = ',')
    return


def visual(original, encoded):
    
    plt.figure("Encoder input - output datasets")
    plt.subplot(211)
    plt.title("Encoded Dataset")
    plt.plot(encoded.T)
    
    plt.subplot(212)    
    plt.title("Original Dataset ")
    plt.plot(original.T)
    plt.show()
    return
    
    
def encode(cleanedDataSet):
    trainData, testData, dataSet = splitData(cleanedDataSet)
    
    original_fetures = 38
    # Keping closer to PC number of PCA for comparison
    reduced_features = 10
    
    old_dimentions = Input(shape = (original_fetures, ))
    
    first_layer_encoder = Dense(30, activation = 'relu')(old_dimentions)
    second_layer_encoder = Dense(20, activation = 'relu')(first_layer_encoder)
    third_layer_encoder = Dense(reduced_features, activation = 'relu')(second_layer_encoder)
    
    first_layer_decoder = Dense(20, activation = 'relu')(third_layer_encoder)
    second_layer_decoder = Dense(30, activation = 'relu')(first_layer_decoder)
    third_layer_decoder = Dense(original_fetures, activation = 'sigmoid')(second_layer_decoder)
    
    # Combine Encoder and Deocder layers
    autoencoder = Model(inputs = old_dimentions, outputs = third_layer_decoder)
    
    autoencoder.summary()
    
    # Compile the Model
    autoencoder.compile(optimizer = 'adadelta', loss = 'binary_crossentropy')
    autoencoder.fit(trainData, trainData, nb_epoch = 50, batch_size = 25, shuffle = True, validation_data = (testData, testData))
    encoder = Model(inputs = old_dimentions, outputs = third_layer_encoder)

    encoded_Data = encoder.predict(dataSet)

    print("\nThe encoder reduced shape is: ", encoded_Data.shape)
    writeResults(encoded_Data)

    visual(dataSet, encoded_Data)
    
    return encoded_Data
