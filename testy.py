from funkcje import *


def test_1():
    assert ile_osob(2,5,2) == 20
    assert ile_osob(1,0,0) == 0
    assert ile_osob(1,'kot',1) == 'none'
    assert ile_osob(1,1.5,1) == 1.5


def test_2():
    assert ile_ze_srodkami(50,"T") == 55
    assert ile_ze_srodkami(50,'N') == 25

