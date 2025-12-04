import pytest
from operaciones import *

#Pruebas unitarias de la funcion "sumar"
def test_sumar1():
    res=sumar([1, 2, 3]) 
    assert res== 6

def test_sumar2():  
    res=sumar([10, 15, 20]) 
    assert res== 45

def test_sumar3():
    res=sumar([]) 
    assert res== 0

#Pruebas unitarias de la funcion "promediar"
def test_promediar1():
    res=promediar([1, 2, 3]) 
    assert res== 2

def test_promediar2():
    res=promediar([10, 15, 25]) 
    assert res== 16.666666666666668

def test_promediar3():
    res=promediar([]) 
    assert res== 0

