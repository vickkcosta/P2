Alunas: Clarice Warwar, Julia Cardoso, Sofia Anzai e Maria Vitória Costa. 

def ler_registro(nome_arquivo):
    registro = []
    with open(nome_arquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            linha = linha.strip()
            if i == 0:
                continue
            if linha:
                partes = linha.split(',')
                try:
                    nome = partes[0].strip()
                    numero = int(partes[1].strip())
                    despesa = float(partes[2].strip())
                    receita = float(partes[3].strip())
                    registro.append({
                        'nome': nome,
                        'numero': numero,
                        'despesa': despesa,
                        'receita': receita
                    })
                except ValueError:
                    continue
    return registro

def buscar_parte_nome(registro, parte_nome):
    nomes = set()
    for entrada in registro:
        if parte_nome.lower() in entrada['nome'].lower():
            nomes.add(entrada['nome'])
    for nome in nomes:
        print(nome)

def buscar_nome_completo(registro, nome_completo):
    casos = [entrada['numero'] for entrada in registro if entrada['nome'].lower() == nome_completo.lower()]
    for caso in casos:
        print(caso)

def buscar_numero_caso(registro, numero_caso):
    for entrada in registro:
        if entrada['numero'] == numero_caso:
            nome = entrada['nome']
            despesa = entrada['despesa']
            receita = entrada['receita']
            diferenca = receita - despesa
            print(f"Nome: {nome}, Despesa: {despesa}, Receita: {receita}, Diferença: {diferenca}")
            return

def calcular_despesa_total(registro):
    despesa_total = sum(entrada['despesa'] for entrada in registro)
    print(f"Despesa Total: {despesa_total}")

def calcular_receita_total(registro):
    receita_total = sum(entrada['receita'] for entrada in registro)
    print(f"Receita Total: {receita_total}")

def caso_maior_despesa(registro):
    maior_despesa = max(registro, key=lambda x: x['despesa'])
    print(f"Nome: {maior_despesa['nome']}, Número: {maior_despesa['numero']}, Receita: {maior_despesa['receita']}, Despesa: {maior_despesa['despesa']}")

def caso_maior_receita(registro):
    maior_receita = max(registro, key=lambda x: x['receita'])
    print(f"Nome: {maior_receita['nome']}, Número: {maior_receita['numero']}, Receita: {maior_receita['receita']}, Despesa: {maior_receita['despesa']}")

def salvar_dados_cliente(registro, nome_completo, nome_arquivo):
    casos = [entrada for entrada in registro if entrada['nome'].lower() == nome_completo.lower()]
    if not casos:
        print(f"Cliente {nome_completo} não encontrado.")
        return
    with open(nome_arquivo, 'w') as arquivo:
        total_despesa = total_receita = 0
        for caso in casos:
            arquivo.write(f"Nome: {caso['nome']}, Número: {caso['numero']}, Receita: {caso['receita']}, Despesa: {caso['despesa']}\n")
            total_despesa += caso['despesa']
            total_receita += caso['receita']
        diferenca = total_receita - total_despesa
        arquivo.write(f"Total de Despesas: {total_despesa}\n")
        arquivo.write(f"Total de Receitas: {total_receita}\n")
        arquivo.write(f"Diferença: {diferenca}\n")
    print(f"Dados do cliente {nome_completo} foram salvos em {nome_arquivo}")

def menu():
    registro = ler_registro('registro.txt')
    while True:
        print("\nMenu:")
        print("1. Buscar por parte do nome")
        print("2. Buscar por nome completo")
        print("3. Buscar por número do caso")
        print("4. Calcular despesa total")
        print("5. Calcular receita total")
        print("6. Caso com maior despesa")
        print("7. Caso com maior receita")
        print("8. Salvar dados do cliente")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            parte_nome = input("Digite parte do nome do cliente: ")
            buscar_parte_nome(registro, parte_nome)
        elif opcao == '2':
            nome_completo = input("Digite o nome completo do cliente: ")
            buscar_nome_completo(registro, nome_completo)
        elif opcao == '3':
            numero_caso = int(input("Digite o número do caso: "))
            buscar_numero_caso(registro, numero_caso)
        elif opcao == '4':
            calcular_despesa_total(registro)
        elif opcao == '5':
            calcular_receita_total(registro)
        elif opcao == '6':
            caso_maior_despesa(registro)
        elif opcao == '7':
            caso_maior_receita(registro)
        elif opcao == '8':
            nome_completo = input("Digite o nome completo do cliente: ")
            nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")
            salvar_dados_cliente(registro, nome_completo, nome_arquivo)
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
