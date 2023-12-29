# Hapësira për të mësuar Python

---

> Ky është një koleksion skriptesh për gjuhën Python që ndahen sipas [temave](#tabela-e-përmbajtjes) dhe përmbajnë shembuj kodesh me shpjegime, raste të ndryshme përdorimi dhe lidhje për lexime të mëtejshme.

Është një **hapësirë lojrash** sepse mund të ndryshoni ose shtoni kodin për të parë se si funksionon dhe [testoni atë](#testing-the-code) duke përdorur pohimet.
Në përgjithësi, kjo mund ta bëjë procesin tuaj të të mësuarit të jetë më ndërveprues dhe të thjeshtë duke ju ndihmuar të rrisni cilësinë e kodimit që në fillim.

Është një **cheatsheet** sepse mund ju mund ti riktheheni këtyre shembujve të kodit sa herë të dëshironi dhe të rikujtoni sintaksat e [deklaratave dhe zhvillimeve sipas standardit të Python](#tabela-e-përmbajtjes). Gjithashtu për shkak se kodi është plot me pohime që do të mund të shihni menjëherë daljen e funksioneve/deklaratave të pritshme pa i nisur ato.

## Si ta përdorni këtë depo

Çdo skript Python në këtë depo ka strukturën e mëposhtme:

```python
"""Lists  <--- Emri i temës këtu

# @see: https://www.learnpython.org/en/Lists  <-- Link për lexime të mëtejshme gjendet këtu

Këtu mund të ketë shpjegim më të detajuar të temës aktuale (dmth informacione të përgjithshme rreth listave).
"""


def test_list_type():
    """Shpjegimi i nëntemës shkon këtu.

    Çdo skedar përmban funksione testimi që ilustrojnë nën-temat (p.sh. llojin e listave, liston metodat).
    """

    # Këtu është një shembull se si të krijoni një listë. <-- Komentet këtu shpjegojnë veprimin
    kuti = [1, 4, 9, 16, 25]

    # Listat mund të indeksohen dhe priten në pjesë
    # Indeksimi kthen një element.
    assert kuti[0] == 1  # <-- Pohimet këtu ilustrojnë rezultatin.
    # Prerja kthen një listë të re.
    assert kuti[-3:] == [9, 16, 25]  # <-- Pohimet këtu ilustrojnë rezultatin.
```

## Zakonisht kur hapni këtë depo ju mund të filloni si më poshtë:

- [Gjeni temën](#tabela-e-përmbajtjes) që dëshironi të mësoni ose rishikoni.
- Lexoni komentet dhe/ose dokumentacionin që është i lidhur në vargun e çdo skripti (si në shembullin e mësipërm).
- Shikoni shembujt dhe pohimet e kodit për të parë shembujt e përdorimit dhe rezultatet e pritura.
- Ndryshoni kodin ose shtoni pohime të reja për të parë se si funksionojnë gjërat.
- [Run tests](#testing-the-code) dhe [lint the code](#linting-the-code) për të parë nëse funksionon dhe është
  shkruar saktë.

## Tabela e Përmbajtjes

1. **Fillimi**
   - [Cfarë është Python](src/fillimi/cfare_eshte_python.md)
   - [Sintaksa Python](src/fillimi/sintaksa_python.md)
   - [Variablat](src/fillimi/test_variables.py)
2. **Operatorët**
   - [Operatorët Aritmetikë](src/operatoret/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
   - [Operatorët Bitwise](src/operatoret/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
   - [Operatorët e Caktimit](src/operatoret/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` etc.)
   - [Operatorët e Krahasimit](src/operatoret/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
   - [Operatorët Logjikë](src/operatoret/test_logical.py) (`and`, `or`, `not`)
   - [Operatorët e Identitetit](src/operatoret/test_identity.py) (`is`, `is not`)
   - [Operatorët e Anëtarësimit](src/operatoret/test_membership.py) (`in`, `not in`)
3. **Llojet e të dhënave / Data Types**
   - [Numrat](src/data_types/test_numbers.py) (perfshin booleans)
   - *[Vargjet/Strings](src/data_types/test_strings.py) dhe metodat
   - [Listat](src/data_types/test_lists.py) dhe metodat (duke përfshirë të kuptuarit e listës)
   - [Tuples](src/data_types/test_tuples.py)
   - [Bashkesia/Set](src/data_types/test_sets.py) dhe metodat
   - [Fjaloret/Dictionaries](src/data_types/test_dictionaries.py)
   - [Lloji modelit](src/data_types/test_type_casting.py)
4. **Control Flow**
   - [The `if` statement](src/control_flow/test_if.py)
   - [The `for` statement](src/control_flow/test_for.py) (and `range()` function)
   - [The `while` statement](src/control_flow/test_while.py)
   - [The `try` statements](src/control_flow/test_try.py)
   - [The `break` statement](src/control_flow/test_break.py)
   - [The `continue` statement](src/control_flow/test_continue.py)
5. **Functions**
   - [Function Definition](src/functions/test_function_definition.py) (`def` and `return` statements)
   - [Scopes of Variables Inside Functions](src/functions/test_function_scopes.py) (`global` and `nonlocal` statements)
   - [Default Argument Values](src/functions/test_function_default_arguments.py)
   - [Keyword Arguments](src/functions/test_function_keyword_arguments.py)
   - [Arbitrary Argument Lists](src/functions/test_function_arbitrary_arguments.py)
   - [Unpacking Argument Lists](src/functions/test_function_unpacking_arguments.py) (`*` and `**` statements)
   - [Lambda Expressions](src/functions/test_lambda_expressions.py) (`lambda` statement)
   - [Documentation Strings](src/functions/test_function_documentation_string.py)
   - [Function Annotations](src/functions/test_function_annotations.py)
   - [Function Decorators](src/functions/test_function_decorators.py)
6. **Classes**
   - [Class Definition](src/classes/test_class_definition.py) (`class` statement)
   - [Class Objects](src/classes/test_class_objects.py)
   - [Instance Objects](src/classes/test_instance_objects.py)
   - [Method Objects](src/classes/test_method_objects.py)
   - [Class and Instance Variables](src/classes/test_class_and_instance_variables.py)
   - [Inheritance](src/classes/test_inheritance.py)
   - [Multiple Inheritance](src/classes/test_multiple_inheritance.py)
7. **Modules**
   - [Modules](src/modules/test_modules.py) (`import` statement)
   - [Packages](src/modules/test_packages.py)
8. **Errors and Exceptions**
   - [Handling Exceptions](src/exceptions/test_handle_exceptions.py) (`try` statement)
   - [Raising Exceptions](src/exceptions/test_raise_exceptions.py) (`raise` statement)
9. **Files**
   - [Reading and writing](src/files/test_file_reading.py) (`with` statement)
   - [Methods of File Objects](src/files/test_file_methods.py)
10. **Additions**
    - [The `pass` statement](src/additions/test_pass.py)
    - [Generators](src/additions/test_generators.py) (`yield` statement)
11. **Brief Tour of the Standard Libraries**
    - [Serialization](src/standard_libraries/test_json.py) (`json` library)
    - [File wildcards](src/standard_libraries/test_glob.py) (`glob` library)
    - [String Pattern Matching](src/standard_libraries/test_re.py) (`re` library)
    - [Mathematics](src/standard_libraries/test_math.py) (`math`, `random`, `statistics` libraries)
    - [Dates and Times](src/standard_libraries/test_datetime.py) (`datetime` library)
    - [Data Compression](src/standard_libraries/test_zlib.py) (`zlib` library)
12. **User input**
    - [Terminal input](src/user_input/test_input.py) (`input` statement)

## Kërkesat e nevojshme

**Instalimi Python**

Sigurohu që keni [Python3 të instaluar](https://realpython.com/installing-python/) në kompjuterin tuaj.

Mirë do ishte të përdornit [venv](https://docs.python.org/3/library/venv.html) për të instaluar paketat e kërkuara të Python në këtë depo

Në varësi të instalimit tuaj, mund të keni akses në interpretuesin Python3 ose nga
ekzekutimi i `python` ose `python3`. E njëjta gjë vlen edhe për menaxherin
e paketave pip i cili mund të jetë ose i aksesueshëm duke ekzekutuar `pip` ose `pip3`.

Ju mund të kontrolloni versionin tuaj të Python duke ekzekutuar në terminal:

```bash
python --version
```

Vini re se në këtë depo sa herë që shihni `python` do të supozohet se është Python **3**.

**Përgatit hapësirën virtuale për paketat, në direktorinë e depos**

Kjo do krijojë një foldër `venv` i cili do përmbajë paketat e instaluara nga kjo depo

```bash
# Siguroju që gjendesh në direktorinë e depos
# krijojmë hapsirën virtual në direktorinë venv
python3 -m venv venv

# aktivizoni këtë hapsirë virtuale (linux/macos)
source venv/bin/activate

# për ta caktivizuar
deactivate
```

Në bazë të sistemit komanda mund të ndryshojë. Lexo më tepër tek [venv](https://docs.python.org/3/library/venv.html).

**Instalojmë paketat e varura**

Instaloni të gjitha varësitë që kërkohen për projektin duke ekzekutuar:

```bash
pip install -r requirements.txt
```

## Testimi kodit

Për të testuar kodin ekzekuto komandën më poshtë për një skript specifik:

```bash
python ./src/vendodhja/test_file.py
```

> Shënim: Kjo mund të shfaqi `AssertionError` nëse një linjë kodi nuk kalon testin pohues (shembull: `assert True` nuk duhet të shfaqi asgjë)

## Përkufizime

- Depo - Depoja e kodit burim, ndryshe quajtur _Repository_
- Python - I referohet gjuhës _Piton_ por e thënë në Anglisht
- Pohim - Formulimi i një pohimi duke përdorur deklaratën `assert` - shikoni shpembuj nga përmbajtja


---

> Ky kod është kopjuar dhe ripërpunuar nga një depo e vjeter [@trekhleb/learn-python](https://github.com/trekhleb/learn-python)

Autori: [Ardit Hyka](https://ardit.bio.link)
