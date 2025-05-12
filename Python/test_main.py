import pytest
import example

def test_tambah():
    assert example.tambah(2, 3) == 5

def test_kurang():
    assert example.kurang(5, 3) == 2
