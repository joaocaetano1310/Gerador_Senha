# Gerador de senha

import random
import string

def gerar_senha(tamanho: int) -> str:
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    senha = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(numeros),
        random.choice(simbolos),
    ]

    todos = letras_minusculas + letras_maiusculas + numeros + simbolos

    for i in range(tamanho - 4):
        senha.append(random.choice(todos))

    random.shuffle(senha)
    return "".join(senha)

print(" ")
print("GERADOR DE SENHA SEGURA ")
print(" ")

while True:
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))

        if tamanho < 4:
            print("❌ O tamanho precisa ser 4 ou mais. Tente novamente ❌")
            continue

        break

    except ValueError:
        print("❌ Digite um número inteiro válido (ex: 8, 12, 16) ❌")

senha_final = gerar_senha(tamanho)
print("✅ Senha gerada: ", senha_final)