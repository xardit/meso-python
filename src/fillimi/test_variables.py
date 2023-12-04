"""Variablat

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

Python është krejtësisht i orientuar në objekte dhe nuk është "i shkruar statikisht".
Ju nuk keni nevojë të deklaroni variablat para se t'i përdorni, ose t'i deklaroni tipin.
Çdo variabël në Python është një objekt.

Në kundërshtim me gjuhët e tjera programuese,
Python nuk ka komandë për deklarimin e një variable.
Një variabël krijohet në momentin kur i caktoni një vlerë për herë të parë.

Një variabël mund të ketë një emër të shkurtër (si x dhe y) ose një emër
më të përshkrueshëm (mosha, emrimakinës, totali_volumit).

Rregullat për variablat në Python:
- Emri i një variabele duhet të fillojë me një shkronjë ose karakterin "_".
- Emri i një variabele nuk mund të fillojë me një numër.
- Emri i një variabele mund të përmbajë vetëm karaktere alfa-numerike dhe "_" (A-z, 0-9, dhe _ ).
- Emrat e variablave ndryshojnë nga madhësia e shkronjave (mosha, Mosha dhe MOSHA janë tre variabla të ndryshme).

"""


def test_variables():
    """Test variables"""

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4  # x is of type int
    variable_with_changed_type = 'Sally'  # x is now of type str

    assert variable_with_changed_type == 'Sally'
