from math import radians, cos, sin, asin, sqrt


__all__ = ["haversine"]


def haversine(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """
    Example:
        lon1 = -103.548851
        lat1 = 32.0004311
        lon2 = -103.6041946
        lat2 = 33.374939

        haversine(lat1, lon1, lat2, lon2)
        95.05067505558074
    """
    # this is in miles
    # For Earth radius in kilometers use 6372.8 km
    R = 3959.87433

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
