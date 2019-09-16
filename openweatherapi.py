import requests

cidade = input('Nome da cidade: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&id=524901&units=metric&APPID=c221537d69c251d2d6ffd4c753750079'

r = requests.get(url)

clima = r.json()



print(f"A temperatura em {cidade} é de {clima['main']['temp']} ºC.")