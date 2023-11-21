import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("co2.csv")
df["co2"] = df["co2"].interpolate()


def recursive_method(df, window_size):
    i = 1
    while i < window_size:
        df[f"co2_{i}"] = df["co2"].shift(-i, axis=0)
        i += 1
    df["target"] = df["co2"].shift(-i, axis=0)
    df.dropna(axis=0, inplace=True)
    return df

window_size = 5
recursive_method(df, window_size)
target = "target"
df["time"] = pd.to_datetime(df["time"])
x = df.drop([target, "time"], axis=1)
y = df[target]

fig, ax = plt.subplots()
ax.plot(df["time"], df["co2"])
plt.show()

x_train = x[:int(len(x)*0.8)]
y_train = y[:int(len(y)*0.8)]
x_test = x[int(len(x)*0.8):]
y_test = y[int(len(y)*0.8):]

reg = LinearRegression()
reg.fit(x_train, y_train)
prediction = reg.predict(x_test)
print(mean_absolute_error(y_test, prediction))
print(mean_squared_error(y_test, prediction))
print(r2_score(y_test, prediction))