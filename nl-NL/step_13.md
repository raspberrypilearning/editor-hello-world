<h2 class="c-project-heading--task">Strings vermenigvuldigen</h2>

\--- task ---

➡️ Sla het willekeurige getal op in een variabele.
➡️ Vermenigvuldig het getal met de 🔥-emoji om de emoji een aantal keer af te drukken dat gelijk is aan de worp van de dobbelstenen.

\--- /task ---

In Python kun je strings zoals emoji's of hele woorden vermenigvuldigen met een getal, zodat ze meerdere keren worden geprint.

Sla het willekeurige getal op in een variabele met de naam `roll`.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
--------------------------------------------------------

# Functiedefinities

def roll_dice():
roll = randint(1,6)

\--- /code ---

Vermenigvuldig het willekeurige getal in `roll` met de 🔥 emoji en druk het resultaat af.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 13
--------------------------------------------------------

# Functiedefinities

def roll_dice():
roll = randint(1,6)
print(f'Je hebt een {roll} {fire \* roll}') gegooid

\--- /code ---

**Test:** Klik op de **Run** knop.
Je uitvoer zou er ongeveer zo uit moeten zien:

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
12345678987654321
De datum en tijd zijn 2023-11-21 16:14:45.140000
Je hebt een 4 gegooid 🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Controleer of alle haakjes hetzelfde zijn als in het bovenstaande codevoorbeeld.

</div>
