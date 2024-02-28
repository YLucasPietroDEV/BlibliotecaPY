import numpy as np  # Importa a biblioteca NumPy para operações numéricas
import sys  # Importa a biblioteca sys para sair do programa

def mostrar_menu():
    # Exibe o menu com opções para o usuário
    print("\nMenu:")
    print("1. Número de notas 7")
    print("2. Mudar a última nota para 4")
    print("3. Nota mais alta")
    print("4. Classificar as notas")
    print("5. Média das notas")
    print("6. Sair")

def numero_notas_7(notas):
    # Retorna o número de notas 7 na lista de notas
    return np.count_nonzero(notas == 7)

def mudar_ultima_nota_para_4(notas):
    # Muda a última nota da lista para 4 e retorna a lista atualizada
    notas[-1] = 4
    return notas

def nota_mais_alta(notas):
    # Retorna a nota mais alta na lista de notas
    return np.max(notas)

def classificar_notas(notas):
    # Classifica as notas em ordem crescente e retorna a lista classificada
    return np.sort(notas)

def media_notas(notas):
    # Calcula e retorna a média das notas
    return np.mean(notas)

# Lista inicial de notas (usando NumPy para criar um array)
notas = np.array([9, 7, 7, 10, 3, 9, 6, 6, 2])

while True:
    # Exibe o menu e solicita a escolha do usuário
    mostrar_menu()
    escolha = input("Escolha uma opção (1-6): ")

    # Verifica a escolha do usuário e executa a operação correspondente
    if escolha == '1':
        print("Número de notas 7:", numero_notas_7(notas))
    elif escolha == '2':
        print("Lista de notas com a última nota alterada para 4:", mudar_ultima_nota_para_4(notas))
    elif escolha == '3':
        print("Nota mais alta:", nota_mais_alta(notas))
    elif escolha == '4':
        print("Notas classificadas:", classificar_notas(notas))
    elif escolha == '5':
        print("Média das notas:", media_notas(notas))
    elif escolha == '6':
        print("Saindo...")
        sys.exit()  # Sair do programa
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
