<h2 class="c-project-heading--task">Get input</h2>

--- task ---

You can use `input()` to ask the person using your program to enter text, and save it as a variable.

--- /task ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 11, 12
---
# Function definitions
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')
--- /code ---

This is what you should see when you run your code.

--- output ---

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:20:41.323000
How many sides on your dice?:
20 # This is where you typed your number
That is a D 20
You rolled a 1 🔥
```

--- /output ---
