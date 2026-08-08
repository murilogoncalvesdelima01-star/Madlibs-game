#MADLIB GAME
from historias import historias
from salvar import salvar_historias, carregar_historias
import time
import textwrap

qualhist=0
opcao = 0  

while opcao == 0:
    print("""
    \033[1;36m╔════════════════════════════════════════╗
    ║                                        ║
    ║      \033[1;33m✦ M A D   L I B S   G A M E ✦\033[1;36m     ║
    ║      \033[0;35m~ escreva histórias malucas ~\033[1;36m     ║
    ║                                        ║
    ╠════════════════════════════════════════╣
    ║                                        ║
    ║  \033[1;32m[1]\033[1;36m 🎮 Jogar                          ║
    ║  \033[1;32m[2]\033[1;36m 📚 Escolher história              ║
    ║  \033[1;32m[3]\033[1;36m 💾 Histórias salvas               ║
    ║  \033[1;32m[4]\033[1;36m ❓ Como jogar                     ║
    ║  \033[1;31m[5]\033[1;36m 🚪 Sair                           ║
    ║                                        ║
    ╚════════════════════════════════════════╝\033[0m
    """)
    entrada = input("\033[1;33m  Escolha uma opção >>> \033[0m")
    if entrada.isdigit():
        opcao = int(entrada)
    else:
        opcao = 0
    print("\033c", end="")

    if opcao == 1 and qualhist==0:
        print("\033[1;31m" + "="*44)
        print("   ⚠️  ERRO: ESCOLHA UMA HISTÓRIA ANTES DE JOGAR!")
        print("="*44 + "\033[0m")
        time.sleep(2)
        print("\033c", end="")
        opcao=0
    elif opcao==1:
        resposta = {}
        for palavra in historias[qualhist]["Perguntas"]:
            resposta[palavra] = input(f"\033[1;33m✏️  Digite um(a) {palavra}: \033[0m")

        titulo = historias[qualhist]["titulo"]
        texto = historias[qualhist]["historia"].format(**resposta)

        print("\033[1;35m" + "═"*44)
        print(f"   📖 {titulo.upper()}")
        print("═"*44 + "\033[0m")
        print("\033[0;36m" + textwrap.fill(texto, width=44) + "\033[0m")
        print("\033[1;35m" + "═"*44 + "\033[0m")
        salvar_historias(titulo, texto)
        time.sleep(5)
        opcao=0
        print("\033c", end="")
    elif opcao == 2:
        while True:
            print("\033[1;36m╔════════════════════════════════════════╗")
            print("║        📚 ESCOLHA A HISTÓRIA 📚         ║")
            print("╠════════════════════════════════════════╣")
            for chave, dados in historias.items():
                linha = f"[{chave}] {dados['titulo']}"
                print(f"║ \033[1;32m{linha.ljust(38)}\033[1;36m ║")
            print(f"╚════════════════════════════════════════╝\033[0m")

            qualhist = input("\033[1;33m  Digite o número da história >>> \033[0m")
            if qualhist not in historias:
                print("\033[1;31m⚠️  HISTÓRIA INVÁLIDA!\033[0m")
            else:
                opcao = 0
                print("\033c", end="")
                break
    elif opcao == 3:
        print("\033[1;35m💾 HISTÓRIAS SALVAS\033[0m")
        salvas = carregar_historias()
        if not salvas:
            print("Nenhuma história salva ainda.")
        else:
            for item in salvas:
                print("\033[1;35m" + "═"*44)
                print(f"   📖 {item['titulo'].upper()}")
                print("═"*44 + "\033[0m")
                print("\033[0;36m" + textwrap.fill(item["texto"], width=44) + "\033[0m")
                print()
        input("\033[1;33mPressione Enter para voltar ao menu...\033[0m")
        print("\033c", end="")
        opcao = 0
    elif opcao == 4:
        print("\033[1;35m❓ COMO JOGAR\033[0m")
        print("Escolha uma história no menu [2] e depois jogue no menu [1].")
        print("Digite as palavras pedidas e veja sua história maluca!")
        time.sleep(5)
        print("\033c", end="")
        opcao = 0
    elif opcao == 5:
        break

