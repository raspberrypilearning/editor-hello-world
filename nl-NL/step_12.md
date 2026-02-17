<h2 class="c-project-heading--task">Willekeurige getallen</h2>

--- task ---

➡️ Kies een willekeurig getal voor de dobbelsteenworp.

--- /task ---

Gebruik de `randint`-functie die je hebt geïmporteerd om een willekeurig getal tussen 1 en 6 te kiezen voor de dobbelsteenworp.

##
--- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
--------------------------------------------------------

# Functiedefinities

def gooi_dobbelsteen():
print(f'Je hebt een {randint(1, 6)} gegooid')

--- /code ---

**Test:** Klik op de **Run** knop.
Wanneer je nu je code nog eens uitvoert, zal er elke keer een nieuw willekeurig getal tussen 1 en 6 worden gekozen.

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
12345678987654321
De datum en tijd zijn 2023-11-21 16:02:12.535000
Je hebt een 6 gegooid
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

`randint` is de afkorting van random integer. Integers zijn gehele getallen.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Controleer de haakjes en accolades als je een foutmelding krijgt. Houd er rekening mee dat hetzelfde getal steeds opnieuw gekozen kan worden. Het is willekeurig!

</div>
