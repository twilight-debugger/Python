def centripetal_force(mass: float, velocity: float, radius: float) -> float:
    """
    Calculate the centripetal force acting on an object in circular motion.

    Formula:
        F = (m * v^2) / r

    Reference:
        https://byjus.com/physics/centripetal-and-centrifugal-force/

    >>> centripetal_force(2, 4, 2)
    16.0
    >>> centripetal_force(1, 3, 1)
    9.0
    >>> centripetal_force(-1, 3, 2)
    Traceback (most recent call last):
        ...
    ValueError: The mass of the body cannot be negative
    >>> centripetal_force(2, 3, 0)
    Traceback (most recent call last):
        ...
    ValueError: The radius must be a positive non-zero number
    """
    if mass < 0:
        raise ValueError("The mass of the body cannot be negative")
    if radius <= 0:
        raise ValueError("The radius must be a positive non-zero number")

    return (mass * velocity**2) / radius
