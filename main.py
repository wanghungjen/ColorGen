from tensorflow.keras import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, Reshape
from tensorflow.keras.utils import to_categorical

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def norm(value):
    return value / 255.0

def plot_rgb(rgb):
    data = [[rgb]]
    plt.figure(figsize=(2,2))
    plt.imshow(data, interpolation='nearest')
    plt.show()

def scale(n):
    return int(n * 255) 

def predict(name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)
    one_hot = to_categorical(padded, num_classes=28)
    pred = model.predict(np.array(one_hot))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    print(name + ',', 'R,G,B:', r,g,b)
    plot_rgb(pred)

data = pd.read_csv('colors.csv')
names = data["name"]

# Character-Level Tokenizing
maxlen = 30
t = Tokenizer(char_level=True)
t.fit_on_texts(names)
tokenized = t.texts_to_sequences(names)
padded_names = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)

# One-hot Encoding
one_hot_names = to_categorical(padded_names) # (number of training samples, max sequence length, number of unique tokens)

# Normalizing
normalized_values = np.column_stack([norm(data["red"]), norm(data["green"]), norm(data["blue"])])

# Model Architecture
model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=(maxlen, 28)))
model.add(LSTM(128))
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse', metrics=['acc'])

# Training
model.fit(one_hot_names, normalized_values, epochs=40, batch_size=32, validation_split=0.1)

# Predict
predict("Red")
predict("Green")
predict("Blue")
predict("Pytorch")
predict("TensorFlow")