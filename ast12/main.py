########### Exercise 1 ###########
import requests
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
print(response.json()['value'])
########### Exercise 2 ###########
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=435bd386abc40026598b127067e8e325&units=metric"
response = requests.get(url).json()
print(response['weather'][0]['description'])
print(f"Temperature: {response['main']['temp']}")