# Calculate Daily Wattage from Solar Power using Location retrieved from IP Address of User

from sigfig import round
from datetime import datetime
from datetime import timedelta
import json
import wbdata
import geoip2.webservice
from requests import get
import requests

apiKey = "f96b7b72baf44398bf1e36632abfff27"
ip = get('https://api.ipify.org').text

datarequest1 = "https://api.ipgeolocation.io/ipgeo?apiKey="
datarequest2 = "&ip="
dataurl = datarequest1 + apiKey + datarequest2 + ip

data = requests.get(dataurl).json()

latitude = data['latitude']
longitude = data['longitude']

sunrequest1 = "https://api.sunrise-sunset.org/json?lat="
sunrequest2 = "&lng="

sunurl = sunrequest1 + latitude + sunrequest2 + longitude

sundata = requests.get(sunurl).json()

sunrise = sundata["results"]["sunrise"]
sunset = sundata["results"]["sunset"]

FMT = "%I:%M:%S %p"

sunhours = datetime.strptime(sunset, FMT) - datetime.strptime(sunrise, FMT)

s = sunhours.total_seconds()
h = s / (60*60)

watts = float(input("What is your Solar Panel's Watts? "))
panels = float(input("How many Solar Panels are installed? "))
dailyusage = watts * panels * h * 0.75

# Average hours of sunlight × solar panel watts x 75% = daily watt-hours

dailyusage = round(dailyusage, sigfigs = 4)
dailyusage = str(dailyusage)

print("You will be generating " + dailyusage + " W  each day")

pause = input("")

# By context, the average UK household uses 8-10 kWh per day

