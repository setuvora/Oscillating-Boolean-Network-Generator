#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:08:18 2021

@author: smv
"""
import numpy as np
import scipy
import random
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams


rcParams['figure.figsize'] = 10, 10
x = True

def makeNetwork(nodes, k):
    #define the possible sign states of the edges
    signStates = [-1, 1]
    signMatrix = np.zeros((nodes, nodes))
    adSignMatrix = np.zeros((nodes, nodes))
    adMatrix = np.zeros((nodes, nodes), dtype=int)
    adMatrixInitial = np.zeros(nodes)
    #assign the position of edges directed at the first node
    if k>0:
        adMatrixInitial[1:k+1] = 1
    else:   
        adMatrixInitial = np.zeros(nodes)
    adMatrix[0] = adMatrixInitial
    for i in range(1, nodes):
        #roll the positions by 1 for the each additional node
        #to complete the adMatrix ie: [0, 1, 1, 1] -> [1, 0, 1, 1]
        adMatrixInitial = np.roll(adMatrixInitial, 1)
        adMatrix[i] = adMatrixInitial
        #randomly assign each edge a sign that is either 1 or -1 into a "sign matrix"
    for x in range(nodes):
        for y in range(nodes):
            signMatrix[x][y] = signStates[randint(0, 1)]
    #multiply the sign matrix by the adjacency matrix to make an adjacency-Sign matrix or "adSign"
    adSignMatrix = adMatrix * signMatrix
    #this will be used to update the network at each time step
    #turn all nodes on initially
    networkState = np.ones(nodes)
    return [adMatrix, adSignMatrix, networkState]

def runNetwork(nodes, k, timesteps):
    #make a network
    [adMatrix, adSignMatrix, networkState] = makeNetwork(nodes, k)
    networkStateTemp = networkState
    timecourse = np.zeros((timesteps, nodes))
    for i in range (timesteps):
        #for each timestep
        for j in range (nodes):
            #for the network state 
            #pass each node through an update rule depending on the sum of the product of the 
            #adSignMatrix * networkState at t-1 
            #store the values in a temporary array for synchronous updating
            if np.sum(adSignMatrix[j] * networkStateTemp) > 0:
                networkState[j] = 1
            if np.sum(adSignMatrix[j] * networkStateTemp) < 0:  
                networkState[j] = 0
            if np.sum(adSignMatrix[j] * networkStateTemp):
                networkState[j] = networkState[j]
        #update the network with the new values of the timestep    
        networkState = networkStateTemp
        timecourse[i] = networkState
    #turn the last two timesteps into lists for comparison
    a = list(timecourse[timesteps-1])
    b = list(timecourse[timesteps-2])
    #compare the last two timesteps, if they are different it implies oscillation
    if (a!= b):
        x = True 
    else:
        #print('No Oscillation')
        x = False  
    return [x, adMatrix, adSignMatrix, timecourse]

def testOscilltion(nodes, k, timesteps):
    g = False
    netNumber = 0
    while g == False:
        [g, adMatrix, adSignMatrix, timecourse] = runNetwork(nodes, k, timesteps)
        netNumber = netNumber + 1
        #print(netNumber)
        #print(adSignMatrix)
        #print('Trial # :' + str(netNumber))
    return g, adMatrix, adSignMatrix, timecourse
    
def runTrials(nodes, k, timesteps):
    trials = 100
    results = np.zeros(trials)
    print("defRun")
    for i in range(0, trials):
        #print("loop")
        g = False
        netNumber = 0
        while g == False and netNumber< 1001:
            #print(g)
            [g, adMatrix, adSignMatrix, timecourse] = runNetwork(nodes, k, timesteps)
            netNumber = netNumber + 1
        print(netNumber)
        if netNumber<1001:
            results[i] = 1/netNumber
        else: 
            netNumber = 0
        #print('Trial # :' + str(netNumber))
        #print(adSignMatrix)
        print(str(i) + ": " + str(netNumber))
    
    print(results)
    return nodes, k, results


resultsMaster = {"Trial": [],  "Result": []}
for i in range(1,101):
        g, adMatrix, adSignMatrix, timecourse = testOscilltion(10, 9, 10)
        timecourse.sort(axis=1)
        resultsMaster["Trial"].append(i)
        resultsMaster["Result"].append(timecourse)


data = pd.DataFrame.from_dict(resultsMaster)
trial = data["Trial"]
Result = data["Result"]
fig, ax = plt.subplots(10, 10, sharex=True, sharey=True)
x = 1
for i in range(0,10):
    for j in range(0,10):  
        r = np.asarray(Result[trial==x])

        sns.heatmap(r[0], cmap='plasma', ax=ax[i,j], cbar = False,
                    square=True)
        x = x + 1
plt.tight_layout()
plt.show()

'''

data = pd.DataFrame.from_dict(resultsMaster)
nodes = data["Nodes"]
k = data["k"]
Result = data["Result"]

    
array = np.zeros((10, 10))

for i in range(1, 11):
    for j in range(1, 11):
        if i>=j:
            array[i-1][j-1] = np.mean(np.mean(Result[(nodes==i) & (k == j)]))

# Compute the correlation matrix
# Generate a mask for the upper triangle
array = np.asmatrix(array, dtype=None)

x_axis_labels = [1,2,3,4,5,6,7,8,9,10] # labels for x-axis
y_axis_labels = [1,2,3,4,5,6,7,8,9,10] # labels for y-axis
mask = np.zeros_like(array)
mask[np.triu_indices_from(mask, 1)] = True
print(array)
print(mask)
sns.heatmap(array, mask=False, square=True, cmap='viridis', 
            xticklabels=x_axis_labels, yticklabels=y_axis_labels)
plt.xlabel('k edges',fontsize=20)
plt.ylabel('Nodes', fontsize=20)
plt.xticks(fontsize = 20)
plt.yticks(rotation=0, fontsize=20) 
plt.show()

ax = sns.heatmap(array, mask=mask, square=True, cmap='viridis', 
            xticklabels=x_axis_labels, yticklabels=y_axis_labels,
            linewidth=1,          
            cbar_kws={'label': 'p(Oscillation)',
                      'shrink': 1},
            )
plt.yticks(rotation=0, fontsize=20) 
plt.xticks(fontsize = 20)
plt.xlabel('Edges per node', fontsize=20)
plt.ylabel('Nodes', fontsize=20)
plt.tight_layout()
plt.show()



resultsMaster = {"Nodes": [], "k": [], "Result": []}

for i in range(1, 12):
    for j in range(1, 12):
        if i>=j:
            print(i, j)
            nodes, k, results = runTrials(i, j, 100)
            
'''
         

    


