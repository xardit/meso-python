"""Numrat.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

There are three numeric types in Python:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Lloji Numrit

    Int, ose integer, është një numër i plotë, pozitiv ose negativ, pa dhjetore, me gjatësi pa limit
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """Boolean

    Booleans përfaqësojnë vlerat e së vërtetës False dhe True. Dy objektet që përfaqësojnë vlerat False dhe True janë të vetmet objekte Boolean. Lloji Boolean është një nënlloj i tipit të numrit të plotë, dhe vlerat Boolean sillen si vlerat 0 dhe 1, respektivisht, pothuajse në të gjitha kontekstet, me përjashtim që kur konvertohet në një varg (string), vargjet "False" ose "True" kthehen, përkatësisht.
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """Float/Numri me presje

    Float, ose "numër me pikë lundruese" është një numër, pozitiv ose negativ,
    duke përmbajtur një ose më shumë numra mbas presjes.
    """

    float_number = 7.0
    # Një mënyrë tjetër për të deklaruar float është përdorimi i funksionit float().
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Float mund të jenë gjithashtu numra shkencorë me një "e" për të treguar fuqinë e 10.
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """Lloji Kompleks/Complex"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """Operacionet bazë"""

    # Shtesa.
    assert 2 + 4 == 6

    # Shumëzimi.
    assert 2 * 4 == 8

    # Pjesëtimi gjithmonë kthen një float
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # Mbetja nga pjesëtimi.
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # Pjesëtimi dysheme kthen numrin dusheme pa presje
    assert 17 // 3 == 5

    # Ngritja në fuqi e numrave.
    assert 5 ** 2 == 25  # 5 në katror
    assert 2 ** 7 == 128  # 2 në fiqi të 7

    # Numrat float/me presje mund të miksonhen me numra të thjeshtë dhe kthejnë një float
    assert 4 * 3.75 - 1 == 14.0
