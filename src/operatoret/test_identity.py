"""Operatorët e identitetit

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët e identitetit përdoren për të krahasuar objektet, jo nëse janë të barabartë, por nëse janë në të vërtetë
i njëjti objekt, me të njëjtin vend në memorie.
"""


def test_identity_operators():
    """Operatorët e identitetit"""

    # Le të ilustrojmë operatorët e identitetit bazuar në listat e mëposhtme.
    lista_frutave_pare = ["apple", "banana"]
    lista_frutave_dyte = ["apple", "banana"]
    lista_frutave_trete = lista_frutave_pare

    # is
    # Rikthen true nëse të dy variablat janë i njëjti objekt.

    # Shembull:
    # lista_frutave_pare dhe lista_frutave_trete janë i njëjti objekt.
    assert lista_frutave_pare is lista_frutave_trete

    # is not
    # Rikthen true nëse të dy variablat nuk janë i njëjti objekt.

    # Shembull:
    # lista_frutave_pare dhe lista_frutave_dyte nuk janë i njëjti objekt, edhe nëse kanë të njëjtën përmbajtje
    assert lista_frutave_pare is not lista_frutave_dyte

    # Për të demonstruar ndryshimin midis "is" dhe "=="
    # ky krahasim kthen "True" sepse lista_frutave_pare është e barabartë me lista_frutave_dyte.
    assert lista_frutave_pare == lista_frutave_dyte
