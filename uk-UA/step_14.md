<h2 class="c-project-heading--task">Отримай дані</h2>

\--- task ---

➡️ Allow the person using your program to type in some input.

\--- /task ---

You can use `input()` to ask the person using your program to enter text, and save it as a variable.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12-13
-----------------------------------------------------------

# Визначення функцій

def roll_dice():
max = input('Кількість сторін кубика:')
print(f'Цей кубик називається D {max}')
roll = randint(1,6)
print(f'Тобі випало число {roll} {fire \* roll}')

\--- /code ---

**Протестуй:** натисни на кнопку **Run**.
Обовʼязково натисни клавішу введення (<kbd>Enter</kbd>) після того, як введеш кількість сторін.
Ось що ти маєш побачити.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:20:41.323000
How many sides on your dice?:
20 
That is a D 20
You rolled a 1 🔥
```
</div>
