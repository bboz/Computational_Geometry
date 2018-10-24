#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def my_product(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def my_length_function(a):   #gelen vektörün uzunluğunu vericek
    return my_product(a,a)**0.5


#düzlemin denklemi ve düzlem üzerindeki noktayı gondericez fonksiyona
def plane_point(plane,point):
    #draw plane
    #draw two point
    #print distance
    plane_normal=[plane[0],plane[1],plane[2]]
    d=my_product(plane,point)/my_length_function(plane_normal)
    
    t=-plane[3]-(my_product(plane_normal,point))
    t=t/my_product(plane_normal,plane_normal)
    
    p_0=[0,0,0]
    p_0[0]=point[0]+t*plane[0]
    p_0[1]=point[1]+t*plane[1]
    p_0[2]=point[2]+t*plane[2]
    return d,t,p_0


# In[51]:


plane_1=[1,2,3,-6]
point_1=[4,2,10]
results = plane_point(plane_1,point_1)[2]  # 38/kok14 verdi bu bize defterde var


# In[52]:


get_ipython().run_line_magic('matplotlib', 'notebook')
a=[1,2,3]
b=[4,5,6]
xx, yy= np.meshgrid(range(10),range(10))
z1 = (-a[0]*xx - a[1]*yy - results[0])*1./a[2]
plt3d=plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z1, color="blue")
plt3d.scatter(point_1[0],point_1[1],point_1[2])
plt.show()


# In[ ]:


#simdi t yi bulucaz t kadar ilerleyerek noktaya ulasıcaz      x+at  ,  y+bt  ,  z+cz  ,  d    ==  ax+by+cz+d
# a(x+at) + b(y+bt) + c(z+ct) + d = 0 
# ax+a^2t+by+b^2t+cz+c^2t+d=0
# t = (-d -ax -by -cz) / (a^2+b^2+c^2)   ==>  burdan -ax -by -cz  yerine P.n (p.n skaler çarpımı üzerlerinde vektör işareti var)
# t= -d -P.n / n.n

