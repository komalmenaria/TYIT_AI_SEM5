import numpy as np
import pandas as pd 
import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Dense,Flatten,Dropout
import matplotlib.pyplot as mp
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape, train_labels.shape)
print(test_images.shape , test_labels.shape)
class_names = ["zero","one","two","three","four","five","six","seven","eight","nine"]
print(train_images[0,5:22,5:22])
mp.figure()
mp.imshow(train_images[0])
mp.colorbar()
train_images = train_images/255.0
test_images = test_images/255.0
mp.figure(figsize=(10,10))
for i in range(20):
    mp.subplot(4,5, i+1)
    mp.xticks([])
    mp.yticks([])
    mp.grid(False)
    mp.imshow(train_images[i])
    mp.xlabel(class_names[train_labels[i]])
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape= (28,28,1)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(48, (3,3), activation='relu'))
model.add(MaxPool2D((2,2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(500, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy',metrics= ['accuracy'] )
model.fit(train_images, train_labels, epochs=10, batch_size = 128, verbose= 2, validation_data= (train_images, train_labels) )
loss, accuracy= model.evaluate(test_images, test_labels, verbose = 1)
loss * 100
print(f'Accuracy: {accuracy*100}')
mp.imshow(train_images[2])
prediction = model.predict(train_images)
print(np.argmax(prediction[2]))
