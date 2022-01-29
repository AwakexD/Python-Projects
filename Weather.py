import json
import requests

API_KEY = "f02666457349dde81b5272c7a0654fbc"
city = input("Enter a city: ")

req_url = f'http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid={API_KEY}'
respons = requests.get(req_url)

if respons.status_code == 200:
    data = respons.json()

    weather = data['list'][0]['weather'][0]['description']
    temp = round(data['list'][0]['main']['temp'], 1)

    print("Weather:", weather)
    print("Temperature:", temp, "°C")
else:
    print("An error occured.")
