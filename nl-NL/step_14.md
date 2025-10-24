<h2 class="c-project-heading--task">Input ophalen</h2>

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

# Functiedefinities

def roll_dice():
max = input('How many sides on your dice?:')
print(f'That is a D {max}')
roll = randint(1,6)
print(f'You rolled a {roll} {fire \* roll}')

\--- /code ---

**Test:** Klik op de **Run** knop.
Zorg ervoor dat je op de knop <kbd>Enter</kbd> klikt nadat je het aantal kanten hebt ingevoerd.
Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

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
