from typing import Iterable


def iterate_by(numbers: Iterable[int]) -> None:
    for number in numbers:
        print(number)


iterate_by([1, 2, 3])
iterate_by(range(1_000))
iterate_by("duck")
