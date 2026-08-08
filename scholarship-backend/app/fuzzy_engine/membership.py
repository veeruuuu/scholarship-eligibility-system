"""
Generic helpers to build fuzzy membership functions from config boundaries.
"""
import numpy as np
import skfuzzy as fuzz


def build_universe(range_min, range_max, step=1):
    """Creates the discretized universe of discourse for a fuzzy variable."""
    return np.arange(range_min, range_max + step, step)


def build_membership(universe, points):
    """
    Builds a membership function from a list of points.
    3 points -> triangular, 4 points -> trapezoidal.
    """
    if len(points) == 3:
        return fuzz.trimf(universe, points)
    elif len(points) == 4:
        return fuzz.trapmf(universe, points)
    else:
        raise ValueError(f"Expected 3 or 4 points, got {len(points)}")