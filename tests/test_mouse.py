"""Tests for the .mouse submodule."""
import pytest
from pytest_mock import MockerFixture

from batmouse.mouse import Mouse
from batmouse.power_supply import ChargingStatus


def test_mouse_model(mocker: MockerFixture) -> None:
    """Test the Mouse model property."""

    power_supply = mocker.Mock()

    mouse = Mouse(power_supply, 'Model', lambda x: x)

    assert mouse.model == 'Model'


def test_mouse_status(mocker: MockerFixture) -> None:
    """Test the Mouse voltage property."""

    power_supply = mocker.Mock()
    status = mocker.PropertyMock(
        side_effect=[
            ChargingStatus.DISCHARGING,
            ChargingStatus.CHARGING,
            ChargingStatus.CHARGED,
        ]
    )
    type(power_supply).status = status

    mouse = Mouse(power_supply, '', lambda x: x)

    assert mouse.status == ChargingStatus.DISCHARGING
    assert mouse.status == ChargingStatus.CHARGING
    assert mouse.status == ChargingStatus.CHARGED


def test_mouse_voltage(mocker: MockerFixture) -> None:
    """Test the Mouse voltage property."""

    power_supply = mocker.Mock()
    voltage = mocker.PropertyMock(side_effect=[1.0, 0.75, 0.5, 0.25, 0.0])
    type(power_supply).voltage = voltage

    mouse = Mouse(power_supply, '', lambda x: x)

    assert mouse.voltage == pytest.approx(1.0)
    assert mouse.voltage == pytest.approx(0.75)
    assert mouse.voltage == pytest.approx(0.50)
    assert mouse.voltage == pytest.approx(0.25)
    assert mouse.voltage == pytest.approx(0.0)


def test_mouse_percentage(mocker: MockerFixture) -> None:
    """Test the Mouse percentage property."""

    power_supply = mocker.Mock()
    voltage = mocker.PropertyMock(side_effect=[1.0, 0.75, 0.5, 0.25, 0.0])
    type(power_supply).voltage = voltage

    mouse = Mouse(power_supply, '', lambda x: x * 100)

    assert mouse.percentage == pytest.approx(100.0)
    assert mouse.percentage == pytest.approx(75.0)
    assert mouse.percentage == pytest.approx(50.0)
    assert mouse.percentage == pytest.approx(25.0)
    assert mouse.percentage == pytest.approx(0.0)
