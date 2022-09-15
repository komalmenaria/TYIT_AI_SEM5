# Step 1 import packages 
import numpy as np
import h5py
import matplotlib.pyplot as plt
# Step 2 define function 
def load_data():
# Step 3 get test , train and classes 
    
    test_data = h5py.File('test_catvnoncat.h5','r')
    test_set_y_origin = np.array(test_data['test_set_y'][:])
    test_set_x_origin = np.array(test_data['test_set_x'][:])
    
    train_data = h5py.File('train_catvnoncat.h5','r')
    train_set_y_origin = np.array(train_data['train_set_y'][:])
    train_set_x_origin = np.array(train_data['train_set_x'][:])
    
    classes = np.array(test_data['list_classes'][:])
# Step 4 reshape and shape train and test data 
    
    train_set_y_origin = train_set_y_origin.reshape(1,train_set_y_origin.shape[0])
    test_set_y_origin = test_set_y_origin.reshape(1,test_set_y_origin.shape[0])
    
# Step 5 return all elements 
    
    return test_set_y_origin, test_set_x_origin ,train_set_y_origin , train_set_x_origin, classes
    
# Step 6 load all elements 
test_set_y_origin, test_set_x_origin ,train_set_y_origin , train_set_x_origin, classes = load_data()
# Step 7 train output 

index = int(input("Enter value:"))
plt.imshow( train_set_x_origin[index])
plt.show()

print("y =" + str(train_set_y_origin[:,index]) + ", it's " + classes[np.squeeze(train_set_y_origin[:,index])].decode("utf-8") +   "' picture.")

