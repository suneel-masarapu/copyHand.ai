# i have not learned any thing yet this is me just trying to replicate stuff

from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

(train_data,train_lables) , (test_data,test_lables) = mnist.load_data()

model = keras.Sequential([
    layers.Dense(512,activation = "relu"),
    layers.Dense(10,activation = 'softmax')
])

model.compile(optimizer="rmsprop",
      loss="sparse_categorical_crossentropy",
      metrics=["accuracy"]
)

train_data = train_data.reshape((60000, 28 * 28))
train_data = train_data.astype("float32") / 255 
test_data = test_data.reshape((10000, 28 * 28))
test_data = test_data.astype("float32") / 255
model.fit(train_data,train_lables,epochs = 5,batch_size = 128)

test = test_data[:10]

predictions = model.predict(test)

print(predictions[0])

test_loss , test_acc = model.evaluate(test_data,test_lables)
print(f"test_acc: {test_acc}")
