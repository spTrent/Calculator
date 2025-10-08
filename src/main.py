import exceptions
import functions


def main() -> None:
    while 1:
        stdin = input('Введите выражение RPN (пустая строка для остановки): ')
        if not stdin:
            break
        try:
            functions.check_accuracy(stdin)
            s = functions.remove_staples(stdin)
            tokens = functions.tokenize(s)
            res = functions.do_rpn(tokens)
            print(res)
        except exceptions.CalculatorError as message:
            print(f'{type(message).__name__}: {message}')


if __name__ == '__main__':
    main()
