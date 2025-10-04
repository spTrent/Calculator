import functions
from exceptions import CalculatorError


def main() -> None:
    stdin = input('Введите выражение в польской нотации: ')
    if not stdin:
        print('Пустая строка')
    try:
        s = functions.remove_staples(stdin)
        tokens = functions.tokenize(s)
        res = functions.do_rpn(tokens)
        with open('log.txt', 'a') as f:
            f.write(f'\n{stdin} -> {res}')
        print(res)
    except CalculatorError as message:
        with open('log.txt', 'a') as f:
            f.write(f'\n{stdin} -> {type(message).__name__}: {message}')
        print(f'{type(message).__name__}: {message}')


if __name__ == '__main__':
    main()
