import pytest

from flight_calculator import calculate_flight_time


def test_zero_weight_returns_maximum_flight_time():
    assert calculate_flight_time(0) == 180


def test_typical_weight_reduces_flight_time():
    assert calculate_flight_time(500) == 130


def test_decimal_weight_returns_calculated_flight_time():
    assert calculate_flight_time(125.5) == pytest.approx(167.45)


def test_weight_at_zero_flight_time_boundary_returns_zero():
    assert calculate_flight_time(1800) == 0


def test_weight_above_boundary_is_capped_at_zero():
    assert calculate_flight_time(2000) == 0


def test_negative_weight_raises_value_error():
    with pytest.raises(
        ValueError,
        match="Weight cannot be negative.",
    ):
        calculate_flight_time(-1)