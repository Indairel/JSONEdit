import json
from urllib.request import urlopen

with open('weather.json') as f:
    data = json.load(f)

# for forecast in data['forecasts']:
#     print(forecast['Date'], forecast['Current forecast is '])
#
# for forecast in data['forecasts']:
#     del forecast['The minimum temperature is ']

for forecast in data['forecasts']:
    pressure = [(json.dumps(forecast['The pressure is '], sort_keys=False))]
    pressure.sort()
    print(pressure)

with open('new_weather.json', 'w') as f:
    json.dump(data, f, indent=2)

api_key = "d6ab15dedfb4aacb18e54fa7c6923195"
city = "Warszawa"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

with urlopen(url) as response:
    source = response.read()

# print(source)

data = json.loads(source)

# print(json.dumps(data, indent=2))
# print(len(data['weather']))

for item in data['weather']:
    # print(item)
    description = item['description']
    print(description)


# with open('weather.json') as g:
#
#     size_to_read = 10
#
#     g_contents = g.read(size_to_read)
#     print(g_contents, end='*')

    # f.seek(0)

    # g_contents = g.read(size_to_read)
    # print(g_contents, end='')

    # print(g.tell())

    # while len(g_contents) > 0:
    #     print(g_contents, end='*')
    #     g_contents = g.read(size_to_read)

    


