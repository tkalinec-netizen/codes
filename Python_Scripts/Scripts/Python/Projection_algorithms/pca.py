# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:27:59 2015

@author: Tomas kalinec
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
import numpy as np 
import time
   
def pca(*args):
 
    from sklearn.decomposition import PCA
  
    if len(args)<2:
        
        start=time.time()
        # import some data to play with
        iris = datasets.load_iris()
        X = iris.data[:, :2]  # we only take the first two features.
        Y = iris.target
        start=time.time()
        x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
        y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
        
        plt.figure(2, figsize=(8, 6))
        plt.clf()
        
        # Plot the training points
        plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.xticks(())
        plt.yticks(())
        
        # To getter a better understanding of interaction of the dimensions
        # plot the first three PCA dimensions
        fig = plt.figure(1, figsize=(8, 6))
        ax = Axes3D(fig, elev=-150, azim=110)
        X_reduced = PCA(n_components=3).fit_transform(iris.data)
        ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y,
                   cmap=plt.cm.Paired)
        t=time.time()-start
        print('Elapsed time is ', t, 's.')
        ax.set_title("First three PCA directions")
        ax.set_xlabel("1st eigenvector")
        ax.w_xaxis.set_ticklabels([])
        ax.set_ylabel("2nd eigenvector")
        ax.w_yaxis.set_ticklabels([])
        ax.set_zlabel("3rd eigenvector")
        ax.w_zaxis.set_ticklabels([])
        s=time.time()-start
        plt.show()
        print('It takes ',s,'sec')
        
    elif len(args)==2:
        t0=time.time()
        X=args[0]
        k=args[1]
        #X=(np.matrix.round(200*np.random.randn(k,l)))/100
        X_reduced = PCA(n_components=3).fit_transform(X)
        t1=time.time()-t0
        return X_reduced
    else:
        print('Zadali jste nespravne argumenty!')
   
    
#def main():
#    X=(np.matrix.round(200*np.random.randn(100,5)))/100
#    pca(X,3)
    #pca()
    
    
#if __name__ == "__main__":
#    main()