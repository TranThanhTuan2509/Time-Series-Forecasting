# [PYTHON] TIME SERIES FORECASTING
# Introduction
- This project was created to forecast CO2 density.
- This data was measured from 1958 to 2001.
- Data here: https://github.com/TranThanhTuan2509/Time-Series-Forecasting/blob/main/co2.csv
- Time series forecasting could be used for stock problems. etc...

# The strategy to predict
- Recursive method
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/6d0bfb67-a18b-4665-a7aa-d8fd5ea8cdcb)
- Direct method
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/b408f5cb-f022-429b-a731-a23361c0aa7f)

# Preprocessing
- This data set only has 2 columns, so you have to add more columns. The number of columns you add depends on your requirements.
- All Time-information columns have to change the datatype to "Datetime" datatype.
- Here is the data virtualization before handling missing data:
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/49c2e2c7-bdda-4142-9ec0-17b22068e41a)
- As you can see, the data following to a period so you have not to handle the missing data by using simple impute or filling missing data with a specific value. The only way to handle this is using interpolation method.
- Here is the data virtualization after using interpolation method:
![image](https://github.com/TranThanhTuan2509/Time-Series-Forecasting/assets/119112296/fc76d7b4-1b93-4352-b88a-d25b594cebec)
- Time series forecasting has not to use the train-test-split method when you train because the time series forecasting properties ( continuous ) while train-test-split random the data.

# Requirement
- Pandas
- Sk-learn


