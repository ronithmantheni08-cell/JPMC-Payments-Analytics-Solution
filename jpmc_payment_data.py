import pandas as pd
import numpy as np
import os

# 1. Setup the directory path
folder_path = '/Users/ronithmantheni/Documents/data'
file_name = 'jpmc_payments_data.csv'
full_path = os.path.join(folder_path, file_name)

# Create the folder
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 2. Generate the Mock Data
np.random.seed(42)
n_rows = 50000

data = {
    'Transaction_ID': range(1001, 1001 + n_rows),
    'User_ID': np.random.randint(5000, 9000, size=n_rows),
    'Device_OS': np.random.choice(['iOS', 'Android', 'Web'], size=n_rows, p=[0.4, 0.4, 0.2]),
    'Payment_Method': np.random.choice(['Credit Card', 'Debit Card', 'ACH', 'Digital Wallet'], size=n_rows),
    'Transaction_Amount': np.round(np.random.uniform(5, 500, size=n_rows), 2),
    # Funnel Steps: 1-Start, 2-Details, 3-Security, 4-Success
    'Last_Step_Reached': np.random.choice([1, 2, 3, 4], size=n_rows, p=[0.1, 0.15, 0.2, 0.55]),
    'Error_Code': np.random.choice(['None', 'Timeout', 'Invalid_CVV', 'Insufficient_Funds', 'Biometric_Fail'], size=n_rows),
    'Processing_Time_Sec': np.random.uniform(0.5, 10.0, size=n_rows)
}

df = pd.DataFrame(data)

# 3. Injecting the "Android Friction" (The bug will solve later)
# We are forcing Android users who hit the Security step (3) to fail with 'Biometric_Fail'
df.loc[(df['Device_OS'] == 'Android') & (df['Last_Step_Reached'] == 3), 'Error_Code'] = 'Biometric_Fail'

# 4. Save the file
df.to_csv(full_path, index=False)

print(f"Success! Your file is saved at: {full_path}")
print(df.head()) # Shows the first 5 rows to verify