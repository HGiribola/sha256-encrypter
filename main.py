import hashlib
import time


def cryptography_hex():
    cript = hashlib.sha256([b''], usedforsecurity=True)
    texto = input(str("Digite o texto a ser criptografado: "))
    time.sleep(1)
    cript.update(texto.encode('utf-8'))
    hash_hex = cript.hexdigest()
    print(f'Texto criptografado em SHA256 representado por hexadecimais: {hash_hex}')


def cryptography_dec():
    cript = hashlib.sha256([b''], usedforsecurity=True)
    texto = input(str("Digite o texto a ser criptografado: "))
    time.sleep(1)
    cript.update(texto.encode('utf-8'))
    hash_dec = cript.digest()
    print(f'Texto criptografado em SHA256 representado por somente decimais: {hash_dec}')


aux = 'Y'
while aux == 'Y':
