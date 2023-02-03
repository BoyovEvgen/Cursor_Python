import sys
import json
from argparse import ArgumentParser
from signers import Signer


def args_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Very strong decoder.")
    parser.add_argument(
        "--secret", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--salt", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--using",
        choices=["pyjwt", "itsdangerous"],
        required=True,
        help="Package to encode / decode.",
    )
    parser.add_argument("--action", choices=["encode", "decode"], required=True)
    parser.add_argument(
        "--input_file", type=str, required=True, help="Input filename *.json"
    )
    parser.add_argument(
        "--output_file", type=str, required=True, help="Output filename *.json"
    )
    return parser


if __name__ == "__main__":

    parser = args_parser()
    namespace = parser.parse_args(sys.argv[1:])
    sign = Signer(secret=namespace.secret, salt=namespace.salt)

    def load_data_from_file():
        """
        Функція зчитує та повертає дані з файлу, який був вказаний аргументом при викликанні программи.
        :return:
        """
        with open(file=namespace.input_file) as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                raise "invalid input data..."

    def choice_of_coding_method():
        """
        Функція повертає метод для кодування/декодування.
        Виявляє цей метод з аргуметів, які вказуються при викликанні програми.
        :return:
        """
        if namespace.action == "encode":
            return sign.jwt_encode if namespace.using == "pyjwt" else sign.itsdangerous_encode
        else:
            return sign.jwt_decode if namespace.using == "pyjwt" else sign.itsdangerous_decode

    def write_data_in_file(data_for_file):
        with open(file=namespace.output_file, mode="w") as f:
            f.write(json.dumps(data_for_file, indent=4))

    coding_method = choice_of_coding_method()
    data = load_data_from_file()
    result = [coding_method(line) for line in data]
    write_data_in_file(result)
