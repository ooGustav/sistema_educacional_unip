import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)

def mostrar_estatisticas(usuario):
    print(Fore.CYAN + "\n--- Estatísticas do Usuário ---" + Style.RESET_ALL)
    progresso = usuario.get('progresso', {})
    for area, valor in progresso.items():
        print(Fore.YELLOW + f"{area.capitalize()}: {valor}% concluído")

    df = pd.DataFrame(list(progresso.items()), columns=['Área', 'Progresso'])

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico de barras
    df.plot(kind='bar', x='Área', y='Progresso', legend=False, ylim=(0, 100),
            color='skyblue', ax=axes[0])
    axes[0].set_title(f"Progresso de {usuario['nome']} (Barras)")
    axes[0].set_xlabel('Área de Conhecimento')
    axes[0].set_ylabel('Progresso (%)')

    # Gráfico de pizza
    axes[1].pie(df['Progresso'], labels=df['Área'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    axes[1].set_title("Distribuição (%) por Área")

    plt.tight_layout()
    plt.show()