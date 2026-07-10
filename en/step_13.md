## Multiply strings

➡️ Multiply the number by the 🔥 emoji to print the emoji a number of times equal to the dice roll.

In Python you can multiply strings such as emojis or whole words by a number, so they print out several times.

Store the random number in a variable called `roll`.

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
