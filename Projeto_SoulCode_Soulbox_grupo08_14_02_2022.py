#**********PRINCIPAL***********
# ULTIMA ATUALIZAÇÃO: 14.02.22 - 17h40
#Integrantes da Equipe:
#Elidy Izidio
#Felipe Rinaldini Santos
#Miriam Sobral
#Ricardo Oliveira


print('********************************************')
print('********** SoulBox - Food Service **********')
print('********************************************\n')

from datetime import datetime

nome_usuario = str(input('Podemos te conhecer melhor? Qual o seu nome? '))
print(f'Olá {nome_usuario}!\nEscolha uma das opções abaixo: \n')

lista_menu1 = ['A - Acessar Programa', 'F - Finalizar Programa']
lista_menu2 = ['', '1 - Lanches', '2 - Bebidas', '3 - Acompanhamentos', '4 - Sobremesa', '5 - Ver Carrinho/Limpar Carrinho', '6 - Finalizar Pedido', '7 - Voltar']
lista_lanches = [['',''], ["1 - Docker: R$", 32.00], ["2 - Kubernets: R$", 42.00], ["3 - Cloud: R$", 26.00], ["4 - Container: R$", 45.00], ["5 - Cancelar", '']]
lista_bebidas = [['',''],['1 - Coca-cola: R$', 8.00], ['2 - Suco de laranja: R$', 9.00], ['3 - Cerveja: R$', 12.00], ['4 - Água: R$', 7.00], ["5 - Cancelar", '']]
lista_acompanhamentos = [['', ''],['1 - Fritas: R$', 18.00], ['2 - Nuggets: R$', 22.00], ['3 - Mussarela empanada: R$', 25.00], ['4 - Onion Rings: R$', 28.00], ["5 - Cancelar", '']]
lista_sobremesas = [['', ''],['1 - Pudim: R$', 10.00], ['2 - Tiramissu: R$', 12.00], ['3 - Brigadeiro: R$', 8.00], ['4 - Torta de limão: R$', 14.00], ["5 - Cancelar", '']]
lista_pagamentos = ['', '1 - Cartão', '2 - Dinheiro', '3 - Cancelar Compra', '4 - Voltar']
lista_pedido = []

esc_bebida = 0
vlr_carrinho = 0
desiste = ''
troco = ''
valor = 0
valida_menu2 = ''
esc_prod = 0

while True:
  for cont in range(len(lista_menu1)):
    print(lista_menu1[cont])
  escolha = str(input('--> '))
  valida_menu2 = str(escolha) ### VERIFICAR SE PODE APAGAR

  if escolha not in "AaFf":
    print("Opção inválida.")
  else:
    if escolha in "Aa":
      while True:
        print('***********************************')
        for cont2 in range(len(lista_menu2)):
          print(lista_menu2[cont2])
        try: #Tratamento para exceção. Caso usuario digite uma String ao invès de numero
          esc_prod = int(input('--> '))
        except:
          print("Opção inválida.\n")
        

        #LANCHES
        if esc_prod == 1: 
          for cont3 in range(len(lista_lanches)):
            print(lista_lanches[cont3][0], lista_lanches[cont3][1])
          esc_lanche = int(input('Adicione um lanche ao carrinho: '))

          if esc_lanche == 5: #cancelar - sair do menu sem escolher nada
            pass
          else:
            lista_pedido.append(lista_lanches[esc_lanche])
            print('\n***********************************')
            print(f'{lista_lanches[esc_lanche]} Adicionado.')
            

        #BEBIDAS
        if esc_prod == 2:
          for cont4 in range(len(lista_bebidas)):
            print(lista_bebidas[cont4][0], lista_bebidas[cont4][1])
          esc_bebida = int(input('Adicione uma bebida ao carrinho: '))

          if esc_bebida == 5:
            pass
          else:
            lista_pedido.append(lista_bebidas[esc_bebida])
            print('\n***********************************')
            print(f'{lista_bebidas[esc_bebida]} Adicionada.')
        
        #ACOMPANHAMENTOS
        if esc_prod == 3:
          for cont5 in range(len(lista_acompanhamentos)):
            print(lista_acompanhamentos[cont5][0], lista_acompanhamentos[cont5][1])
          esc_acomp = int(input("Adicione um acompanhamento ao carrinho: "))

          if esc_acomp == 5:
            pass
          else:
            lista_pedido.append(lista_acompanhamentos[esc_acomp])
            print('\n***********************************')
            print(f'{lista_acompanhamentos[esc_acomp]} Adicionado.')

        #SOBREMESAS ***Miriam
        if esc_prod == 4:
          for cont5 in range(len(lista_sobremesas)):
            print(lista_sobremesas[cont5][0], lista_sobremesas[cont5][1])
          esc_prod = int(input("Adicione uma sobremesa ao carrinho: "))
          
          if esc_prod == 5:
            pass
          else:
            lista_pedido.append(lista_sobremesas[esc_prod])
            print('\n***********************************')
            print(f'{lista_sobremesas[esc_prod]} Adicionado.')

      #VER CARRINHO / LIMPAR CARRINHO
        if esc_prod == 5:
          if not lista_pedido:
            print("Carrinho vazio.")
          else:
            print('\n***********************************')
            for i in range(len(lista_pedido)):
              print(lista_pedido[i])
            print('***********************************')
            limpar = input("Deseja limpar o carrinho? (S/N) ")
            if limpar in "Ss":
              lista_pedido.clear()
              vlr_carrinho = 0
              print('\n***********************************')
              print("O carrinho está vazio!")

      #SUBTOTAL: Aparece sempre após adicionar um ítem no carrinho, no menu principal
        if not lista_pedido:
          pass
        else:
          vlr_carrinho = 0
          for cont_c in range(len(lista_pedido)):
            vlr_carrinho += lista_pedido[cont_c][1]
          print('\n***********************************')
          print(f'Valor do carrinho: {vlr_carrinho}')


      #CHECKOUT - PAGAMENTO ** Miriam
        if esc_prod == 6:
          if not lista_pedido:
            print('Carrinho está vazio! Adicione um produto ou finalize o programa.')
          else:
            lista_pagamentos=int(input('''Formas de Pagamento:
            [1]Cartão
            [2]Dinheiro
            [3]Cancelar a compra
            [4]Voltar
            Digite a opção: '''))
            if lista_pagamentos == 1:
                print('Insira o seu cartão.')
                print('###########################')
                print(datetime.today().strftime('%Y-%m-%d %H:%M'))
                print('Pedido realizado:\n')
                for cont_p in range(len(lista_pedido)):
                  print(lista_pedido[cont_p][0], lista_pedido[cont_p][1])
                print('###########################')
                print(f'\nValor total do pedido: R${vlr_carrinho}')
                print('\nRetire seu pedido no box.')
                print('\nRetire o seu comprovante.')
                print('\nDirija-se ao box para a retirada do pedido.\n')
                print('Obrigada e Volte sempre.')
                break

            if lista_pagamentos == 2:
              troco = input('Precisa de troco?(S/N)')
              if troco not in "NnSs":
                print("Opção inválida.")
              elif troco in "Nn":
                print('Insira suas notas e Obrigada por sua compra!')
                print('\nObrigado, seu pedido foi concluído!')
              elif troco in "Ss":
                valor = int(input("Informe o valor de suas notas: "))
                valor = valor - vlr_carrinho
                print(f"Insira suas notas.")
                print(f"\nRetire o seu troco no valor de R${valor}\n")

                nota50 = valor // 50
                valor %=  50
                nota20 = valor // 20
                valor %= 20
                nota10 = valor // 10
                valor %= 10
                nota5 = valor // 5
                valor %= 5
                nota2 = valor // 2
                valor %= 2
                nota1 = valor // 1
                valor %= 1

                print(f"notas de 50 = {nota50}")
                print(f"notas de 20 = {nota20}")
                print(f"notas de 10 = {nota10}")
                print(f"notas de 5 = {nota5}")
                print(f"notas de 2 = {nota2}")
                print(f"notas de 1 = {nota1}")
                
                print('\nObrigado, seu pedido foi concluído!')
                print('################################################')
                #print(datetime.today())
                print(datetime.today().strftime('%Y-%m-%d %H:%M'))
                print('Pedido realizado:\n')
                for cont_p in range(len(lista_pedido)):
                  print(lista_pedido[cont_p][0], lista_pedido[cont_p][1] )
                print('################################################')
                print(f'Valor total do pedido: R${vlr_carrinho}')
                print('################################################')
                print('Retire o seu comprovante.')
                print('\nDirija-se ao box para a retirada do pedido.')
                print('################################################')
                break
                
            if lista_pagamentos == 3:
              print('\nDesculpe por alguma inconveniência!')
              print('Tem certeza que deseja cancelar o seu pedido? (S/N)')
              
              for cont_p in range(len(lista_pedido)):
                print(lista_pedido[cont_p][0], lista_pedido[cont_p][1] )
              print(f'Valor do carriho: R${vlr_carrinho}')
              desiste = input('--> ')
              if desiste in "Ss":
                lista_pedido.clear()
                vlr_carrinho = 0
              pass
            if lista_pagamentos == 4:#Voltar
              pass
        elif esc_prod == 7: #Retorna ao 1o menu
          break

        else: #Menu 2 - Caso o usuario digite um numero que nao existe o menu.
          if esc_prod <= 0 or esc_prod > 7:
            print("Opção Inválida. Escolha uma opção existente.")   



    else:
      if escolha in "Ff":
        print('Sessão encerrada')
        break



