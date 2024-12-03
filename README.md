# Cibersecurity Desafio Ransomware

## Descrição

Este projeto simula a criptografia e descriptografia de arquivos usando o algoritmo **AES** (Advanced Encryption Standard) no modo **CTR** (Counter), uma técnica comum utilizada em ataques de **ransomware**. O objetivo é demonstrar como um arquivo pode ser criptografado e depois descriptografado, simulando um cenário de ataque ransomware.

Este repositório contém dois scripts:
1. **Criptografia**: Criptografa um arquivo de texto com uma chave fornecida.
2. **Descriptografia**: Descriptografa um arquivo criptografado utilizando a mesma chave.

## Funcionalidade

1. **Criptografia**:
    - Um arquivo de texto (`teste.txt`) será criptografado usando a chave fornecida.
    - O arquivo criptografado será salvo com a extensão `.ransomwaretroll`.
    - O arquivo original será removido após a criptografia.

2. **Descriptografia**:
    - O arquivo criptografado (`teste.txt.ransomwaretroll`) será restaurado ao seu estado original.
    - O arquivo descriptografado será salvo com o nome original (`teste.txt`).

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. O código depende da biblioteca `pyaes`, que pode ser instalada com o seguinte comando:

```bash
pip install pyaes
