import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("co2.csv")
df["co2"] = df["co2"].interpolate()


def direct_method(df, window_size, target_size):
    i = 1
    while i < window_size:
        df[f"co2_{i}"] = df["co2"].shift(-i, axis=0)
        i += 1
    i = 0
    while i < target_size:
        df[f"target_{i+1}"] = df["co2"].shift(-i - window_size, axis=0)
        i += 1

    df.dropna(axis=0, inplace=True)
    return df

window_size = 5
target_size = 3
direct_method(df, window_size, target_size)
df["time"] = pd.to_datetime(df["time"])
target = [f"target_{i+1}" for i in range(target_size)]

x = df.drop(["time"] + target, axis=1)
y = df[target]

x_train = x[:int(len(x)*0.8)]
y_train = y[:int(len(y)*0.8)]
x_test = x[int(len(x)*0.8):]
y_test = y[int(len(y)*0.8):]

regs = [LinearRegression() for _ in range(target_size)]

for i, reg in enumerate(regs):
    reg.fit(x_train, y_train[f"target_{i+1}"])
    prediction = reg.predict(x_test)
    print(r2_score(y_test[f"target_{i+1}"], prediction))