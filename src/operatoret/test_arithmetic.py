"""Operatorët aritmetikë

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët aritmetikë përdoren me vlera numerike për të kryer veprime të zakonshme matematikore
"""


def test_arithmetic_operators():
    """Operatorët aritmetikë"""

    # Mbledhja.
    assert 5 + 3 == 8

    # Zbritja.
    assert 5 - 3 == 2

    # Shumëzimi.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # Pjesëtimi.
    # Rezultati i pjesëtimit është numri me presje (float).
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Mbetja nga pjesëtimi.
    assert 5 % 3 == 2

    # Ngritja në fuqi e numrave.
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # Pjesëtimi dysheme.
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
