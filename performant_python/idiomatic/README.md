# Idiomatic "optimizations"
Pursuant to the notion that there _"should be one-- and preferably only one --obvious way to do it"_, writing idiomatic Python can often result in speedier code.
This is one area of optimization that you can (and should) always consider in any project.

That being said, I can't list _every_ "Pythonic" trait.
Instead, I'll list a couple seemingly-innocuous examples that receive decent performance improvement when written in an idiomatic fashion.

### Loops
Likely the most commonly-cited example, Python's list comprehensions are generally faster than comparable for loops.

```python INJECT_CODE(loops.py)
def for_loop():
    input = range(100_000)
    output = []
    
    for i in input:
        if i % 2 == 0:
            output.append(i)
    
    return output


def list_comp():
    return [
        i for i in range(100_000)
        if i % 2 == 0
    ]
```

The two loops above do the exact same thing, but (on on my machine) `list_comp` runs ~25% faster:
```python
>>> %timeit for_loop()
7.2 ms ± 13.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

>>> %timeit list_comp()
5.82 ms ± 23.8 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

### Strings
C-like string formatting is also a little slower than the more Python f-string formatting.

```python INJECT_CODE(strings.py)
def c_style():
    name = "Foo"
    return "Hello, %s" % name


def f_string():
    name = "Foo"
    return f"Hello, {name}"
```

Not that anyone is going to lose their minds savings 50 nanoseconds, but the newer f-string example is nevertheless over 40% faster than the C-style version:

```python
>>> %timeit c_style()
149 ns ± 1.42 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

>>> %timeit f_string()
105 ns ± 0.24 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```
