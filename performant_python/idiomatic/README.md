# Idiomatic "optimizations"
Pursuant to the notion that there _"should be one-- and preferably only one --obvious way to do it"_, writing idiomatic Python can often result in speedier code.
This is one area of optimization that you can (and should) always consider in any project.

That being said, I can't list _every_ "Pythonic" trait.
Instead, I'll list a couple seemingly-innocuous examples that receive decent performance improvement when written in an idiomatic fashion.

### Loops
Likely the most commonly-cited example, Python's list comprehensions are generally faster than comparable for loops.

### Strings
C-like string formatting is also a little slower than the more Python f-string formatting.
