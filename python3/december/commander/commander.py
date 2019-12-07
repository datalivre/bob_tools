# _*_ coding:utf-8 _*_
# @author Robert Carlos                 #
# email robert.carlos@linuxmail.org     #
# 2019-Dec (CC BY 3.0 BR)               #

import argparse
import errno
import subprocess
from os import path
from sys import argv, exit


def get_file(filename):
    if path.isfile(filename):
        file_list = []
        try:
            with open(filename, 'r', encoding='utf8') as f:
                file_list = [line.lower().strip()
                             for line in f if '#' not in line]
            return file_list
        except Exception as e:
            print(e)
            exit(errno.EPERM)
    else:
        print(f'File "{filename}" not found')
        exit(errno.EPERM)


def commander(command_file, func_get_file):
    if len(argv) < 2:
        command_list = func_get_file(command_file)
    else:
        command_list = [cmd.strip() for cmd in argv[2].split(",")]
    for cmd in command_list:
        print("comm@nder: ", cmd, "\n----------")
        try:
            output = subprocess.check_output(cmd, shell=True)
            print(output.decode("utf-8"))
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Executa um ou mais comandos no host local.")
    parser.add_argument("-c", action="store", dest="cmd",
                        default="confile", required=False,
                        help="insira um ou mais comandos separados por vírgula entre aspas.")
    args = parser.parse_args()
    commander(args.cmd, get_file)
