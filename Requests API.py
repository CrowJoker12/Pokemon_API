import requests
from time import sleep

attack = input("Type of Attack: ")
print('=-='*5)
print('Processing...')
sleep(2)
info = requests.get(f'https://api-fraquezaresistencia-pokemon.gabriel-ferrazf.repl.co/{attack}')
info = info.json()
print('=-='*5)
print(f'Super Effective against:{info["Deal 2x in:"]}')
print(f'Effective against:{info["Deal 1x in:"]}')
print(f'Not Very Effective against:{info["Deal 0.5x in:"]}')
print(f'Ineffective against:{info["Deal no damage:"]}')
