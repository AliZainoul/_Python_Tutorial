# Examples directory

This folder contains small, focused Python example scripts used for learning and demonstrating
core Python concepts: argument unpacking, date/time handling, basic data structures, iteration,
and small utility patterns. Each script is standalone and can be run with the system Python
interpreter.

## Quick navigation

- `args_headache.py` — Demonstrates differences between `args` and `*args` in function definitions and printing behavior. Useful to learn how Python unpacks arguments.
- `args_kwargs_cart.py` — A small `ShoppingCart` class showing `*args` / `**kwargs` usage, `namedtuple`, and a `calculate_total` method.
- `args_kwargs_person.py` — Simple example building person dicts with `**kwargs` and printing them.
- `date_time.py` — Examples for `datetime.now()`, formatting with `strftime`, and extracting date/time components.
- `find_student.py` — Small search helper that finds students by id, name, or age using simple comparison ops.
- `input_args.py` — Examples for reading input/command-line style arguments.
- `math_utils.py`, `library.py`, `my_iterable.py` — utility/example modules demonstrating functions and iteration patterns.

There are also subfolders that contain more organized examples and packages:

- `data_structures/` — Data structure focused examples.
- `name_mangling/`, `oop/`, `operators/`, `package_test/`, `range/` — focused topic examples and small modules.

## Try it

Run an example directly from the command line (macOS/Linux/zsh):

```bash
python3 examples/args_headache.py
python3 examples/args_kwargs_cart.py
python3 examples/date_time.py
```

## Tips

- Read the docstrings at the top of each script for intent and usage notes.
- Many example files are safe to run; others may prompt for input — run them interactively.
- Use these scripts as small building blocks when experimenting in a REPL or a new project.

## Contributing

If you add more examples, please update this README with a one-line description and any
special run instructions.
