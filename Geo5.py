
# coding: utf-8

# In[13]:

# define a vectorel function and
# define its derivative
# comment them
# draw the derivative dor a point in the curve
# https://calculus-notes.readthedocs.io/en/latest/1.2_calc_derivatives.html

# sin t cos t  t  vektör değerli fonk grafiğini çiziniz
# teğet olan vektörü çiziniz

# sint,cost,t
# cost,sint,1  türevi
# t=10

#b şıkkı
#x=a cos t
#y=b sin t  olarak tanımlanmış eğrinin t = 3*pi/2 deki teğet doğrusunu çiziniz

#c şıkkı   x=6t  y=3t^2  z=t  olan eğrinin t=10 daki teğetini çiziniz


# In[17]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().magic('matplotlib notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)  # 0 dan 8pi ye kadar n tane nokat oluştur
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)

#ax.set_axis_off()

theta_current = 3 * np.pi/2  #türevini aldık çalıştığımız nokta 3*np.pi/2 olsun dedik ordaki türev x_1,y_1,z_1 vektörü 
x_1=math.cos(theta_current)  #bunlar ordaki teğet olan vektörün büyüklüğü
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current) 
y_2=-math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s) # iki nokta var birleştiriceğiz
plt.show()


# In[19]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().magic('matplotlib notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)  # 0 dan 8pi ye kadar n tane nokat oluştur
a=5
b=7
x = a*np.sin(theta)
y = b*np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)

#ax.set_axis_off()

theta_current = 3 * np.pi/2  #türevini aldık çalıştığımız nokta 3*np.pi/2 olsun dedik ordaki türev x_1,y_1,z_1 vektörü 
x_1=math.cos(theta_current)  #bunlar ordaki teğet olan vektörün büyüklüğü
y_1=math.sin(theta_current)
z_1=1

x_2=a*math.sin(theta_current) 
y_2=b*-math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s) # iki nokta var birleştiriceğiz
plt.show()


# In[ ]:



