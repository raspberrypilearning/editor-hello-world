<h2 class="c-project-heading--task">Obtenir une entrée</h2>

➡️ Permettre à la personne qui utilise ton programme de saisir des données.

Tu peux utiliser `input()` pour demander à la personne utilisant ton programme de saisir du texte et de l'enregistrer en tant que variable.

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

## Now run your code

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

Click the **Run** button, type a number such as `20`, and check that the program says `That is a D 20` before showing a dice roll.
