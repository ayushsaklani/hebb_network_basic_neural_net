import numpy as np 
from random import randint
X=np.array([[1,1,1,-1,1,-1,1,1,1],[1,1,1,1,-1,1,1,1,1]])
Y=np.array([[1],[-1]])

#print X[0],X[1],Y[0],Y[1]
# setting up random weights
weights=np.zeros((9))
#print weights

def update_weight(X,Y,weights):
    for i in range(2):
         
        weights=weights+X[i]*Y[i]
        #print weights
        
    return weights
        
weights=update_weight(X,Y,weights)
print weights

print('Checking after learning selecting a input at ranodom')
rand_int=randint(0,1)

print('selected unput is %d'%rand_int)
print X[rand_int]
def check_learning(X,weights,rand_int):
    Yin=0
    for i in range(9):
        Yin+=X[rand_int,i]*weights[i]
    if Yin<0:
        Yin=-1
    else:
        Yin=1
    return Yin

Yin=check_learning(X,weights,rand_int)
print Yin
        
