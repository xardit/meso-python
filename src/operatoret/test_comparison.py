"""Operatorët e krahasimit

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët e krahasimit përdoren për të krahasuar dy vlera
"""


def test_comparison_operators():
    """Operatorët e krahasimit"""

    # Equal.
    numer = 5
    assert numer == 5

    # Not equal.
    numer = 5
    assert numer != 3

    # Greater than.
    numer = 5
    assert numer > 3

    # Less than.
    numer = 5
    assert numer < 8

    # Greater than or equal to
    numer = 5
    assert numer >= 5
    assert numer >= 4

    # Less than or equal to
    numer = 5
    assert numer <= 5
    assert numer <= 6
