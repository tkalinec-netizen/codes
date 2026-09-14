# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:10:42 2015

@author: Tomas Kalinec
"""

def main():
   from functools import wraps
   import numpy as np
   import scipy.io as io
   import time
   import math
   from sklearn import datasets
   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   from sammon import sammon

   """Test sammon.py by plotting a projection of iris flower data. 
      
   Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
   The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
   (MIT License, http://www.opensource.org/licenses/mit-license.php)
   """
   # Load the iris data
   iris = datasets.load_iris()
   X = iris.data
   target = iris.target
   names = iris.target_names
   a={}
   tmp1=[]
   tmp2=[]
   # Run the Sammon projection
   start = time.time()
   display = 1
   n = 3
   for i in range(0, 10):
       t=time.time()
       [y1,E1] = sammon(X,2,display)
       tmp1.append(time.time()-t)
   elapsed = (time.time() - start)
   if (elapsed)>1:
       sec=math.floor(elapsed)
       ms=elapsed-sec
       print('Elapsed time is ',elapsed, 'sec.')
   else:
       ms=elapsed
       print('Elapsed time in 2-d is ', ms, 'ms.')
   print('Average time of featuring in 2-d is:', sum(tmp1)/10)
   
   start = time.time()
   display  = 1
   n = 3
   for i in range(0, 10):
       t=time.time()
       [y2,E2] = sammon(X,3,display)
       tmp2.append(time.time()-t)
   elapsed = (time.time() - start)
   if (elapsed)>1:
       sec=math.floor(elapsed)
       ms=elapsed-sec
       print('Elapsed time in 3-d is ',elapsed, 'sec.')
   else:
       ms=elapsed
       print('Elapsed time is ', ms, 'ms.')
   print('Average time of featuring in 3-d is:', sum(tmp2)/10)   
   
   a['E1']=E1
   a['y1']=y1
   a['t1']=tmp1
   a['E2']=E2
   a['y2']=y2
   a['t2']=tmp2
   io.savemat('data_1',a)
   # Plot 
   plt.figure(1)
   plt.scatter(y1[target ==0, 0], y1[target ==0, 1], s=20, c='r', marker='o',label=names[0])
   plt.scatter(y1[target ==1, 0], y1[target ==1, 1], s=20, c='b', marker='D',label=names[1])
   plt.scatter(y1[target ==2, 0], y1[target ==2, 1], s=20, c='y', marker='v',label=names[2])
   plt.title('Sammon projection of iris flower data, stress is '+str(E1))
   plt.legend(loc=3)
   plt.show()
   
   fig = plt.figure(2)
   ax = fig.add_subplot(111, projection='3d')        
   ax.scatter(y2[target ==0, 0], y2[target ==0, 1], y2[target ==0, 2], c='r', marker='o',label=names[0])
   ax.scatter(y2[target ==1, 0], y2[target ==1, 1], y2[target ==1, 2], c='b', marker='D',label=names[1])
   ax.scatter(y2[target ==2, 0], y2[target ==2, 1], y2[target ==2, 2], c='y', marker='v',label=names[2])
   plt.title('Sammon projection of iris flower data, stress is '+str(E2))
   ax.legend(loc=3)
   plt.show()
   

if __name__ == "__main__":
    main()