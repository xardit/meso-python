"""Operatorët e anëtarësimit

@see: https://www.w3schools.com/python/python_operators.asp

Operatorët e anëtarësimit përdoren për të testuar nëse një sekuencë paraqitet në një objekt.
"""


def test_membership_operators():
    """Operatorët e anëtarësimit"""

    # Le të përdorim listën e mëposhtme të frutave për të ilustruar konceptin e anëtarësimit.
    lista_frutave = ["apple", "banana"]

    # in
    # Kthen True nëse një sekuencë me vlerën e specifikuar është e pranishme në objekt.

    # Kthen True sepse një sekuencë me vlerën "banane" është në listë
    assert "banana" in lista_frutave

    # not in
    # Kthen True nëse një sekuencë me vlerën e specifikuar nuk është e pranishme në objekt

    # Kthen True sepse një sekuencë me vlerën "pineapple" nuk është në listë.
    assert "pineapple" not in lista_frutave
