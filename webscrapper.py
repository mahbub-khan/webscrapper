import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8346&lon=-87.6289')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
current_location = soup.find(id='current-conditions')

# print(week)
items = week.find_all(class_='tombstone-container')

location_title = current_location.find(class_='panel-title').get_text()

print()
print(location_title)
print()

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_descriptions)
# print(temperatures)

weather_stuff = pd.DataFrame({
    'Period': period_names,
    'Description': short_descriptions,
    'Temperatures': temperatures,
    })

print(weather_stuff)
#weather_stuff.to_csv('weather.csv')