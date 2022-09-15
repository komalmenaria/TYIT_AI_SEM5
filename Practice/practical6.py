# Step 1 import packages 
import numpy as np
# Step 2 define function unitStep , preceptionalmodel , OR_Logicfunctio , AND_Logicfunction

def unitStep(v):
    if v >= 0:
      return 1
    else :
      return 0

    
def preceptronmodel(x , w , b):
    v = np.dot(w,x)+b
    y = unitStep(v)
    return y

def OR_Logicfunction(x):
    w = np.array([1,1])
    bOR = -0.5
    return preceptronmodel(x,w,bOR)  

def AND_Logicfunction(x):
    w = np.array([1,1])
    bAND = -1.5
    return preceptronmodel(x,w,bAND)



# Step 3 creating test sets 
test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])

# Step 4 call OR  AND output 

print("OR({},{})={}".format(0,0,OR_Logicfunction(test1)))
print("OR({},{})={}".format(0,1,OR_Logicfunction(test2)))
print("OR({},{})={}".format(1,0,OR_Logicfunction(test3)))
print("OR({},{})={}".format(1,1,OR_Logicfunction(test4)))

print("\n")
print("AND({},{})={}".format(0,0,AND_Logicfunction(test1)))
print("AND({},{})={}".format(0,1,AND_Logicfunction(test2)))
print("AND({},{})={}".format(1,0,AND_Logicfunction(test3)))
print("AND({},{})={}".format(1,1,AND_Logicfunction(test4)))

