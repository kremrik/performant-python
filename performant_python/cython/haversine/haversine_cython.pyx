# -*- coding: utf-8 -*-
# cython: language_level=3


cimport cython
from libc.math cimport cos, sin
from libc.math cimport asin
from libc.math cimport sqrt
from libc.math cimport M_PI


@cython.cdivision(True)
cpdef double haversine(
    double lat1,
    double lon1,
    double lat2,
    double lon2
):
    cdef double R = 3959.87433

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = (
        sin(dLat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    )
    c = 2 * asin(sqrt(a))

    return R * c


@cython.cdivision(True)
cdef inline double radians(double degrees):
    """
    This fnc is a build-in in CPython
    Building this way is a tad slower
    """
    rads = degrees * (M_PI / 180.0)
    return rads
