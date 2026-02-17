<h2 class="c-project-heading--task">Invoer ophalen</h2>

\--- task ---

➡️ Laat de persoon die jouw programma gebruikt, iets invoeren.

\--- /task ---

Met `input()` kun je de persoon die jouw programma gebruikt vragen om tekst in te voeren en deze tekst als variabele opslaan.

## --- code ---

language: python
line_numbers: true
line_number_start: 10
line_highlights: 12-13
-----------------------------------------------------------

# Functiedefinities

def gooi_dobbelsteen():
max = input('Hoeveel zijden heeft je dobbelsteen?:')
print(f'Dat is een D {max}')
worp = randint(1,6)
print(f'Je hebt een {worp} {vuur \* worp}') gegooid

\--- /code ---

**Test:** Klik op de **Run** knop.
Zorg ervoor dat je op de knop <kbd>Enter</kbd> klikt nadat je het aantal kanten hebt ingevoerd.
Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
12345678987654321
De datum en tijd zijn 2023-11-21 16:20:41.323000
Hoeveel zijden heeft je dobbelsteen?:
20 
Dat is een D 20
Je hebt een 1 gegooid 🔥
```
</div>
