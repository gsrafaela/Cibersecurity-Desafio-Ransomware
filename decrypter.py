import os
import pyaes
from getpass import getpass

# Função para obter a chave de maneira mais segura (input do usuário ou variável de ambiente)
def get_decryption_key():
    key = os.getenv('DECRYPTION_KEY')  # Tenta obter a chave de uma variável de ambiente
    if key is None:
        # Se não encontrar na variável de ambiente, pede ao usuário
        key = getpass("Digite a chave de descriptografia: ")
    return key.encode()  # Certifique-se de que a chave esteja no formato byte

# Função para descriptografar um arquivo
def decrypt_file(file_name, decryption_key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Inicializar a criptografia AES no modo CTR com a chave fornecida
        aes = pyaes.AESModeOfOperationCTR(decryption_key)

        # Descriptografar os dados
        decrypted_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.rsplit('.', 1)[0]  # Remover a extensão do arquivo original
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypted_data)

        print(f"Arquivo descriptografado com sucesso! Arquivo salvo como: {new_file_name}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")

# Função principal
def main():
    # Nome do arquivo criptografado
    file_name = "teste.txt.ransomwaretroll"

    # Obter chave de descriptografia
    decryption_key = get_decryption_key()

    # Descriptografar o arquivo
    decrypt_file(file_name, decryption_key)

if __name__ == "__main__":
    main()
