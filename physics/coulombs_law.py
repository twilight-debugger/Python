"""
The force of attraction between two charges at a distance r from their centre points.

F = k * q1 * q2 / r^2

Where, k = Coulomb's constant [1/(4π*ε0)]
       q1 = charge of first body (C)
       q2 = charge of second body (C)
       r = distance between two charged bodies (m)

"""


def coulombs_law(q1: float, q2: float, radius: float) -> float:
    """
    Calculate the electrostatic force of attraction or repulsion
    between two point charges

    >>> coulombs_law(15.5, 20, 15)
    12382849136.06
    >>> coulombs_law(1, 15, 5)
    5392531075.38
    >>> coulombs_law(20, -50, 15)
    -39944674632.44
    >>> coulombs_law(-5, -8, 10)
    3595020716.92
    >>> coulombs_law(50, 100, 50)
    17975103584.6
    """
    if radius <= 0:
        raise ValueError("The radius is always a positive number")
    return round(((8.9875517923 * 10**9) * q1 * q2) / (radius**2), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
