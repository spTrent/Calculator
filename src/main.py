import src.exceptions
import src.functions


def main() -> None:
    while 1:
        stdin = input('Введите выражение RPN (пустая строка для остановки): ')
        if not stdin:
            break
        try:
            src.functions.check_accuracy(stdin)
            s = src.functions.remove_staples(stdin)
            tokens = src.functions.tokenize(s)
            res = src.functions.do_rpn(tokens)
            print(res)
        except src.exceptions.CalculatorError as message:
            print(f'{type(message).__name__}: {message}')


if __name__ == '__main__':
    main()
