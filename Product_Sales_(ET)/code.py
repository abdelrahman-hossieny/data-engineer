import matplotlib.pyplot as plt
import pandas as pd
#read data from csv using pandas
df = pd.read_csv(r'archive\statsfinal.csv')

# Rename the column for clarity
df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
#print(df)

# Drop rows with missing values
df = df.dropna()

# Calculate total of p3 * p4
df['Total_p3_x_p4'] = df['S-P3'] * df['S-P4']
total = df['Total_p3_x_p4'].sum()
#print(f"Total p3 * p4 =  {total}")

#**************month sales*****************
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_p3_x_p4'].sum()
print("monthly sales :")
print(monthly_sales)

#**************Best selling products:*****************
# Sum quantities for each product type
quantity_columns = ['Q-P1', 'Q-P2', 'Q-P3', 'Q-P4']
df_quantity = df[quantity_columns].sum()

# Sort and display total quantities for each product type
sorted_quantity = df_quantity.sort_values(ascending=False)
print("Total quantities for each product:")
print(sorted_quantity)
print(df)
#********************Data visualization*************

# Plot monthly sales data
plt.figure(figsize=(10, 6))
if not monthly_sales.empty:
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot for monthly sales.")

# Plot product sales data
plt.figure(figsize=(10, 6))
df_quantity.plot(kind='bar', color='salmon')
plt.title('Total Sales of Products')
plt.xlabel('Product Type')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
