<h2 class="c-project-heading--task">Виведи дату</h2>

\--- task ---

➡️ Виведи поточну дату та час.

\--- /task ---

Додай ще один рядок до коду, щоб зробити `print()` поточної дати й часу.

Отримати поточну дату та час можна за допомогою функції `now()` з модуля `datetime`:

--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 16
---

print(f'{python} is good at maths!')
print(f'{111111111 * 111111111}')
print(f'The date and time is {datetime.now()}')

--- /code ---

**Test:** Click the **Run** button.
This is what you should see when you run your code, but the date and time will be different.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 15:34:10.148000
```
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Check all your brackets `()` and curly brackets `{}` to make sure they are all opened and closed in the correct place.

</div>
