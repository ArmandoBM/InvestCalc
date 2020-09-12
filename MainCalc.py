print("Bem vindo à calculadora financeira")

#Conversor de taxa
def conversor_de_taxa(taxa_dada, opcao):
  if opcao == '1':
    #ano para mês
    taxa_mes = ((1 + taxa_dada)**(1/12)) -1
    print("Ao mês será: " + str(taxa_mes))

  if opcao == '2':
    #mês para ano
    taxa_ano = ((1 + taxa_dada)**12) - 1
    print("Ao ano será: " + str(taxa_ano))



#Calculo os juros reais
def juros_reais(taxa_nominal, inflacao):
  juros = ((1+taxa_nominal)/(1+inflacao)-1)*100
  print("Os juros reais são: " + str(juros))
  return juros


#Investimentos sem aportes mensais
def sem_aplicacao(capital, taxa, tempo):
  montante = capital * ((1 + taxa/100)**tempo)
  return montante


#Investimentos com aportes mensais
def com_aplicacao(capital, valor_mensal, taxa, tempo):
  montante_parcial = capital
  tempo -= 1
  while tempo > 0:
    montante_parcial = montante_parcial + valor_mensal
    montante_parcial = montante_parcial * (1 + taxa/100)
    tempo -= 1
  

  return montante_parcial



#Início do programa
sair = False
while sair == False:
  print("Selecione a opção:")
  print("\t 1-Calcular juros compostos sem aplicações mensais.\n\t 2-Calcular juros compostos com aplicações mensais.\n\t 3-Conversor de Taxa \n\t 4-Calcular Juros Reais \n\t 5-Sair")

  selecao = input("Selecione a opcão: ")

  #1-Calcular juros compostos sem aplicações 
  if selecao == '1':

    capital = float(input("Coloque o valor inicial aplicado:"))

    taxa = float(input("Coloque a taxa da aplicação em %:"))

    inflacao = float(input("Coloque a inflacao prevista em %:"))

    tempo = int(input("Coloque tempo aplicado, em meses:"))

    taxa = taxa / 100

    inflacao = inflacao / 100

    taxa_real = juros_reais(taxa, inflacao)

    montante = sem_aplicacao(capital, taxa_real, tempo)

    print("O valor obtido é: " + str(montante))





  #2-Calcular juros compostos com aplicações 
  if selecao == '2':
    
    capital = float(input("Coloque o valor inicial aplicado:"))

    valor_mes = float(input("Coloque o valor mensal aplicado:"))

    taxa = float(input("Coloque a taxa da aplicação em %:"))

    inflacao = float(input("Coloque a inflacao prevista em %:"))

    tempo = int(input("Coloque tempo aplicado, em meses:"))

    taxa = taxa / 100
    inflacao = inflacao / 100

    taxa_real = juros_reais(taxa, inflacao)
    print("Juros reais: " + str(taxa_real))

    montante = com_aplicacao(capital, valor_mes, taxa_real, tempo)

    print("O valor obtido é: " + str(montante))




  
  #Conversor de taxas
  if selecao == '3':
    taxa = float(input("Coloque a taxa em %:" ))
    taxa = taxa / 100
    print("Selecione 1 - Ano para Mês ou 2 - Mês para Ano")
    taxa_escolha = input("Selecione a opcão:")
    taxa_resultado = conversor_de_taxa(taxa, taxa_escolha)


  if selecao == '4':
    taxa = float(input("Coloque a taxa de juros em %:  "))

    taxa = taxa/100
    inflacao = float(input("Coloque a inflação em %: "))
    inflacao = inflacao/100

  juros_final = juros_reais(taxa, inflacao)
  print("Os juros reais são de: " + str(juros_final))

if selecao == '5':
  sair = True
 