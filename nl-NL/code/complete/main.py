# imports
from datetime import datetime
from random import randint

wereld = '🌍🌎🌏'
python = 'Python 🐍'
vuur = '🔥'

# Functiedefinities        
def gooi_dobbelsteen():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1, int(max))
    print(f'You rolled a {roll} {fire * roll}')
    
# Zet de code om uit te voeren hieronder
print(f'Hello {world}')
print(f'Welcome to {python}')
print(f'{python} is good at maths!')
print(f'{111111111 * 111111111}')
print(f'The date and time is {datetime.now()}')
gooi_dobbelsteen() #Roep de dobbelsteen functie aan
print(f'I ❤️ ...')   
print(f'... maakt mij 😃')   
print(f'I would like to make ... with {python}')
