# _*_ coding:utf-8 _*_
# @author Robert Carlos                 #
# email robert.carlos@linuxmail.org     #
# 2019-Dec (CC BY 3.0 BR)               #

import errno
from os import path
from sys import exit


def compare(filename):
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


if __name__ == "__main__":
    hosts1 = compare('file1.txt')
    hosts2 = compare('file2.txt')

    out = [h for h in hosts1 if h not in hosts2]
    print(out)
