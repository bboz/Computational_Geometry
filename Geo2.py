
# coding: utf-8

# In[44]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1=np.array([0,0,0]) #orjinden geçen x=1 y=-2 z=1 olan bir normal var meshgrid yapısı ile oluşturucaz  point - nokta , normal-doğru
normal1=np.array([1,-2,1])

point2=np.array([0,-4,0])
normal2=np.array([0,2,-8])

point3=np.array([0,0,1])
normal3=np.array([-4,5,9])

point_test = np.array([1,-1,1])   #np bu listeleri çarpabiliyor , kullanmadan yaparsak hata alırız
normal_test = np.array([1,-2,1])
np.sum(point_test*normal_test)

d1 = -np.sum(point1*normal1) # dot product -- distance
d2 = -np.sum(point2*normal2) # dot product -- distance
d3 = -np.sum(point3*normal3) # dot product -- distance
d1,d2,d3

# 4x+5y+6z+7   -<4,5,6>.<x,y,z> = d    skaler çarpma aradaki işlem
xx,yy=np.meshgrid(range(5),range(5))

xx  # 5^3 değeri 125 tane değer geliyor 3 boyutlu
yy

z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')  #  ax+by+cz+d=0 bir doğruysa şu şekilde çevirebiliyoruz z=(-d-ax-by)/c


# In[43]:

point_test = np.array([1,-1,1])   #np bu listeleri çarpabiliyor , kullanmadan yaparsak hata alırız
normal_test = np.array([1,-2,1])
np.sum(point_test*normal_test)


# In[19]:

d1 = -np.sum(point1*normal1) # dot product -- distance
d2 = -np.sum(point2*normal2) # dot product -- distance
d3 = -np.sum(point3*normal3) # dot product -- distance
d1,d2,d3


# In[28]:

# 4x+5y+6z+7   -<4,5,6>.<x,y,z> = d    skaler çarpma aradaki işlem
xx,yy=np.meshgrid(range(5),range(5))


# In[29]:

xx  # 5^3 değeri 125 tane değer geliyor 3 boyutlu


# In[30]:

yy


# In[41]:

z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')  #  ax+by+cz+d=0 bir doğruysa şu şekilde çevirebiliyoruz z=(-d-ax-by)/c


# 

# In[45]:

#<sint,cost,t> deniyelim çizdirelim
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = theta
z =  np.sin(theta)
y =  np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)

# An line through the centre of the helix
ax.plot((-theta_max*0.2, theta_max * 1.2), (0,0), (0,0), color='k', lw=2)
# sin/cos components of the helix (e.g. electric and magnetic field
# components of a circularly-polarized electromagnetic wave
ax.plot(x, y, 0, color='r', lw=1, alpha=0.5)
ax.plot(x, [0]*n, z, color='m', lw=1, alpha=0.5)

# Remove axis planes, ticks and labels
ax.set_axis_off()
plt.show()


# In[47]:

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

n=1000
thete_max=0*np.pi
theta=np.linspace(0,theta_max,n)
x=np.sin(theta) #theta
y=np.cos(theta)
z=theta
ax.plot(x,y,z,'b',lw=2)


# In[ ]:



