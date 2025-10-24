<h2 class="c-project-heading--task">Nombres aléatoires</h2>

\--- task ---

➡️ Choose a random number for the dice roll.

\--- /task ---

Use the `randint` function you imported to choose a random number between 1 and 6 for the dice roll.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
--------------------------------------------------------

# Définitions de fonctions

def roll_dice():
print(f'You rolled a {randint(1, 6)}')

\--- /code ---

**Test :** clique sur le bouton **Run**.
Maintenant, lorsque tu exécutes ton code, un nouveau nombre aléatoire entre 1 et 6 sera choisi à chaque fois.

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

### Conseil

`randint` is short for random integer. Integers are whole numbers.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Check your brackets and curly brackets if you get and error. Take note that the same number might be chosen over and over again. It's random!

</div>
