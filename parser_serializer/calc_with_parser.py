import argparse
import math


def arg_parser():
    parser = argparse.ArgumentParser('You must to enter 2 numbers and a mathematical operation for them. '
                                     'example: 2 + 2')
    parser.add_argument('num_1', type=float, help='first num')
    parser.add_argument('action', choices=['+', '-', '*', '/'], help='action for num')
    parser.add_argument('num_2', type=float, help='second num')
    parser.add_argument('--int', action='store_true', help='round to whole number')

    return parser.parse_args()


def calc():
    args = arg_parser()
    print(args)
    res = None
    match args.action:
        case '+':
            res = args.num_1 + args.num_2
        case '-':
            res = args.num_1 - args.num_2
        case '*':
            res = args.num_1 * args.num_2
        case '/':
            if args.num_2 != 0:
                res = args.num_1 / args.num_2
            else:
                print('Division by 0 is not possible')
    if args.int:
        res = math.ceil(res)
    print(res)


if __name__ == "__main__":
    calc()
