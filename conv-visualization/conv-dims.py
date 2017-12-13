from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=4, strides=4, padding='valid', 
    activation='relu', input_shape=(200, 200, 1)))
model.summary()
