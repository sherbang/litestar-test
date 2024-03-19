import pytest

import fizzbuzz


def test_get_fizzbuzz():
    assert fizzbuzz.get_fizzbuzz(1) == "1"
    assert fizzbuzz.get_fizzbuzz(2) == "2"
    assert fizzbuzz.get_fizzbuzz(3) == "Fizz"
    assert fizzbuzz.get_fizzbuzz(5) == "Buzz"
    assert fizzbuzz.get_fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz.get_fizzbuzz(98) == "98"
    assert fizzbuzz.get_fizzbuzz(99) == "Fizz"
    assert fizzbuzz.get_fizzbuzz(100) == "Buzz"


def test_main(capsys: pytest.CaptureFixture[str]):
    fizzbuzz.main()
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")

    assert len(lines) == 100

    assert lines[0] == "1"

    assert lines[-1] == "Buzz"
