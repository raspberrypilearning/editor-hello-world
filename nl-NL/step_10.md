<h2 class="c-project-heading--task">Gooi dobbelstenen</h2>

--- task ---

➡️ Maak een functie om het gooien van een dobbelsteen te simuleren.

➡️ Roep de functie aan om de code erin uit te voeren.

--- /task ---

Maak een functie genaamd `gooi_dobbelsteen()`, die het getal 4 afdrukt.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 11
---

# Functiedefinities

def gooi_dobbelsteen():
    print(f'Je hebt een {4} gegooid')

# Zet de code om uit te voeren hier onder

--- /code ---

Roep vervolgens de functie onderaan je code aan.

--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 19
---
print(f'De datum en tijd zijn {datetime.now()}')
gooi_dobbelsteen()

--- /code ---

**Test:** Klik op de **Run** knop.
Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
12345678987654321
De datum en tijd zijn 2023-11-21 15:55:33.038000
Je hebt een 4 gegooid
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Je kunt de **Tab**-toets op jouw toetsenbord gebruiken om 4 spaties in te voegen. Door op **Shift** en **Tab** te drukken, worden de 4 spaties verwijderd.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Controleer of er haakjes `()` en een dubbele punt `:` aan het einde van jouw functiedefinitie staan. Controleer ook of je haakjes `()` gebruikt wanneer je jouw functie aanroept.

</div>
