import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for the Nike By You business with binary sales, decreased purchases, click count, and wait time
start_date = datetime(2023, 2, 13)
end_date = datetime(2024, 2, 13)
num_days = (end_date - start_date).days

data = {
    'Date': [start_date + timedelta(days=np.random.randint(num_days)) for _ in range(10000)],
    'Product_ID': np.random.randint(1, 100, size=10000),
    'Product_Category': np.random.choice(['Running', 'Basketball', 'Training'], size=10000),
    'Clicks': np.random.randint(5, 51, size=10000),  # Vary clicks between 5 and 50
    'Sales': 0,  # Initialize Sales column to 0
    
    'Price': np.random.uniform(50, 200, size=10000),
    'Customer_Age': np.random.randint(18, 60, size=10000),
    'Customer_Gender': np.random.choice(['Male', 'Female'], size=10000),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=10000),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define a function to set random Sales values based on the year being 2024
def set_random_sales(row):
    if row['Date'].year == 2024:
        return np.random.choice([0, 1], p=[0.9, 0.1])
    else:
        return np.random.choice([0, 1], p=[0.7, 0.3])
    
def set_marketing(row):
    if row['Sales'] == 1:
        return np.random.choice([0, 1], p=[0.3, 0.7])
    else:
        return np.random.choice([0, 1], p=[0.6, 0.4])
    
    
def set_browser(row):    
    browsers = ['Chrome', 'Edge', 'Firefox', 'Safari']
    if row['Wait_Time'] >= 80:
        browser = browsers[np.random.choice([0, 1, 2, 3], p=[0.7, 0.1, 0.1, 0.1])]
        return browser
    else:
        browser = browsers[np.random.choice([0, 1, 2, 3], p=[0.1, 0.3, 0.3, 0.3])]
        return browser
    

# Apply the function to each row
df['Sales'] = df.apply(set_random_sales, axis=1)

# Add Click_Count column with higher average for clients who made a purchase
df['Click_Count'] = np.where(df['Sales'] == 1, np.random.randint(15, 51, size=len(df)), np.random.randint(5, 15, size=len(df)))

# Add Wait_Time column with lower average for clients who made a purchase
df['Wait_Time'] = np.where(df['Sales'] == 1, np.random.randint(5, 31, size=len(df)), np.random.randint(30, 131, size=len(df)))

#Apply browsers function
df['Browser'] = df.apply(set_browser, axis=1)

df['Marketing'] = df.apply(set_marketing, axis=1)


# Count sales for each month
monthly_sales = df[df['Sales'] == 1].set_index('Date').resample('M').size()

# Display the count of sales for each month
monthly_sales = df[df['Sales'] == 0].set_index('Date').resample('M').size()
print(len(df['Sales'][df['Date'].dt.year >= 2024]))
print(monthly_sales)


df.to_csv('Nike_data.csv')
