import json
import os

try:
    import pwinput
    def pedir_senha(prompt="Senha: "):
        return pwinput.pwinput(prompt=prompt, mask="*")
except ImportError:
    import getpass
    def pedir_senha(prompt="Senha: "):
        return getpass.getpass(prompt)

from colorama import init, Fore, Style
init(autoreset=True)

from seguranca import hash_senha, verificar_senha
from util import carregar_dados, salvar_dados, menu_principal

ARQUIVO_USUARIOS = 'users.json'

if not os.path.exists(ARQUIVO_USUARIOS):
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump([], f)

def cadastrar_usuario():
    print(Fore.CYAN + "\n" + "-" * 10 + " CADASTRO DE USUÁRIO " + "-" * 10)
    nome = input("Nome completo: ")
    email = input("Email: ")
    senha = pedir_senha("Senha: ")
    senha_hash = hash_senha(senha)

    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    if any(u['email'] == email for u in usuarios):
        print(Fore.RED + "Este e-mail já está cadastrado.")
        return

    novo_usuario = {
        'nome': nome,
        'email': email,
        'senha': senha_hash,
        'progresso': {'logica': 0, 'python': 0, 'seguranca': 0}
    }
    usuarios.append(novo_usuario)
    salvar_dados(ARQUIVO_USUARIOS, usuarios)
    print(Fore.GREEN + "Usuário cadastrado com sucesso!")

def login():
    print(Fore.CYAN + "\n" + "-" * 13 + " LOGIN " + "-" * 13)
    email = input("Email: ")
    senha = pedir_senha("Senha: ")

    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    for u in usuarios:
        if u['email'] == email and verificar_senha(senha, u['senha']):
            print(Fore.GREEN + f"Bem-vindo, {u['nome']}!")
            menu_principal(u, usuarios)
            return
    print(Fore.RED + "Email ou senha incorretos.")

def iniciar():
    while True:
        print(Fore.YELLOW + "\n" + "=" * 40)
        print(Fore.YELLOW + "    PLATAFORMA DE EDUCAÇÃO DIGITAL")
        print(Fore.YELLOW + "=" * 40 + Style.RESET_ALL)
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print(Fore.RED + "Opção inválida.")

if __name__ == "__main__":
    iniciar()