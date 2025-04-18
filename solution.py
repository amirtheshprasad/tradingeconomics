import requests
import matplotlib.pyplot as plt

# Replace with your Trading Economics API key
API_KEY = "3801df7ab59c4ac:5400skf0cjna1st"

# Function to fetch historical data
def fetch_historical_data(country, indicator):
    url = f"https://api.tradingeconomics.com/historical/country/{country}/indicator/{indicator}?c={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

# Fetch data for a specific country and indicator
country = "New Zealand"
indicator = "GDP"
data = fetch_historical_data(country, indicator)
# print(data)
# Extract dates and values
dates = [item["DateTime"] for item in data]
values = [item["Value"] for item in data]

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker="o")
plt.title(f"{indicator} for {country}")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()