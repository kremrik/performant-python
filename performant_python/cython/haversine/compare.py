from haversine_cython import haversine as haversine_c
from haversine_python import haversine as haversine_p

from time import time


lon1 = -103.548851
lat1 = 32.0004311
lon2 = -103.6041946
lat2 = 33.374939


t0 = time()
for _ in range(10000000):
    haversine_c(lat1, lon1, lat2, lon2)
t1 = time()

elapsed = t1 - t0
print(f"Cython: {elapsed:1.3} seconds")


t0 = time()
for _ in range(10000000):
    haversine_p(lat1, lon1, lat2, lon2)
t1 = time()

elapsed = t1 - t0
print(f"CPython: {elapsed:1.3} seconds")
