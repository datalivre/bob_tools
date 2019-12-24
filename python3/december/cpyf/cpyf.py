import argparse
import errno
from random import randint
from sys import exit

import numpy as np


def get_distrito(distrito):
    return {
        "rio grande do sul": 0, "distrito federal": 1,
        "goiás": 1, "mato grosso do sul": 1,
        "tocantins": 1, "pará": 2, "amazonas": 2,
        "acre": 2, "amapá": 2, "rondônia": 2,
        "roraima": 2, "ceará": 3, "maranhão": 3,
        "piauí": 3, "pernambuco": 4,
        "rio grande do norte": 4, "paraíba": 4,
        "alagoas": 4, "bahia": 5, "sergipe": 5,
        "minas gerais": 6, "rio de janeiro": 7,
        "espírito santo": 7, "são paulo": 8,
        "paraná": 9, "santa catarina": 9
    }.get(distrito)


def rand_cpf(f_get_distrito, distrito, cpf):
    if cpf is not None:
        try:
            return list([int(n) for n in cpf])[:-2]
        except ValueError:
            print("Certifique-se de ter inserido um número válido.")
            exit(errno.EPERM)
    else:
        cpf = [randint(0, 9) for _ in range(0, 9)]
        if distrito is not None:
            cpf.pop(-1)
            cpf.append((f_get_distrito(distrito.lower())))
        return cpf


def cpyf(f_get_distrito, f_rand_cpf, distrito, cpfin):
    cpf = f_rand_cpf(f_get_distrito, distrito, cpfin)
    try:
        for peso in [10, 9, 8, 7, 6, 5, 4, 3, 2], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]:
            resto = sum(np.multiply(cpf, peso)) % 11
            cpf.append(0 if resto < 2 else 11 - resto)
        if cpfin is not None:
            return (''.join(str(n) for n in cpf) == cpfin)
        return cpf
    except TypeError:
        print("Certifique-se de ter inserido um número válido.")
        exit(errno.EPERM)
    except ValueError:
        print("Certifique-se de ter inserido um número válido.")
        exit(errno.EPERM)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Gerador e validador de CPF com a possibilidade de escolha de estado.")
    parser.add_argument("-d", action="store", dest="dist", required=False,
                        default=None, help="insira o nome de um estado brasileiro.")
    parser.add_argument("-c", action="store", dest="cpf", required=False,
                        default=None, help="insira um cpf para ser verificado.")
    args = parser.parse_args()

    print(cpyf(get_distrito, rand_cpf, args.dist, args.cpf))
