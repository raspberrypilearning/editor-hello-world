<h2 class="c-project-heading--task">Gooi dobbelstenen</h2>

➡️ Maak een functie om het gooien van een dobbelsteen te simuleren.

Maak een functie genaamd `gooi_dobbelsteen()`, die het getal 4 afdrukt.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 11
---

# Function definitions        
def roll_dice():
    print(f'You rolled a {4}')
    
# Put code to run under here

--- /code ---

Then, call the function at the bottom of your code.

--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 19
---
print(f'The date and time is {datetime.now()}')
roll_dice()

--- /code ---

## Now run your code

This is what you should see when you run your code.

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

### Tip

<div class="c-project-callout c-project-callout--tip">

You can use the **Tab** key on your keyboard to insert 4 spaces. Pressing **Shift** and **Tab** will remove the 4 spaces.

</div>

### Debugging

<div class="c-project-callout c-project-callout--debug">

Check that you have brackets `()` and a colon `:` at the end of your function definition. Also check you are using brackets `()` when you call your function.

</div>

Click the **Run** button and check that the last line says `You rolled a 4`.
