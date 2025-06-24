def converter_para_decimal(numero_str, base_origem):
    try:
        return int(numero_str, base_origem)
    except ValueError:
        print("Erro: número inválido para a base fornecida.")
        return None

def converter_da_decimal(valor, base_destino):
    if base_destino == 2:
        return bin(valor)[2:]
    elif base_destino == 8:
        return oct(valor)[2:]
    elif base_destino == 10:
        return str(valor)
    elif base_destino == 16:
        return hex(valor)[2:].upper()
    else:
        print("Base de destino inválida.")
        return None

def formatar_numero(numero_str, digitos, sinal_antes=True, negativo=False):
    numero_str = numero_str.zfill(digitos)
    if negativo:
        return f"-{numero_str}" if sinal_antes else f"{numero_str}-"
    return numero_str

def exibir_menu():
    print("\n=== Conversor de Bases ===")
    print("1 - Converter número")
    print("2 - Mostrar resultados armazenados")
    print("0 - Sair")

def main():
    memoria = {}
    contador = 1

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_str = input("Digite o número: ").strip()
            base_origem = int(input("Base de origem (2, 8, 10, 16): "))
            decimal = converter_para_decimal(numero_str, base_origem)

            if decimal is not None:
                base_destino = int(input("Base de destino (2, 8, 10, 16): "))
                digitos = int(input("Mínimo de dígitos a exibir: "))
                sinal_posicao = input("Sinal antes ou depois? (a/d): ").lower()

                negativo = decimal < 0
                convertido = converter_da_decimal(abs(decimal), base_destino)
                final = formatar_numero(convertido, digitos, sinal_antes=(sinal_posicao == 'a'), negativo=negativo)

                memoria[f"Conv{contador}"] = {
                    "original": numero_str,
                    "base_origem": base_origem,
                    "decimal": decimal,
                    "base_destino": base_destino,
                    "resultado": final
                }

                print(f"\nResultado da conversão: {final}")
                contador += 1

        elif opcao == "2":
            print("\n--- Resultados Armazenados ---")
            if not memoria:
                print("Nenhum resultado armazenado.")
            for chave, dados in memoria.items():
                print(f"{chave}: {dados['original']} (base {dados['base_origem']}) → {dados['resultado']} (base {dados['base_destino']})")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
