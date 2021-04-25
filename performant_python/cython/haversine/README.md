# Testing Cython vs CPython with haversine distance

### Build Cython file
```
python setup.py build_ext --inplace
```

### Comparison to CPython
Running on my relatively old machine:

```python
# ipython shell

from haversine_python import haversine as haversine_p
from haversine_cython import haversine as haversine_c

lon1 = -103.548851
lat1 = 32.0004311
lon2 = -103.6041946
lat2 = 33.374939

%timeit haversine_p(lat1, lon1, lat2, lon2)
753 ns ± 18.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit haversine_c(lat1, lon1, lat2, lon2)
137 ns ± 2.27 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

Even though the Python `math` library is a wrapper around the C `cmath` module (see [docs](https://docs.python.org/3/library/math.html)),
the Cython implementation is still 5.5x faster (on my machine).
Not bad for the marginal additional effort.

### Comparison to Java
WIP

### References
- The [docs](https://cython.readthedocs.io/en/latest/index.html)
- This haversine [example](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
- A very helpful [example](https://idlecoding.com/faster-image-transforms-with-cython/) of profiling and usage
