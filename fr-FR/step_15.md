<h2 class="c-project-heading--task">Changer le dé</h2>

\--- task ---

➡️ Modifier les données d’entrée en un entier.
➡️ Génèrer un nombre aléatoire compris entre 1 et le nombre de faces saisi par l'utilisateur.

\--- /task ---

Les entrées sont toujours stockées sous forme de texte, mais nous devons utiliser l'entrée stockée dans `max` pour spécifier le plus grand nombre qui pourrait être obtenu.

`max` est une chaîne, elle doit donc être changée en un entier `int()`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
---

# Function definitions        
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1, int(max))
    print(f'You rolled a {roll} {fire * roll}')
    
--- /code ---

**Test:** Click the **Run** button.
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

### Astuce

Changing one type of data to another type of data is called **type casting**.

</div>