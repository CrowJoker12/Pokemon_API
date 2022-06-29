import requests
from time import sleep

ataque = input("Tipo de Ataque: ")
print('=-='*5)
print('Processando...')
sleep(2)
info = requests.get(f'https://api-fraquezaresistencia-pokemon.gabriel-ferrazf.repl.co/{ataque}')
info = info.json()
print('=-='*5)
print(f'Super Efetivo a:{info["Causa 2x a:"]}')
print(f'Efetivo a:{info["Causa 1x a"]}')
print(f'Não Muito Efetivo a:{info["Causa 0.5x a:"]}')
print(f'Inefetivo a:{info["Nao causa dano:"]}')
