# imports
from datetime import datetime
from random import randint

world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'

# Визначення функцій        
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1, int(max))
    print(f'You rolled a {roll} {fire * roll}')
    
# Нижче розмісти код, який потрібно виконати
print('Привіт,' {world}')
print(f'Welcome to {python}')
print(f'{python} знається на математиці!')
print(f'{111111111 * 111111111}')
print(f'The date and time is {datetime.now()}')
roll_dice()  # Виклич функцію, яка кидає кубик
print(f'I ❤️ ...')   
print(f'... викликає у мене 😃')   
print(f'I would like to make ... у {python}')
