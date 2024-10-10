
# Project two: Weather Data Collection and Analysis using Python

## Project Goal
The goal of this project is to collect and analyze weather data from the weather.com website, save the data into a CSV file, and visualize it using graphs.

---

## Tools Used
- **Python**: The primary programming language used for the project.
- **Requests**: A library for sending HTTP requests to retrieve webpage content.
- **BeautifulSoup**: A library for parsing and extracting data from HTML content.
- **Pandas**: A library for data manipulation and analysis, including reading and writing CSV files.
- **Matplotlib**: A library for creating visualizations to represent the data.

---

## Workflow
1. **Fetching Weather Data**  
   Used the `requests` library to send an HTTP request to the weather website (weather.com) and retrieve the webpage content.

2. **Data Extraction**  
   After receiving the webpage content, the `BeautifulSoup` library was used to parse the HTML and extract required information, such as temperature, humidity, and weather conditions.

3. **Storing Data**  
   The extracted data was stored in a CSV file using the `pandas` library, allowing for easy access and analysis of the data later on.

4. **Visualizing the Data**  
   The `Matplotlib` library was used to create graphs that visually represent the changes in temperature over time.

---

## Project Outputs
- **CSV File** containing the collected data, including temperature, humidity, and weather conditions at different timestamps.
- **Graph** showing the trend of temperature changes over time.

---

## Notes
- The data is updated each time the program is run, providing a series of readings over time.
- The project can be modified to include additional data sources or analyze other aspects of weather data.


You can copy this formatted README for your GitHub repository!

