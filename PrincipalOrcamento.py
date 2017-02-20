from Orçamento import Orcamento

class Principal:
    if __name__ == '__main__':

        usuario = Orcamento(43.0, 13.0, 9.0, 4.0, 4.0, 2.0, 8.0, 7.0, 3.0, 3.0, 4.0, 100.0)

        i=1
        while i != 0:

            while i != 0:
                try:
                    ano = int(input("Digite um ano entre 2016 e 2036: "))
                    if ano > 2016 and ano <= 2036:
                        valorGlobal = int(input("Digite o valor global de 2016(em milhões): "))
                        populacao2016 = int(input("Digite a população aproximada, em milhões, em 2016: "))
                        populacao = int(input("Digite a população aproximada, em milhões, do ano que deseja saber o orçamento:"))
                        break
                    else:
                        print("Informe um ano somente entre 2016 e 2036:")

                except (ValueError):
                    print("Valor inválido!")

            print("-----------------------------")

            print("Digite 1 para calcular orçamento do ano que deseja.")
            print("Digite 2 caso queira alterar porcentagens do orçamento.")
            print("Digite 3 se deseja saber o custo por usuário do ano que informar e saber se houve uma queda ou aumento em relação a 2016.")
            print("Digite 4 se almeja sair.")

            print("-----------------------------")

            try:
                opcao = int(input("Digite a opção que deseja:"))

                usuario.Menu(opcao,ano,valorGlobal,populacao,populacao2016)
            except (ValueError):
                print("Opção inválida!")

            try:
                opcaoFinal = int(input("Deseja continuar? Digite 1 para continuar ou qualquer tecla para sair:"))

                if opcaoFinal == 1:
                    pass
                else:
                    exit()
            except (ValueError):
                    exit()

