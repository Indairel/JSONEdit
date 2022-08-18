import json

with open('weather.json') as f:
    data = json.load(f)

for forecast in data['forecasts']:
    print(forecast['Date'], forecast['Current forecast is '])

for forecast in data['forecasts']:
    del forecast['The minimum temperature is ']

with open('new_weather.json', 'w') as f:
    json.dump(data, f, indent=2)