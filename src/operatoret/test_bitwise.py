"""Operatorët bitwise

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët bitwise manipulojnë numrat në nivel bit.
"""


def test_bitwise_operators():
    """Operatorët bitwise"""

    # AND
    # Vendos çdo bit në 1 nëse të dy bitët janë 1.
    #
    # Shembull:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # OR
    # Vendos çdo bit në 1 nëse njëri nga dy bit është 1.
    #
    # Shembull:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # NOT
    # Përmbys të gjitha bitet.
    assert ~5 == -6

    # XOR
    # Vendos çdo bit në 1 nëse vetëm një nga dy bit është 1.
    #
    # Shembull:
    # 5 = 0b0101
    # 3 = 0b0011
    numer = 5  # 0b0101
    numer ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Zhvendosje djathtas
    # Duke shtyrë kopjet e pjesës më të majtë brenda nga e majta dhe lërini të bien pjesët më të djathta.
    #
    # Shembull:
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001

    # Mbushje zero / zhvendosje majtas
    # Zhvendosni majtas duke shtyrë zerot nga e djathta dhe lërini pjesët më të majta të bien.
    #
    # Shembull:
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
