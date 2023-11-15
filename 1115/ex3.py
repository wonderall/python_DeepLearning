from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.Dense(128, activation ='relu', input_shape=(26,)))
model.add(keras.layers.Dense(256, activation ='relu'))
model.add(keras.layers.Dense(64, activation ='relu'))
model.add(keras.layers.Dense(1))
model.summary()

model.compile(loss='mse', optimizer ='adam', metrics=['mae'])