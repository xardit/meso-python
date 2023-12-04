"""Operatorët logjikë

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët logjikë përdoren për të kombinuar deklaratat e kushtëzuara.
"""


def test_logical_operators():
    """Operatorët logjikë"""

    # Let's work with these number to illustrate logic operators.
    numri_pare = 5
    numri_dyte = 10

    # and
    # Returns True if both statements are true.
    assert numri_pare > 0 and numri_dyte < 20

    # or
    # Returns True if one of the statements is true
    assert numri_pare > 5 or numri_dyte < 20

    # not
    # Reverse the result, returns False if the result is true.
    # pylint: disable=unneeded-not
    assert not numri_pare == numri_dyte
    assert numri_pare != numri_dyte
