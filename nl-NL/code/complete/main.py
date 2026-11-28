# import
from datetime import datetime
from random import randint

wereld = '🌍🌎🌏'
python = 'Python 🐍'
vuur = '🔥'

# Functiedefinities        
def gooi_dobbelsteen():
    max = input('Hoeveel zijden heeft je dobbelsteen?:')
    print(f'Dat is een D {max}')
    worp = randint(1, int(max))
    print(f'Je hebt een {worp} {vuur * worp}') gegooid
    
# Zet de code om uit te voeren hieronder
print(f'Hallo {wereld}')
print(f"Welkom bij {python}')
print(f'{python} is goed in wiskunde!')
print(f'{111111111 * 111111111}')
print(f'De datum en tijd zijn {datetime.now()}')
gooi_dobbelsteen() # Roep de gooi dobbelsteen functie aan
print(f'Ik ❤️ ...')   
print(f'... maakt mij 😃')   
print(f'Ik zou graag ... willen maken met {python}')
