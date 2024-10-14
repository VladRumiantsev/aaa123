import numpy as np
import pandas as pd
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
income = np.array([15000, 17500, 20000, 23000, 28800, 32400, 35000, 38650, 41000, 43500])
income_without_tax = income * 0.7
expenses = np.array([10000, 12000, 13500, 16600, 19500, 28000, 30000, 32600, 33800, 35000])
data = {
    'Month': months,
    'Income_without_tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)
print("Complete DataFrame:")
print(df)
first_quarter_data = df.iloc[0:3]
print("\nFirst Quarter Data:")
print(first_quarter_data)