<h2 class="c-project-heading--task">Tekenreeksen vermenigvuldigen</h2>

\--- task ---

➡️ Sla het willekeurige getal op in een variabele.
➡️ Vermenigvuldig het getal met de 🔥-emoji om de emoji een aantal keer af te drukken dat gelijk is aan de worp van de dobbelsteen.

\--- /task ---

In Python kun je tekenreeksen zoals emoji's of hele woorden vermenigvuldigen met een getal, zodat ze meerdere keren worden geprint.

Sla het willekeurige getal op in een variabele met de naam `worp`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
---

# Function definitions        
def roll_dice():
    roll = randint(1,6)

--- /code ---

Multiply the random number stored in `roll` by the 🔥 emoji, and print the result.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 13
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
