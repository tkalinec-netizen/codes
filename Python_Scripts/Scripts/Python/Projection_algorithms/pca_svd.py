# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:55:14 2016

@author: Tom83 Kalinec
"""

from numpy import *
import operator
from os import listdir
import matplotlib
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import *
from scipy.stats.stats import pearsonr


def svd(data, S=2):
    samples,features = shape(data) 
    #calculate SVD
    U, s, V = linalg.svd( data )
    Sig = mat(eye(S)*s[:S])
    #tak out columns you don't need
    newdata = U[:,:S]
     
    # this line is used to retrieve dataset 
    #~ new = U[:,:2]*Sig*V[:2,:]
 
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    colors = ['blue','red','black']
    for i in range(samples):
        ax.scatter(newdata[i,0],newdata[i,1], color= colors[int(data[i,-1])])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
         

def main():
    # Nacteni dat (vzorku)
    iris = datasets.load_iris()
    raw_data= iris.data[:, :4]
    samples,features = shape(raw_data)
    data = mat(raw_data[:,:4])
    # Vyber z nahodnych dat (vzorku)
    #X=(np.matrix.round(10*np.random.randn(100,4)))/100
    #data = mat(X[:,:4])
    # Spusteni programu
    svd(data,2)
    
if __name__ == "__main__":
    main()   
