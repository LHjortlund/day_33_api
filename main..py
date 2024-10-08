import requests
from datetime import datetime


#________________ CONSTANTS ------------#

MY_LAT = 56.162937
MY_LONG = 10.203921



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Copenhagen"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(response.text)


sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

print(sunset)

time_now = datetime.now()
print(time_now.hour)
