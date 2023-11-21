# [PYTHON] TIME SERIES FORECASTING
# Introduction
- This project was created to forecast the amount of CO2.
- This data was measured from 1958 to 2001.
- Data here: https://github.com/TranThanhTuan2509/Time-Series-Forecasting/blob/main/co2.csv
- Time series forecasting could be used for Stock Forecasting, Financial Forecasting, Energy Consumption Forecasting, Weather Forecasting, etc..

# The strategy to predict
- Recursive method
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/6d0bfb67-a18b-4665-a7aa-d8fd5ea8cdcb)
- Direct method
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/b408f5cb-f022-429b-a731-a23361c0aa7f)

# Preprocessing
- This dataset currently comprises only 2 columns, so you need to add more columns behind CO2 columns to be suitable with the 2 methods above. The number of columns to be added depends on your specific requirements.
- All Time-information columns have to change the datatype to "Datetime".
- Here is the data virtualization before handling missing data:
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/49c2e2c7-bdda-4142-9ec0-17b22068e41a)
- As you can see, the data follows a pattern, so you do not have to handle the missing data by using simple imputation or filling it with a specific value. The only way to handle this is by using the interpolation method
- Here is the data virtualization after using the interpolation method:
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/fc76d7b4-1b93-4352-b88a-d25b594cebec)
- In time series forecasting, the train-test-split method should not be used during training because time series data has continuous properties, whereas train-test-split randomizes the data

# Requirement
- Pandas
- sk-learn


