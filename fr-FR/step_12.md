<h2 class="c-project-heading--task">Nombres aléatoires</h2>

➡️ Choisir un nombre aléatoire pour le lancer de dés.

Utilise la fonction `randint` que tu as importée pour choisir un nombre aléatoire entre 1 et 6 pour le lancer de dés.

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

## Now run your code

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

### Astuce

<div class="c-project-callout c-project-callout--tip">

`randint` is short for random integer. Integers are whole numbers.

</div>

### Debugging

<div class="c-project-callout c-project-callout--debug">

Check your brackets and curly brackets if you get and error. Take note that the same number might be chosen over and over again. It's random!

</div>

Click the **Run** button and check that the last line says `You rolled a` followed by a number from 1 to 6.
