import pytest
import app


def test_sumar():
    assert app.sumar(2, 3) == 5


def test_restar():
    assert app.restar(5, 2) == 3


def test_multiplicar():
    assert app.multiplicar(3, 4) == 12


def test_dividir():
    assert app.dividir(8, 2) == 4


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        app.dividir(1, 0)


def test_potencia():
    assert app.potencia(2, 3) == 8


def test_es_par():
    assert app.es_par(4) is True
    assert app.es_par(3) is False


def test_main_prints(capsys):
    app.main()
    captured = capsys.readouterr()
    assert "Calculadora demo" in captured.out
"""
Tests para la aplicación de calculadora
"""
import pytest
from app import sumar, restar, multiplicar, dividir, potencia, es_par


def test_sumar():
    """Test de suma"""
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0


def test_restar():
    """Test de resta"""
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5
    assert restar(10, 10) == 0


def test_multiplicar():
    """Test de multiplicación"""
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 5) == 0


def test_dividir():
    """Test de división"""
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    assert dividir(7, 2) == 3.5


def test_dividir_por_cero():
    """Test de división por cero"""
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(5, 0)


def test_potencia():
    """Test de potencia"""
    assert potencia(2, 3) == 8
    assert potencia(5, 2) == 25
    assert potencia(10, 0) == 1


def test_es_par():
    """Test de número par"""
    assert es_par(4) is True
    assert es_par(7) is False
    assert es_par(0) is True
    assert es_par(-2) is True


def test_main_prints(capsys):
    """Llamar a main() para cubrir las líneas de impresión"""
    from app import main
    main()
    captured = capsys.readouterr()
    assert "Calculadora Simple" in captured.out
