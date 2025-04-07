
import re


padroes = {
    "1": {
        "descricao": "Binário Par (termina com 0)",
        "regex": r'^[01]*0$'
    },
    "2": {
        "descricao": "Binário termina com '00'",
        "regex": r'^[01]*00$'
    },
    "3": {
        "descricao": "String entre aspas duplas",
        "regex": r'^"([^"\\]|\\.)*"$'
    },
    "4": {
        "descricao": "Telefone em SC (47, 48, 49)",
        "regex": r'^\(?0?(47|48|49)\)?[-.\s]?[2-9][0-9]{3,4}[-.\s]?[0-9]{4}$'
    },
    "5": {
        "descricao": "Placa de veículo brasileira (Mercosul ou antigo)",
        "regex": r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'
    },
    "6": {
        "descricao": "Email terminando em .br ou .com.br",
        "regex": r'^[\w\.-]+@[\w\.-]+\.(br|com\.br)$'
    },
    "7": {
        "descricao": "Comentário de linha (// ou #)",
        "regex": r'^//.*|^#.*'
    },
    "8": {
        "descricao": "Comentário de múltiplas linhas (/*...*/ ou aspas triplas)",
        "regex": r'^/\*[\s\S]*?\*/$|^\'\'\'[\s\S]*?\'\'\'$|^\"\"\"\"[\s\S]*?\"\"\"\"$'
    }
}


def validar_expressao(codigo, texto):
    if codigo in padroes:
        regex = padroes[codigo]["regex"]
        if re.fullmatch(regex, texto):
            return "Válido!"
        else:
            return "Inválido."
    else:
        return "Opção inválida."


def menu():
    while True:
        print("\nValidador de Expressões Regulares")
        for chave, valor in padroes.items():
            print(f"{chave} - {valor['descricao']}")
        opcao = input("\nEscolha uma opção (ou digite 'sair'): ")

        if opcao.lower() == 'sair':
            print("Encerrando programa.")
            break

        entrada = input("Digite o texto para validar: ")
        resultado = validar_expressao(opcao, entrada)
        print("Resultado:", resultado)

# Executar programa
if __name__ == "__main__":
    menu()
