# _*_ coding:utf-8 _*_
# @author Robert Carlos                 #
# email robert.carlos@linuxmail.org     #
# 2019-Dec (CC BY 3.0 BR)               #

import argparse
import errno
from os import path
from sys import exit


def get_file(filename):
    if path.isfile(filename):
        host_file = []
        try:
            with open(filename, 'r', encoding='utf8') as f:
                host_file = [line.strip() for line in f if '#' not in line]
            return host_file
        except Exception as e:
            print(e)
            exit(errno.EPERM)
    else:
        print(f'File "{filename}" not found')
        exit(errno.EPERM)


def compyre(func_get_file, file_1, file_2):
    list_file_1 = func_get_file(file_1)
    list_file_2 = func_get_file(file_2)
    return [f for f in list_file_1 if f not in list_file_2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Compara dois arquivos linha a linha e retorna a diferença.')
    parser.add_argument('-f1', action='store', dest='file1',
                        default='file1', required=False,
                        help='first file name.')
    parser.add_argument('-f2', action='store', dest='file2',
                        default='file2', required=False,
                        help='second file name.')
    args = parser.parse_args()

    print(compyre(get_file, args.file1, args.file2))
