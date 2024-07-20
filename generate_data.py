import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of transactions
num_transactions = 10000

# Generate transaction IDs
transaction_ids = [f'TX{i:05d}' for i in range(num_transactions)]

# Generate random transaction amounts
amounts = np.random.uniform(1, 5000, num_transactions).round(2)

# Generate random transaction times
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
date_range = end_date - start_date

transaction_times = [start_date + timedelta(seconds=random.randint(0, int(date_range.total_seconds())))
                     for _ in range(num_transactions)]

# Generate random user IDs
user_ids = [random.randint(1, 1000) for _ in range(num_transactions)]

# Generate random merchant IDs
merchant_ids = [random.randint(1, 1000) for _ in range(num_transactions)]

# Generate random transaction locations
locations = [f'Location_{random.randint(1, 100)}' for _ in range(num_transactions)]

# Generate fraudulent labels (imbalanced dataset)
fraud_probability = 0.05
is_fraud = np.random.choice([0, 1], size=num_transactions, p=[1-fraud_probability, fraud_probability])

# Create a DataFrame
data = {
    'transaction_id': transaction_ids,
    'amount': amounts,
    'transaction_time': transaction_times,
    'user_id': user_ids,
    'merchant_id': merchant_ids,
    'location': locations,
    'is_fraud': is_fraud
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('transactions.csv', index=False)

print("Synthetic transaction data generated and saved to 'transactions.csv'.")
