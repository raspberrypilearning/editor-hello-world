<h2 class="c-project-heading--task">Multiply strings</h2>

--- task ---

In Python you can multiply strings such as emojis or whole words by a number, so they print out several times.

Change your function to store the random number in a variable called `roll`, then print it out.

--- /task ---

Your code should look like this:

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12-13
---
# Function definitions        
def roll_dice():
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')
--- /code ---

**Test:** Click the **Run** button.
Your output code should look something like this:

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
