import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.model_selection import train_test_split

# Loading the dataset
df = pd.read_csv("Housingdata.csv")

# Check for missing values
print(df.isnull().sum())
# replace null values with mean value for each column
df = df.fillna(df.mean())

# Scaling
min_max_scaler = MinMaxScaler()
column_selected = ['INDUS','NOX','PTRATIO','RM','TAX','AGE','LSTAT','DIS']
x = df.loc[:, column_selected]
y = df['MEDV']
x_scaled = min_max_scaler.fit_transform(x)
x = pd.DataFrame(x_scaled, columns=column_selected)

# Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Training the Random Forest model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(x_train, y_train)

# Pickling the MinMaxScaler
with open('minmax_scaler.pkl', 'wb') as f:
    pickle.dump(min_max_scaler, f)

# Pickling the Random Forest model
with open('model.pkl', 'wb') as f:
    pickle.dump(rf_regressor, f)
