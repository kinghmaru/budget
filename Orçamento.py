#coding=utf-8
class Orcamento:

    __previdencia = None
    __folhaPagamento = None
    __inativos_aposentados = None
    __abono_seguroDesemprego = None
    __beneficios = None
    __bolsaFamilia = None
    __outras = None
    __saude = None
    __educacao = None
    __PAC = None
    __outrosMinisterios = None
    __orcamentoTotal = None
    __InflacoesAnos = None


    def __init__(self,previdencia,folhaPagamento,inativos_aposentados,abono_seguroDesemprego,
                  beneficios,bolsaFamilia,outras,saude,educacao,PAC,outrosMinisterios,orcamentoTotal):

        self.__previdencia = previdencia
        self.__folhaPagamento = folhaPagamento
        self.__inativos_aposentados = inativos_aposentados
        self.__abono_seguroDesemprego = abono_seguroDesemprego
        self.__beneficios = beneficios
        self.__bolsaFamilia = bolsaFamilia
        self.__outras = outras
        self.__saude = saude
        self.__educacao = educacao
        self.__PAC = PAC
        self.__outrosMinisterios = outrosMinisterios
        self.__orcamentoTotal = orcamentoTotal
        self.__InflacoesAnos = []

    def Menu(self,opcao,ano,valorGlobal,populacao,populacao2016):
        if opcao == 1:
            print("Ano de",ano,":",self.MostrarInflacao(valorGlobal,ano))

        elif opcao == 2:
            print("1 - Previdência (Obrigatório): ",self.__previdencia,"%")
            print("2 - Folha de Pagamento (Obrigatório): ",self.__folhaPagamento,"%")
            print("3 - Inativos e Aposentados (Obrigatório): ",self.__inativos_aposentados,"%")
            print("4 - Abono e Seguro Desemprego (Obrigatório): ",self.__abono_seguroDesemprego,"%")
            print("5 - Benefícios (Obrigatório): ",self.__beneficios,"%")
            print("6 - Bolsa Família : ",self.__bolsaFamilia,"%")
            print("7 - Outras: ",self.__outras,"%")
            print("8 - Saúde: ",self.__saude,"%")
            print("9 - Educação: ",self.__educacao,"%")
            print("10 - PAC: ",self.__PAC,"%")
            print("11 - Outros Ministérios: ",self.__outrosMinisterios,"%")
            print("Orçamento: ",self.__orcamentoTotal,"%")

            print("-----------------------------")

            opcaoGasto = int(input("Digite o gasto que deseja alterar de acordo com seu número correspondente: "))

            if opcaoGasto == 6:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos?"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__bolsaFamilia += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                            print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__bolsaFamilia-quant > 0:
                        self.__bolsaFamilia -= quant
                        self.__orcamentoTotal -= quant

                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            elif opcaoGasto == 7:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos?"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__outras += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                        print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__outras - quant > 0:
                        self.__outras -= quant
                        self.__orcamentoTotal -= quant
                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            elif opcaoGasto == 8:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos:"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__saude += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                        print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__saude - quant > 0:
                        if self.__saude > 7.0 and self.__saude - quant >= 7.0:
                            self.__saude -= quant
                            self.__orcamentoTotal -= quant
                        else:
                            print("Mínimo de investimento ferido!")
                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            elif opcaoGasto == 9:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos:"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__educacao += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                        print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__educacao - quant > 0:
                        if self.__educacao > 3.0 and self.__educacao - quant >= 3.0:
                            self.__educacao -= quant
                            self.__orcamentoTotal -= quant

                        else:
                            print("Mínimo de investimento ferido!")
                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            elif opcaoGasto == 10:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos:"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__PAC += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                        print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__PAC - quant > 0:
                            self.__PAC -= quant
                            self.__orcamentoTotal -= quant
                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            elif opcaoGasto == 11:
                ajuste = int(input("Digite 1 para aumentar ou 2 para diminuir os gastos:"))
                if ajuste == 1:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if quant < 27:
                        if self.__orcamentoTotal != 100:
                            if self.__orcamentoTotal + quant <= 100:
                                self.__orcamentoTotal += quant
                                self.__outrosMinisterios += quant
                            else:
                                print("Gastos extremos demais!")
                    else:
                        print("Orçamento já está 100%!")

                elif ajuste == 2:
                    quant = float(input("Informe a quantidade, em porcentagem: "))
                    if self.__outrosMinisterios - quant > 0:
                            self.__outrosMinisterios -= quant
                            self.__orcamentoTotal -= quant
                    else:
                        print("Gastos extremos demais!")

                else:
                    print("Digite se vai diminuir ou aumentar!")

            else:
                print("Gasto obrigatório ou o valor é inválido!")

        elif opcao == 3:
            if self.CustoPorUsuario(populacao,self.MostrarInflacao(valorGlobal,ano)) > self.CustoPorUsuario(populacao2016,valorGlobal):
                print("Ano de 2016:",self.CustoPorUsuario(populacao2016,valorGlobal))
                print("Ano de ",ano,":",self.CustoPorUsuario(populacao,self.MostrarInflacao(valorGlobal,ano)))
                print("Houve um aumento no valor por usuário!")
            elif self.CustoPorUsuario(populacao,self.MostrarInflacao(valorGlobal,ano)) < self.CustoPorUsuario(populacao2016,valorGlobal):
                print("Ano de 2016:", self.CustoPorUsuario(populacao2016, valorGlobal))
                print("Ano de ", ano, ":", self.CustoPorUsuario(populacao, self.MostrarInflacao(valorGlobal, ano)))
                print("Houve uma queda no valor por usuário!")
            else:
                print("Ano de 2016:", self.CustoPorUsuario(populacao2016, valorGlobal))
                print("Ano de ", ano, ":", self.CustoPorUsuario(populacao, self.MostrarInflacao(valorGlobal, ano)))
                print("Não houve queda e nem aumento, pois ambos foram iguais.")

        elif opcao == 4:
            exit()

        else:
            print("Opção inválida!")

    #Método de cálculo da inflação

    def MostrarInflacao(self, valorGlobal, ano):
        if ano >= 2016 and ano <= 2036:
            AuxGlobal = 0
            valor = valorGlobal
            Inflacao = None
            for i in range(2016, ano):
                AuxGlobal = valor * 0.05
                valor = valor + AuxGlobal
                self.__InflacoesAnos.append(valor)
            for j in range(ano - 2016):
                x = ano - 2016
                if j == x - 1:
                    Inflacao = self.__InflacoesAnos[j]
            return Inflacao

    #Método para calcular e definir o custo por indivíduo baseado na população

    def CustoPorUsuario(self,populacao,valorGlobal):
        total = valorGlobal / populacao
        return total





    
        
