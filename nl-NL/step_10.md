<h2 class="c-project-heading--task">Roll dice</h2>

\--- task ---

➡️ Create a function to simulate rolling a dice.

➡️ Call the function to run the code inside it.

\--- /task ---

Create a function called `roll_dice()`, that prints out the number 4.

## --- code ---

language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 11
------------------------------------------------------------

# Functiedefinities

def roll_dice():
print(f'You rolled a {4}')

# Zet de code om uit te voeren hier onder

\--- /code ---

Roep vervolgens de functie onderaan je code aan.

## --- code ---

language: python
line_numbers: true
line_number_start: 18
line_highlights: 19
--------------------------------------------------------

print(f'The date and time is {datetime.now()}')
roll_dice()

\--- /code ---

**Test:** Klik op de **Run** knop.
Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 15:55:33.038000
You rolled a 4
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can use the **Tab** key on your keyboard to insert 4 spaces. Pressing **Shift** and **Tab** will remove the 4 spaces.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Check that you have brackets `()` and a colon `:` at the end of your function definition. Also check you are using brackets `()` when you call your function.

</div>
