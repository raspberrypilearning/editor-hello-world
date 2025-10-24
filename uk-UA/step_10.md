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

# Визначення функцій

def roll_dice():
print(f'Тобі випало число {4}')

# Нижче розмісти код, який потрібно виконати

\--- /code ---

Тепер виклич функцію під кодом.

## --- code ---

language: python
line_numbers: true
line_number_start: 18
line_highlights: 19
--------------------------------------------------------

print(f'Дата й час — {datetime.now()}')
roll_dice()

\--- /code ---

**Протестуй:** натисни на кнопку **Run**.
Ось що ти маєш побачити.

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

### Debugging

Check that you have brackets `()` and a colon `:` at the end of your function definition. Also check you are using brackets `()` when you call your function.

</div>
