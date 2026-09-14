# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:20:43 2016

@author: Kalinec T
"""

from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from numpy.linalg import *
from scipy.stats.stats import pearsonr
  
def PCA (X,N):
    """ Function doc """ 
    data = mat(log10(X))
    means = mean(data,axis=0)
    data = data - means;
    samples,features = shape(data)
    # Covariance matrix
    covar = cov(data,rowvar=0)
 
    #eigvalues
    eigvalues,eigvectors = eig(covar)
 
    #sort it from big to small
    index = argsort(eigvalues)
    index = index[:-(N+1):-1]
    eigvector_sorted = eigvectors[:,index]
 
    # summary it transfor into low Dimensions 
    newdata = data*eigvector_sorted
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    colors = ['blue','red','black']
    for i in range(samples):
        ax.scatter(newdata[i,0],newdata[i,1], color= colors[int(X[i,-1])])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
     
    return newdata;

def main(): 
    iris = datasets.load_iris()
    data = iris.data
    #data = mat(raw_data[:,:4])
    X = (np.matrix.round(100*np.random.randn(100,4)))/100
    PCA(data,N=2)
    
if __name__ == "__main__":
    main()
    