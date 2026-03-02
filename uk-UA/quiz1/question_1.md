## Вдосконалення твого проєкту

## --- question ---

## legend: Питання 1 з 3

Цей код встановлює змінну `world` (англійською «світ»), яка буде містити текст '🌍🌎🌏' (три різні емоджі земної кулі):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Which code correctly uses the `world` variable and outputs Hello 🌍🌎🌏?

![The output area from the code editor with Hello 🌍🌎🌏 showing.](images/quiz1.png)

\--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hello' world)

--- /code ---

\--- feedback ---

Not quite, `output` is not the way to output messages to the screen.

\--- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello' world)

--- /code ---

\--- feedback ---

Not quite, in Python `print` outputs messages to the screen, but something is missing in this example.

\--- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello {world}')

--- /code ---

\--- feedback ---

That's correct, in Python `print(f'')` outputs messages to the screen. The text output is inside single quotes `'` , and curly braces `{}` are used to print the `world` variable.

\--- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello {world}')

--- /code ---

\--- feedback ---

Not quite, in Python `print` outputs messages to the screen, but something is missing in this example.

\--- /feedback ---

\--- /choices ---

\--- /question ---
