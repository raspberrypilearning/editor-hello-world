<h2 class="c-project-heading--task">Random numbers</h2>

--- task ---

Change your `roll_dice()` function so that it chooses a random number each time the code is run.

--- /task ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 11
---
# Function definitions        
def roll_dice():
    print('You rolled a {randint(1, 6)})
--- /code ---

--- tip ---

`randint` is short for random integer. Integers are whole numbers.

--- /tip ---

This is what you should see when you run your code, and a new random number between 1 and 6 will be chosen each time.

--- output ---

```python
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:02:12.535000
You rolled a 6
```

--- /output ---

--- debug ---

Check your brackets and curly brackets if you get and error. Also remember that the same number might be chosen over and over again. It's random!

--- /debug ---
