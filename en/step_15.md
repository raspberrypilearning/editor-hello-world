## Change the dice

➡️ Generate a random number between 1 and the number of sides the user typed in.

Inputs are always stored as text, but we need to use the input stored in `max` to specify the largest number that could be rolled. 

`max` is a string, so it needs changing to an integer `int()`.

```python line_numbers="true" line_number_start="10" line_highlights="14"

# Function definitions        
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1, int(max))
    print(f'You rolled a {roll} {fire * roll}')
    
```

## Now run your code

This is what you should see:

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

> [!TIP]
>
> Changing one type of data to another type of data is called **type casting**.

Click the **Run** button, type a number of sides, and check that the dice roll can be any number from 1 up to the number you entered.
