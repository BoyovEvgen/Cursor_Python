import argparse
import re
import os
from os.path import isfile
from os.path import join as joinpath
import time


def arg_parser():
    parser = argparse.ArgumentParser('Counting the number of words in a given file or file in dir')
    parser.add_argument('-name_file', help='enter name file')
    parser.add_argument('-c', action='store_true', help='number of files in current dir')
    parser.add_argument('-l', '--last', action='store_true', help='last created or modified file')
    parser.add_argument('-d', type=str, help='folder path')
    return parser.parse_args()


def main():
    arg = arg_parser()
    print(arg)
    if arg.name_file:
        calc_word(arg.name_file)
    if arg.c:
        calc_file_in_dir(arg.d or os.getcwdb())
    if arg.last:
        get_last_file(arg.d or os.getcwdb())


def calc_word(file):  ## для тестування використовував файли data.json, data.csv в цьому ж каталозі
    with open(file) as f:
        text = f.read()
    text = re.sub(r'\d', '', text)
    word = re.findall(r'\w+', text)
    print(len(word))


def calc_file_in_dir(path):
    files_path = get_list_of_path_file(path)
    print(len(files_path))


def get_last_file(path):
    files_path = get_list_of_path_file(path)
    min_old = min(time.ctime(os.path.getmtime(file)) for file in files_path)
    print(min_old)


def get_list_of_path_file(path):
    files_path = []
    for i in os.listdir(path):
        path_file = joinpath(path, i)
        if isfile(path_file):
            files_path.append(path_file)
    return files_path


if __name__ == "__main__":
    main()


