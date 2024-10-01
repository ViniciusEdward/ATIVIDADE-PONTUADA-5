import os
os.system("cls || clear")

# Estrutura de dados.
lista_familia = []
lista_salario = []
contador = 0

while True :
    print("""
        \t=== MENU ===
        A - Adicionar família
        E - Exibir resultados
        S - Sair  
          """)
   
    resposta = input("Deseja inserir mais uma família: ").upper()
   
    match resposta:
        case "A":
            os.system("cls || clear")
            qntd_filhos = int(input("\nQuantos filhos você tem: "))
            salario = float(input("Diga quanto você ganha: "))

            contador += 1
            lista_familia.append(qntd_filhos)
            lista_salario.append(salario)

        case "E":
            maior_salario = max(lista_salario)
            menor_salario = min(lista_salario)
            soma_salario = sum(lista_salario)
            soma_filhos = sum(lista_familia)
            media_filhos = soma_filhos / contador
            media_salario = soma_salario / contador
            os.system("cls || clear")
            print("=== Exibindo resultados ===")
            print(f"\nTotal de famílias que responderam a pesquisa: {contador}")
            print(f"Média do salário da população: R${media_salario:.2f}")
            print(f"Média do número de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R${maior_salario:.2f}")
            print(f"Menor salário: R${menor_salario:.2f}")
            break

        case "S":
            print("Você selecionou a opção de saída")
            break

        case _:
            print("Opção inválida")

# Definindo arquivo para salvar os dados.
nome_do_arquivo = "pesquisa_prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_familia:
    # Percorrendo vetor/lista.
    for i in range(1):
        #Escrevendo no arquivo uma linha de cada vez.
        arquivo_familia.write(f"Total de famílias que responderam: {contador}, Média salarial: R${media_salario:.2f}, Média do número de filhos: {media_filhos}, Maior salário: R${maior_salario:.2f}, Menor salário: R${menor_salario:.2f}\n")

arquivo_familia.close()