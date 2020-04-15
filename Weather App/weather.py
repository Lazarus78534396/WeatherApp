import requests

url = 'http://api.weatherstack.com/current?access_key='
access_key = 'aaccd030b6d03fe72f96830021667240&query='
query = 'Manzini'
w=url+access_key+query
r = requests.get(w).json()
temp = r['current']['temperature']
disc = r['current']['weather_descriptions'][0]
humidity =  r['current']['humidity']
country = r['location']['country']
print(country)