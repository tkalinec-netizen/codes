# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:43:14 2015

@author: Kalinec T
"""
def clustering(num,n, cl):
    
    import numpy as np
    import time
    import math
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    
    from sklearn.cluster import KMeans
    from sklearn import datasets
    
    np.random.seed(5)
    X=(np.matrix.round(2000*np.random.randn(num,n)))/100
    centers = [[1, 1], [-1, -1], [1, -1]]
    n_clusters = len(centers)
    #print(n_clusters)
    t0 = time.time()
    k_means = KMeans(init='k-means++', n_clusters=cl, n_init=10)
    k_means.fit(X)
    t_batch = time.time() - t0
    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels_unique = np.unique(k_means_labels)
    #print(k_means_labels_unique,k_means_labels)
    #plot
   
    colors = ['#4EACC5', '#FF9C34', '#4E9A06']
    
    #ax = fig.add_subplot(1, 3, 1)
    #for k, col in zip(range(n_clusters), colors):
    #    my_members = k_means_labels == k
    #    cluster_center = k_means_cluster_centers[k]
    #    plt.plot(X[my_members, 0], X[my_members, 1], 'w',
    #            markerfacecolor=col, marker='.')
    #    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
    #            markeredgecolor='k', markersize=6)
   # plt.title('KMeans')
    
    #plt.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (
   #    t_batch, k_means.inertia_))
   # plt.show()
    target=k_means_labels
    
    return [X[:, [1,2,3]],target]

#def main():
    #X=(np.matrix.round(200*np.random.randn(100,5)))/100
#    x=clustering(10,5,3)
#    print(x[0])
    
    
#if __name__ == "__main__":
 #   main()   