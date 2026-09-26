## Random numbers

➡️ Kies een willekeurig getal voor de dobbelsteenworp.

Gebruik de `randint`-functie die je hebt geïmporteerd om een willekeurig getal tussen 1 en 6 te kiezen voor de dobbelsteenworp.

```python line_numbers="true" line_number_start="10" line_highlights="12"

# Function definitions 
def roll_dice():
    print(f'You rolled a {randint(1, 6)}')
    
```

## Now run your code

Now when you run your code, a new random number between 1 and 6 will be chosen each time.

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:02:12.535000
You rolled a 6
```

> [!TIP]
>
> `randint` is short for random integer. Integers are whole numbers.

> [!DEBUG]
>
> Check your brackets and curly brackets if you get an error. Take note that the same number might be chosen over and over again. It's random!

Click the **Run** button and check that the last line says `You rolled a` followed by a number from 1 to 6.
