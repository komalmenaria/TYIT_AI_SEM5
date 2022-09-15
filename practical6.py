# import necessary packages
from tkinter import Y
import numpy as np

#define 4 function unitStep , perceptronModel , OR_Logicfunction , AND_Logicfunction

def unitStep(v):
    if v >= 0:
     return 1
    else :
     return 0


def perceptronModel(x , w , b):
    v = np.dot(w,x)+b
    y=unitStep(v)
    return y 

def OR_Logicfunction(x):
    w = np.array([1,1])
    bOR = -0.5
    return perceptronModel(x,w,bOR)

def AND_Logicfunction(x):
    w = np.array([1,1])
    bAND = -1.5
    return perceptronModel(x,w,bAND)

test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])


print("OR({},{})={}".format(0,0,OR_Logicfunction(test1)))
print("OR({},{})={}".format(0,1,OR_Logicfunction(test2)))
print("OR({},{})={}".format(1,0,OR_Logicfunction(test3)))
print("OR({},{})={}".format(1,1,OR_Logicfunction(test4)))

print("\n")
print("AND({},{})={}".format(0,0,AND_Logicfunction(test1)))
print("AND({},{})={}".format(0,1,AND_Logicfunction(test2)))
print("AND({},{})={}".format(1,0,AND_Logicfunction(test3)))
print("AND({},{})={}".format(1,1,AND_Logicfunction(test4)))

