# Performant Python
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Overview
This repo contains the various tips, tricks, and resources I've encountered for squeezing maximum performance out of Python.
It's intended to be a continual work-in-progress.

### Contents
- [cython](./performant_python/cython)
- [ffi](./performant_python/ffi)
- [idiomatic](./performant_python/idiomatic)
- [interpreters](./performant_python/interpreters)
- [itertools](./performant_python/itertools)
- [profiling](./performant_python/profiling)

### Heuristics and Workflow
There are two big questions that need to be asked when attempting to optimize:
1. Where in the code do I need to focus my attention?
1. Which optimizations should I consider?

This section will be relatively high-level, recognizing that my competence in this area is ever-evolving (as is the Python ecosystem in this area).
