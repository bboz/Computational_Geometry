import matplotlib.pyplot as plt
x=[4,0]
y=[0,3]
get_ipython().magic('matplotlib inline')
plt.plot(x,y)

def my_draw_a_vector_from_origin(v):
    # from origin to v
    plt.axes().set_aspect('equal')
    x=[0,v[0]]
    y=[0,v[1]]
    plt.xlim(-10,15) #sınır değerleri ayarlıyoruz
    plt.ylim(-10,15)
    plt.plot(x,y)
my_draw_a_vector_from_origin([5,67])


def my_draw_a_vector_from_v_to_w(v,w):
    # from origin to v
    x=[v[0],w[0]]
    y=[v[1],w[1]]
    plt.xlim(-10,15) #sınır değerleri ayarlıyoruz
    plt.ylim(-10,15) #sınır değerleri ayarlıyoruz
    plt.plot(x,y)
my_draw_a_vector_from_v_to_w([5,6],[5,20])


#vektorun bir baska vektor ile skaler carpimi yapıcak
def my_scalar_product(a,b):
    return (a[0]*b[0]+a[1]*b[1])
v=[3,4]
w=[4,7]
my_scalar_product(v,w)
#dik durumda iki vektor carpinca sifir gelmeli
v=[0,4]
w=[3,0]
my_scalar_product(v,w)


my_draw_a_vector_from_origin(v)
my_draw_a_vector_from_origin(w)
my_scalar_product(v,w)


my_draw_a_vector_from_v_to_w([5,5],[10,12])
my_draw_a_vector_from_origin([-7,5])


my_draw_a_vector_from_origin([4,3])
my_draw_a_vector_from_origin([-3,4])
my_scalar_product([4,3],[-3,4])

def distance(v,w):
    return (((v[0]-w[0])**2) + ((v[1]-w[1])**2))**.5

def my_vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]

def my_vector_substract(v,w):
    return [v[0]-w[0],v[1]-w[1]]

def my_vector_multiply_with_scalar(c,v):
    return [c*v[0],c*v[1]]

a=[3,0]
b=[0,4]
print("toplam  : ",my_vector_add(a,b))
print("fark    : ",my_vector_substract(a,b))
print("5 kati  : ",my_vector_multiply_with_scalar(5,b))
print("uzunluk :",distance(a,b))