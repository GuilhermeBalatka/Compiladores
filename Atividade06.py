def tabela_de_simbolos_avancada():
    tabela = {}

    def adicionar_simbolo(simbolo, atributos=None):
        if atributos is None:
            atributos = {}
        tabela[simbolo] = atributos

    def buscar_simbolo(simbolo):
        return tabela.get(simbolo)

    def associar_atributos(simbolo, novos_atributos):
        if simbolo in tabela:
            tabela[simbolo].update(novos_atributos)
        else:
            print(f"Símbolo '{simbolo}' não encontrado.")

    def exibir_tabela_ordenada():
        for simbolo in sorted(tabela):
            print(f"{simbolo}: {tabela[simbolo]}")

    return adicionar_simbolo, buscar_simbolo, associar_atributos, exibir_tabela_ordenada

def menu_tabela_simbolos():
    adicionar, buscar, associar, exibir = tabela_de_simbolos_avancada()

    while True:
        print("\n--- Tabela de Símbolos ---")
        print("1. Adicionar símbolo")
        print("2. Buscar símbolo")
        print("3. Associar atributos a símbolo")
        print("4. Exibir tabela ordenada")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do símbolo: ")
            atributos_str = input("Atributos (ex: tipo=int, escopo=global): ")
            atributos = dict(item.split("=") for item in atributos_str.split(",") if "=" in item)
            adicionar(nome, atributos)
        elif opcao == "2":
            nome = input("Nome do símbolo: ")
            resultado = buscar(nome)
            if resultado:
                print(f"{nome}: {resultado}")
            else:
                print("Símbolo não encontrado.")
        elif opcao == "3":
            nome = input("Nome do símbolo: ")
            novos_atrs = input("Novos atributos (ex: tipo=char, linha=12): ")
            atributos = dict(item.split("=") for item in novos_atrs.split(",") if "=" in item)
            associar(nome, atributos)
        elif opcao == "4":
            exibir()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_tabela_simbolos()
