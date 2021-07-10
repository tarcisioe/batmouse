"""Tests for the .convert_voltage submodule."""
import pytest

from batmouse.convert_voltage import convert_by_table, convert_logitech_g703


def test_convert_by_table_simple_table() -> None:
    """Test convert_by_table with a simple table that goes from 0.0 V to 1.0 V."""
    simple_table = [x / 100 for x in range(0, 101)]

    assert convert_by_table(simple_table, -1.0) == pytest.approx(0.0)
    assert convert_by_table(simple_table, 0.0) == pytest.approx(0.0)
    assert convert_by_table(simple_table, 0.25) == pytest.approx(25.0)
    assert convert_by_table(simple_table, 0.5) == pytest.approx(50.0)
    assert convert_by_table(simple_table, 0.75) == pytest.approx(75.0)
    assert convert_by_table(simple_table, 1.0) == pytest.approx(100.0)
    assert convert_by_table(simple_table, 1.5) == pytest.approx(100.0)


def test_convert_logitech_g703() -> None:
    """Test convert_logitech_g703 with known values."""
    assert convert_logitech_g703(0.0) == pytest.approx(0.0)
    assert convert_logitech_g703(3.5) == pytest.approx(0.0)
    assert convert_logitech_g703(3.6855) == pytest.approx(12.5)
    assert convert_logitech_g703(3.734) == pytest.approx(25.0)
    assert convert_logitech_g703(3.771) == pytest.approx(37.5)
    assert convert_logitech_g703(3.811) == pytest.approx(50.0)
    assert convert_logitech_g703(3.8735) == pytest.approx(62.5)
    assert convert_logitech_g703(3.955) == pytest.approx(75.0)
    assert convert_logitech_g703(4.047) == pytest.approx(87.5)
    assert convert_logitech_g703(4.186) == pytest.approx(100.0)
    assert convert_logitech_g703(5.0) == pytest.approx(100.0)
