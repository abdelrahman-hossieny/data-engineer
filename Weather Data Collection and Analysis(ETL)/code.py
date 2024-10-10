import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL of the weather page
url = "https://weather.com/weather/today/l/ad1f0514804c519d418eed7e5c594bf6e3b5f35a95e3a0ed5887bb67ec8a1667"  #https://weather.com/weather/today/l/LOCATION_CODE

# Sending a request to get the content of the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
# #Here the status of the request is checked using response.status_code.
#  If the value is 200, it means that the request was successful, and the server sent the page content.
# Other status codes:
# 404: Page not found 500: Internal server error 403: Access denied (you do not have permission to access).

# Parse the content using BeautifulSoup
if response.status_code == 200:    
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Webpage loaded successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
# If the request is successful, we use BeautifulSoup to parse the HTML content of the webpage (response.text).
# The html.parser argument tells BeautifulSoup to use the built-in HTML parser to interpret the content.


# Extracting temperature (class name might vary depending on the website)
temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
# condition = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text

# Printing the results
print(f"Temperature: {temperature}")
# print(f"Condition: {condition}")

import pandas as pd
from datetime import datetime

# Extract data
temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
condition = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p").text
humidity = soup.find('div', class_="WeatherDetailsListItem--wxData--kK35q").text

# Prepare data as a DataFrame
data = {
    'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    'Temperature': [temperature],
    'Condition': [condition],
    'Humidity': [humidity]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write data to a CSV file (append mode)
df.to_csv('weather_data.csv', mode='a', header=False, index=False)

print("Weather data saved successfully.")



# Read the collected weather data
df = pd.read_csv('weather_data.csv', names=['Timestamp', 'Temperature', 'Condition', 'Humidity'])

# Convert Temperature to numeric (remove non-numeric characters like '°')
df['Temperature'] = df['Temperature'].str.extract(r'(\d+)').astype(float)

# Plot temperature over time
df.plot(x='Timestamp', y='Temperature', kind='line', title='Temperature Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.show()
