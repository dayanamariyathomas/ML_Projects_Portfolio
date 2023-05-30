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
column_selected = ['CRIM', 'INDUS', 'RAD', 'NOX', 'PTRATIO', 'RM', 'TAX', 'B', 'AGE', 'LSTAT', 'DIS']
x = df.loc[:, column_selected]
y = df['MEDV']
x_scaled = min_max_scaler.fit_transform(x)
x = pd.DataFrame(x_scaled, columns=column_selected)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Training the Random Forest model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Pickling the MinMaxScaler and Random Forest model
with open('minmax_scaler.pkl', 'wb') as f:
    pickle.dump(min_max_scaler, f)

with open('model.pkl', 'wb') as f:
    pickle.dump(rf_regressor, f)

# Loading the scaler and model for prediction
with open('minmax_scaler.pkl', 'rb') as f:
    min_max_scaler = pickle.load(f)

with open('model.pkl', 'rb') as f:
    rf_regressor = pickle.load(f)

# Example prediction
example_data = [[0.1, 8.0, 3.0, 0.5, 18.0, 6.0, 400.0, 390.0, 50.0, 10.0, 4.0]]
scaled_data = min_max_scaler.transform(example_data)
predicted_price = rf_regressor.predict(scaled_data)
print("Predicted price:", predicted_price)
