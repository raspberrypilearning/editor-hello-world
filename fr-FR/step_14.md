<h2 class="c-project-heading--task">Obtenir une entrée</h2>

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

# Définitions de fonctions

def roll_dice():
max = input('How many sides on your dice?:')
print(f'That is a D {max}')
roll = randint(1,6)
print(f'You rolled a {roll} {fire \* roll}')

\--- /code ---

**Test :** clique sur le bouton **Run**.
Assure-toi d'appuyer sur la touche <kbd> Entrée</kbd> après avoir saisi le nombre de faces.
Tu devrais voir ceci lorsque tu exécutes ton code .

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
