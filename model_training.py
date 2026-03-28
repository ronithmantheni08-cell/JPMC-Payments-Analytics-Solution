import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

# 1. Load Data
file_path = '/Users/ronithmantheni/Documents/data/jpmc_payments_data.csv'
df = pd.read_csv(file_path)

# 2. Prepare the Data (Feature Engineering)
# We choose our "Inputs" (X) and our "Target" (y)
# We turn 'Success' into 1 and 'Failure' into 0
df['Target'] = (df['Last_Step_Reached'] == 4).astype(int)

# Convert text (Device/Method) into numbers so the model can read them
X = pd.get_dummies(df[['Device_OS', 'Payment_Method', 'Transaction_Amount']])
y = df['Target']

# 3. Split the data
# We use 80% to train the model and 20% to test if it's smart
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Model (The 'Brain')
model = RandomForestClassifier()
print("Training the model... please wait...")
model.fit(X_train, y_train)

# 5. Check Accuracy
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

print(f"Model Training Complete!")
print(f"Accuracy Score: {score * 100:.2f}%")