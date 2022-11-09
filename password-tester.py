from tqdm import tqdm

import argparse
import itertools
import random
import string
import time

characters = ""


def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, required=True)
    parser.add_argument('--num', type=int, required=True)
    parser.add_argument('--upper', type=int, required=True)
    parser.add_argument('--lower', type=int, required=True)
    parser.add_argument('--char', type=int, required=True)
    args = parser.parse_args()

    num = args.num == 1
    upper = args.upper == 1
    lower = args.lower == 1
    char = args.char == 1
    global characters

    if num:
        characters += string.digits
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if char:
        characters += string.punctuation
    return args.size, num, upper, lower, char


def ensure_policies(num, upper, lower, char):
    password = ""
    if num:
        n = random.choice(string.digits)
        password += n
    if lower:
        l = random.choice(string.ascii_lowercase)
        password += l
    if upper:
        u = random.choice(string.ascii_uppercase)
        password += u
    if char:
        c = random.choice(string.punctuation)
        password += c

    return password


def generate_password(size, num, upper, lower, char):
    # Aqui irá garantir que cada política de senha definida seja implementada
    password = ensure_policies(num, upper, lower, char)

    # Por fim garante que a senha terá o tamanho definido preenchendo com qualquer um dos caracteres que se encaixe na política
    while (len(password) < size):
        password = random.choice(characters) + password

    return password


def brute_force(password):
    # Estima quanto tempo irá levar para descobrir a senha de acordo com a quantidade de caracteres e o índice do primeiro caracter da senha
    estimated_time = int((characters.index(
        password[0]) / len(characters)) * (len(characters) ** len(password)))

    # Transforma em uma tupla porque é o formato de retorno da iteração
    password_tuple = tuple(password)

    # Transforma a string em um array de char
    char_list = [[x for x in characters]] * len(password)

    for combination in tqdm(itertools.product(*char_list), total=estimated_time):
        if combination == password_tuple:
            return combination


if __name__ == "__main__":
    # leitura dos parâmetros passados por argumentos
    size, num, upper, lower, char = read_arguments()

    # geração da senha com as políticas definidas
    password = generate_password(size, num, upper, lower, char)

    # Chamada do algoritmo brute_force para vermos em quanto tempo a senha é descoberta
    print(f"Tentativa de quebrar a senha: {password}")
    start_time = int(time.time())
    result = brute_force(password)
    endTime = int(time.time())
    print(f"Senha identificada {result} em {endTime - start_time}s")
