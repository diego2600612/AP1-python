def ler_float(mensagem, minimo=0, maximo=10):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Valor fora do intervalo permitido ({minimo} a {maximo}).")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def verificar_aprovacao():
    print("\n=== VERIFICACAO DE APROVACAO ===")

    nota = ler_float("Digite a nota do aluno (0 a 10): ", 0, 10)
    frequencia = ler_float("Digite a frequencia do aluno (0 a 100): ", 0, 100)

    print(f"Nota: {nota} - Frequencia: {frequencia}%")

    if frequencia >= 75 and nota >= 7.0:
        print("RESULTADO: APROVADO - Nota e frequencia suficientes")
    elif frequencia >= 75:
        print(f"RESULTADO: REPROVADO - Frequencia OK, mas nota {nota} abaixo de 7.0")
    else:
        print(f"RESULTADO: REPROVADO - Frequencia {frequencia}% abaixo de 75%")


def classificar_nota():
    print("\n=== CLASSIFICACAO DE NOTA ===")

    nota = ler_float("Digite a nota para classificar (0 a 10): ", 0, 10)
    print(f"Nota: {nota}")

    if nota >= 9.0:
        classificacao = "EXCELENTE"
    elif nota >= 7.0:
        classificacao = "BOM"
    elif nota >= 5.0:
        classificacao = "REGULAR"
    elif nota >= 3.0:
        classificacao = "RUIM"
    else:
        classificacao = "PESSIMO"

    print(f"CLASSIFICACAO: {classificacao}")


def processar_menu():
    print("\n=== PROCESSADOR DE MENU ===")
    print("1 - Listar alunos")
    print("2 - Cadastrar aluno")
    print("3 - Calcular media")
    print("4 - Sair do sistema")

    opcao = input("Digite a opcao desejada: ")

    menu = {
        "1": "OPCAO 1: Listar alunos",
        "2": "OPCAO 2: Cadastrar aluno",
        "3": "OPCAO 3: Calcular media",
        "4": "OPCAO 4: Sair do sistema",
        "sair": "OPCAO 4: Sair do sistema"
    }

    print(menu.get(opcao, f"OPCAO INVALIDA: {opcao}"))


def avaliar_aluno():
    print("\n=== AVALIACAO DO ALUNO ===")

    nome = input("Digite o nome do aluno: ")
    nota = ler_float("Digite a nota do aluno (0 a 10): ", 0, 10)
    faltas = ler_inteiro("Digite o numero de faltas: ", 0)

    print(f"Aluno: {nome} - Nota: {nota} - Faltas: {faltas}")

    if nota >= 9.0:
        print(f"{nome}: ALUNO DESTAQUE - Nota {nota}")
    elif nota >= 7.0 and faltas <= 10:
        print(f"{nome}: APROVADO - Nota {nota}, Faltas {faltas}")
    elif nota >= 5.0 and faltas <= 10:
        print(f"{nome}: EM RECUPERACAO - Nota {nota}, Faltas {faltas}")
    else:
        print(f"{nome}: REPROVADO - Nota {nota}, Faltas {faltas}")


def verificar_multiplos_alunos():
    print("\n=== VERIFICAR MULTIPLOS ALUNOS ===")

    while True:
        verificar_aprovacao()
        continuar = input("\nVerificar outro aluno? (s/n): ").strip().lower()
        if continuar != "s":
            break


def classificar_multiplas_notas():
    print("\n=== CLASSIFICAR MULTIPLAS NOTAS ===")

    while True:
        classificar_nota()
        continuar = input("\nClassificar outra nota? (s/n): ").strip().lower()
        if continuar != "s":
            break


def processar_lista_alunos():
    print("\n=== PROCESSAR LISTA DE ALUNOS ===")

    alunos = []
    while True:
        nome = input("Nome do aluno: ")
        nota = ler_float("Nota (0 a 10): ", 0, 10)
        faltas = ler_inteiro("Faltas: ", 0)

        alunos.append({"nome": nome, "nota": nota, "faltas": faltas})

        continuar = input("Adicionar outro aluno? (s/n): ").strip().lower()
        if continuar != "s":
            break

    if alunos:
        print("\n" + "-" * 30)
        print("RESULTADOS:")
        print("-" * 30)

        for aluno in alunos:
            nota = aluno["nota"]
            faltas = aluno["faltas"]

            if nota >= 9.0:
                status = f"{aluno['nome']}: ALUNO DESTAQUE - Nota {nota}"
            elif nota >= 7.0 and faltas <= 10:
                status = f"{aluno['nome']}: APROVADO - Nota {nota}, Faltas {faltas}"
            elif nota >= 5.0 and faltas <= 10:
                status = f"{aluno['nome']}: EM RECUPERACAO - Nota {nota}, Faltas {faltas}"
            else:
                status = f"{aluno['nome']}: REPROVADO - Nota {nota}, Faltas {faltas}"

            print(status)


def main():
    print("=" * 50)
    print("SISTEMA ESCOLAR SIMPLES")
    print("Demonstracao de estruturas de selecao")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Verificar Aprovacao")
        print("2 - Classificar Nota")
        print("3 - Processar Menu")
        print("4 - Avaliar Aluno")
        print("5 - Sair")

        opcao = input("\nEscolha uma opcao (1-5): ")

        if opcao == "1":
            verificar_aprovacao()
        elif opcao == "2":
            classificar_nota()
        elif opcao == "3":
            processar_menu()
        elif opcao == "4":
            avaliar_aluno()
        elif opcao == "5":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        input("\nPressione Enter para continuar...")


def menu_avancado():
    print("=" * 50)
    print("SISTEMA ESCOLAR - MENU AVANCADO")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("OPCOES:")
        print("-" * 50)
        print("1 - Verificar Aprovacao")
        print("2 - Classificar Nota")
        print("3 - Processar Menu")
        print("4 - Avaliar Aluno")
        print("5 - Verificar Multiplos Alunos")
        print("6 - Classificar Multiplas Notas")
        print("7 - Processar Lista de Alunos")
        print("8 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            verificar_aprovacao()
        elif opcao == "2":
            classificar_nota()
        elif opcao == "3":
            processar_menu()
        elif opcao == "4":
            avaliar_aluno()
        elif opcao == "5":
            verificar_multiplos_alunos()
        elif opcao == "6":
            classificar_multiplas_notas()
        elif opcao == "7":
            processar_lista_alunos()
        elif opcao in ("8", "sair"):
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        if opcao != "8":
            input("\nPressione Enter para continuar...")


def testar_rapido():
    print("\n=== TESTE RAPIDO ===")
    print("1 - Testar Aprovacao")
    print("2 - Testar Classificacao")
    print("3 - Testar Match Case")
    print("4 - Testar Guarda")

    opcao = input("Escolha um teste (1-4): ")

    if opcao == "1":
        verificar_aprovacao()
    elif opcao == "2":
        classificar_nota()
    elif opcao == "3":
        processar_menu()
    elif opcao == "4":
        avaliar_aluno()
    else:
        print("Opcao invalida!")


if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA ESCOLAR - VERSOES DISPONIVEIS")
    print("=" * 50)
    print("1 - Menu Interativo")
    print("2 - Menu Avancado")
    print("3 - Teste Rapido")
    print("4 - Sair")

    versao = input("\nEscolha uma versao (1-4): ")

    if versao == "1":
        main()
    elif versao == "2":
        menu_avancado()
    elif versao == "3":
        testar_rapido()
    elif versao == "4":
        print("Saindo...")
    else:
        print("Opcao invalida!")