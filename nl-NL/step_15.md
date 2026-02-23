<h2 class="c-project-heading--task">Verander de dobbelstenen</h2>

--- task ---

➡️ Wijzig de invoergegevens naar een geheel getal.
➡️ Genereer een willekeurig getal tussen 1 en het aantal zijden dat de gebruiker heeft ingevoerd.

--- /task ---

Invoer wordt altijd opgeslagen als tekst, maar we moeten de invoer in `max` gebruiken om het grootste getal op te geven dat kan worden geworpen.

`max` is een tekenreeks en moet daarom worden gewijzigd naar een integer `int()`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
---

# Functiedefinities

def gooi_dobbelsteen():
    max = input('Hoeveel zijden heeft je dobbelsteen?:')
    print(f'Dat is een D {max}')
    worp = randint(1, int(max))
    print(f'Je hebt een {worp} {vuur * worp} gegooid')

--- /code ---

**Test:** Klik op de **Run** knop.
Dit is wat je zou moeten zien:

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
12345678987654321
De datum en tijd zijn 2023-11-21 16:27:24.101000
Hoeveel zijden heeft je dobbelsteen?:12
Dat is een D 12
Je hebt een 5 gegooid 🔥🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Het veranderen van het ene gegevenstype naar het andere gegevenstype wordt **type casting** genoemd.

</div>