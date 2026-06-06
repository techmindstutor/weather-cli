from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()
apikey=os.getenv("OPENWEATHER_API_KEY")
city=input("Enter a city to check its weather: ")
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,            # the city name from input()
    "appid": apikey,     # your key, loaded from .env
    "units": "metric"     # so temperature comes back in Celsius
}
try:
    response=requests.get(url,params=params,timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Couldn't reach the weather service {e}")
    exit()
if response.status_code==200:
    data=response.json()
#   print(json.dumps(data, indent=2))
    print(f"---weather condition of {city}----")
    print(f"Temperature : {data["main"]["temp"]}°C")
    print(f"Condition : {data["weather"][0]["description"]}")
    print(f"Wind Speed : {data["wind"]["speed"]}m/s")
elif response.status_code == 404:
    print(f"City '{city}' not found. Check the spelling.")
elif response.status_code == 401:
    print("API key invalid or not yet activated. New keys take ~2 hours.")
else:
    print(f"Something went wrong. Status code: {response.status_code}")


