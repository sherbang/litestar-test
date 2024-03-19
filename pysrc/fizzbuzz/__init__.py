def get_fizzbuzz(i: int) -> str:
    if (i % 3) + (i % 5) == 0:
        return "FizzBuzz"
    if (i % 3) == 0:
        return "Fizz"
    if (i % 5) == 0:
        return "Buzz"
    return str(i)


def main() -> None:
    for i in range(1, 101):
        print(get_fizzbuzz(i))
