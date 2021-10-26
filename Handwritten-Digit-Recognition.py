# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h9rUD_gntyhNhfN55Wgau8MDCx0uedkk
"""

import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

from keras.datasets import mnist
objects = mnist
(train_img,train_lab),(test_img,test_lab) = objects.load_data()

for i in range(20):
  plt.subplot(4,5,i+1)
  plt.imshow(train_img[i],cmap='gray_r')
  plt.title("Digit : {}".format(train_lab[i]))
  plt.subplots_adjust(hspace=0.5)
  plt.axis('off')

print('Training images shape:', train_img.shape)
print('Testing images shape:', test_img.shape)

plt.hist(train_img[0].reshape(784),facecolor='orange')
plt.title('Pixel vs its intensity',fontsize = 16)
plt.ylabel('PIXEL')
plt.xlabel('Intensity')

train_img=train_img/255.0
test_img=test_img/255.0

plt.hist(train_img[0].reshape(784),facecolor='orange')
plt.title('pixel vs its intensity', fontsize = 16)
plt.ylabel('PIXEL')
plt.xlabel('Intensity')

from keras.models import Sequential
from keras.layers import Flatten,Dense
model=Sequential()
input_layer = Flatten(input_shape = (28,28))
model.add(input_layer)
hidden_layer1 = Dense(512, activation = 'relu')
model.add(hidden_layer1)
hidden_layer2 = Dense(512, activation='relu')
model.add(hidden_layer2)
output_layer = Dense(10,activation='softmax')
model.add(output_layer)

model.compile(optimizer='adam', 
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_img, train_lab, epochs=100)

model.save('handwritten digit recognition')

loss_and_acc = model.evaluate(test_img,test_lab,verbose=2)

plt.imshow(test_img[10],cmap='gray_r')
plt.title('actual value:{}'.format(test_lab[10]))
predicition=model.predict(test_img)
plt.axis('off')
print('predicted Value:',np.argmax(predicition[10]))
if(test_lab[10]==(np.argmax(predicition[10]))):
  print('Successful predicition')
else:
  print('Unsuccessful prediction')

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import  load_model

def load_image(filename):
  img = load_img(filename, grayscale=True, target_size=(28,28))
  img=img_to_array(img)
  img = img.reshape(1,28,28)
  img= img.astype('float32')
  img =img / 255.0
  return img

from google.colab import files
uploaded = files.upload()

from IPython.display import Image
Image('number_in_green_rounded_square_clip_art.jpg',width=250,height=250)

img = load_image('istockphoto-174800594-170667a.jpg')
digit = model.predict(img)
print('Predicted value:',np.argmax(digit))
