import pytest
import os
from manipulacao import Manipulador

@pytest.fixture
def manip():
    return Manipulador()

def test_soma(manip):
    assert manip.soma(3, 4) == 7

def test_invert_string(manip):
    assert manip.invert_string("oi") == "io"

def test_ePar(manip):
    assert manip.ePar(44) == True 

@pytest.mark.parametrize("entrada, saida", [(3, 6), (4, 24), (5, 120)])
def test_fatorial(manip, entrada, saida):
    return manip.fatorial(entrada) == saida

@pytest.fixture
def test_setup_arquivo():
    if os.path.exists("teste.txt"):
        os.remove("teste.txt")
    
    yield

    if os.path.exists("teste.txt"):
        os.remove("teste.txt")
    

def test_criar_arquivo(manip, test_setup_arquivo):
    assert manip.criar_arquivo("teste.txt", "Hello World!")

def test_ler_arquivo(manip, test_setup_arquivo):
    assert manip.criar_arquivo("teste.txt", "Hello World!")
    assert manip.ler_arquivo("teste.txt") == ("Hello World!")