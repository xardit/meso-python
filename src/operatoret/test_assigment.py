"""Operatorët e caktimit

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët e caktimit përdoren për të caktuar vlera tek variablat
"""


def test_assignment_operator():
    """Operatorët e caktimit"""

    # Caktimi: =
    numer = 5
    assert numer == 5

    # Caktime të shumëfishta.
    # Variablat variabla_pare dhe variabla_dyte marrin njëkohësisht vlerat e reja 0 dhe 1.
    variabla_pare, variabla_dyte = 0, 1
    assert variabla_pare == 0
    assert variabla_dyte == 1

    # Ju madje mund të ndërroni vlerat e variablave duke përdorur caktime të shumëfishta.
    variabla_pare, variabla_dyte = variabla_dyte, variabla_pare
    assert variabla_pare == 1
    assert variabla_dyte == 0


def test_augmented_assignment_operators():
    """Operatori i caktimit të kombinuar me operatorët aritmetikë dhe bitwise"""

    # Caktimi: +=
    numer = 5
    numer += 3
    assert numer == 8

    # Caktimi: -=
    numer = 5
    numer -= 3
    assert numer == 2

    # Caktimi: *=
    numer = 5
    numer *= 3
    assert numer == 15

    # Caktimi: /=
    numer = 8
    numer /= 4
    assert numer == 2

    # Caktimi: %=
    numer = 8
    numer %= 3
    assert numer == 2

    # Caktimi: %=
    numer = 5
    numer %= 3
    assert numer == 2

    # Caktimi: //=
    numer = 5
    numer //= 3
    assert numer == 1

    # Caktimi: **=
    numer = 5
    numer **= 3
    assert numer == 125

    # Caktimi: &=
    numer = 5  # 0b0101
    numer &= 3  # 0b0011
    assert numer == 1  # 0b0001

    # Caktimi: |=
    numer = 5  # 0b0101
    numer |= 3  # 0b0011
    assert numer == 7  # 0b0111

    # Caktimi: ^=
    numer = 5  # 0b0101
    numer ^= 3  # 0b0011
    assert numer == 6  # 0b0110

    # Caktimi: >>=
    numer = 5
    numer >>= 3
    assert numer == 0  # (((5 // 2) // 2) // 2)

    # Caktimi: <<=
    numer = 5
    numer <<= 3
    assert numer == 40  # 5 * 2 * 2 * 2
