from typing import Callable


def zero(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 0
    if not operator:
        return int_number
    return operator(int_number)


def one(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 1
    if not operator:
        return int_number
    return operator(int_number)


def two(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 2
    if not operator:
        return int_number
    return operator(int_number)


def three(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 3
    if not operator:
        return int_number
    return operator(int_number)


def four(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 4
    if not operator:
        return int_number
    return operator(int_number)


def five(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 5
    if not operator:
        return int_number
    return operator(int_number)


def six(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 6
    if not operator:
        return int_number
    return operator(int_number)


def seven(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 7
    if not operator:
        return int_number
    return operator(int_number)


def eight(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 8
    if not operator:
        return int_number
    return operator(int_number)


def nine(operator: Callable[[int], int] | None = None) -> int:
    int_number: int = 9
    if not operator:
        return int_number
    return operator(int_number)


def plus(numeric_function: int) -> Callable[[int], int]:
    def operator(first_num):
        return first_num + numeric_function

    return operator


def minus(numeric_function: int) -> Callable[[int], int]:
    def operator(first_num):
        return first_num - numeric_function

    return operator


def times(numeric_function: int) -> Callable[[int], int]:
    def operator(first_num):
        return first_num * numeric_function

    return operator


def divided_by(numeric_function: int) -> Callable[[int], int]:
    def operator(first_num):
        return first_num / numeric_function

    return operator


if __name__ == '__main__':
    res = four(times(five()))
    assert res == 20, f'expected {20}, result: {res}'

    res = one(plus(eight()))
    assert res == 9, f'expected {9}, result: {res}'

    res = seven(minus(three()))
    assert res == 4, f'expected {4}, result: {res}'

    res = nine(divided_by(three()))
    assert res == 3, f'expected {3}, result: {res}'
