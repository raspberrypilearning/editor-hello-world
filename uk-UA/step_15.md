<h2 class="c-project-heading--task">Change the dice</h2>

\--- task ---

➡️ Change the input data to an integer.
➡️ Generate a random number between 1 and the number of sides the user typed in.

\--- /task ---

Inputs are always stored as text, but we need to use the input stored in `max` to specify the largest number that could be rolled.

`max` is a string, so it needs changing to an integer `int()`.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
--------------------------------------------------------

# Визначення функцій

def roll_dice():
max = input('Кількість сторін кубика:')
print(f'Цей кубик називається D {max}')
roll = randint(1, int(max))
print(f'Тобі випало число {roll} {fire \* roll}')

\--- /code ---

**Протестуй:** натисни на кнопку **Run**.
This is what you should see:

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:27:24.101000
How many sides on your dice?:12
That is a D 12
You rolled a 5 🔥🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Changing one type of data to another type of data is called **type casting**.

</div>