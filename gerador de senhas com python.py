import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Gerador de Senhas Aleatórias")
    
    # Coleta de dados do usuário
    num_senhas = int(input("Quantas senhas você deseja gerar? "))
    tamanho_senha = int(input("Qual o comprimento de cada senha? "))

    # Geração e exibição das senhas
    senhas = [gerar_senha(tamanho_senha) for _ in range(num_senhas)]

    print("\nSenhas Geradas:")
    for i, senha in enumerate(senhas, 1):
        print(f"Senha {i}: {senha}")

if __name__ == "__main__":
    main()
