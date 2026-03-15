<h2 class="c-project-heading--task">Випадкові числа</h2>

\--- task ---

➡️ Отримай випадкове число для кидка кубика.

\--- /task ---

Використай імпортовану тобою функцію `randint`, щоб отримати випадкове число від 1 до 6 для кидка кубика.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
---

# Function definitions 
def roll_dice():
    print(f'You rolled a {randint(1, 6)}')
    
--- /code ---

**Test:** Click the **Run** button.
Now when you run your code, a new random number between 1 and 6 will be chosen each time.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:02:12.535000
You rolled a 6
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

`randint` is short for random integer. Integers are whole numbers.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Check your brackets and curly brackets if you get and error. Take note that the same number might be chosen over and over again. It's random!

</div>
