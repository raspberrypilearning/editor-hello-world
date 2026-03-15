<h2 class="c-project-heading--task">Отримай дані</h2>

\--- task ---

➡️ Дай можливість людині, яка користується твоєю програмою, ввести власні дані.

\--- /task ---

За допомогою функції `input()` (англійською «вхідні дані») ти можеш попросити людину, яка використовує твою програму, ввести якийсь текст.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12-13
---

# Function definitions
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')

--- /code ---

**Test:** Click the **Run** button.
Ensure you press the <kbd> Enter </kbd> key after inputting how many sides.
This is what you should see when you run your code.

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
