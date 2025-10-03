import functions
from exceptions import CalculatorError


def main() -> None:
    stdin = input("Введите выражение в польской нотации: ")
    if not stdin:
        print("Пустая строка")
    else:
        try:
            tokens = functions.tokenize(stdin)
            res = functions.do_rpn(tokens)
            print(res)
        except CalculatorError as message:
            print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
