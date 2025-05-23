
import json
from colorama import Fore, Style
from estatisticas import mostrar_estatisticas

def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def mostrar_conteudo(caminho_arquivo, usuario, area, todos_usuarios):
    print(Fore.CYAN + "\n" + "-" * 10 + f" CONTEÚDO: {area.upper()} " + "-" * 10 + Style.RESET_ALL)
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(conteudo)
            progresso_atual = usuario['progresso'][area]
            if progresso_atual < 100:
                usuario['progresso'][area] = min(100, progresso_atual + 20)
                salvar_dados('users.json', todos_usuarios)
                print(Fore.GREEN + f"Você completou {usuario['progresso'][area]}% deste conteúdo.")
            else:
                print(Fore.YELLOW + "Você já completou 100% deste conteúdo.")
    except FileNotFoundError:
        print(Fore.RED + "Conteúdo não encontrado.")

def menu_principal(usuario, todos_usuarios):
    from main import pedir_senha
    from seguranca import verificar_senha
    from util import salvar_dados

    while True:
        print(Fore.YELLOW + "\n" + "=" * 30)
        print(Fore.YELLOW + "       MENU PRINCIPAL")
        print(Fore.YELLOW + "=" * 30 + Style.RESET_ALL)
        print("1. Acessar conteúdo de Lógica Computacional")
        print("2. Acessar conteúdo de Python Básico")
        print("3. Acessar conteúdo de Segurança Digital")
        print("4. Ver estatísticas")
        print("5. Ver Diretrizes de Privacidade (LGPD)")
        print("6. Sair")
        print("7. Excluir conta")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_conteudo("conteudos/logica.txt", usuario, 'logica', todos_usuarios)
        elif opcao == '2':
            mostrar_conteudo("conteudos/python.txt", usuario, 'python', todos_usuarios)
        elif opcao == '3':
            mostrar_conteudo("conteudos/seguranca.txt", usuario, 'seguranca', todos_usuarios)
        elif opcao == '4':
            mostrar_estatisticas(usuario)
        elif opcao == '5':
            try:
                with open("diretrizes.txt", "r", encoding="utf-8") as f:
                    print(Fore.CYAN + "\n--- DIRETRIZES DE PRIVACIDADE ---\n" + Style.RESET_ALL)
                    print(f.read())
            except FileNotFoundError:
                print(Fore.RED + "Arquivo 'diretrizes.txt' não encontrado.")
        elif opcao == '6':
            print("Voltando ao menu inicial...")
            break
        elif opcao == '7':
            confirmar = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
            if confirmar == 's':
                senha = pedir_senha("Confirme sua senha: ")
                if verificar_senha(senha, usuario['senha']):
                    todos_usuarios.remove(usuario)
                    salvar_dados('users.json', todos_usuarios)
                    print(Fore.GREEN + "Conta excluída com sucesso.")
                    break
                else:
                    print(Fore.RED + "Senha incorreta. Conta não excluída.")
        else:
            print(Fore.RED + "Opção inválida.")