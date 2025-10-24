## --- question ---

## legend: Питання 3 з 3

Ця функція виводить два випадкових числа:

## --- code ---

## language: python

def two_dice():
print('First number:', randint(1, 6))
print('Second number:', randint(1, 6))

\--- /code ---

Яким кодом можна викликати і запустити цю функцію?

![The code editor with output area showing two randomly generated numbers.](images/quiz3.png)

\--- choices ---

- ( )

## --- code ---

## language: python

def two_dice():
print('First number:', randint(1, 6))
print('Second number:', randint(1, 6))

\--- /code ---

\--- feedback ---

Ні, це код визначає функцію, але не запускає її. Для виклику функції потрібен інший код.

\--- /feedback ---

- ( )
  \--- code ---

---

## language: python

two_dice

\--- /code ---

\--- feedback ---

Майже! `two_dice` is the name of the function, but to call it you need more than just the name.

\--- /feedback ---

- ()

## --- code ---

## language: python

two_dice[]

\--- /code ---

\--- feedback ---

Не зовсім так. Подумай про тип дужок, які ми використовували для виклику функцій у твоєму проєкті.

\--- /feedback ---

- (x)

## --- code ---

## language: python

two_dice()

\--- /code ---

\--- feedback ---

That's correct, using the function name followed by `(` `)` brackets will call the function.

\--- /feedback ---

\--- /choices ---

\--- /question ---
