<h2 class="c-project-heading--task">Multiply strings</h2>

\--- task ---

➡️ Store the random number in a variable.
➡️ Multiply the number by the 🔥 emoji to print the emoji a number of times equal to the dice roll.

\--- /task ---

In Python kun je strings zoals emoji's of hele woorden vermenigvuldigen met een getal, zodat ze meerdere keren worden geprint.

Store the random number in a variable called `roll`.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
--------------------------------------------------------

# Functiedefinities

def roll_dice():
roll = randint(1,6)

\--- /code ---

Multiply the random number stored in `roll` by the 🔥 emoji, and print the result.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 13
--------------------------------------------------------

# Functiedefinities

def roll_dice():
roll = randint(1,6)
print(f'You rolled a {roll} {fire \* roll}')

\--- /code ---

**Test:** Klik op de **Run** knop.
Je uitvoer zou er ongeveer zo uit moeten zien:

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:14:45.140000
You rolled a 4 🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Check all your brackets are the same as the code example above.

</div>
