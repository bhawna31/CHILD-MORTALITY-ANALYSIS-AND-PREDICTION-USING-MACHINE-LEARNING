import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv("dataset/data.csv")
df = df[df['Country'] == 'India'].sort_values('Year')

data = df['Value'].values.reshape(-1, 1)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

X, y = [], []
for i in range(3, len(data_scaled)):
    X.append(data_scaled[i-3:i])
    y.append(data_scaled[i])

X, y = np.array(X), np.array(y)

model = Sequential([
    LSTM(50, input_shape=(X.shape[1], 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=20)

print("LSTM trained!")

# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Input

# df = pd.read_csv("dataset/data.csv")
# df = df[df['Country'] == 'India'].sort_values('Year')

# data = df['Value'].values.reshape(-1, 1)

# scaler = MinMaxScaler()
# data_scaled = scaler.fit_transform(data)

# X, y = [], []
# for i in range(3, len(data_scaled)):
#     X.append(data_scaled[i-3:i])
#     y.append(data_scaled[i])

# X, y = np.array(X), np.array(y)

# model = Sequential([
#     Input(shape=(X.shape[1], 1)),
#     LSTM(50),
#     Dense(1)
# ])

# model.compile(optimizer='adam', loss='mse')
# model.fit(X, y, epochs=20)

# print("LSTM trained successfully!")