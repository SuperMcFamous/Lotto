#Lottery PowerBall number Generator
#Made by SuperMcFamous

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Prepare data
def prepare_data(data, n_features):
    X, y = [], []
    for i in range(len(data)):
        end_ix = i + n_features
        if end_ix > len(data)-1:
            break
        seq_x, seq_y = data[i:end_ix, :-1], data[end_ix, :-1]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

# Historical data
historical_data = [
    (8, 38, 52, 54, 64, 15),
    (8, 44, 45, 51, 69, 12),
    (19, 29, 35, 36, 45, 16),
    (28, 38, 52, 54, 68, 8),
    (17, 34, 56, 60, 61, 9),
    (9, 30, 39, 49, 59, 21),
    (6, 33, 35, 36, 64, 24),
    (5, 16, 18, 26, 67, 4),
    (1, 7, 48, 64, 68, 5),
    (19, 36, 37, 42, 59, 19),
    (19, 42, 45, 55, 69, 6),
    (5, 14, 29, 38, 66, 1),
    (3, 6, 39, 49, 67, 21),
    (7, 41, 43, 44, 51, 5),
    (14, 20, 23, 53, 69, 4),
    (1, 11, 19, 21, 68, 15),
    (11, 38, 47, 67, 69, 14),
    (9, 30, 53, 55, 62, 23),
    (2, 20, 22, 26, 47, 21),
    (12, 16, 33, 39, 52, 1),
    (4, 35, 41, 44, 58, 25),
    (24, 29, 44, 47, 54, 2),
    (7, 16, 41, 56, 61, 23),
    (7, 33, 40, 43, 69, 10),
    (6, 7, 12, 24, 36, 15),
    (6, 21, 23, 39, 54, 23),
    (22, 27, 44, 52, 69, 9),
    (11, 38, 41, 62, 65, 15),
    (19, 24, 40, 42, 56, 23),
    (12, 13, 33, 50, 52, 23),
    (37, 46, 57, 60, 66, 8),
    (7, 11, 19, 53, 68, 23),
    (6, 23, 25, 34, 51, 3),
    (13, 22, 27, 54, 66, 9),
    (10, 17, 20, 39, 44, 16),
    (12, 23, 44, 57, 61, 5),
    (21, 29, 54, 59, 62, 4),
    (1, 3, 7, 16, 66, 5),
    (30, 36, 49, 52, 63, 16),
    (6, 19, 28, 44, 60, 10),
    (36, 42, 50, 52, 67, 26),
    (3, 18, 27, 36, 53, 12),
    (16, 26, 29, 38, 50, 6),
    (24, 29, 42, 51, 54, 16),
    (3, 8, 40, 53, 58, 3),
    (4, 27, 33, 41, 42, 14),
    (4, 23, 45, 50, 53, 17),
    (6, 28, 59, 62, 69, 21),
    (1, 4, 45, 47, 67, 18),
    (17, 36, 43, 53, 67, 14),
    (27, 28, 34, 37, 44, 8),
    (12, 21, 62, 67, 69, 17),
]

# Convert to numpy array
historical_data = np.array(historical_data)

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(historical_data)

# Prepare the data
n_features = 3
X, y = prepare_data(scaled_data, n_features)

# Reshape from [samples, timesteps, features] to [samples, timesteps, features]
n_input = X.shape[1] * X.shape[2]
X = X.reshape((X.shape[0], X.shape[1], X.shape[2]))

# Define model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_features, X.shape[2])))
model.add(Dense(y.shape[1]))
model.compile(optimizer='adam', loss='mse')

# Fit model
model.fit(X, y, epochs=300, verbose=0)

# Make prediction
x_input = scaled_data[-n_features:, :-1].reshape((1, n_features, scaled_data.shape[1] - 1))
yhat = model.predict(x_input, verbose=0)

# Inverse scale the prediction
yhat = scaler.inverse_transform(np.hstack((yhat, np.zeros((yhat.shape[0], 1)))))[:, :-1]

predicted_numbers = np.round(yhat).astype(int).flatten()

# Print predicted numbers
print(f"Predicted next numbers: {predicted_numbers}")

# Predict Powerball
# For simplicity, we use the mean of historical Powerball numbers as a naive prediction
predicted_powerball = int(np.mean(historical_data[:, -1]))
print(f"Predicted next Powerball: {predicted_powerball}")
