<h2 class="c-project-heading--task">Multiply strings</h2>

\--- task ---

➡️ Store the random number in a variable.
➡️ Multiply the number by the 🔥 emoji to print the emoji a number of times equal to the dice roll.

\--- /task ---

У Python ти можеш помножити на якесь число рядки, наприклад емоджі або цілі слова, і вони виводитимуться кілька разів.

Store the random number in a variable called `roll`.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
--------------------------------------------------------

# Визначення функцій

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

# Визначення функцій

def roll_dice():
roll = randint(1,6)
print(f'Тобі випало число {roll} {fire \* roll}')

\--- /code ---

**Протестуй:** натисни на кнопку **Run**.
Твій код на виході має виглядати приблизно так:

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

### Debugging

Check all your brackets are the same as the code example above.

</div>
