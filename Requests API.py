import requests
from time import sleep

attack = input("Type of Attack: ")
print('=-='*5)
print('Processing...')
sleep(2)
info = requests.get(f'https://API-WeaknessResistences-Pokemon.gabriel-ferrazf.repl.co/{attack}')
info = info.json()
print('=-='*5)
print(f'\033[32mSuper Effective\033[0m against:{info["Deal 2x in:"]}')
print(f'Effective against:{info["Deal 1x in:"]}')
print(f'\033[31mNot Very\033[0m Effective against:{info["Deal 0.5x in:"]}')
print(f'\033[37mIneffective\033[0m against:{info["Deal no damage:"]}')
