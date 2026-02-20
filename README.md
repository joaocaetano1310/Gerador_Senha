# 🔐 Gerador de Senhas Seguras (Python)

Este projeto é um utilitário simples e eficiente para a criação de senhas fortes, garantindo que o usuário tenha combinações aleatórias que seguem boas práticas de segurança.

## 🛠️ Funcionalidades

O script garante que cada senha gerada contenha uma mistura equilibrada de caracteres, incluindo obrigatoriamente:
* **Letras Minúsculas** (a-z)
* **Letras Maiúsculas** (A-Z)
* **Números** (0-9)
* **Símbolos** (caracteres especiais e pontuação)

Além disso, o programa:
* Permite que o usuário escolha o **tamanho total** da senha (mínimo de 4 caracteres).
* Realiza um **embaralhamento (shuffle)** final para que a ordem dos caracteres obrigatórios não seja previsível.
* Possui **tratamento de erros** para garantir que apenas números inteiros válidos sejam aceitos na entrada.

## 🚀 Como executar

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Salve o código em um arquivo chamado `gerador_senha.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python gerador_senha.py
