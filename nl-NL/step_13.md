## Multiply strings

➡️ Vermenigvuldig het getal met de 🔥-emoji om de emoji een aantal keer af te drukken dat gelijk is aan de worp van de dobbelsteen.

In Python kun je tekenreeksen zoals emoji's of hele woorden vermenigvuldigen met een getal, zodat ze meerdere keren worden geprint.

Sla het willekeurige getal op in een variabele met de naam `worp`.

```python line_numbers="true" line_number_start="10" line_highlights="12"

# Function definitions        
def roll_dice():
    roll = randint(1,6)

```

Multiply the random number stored in `roll` by the 🔥 emoji, and print the result.

```python line_numbers="true" line_number_start="10" line_highlights="13"

# Function definitions        
def roll_dice():
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')
    
```

## Now run your code

Your output code should look something like this:

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:14:45.140000
You rolled a 4 🔥🔥🔥🔥
```

> [!DEBUG]
>
> Check all your brackets are the same as the code example above.

Click the **Run** button and check that the last line shows the dice number and the same number of fire emojis.
