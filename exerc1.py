
agenda ={}
  
def adicionar():
    nome=input("\nDigite o nome do contato")
    telefone=input("\nDigite o número de telefone de "+nome)
    agenda[nome]= telefone
    
    
def exibirtodos():
    for i,v in agenda.items():
        print(f'\nNome: {i}')
        print(f'Telefone: {v}')


def remover():
    remove=input("\nQual contato deseja remover?")
    if remove in agenda:  
           del agenda[remove]
           print("Contato removido")
    else:
           print("Não existe contato com esse nome")


def buscar():
    nome2=input("\nDigite o nome do contato")
    for chave,valor in agenda.items():
        if chave ==nome2:
              print('Nome: '+nome2+'\nTelefone: '+valor)
        else:
            print("Não há nenhum contato com esse nome")
    
          
def menu():
    x=True
    while x==True:
        opc=input("\nDigite 1 para adicionar mais contatos, 2 para exibir os contatos, 3 para buscar algum contato, 4 para excluir algum contato e 0 para encerrar o programa")

        if opc == "1":
            adicionar()
        elif opc=="2":      
                exibirtodos()
        elif opc=="3":
            buscar()  
        elif opc=="4":        
              remover()
        else:
                    print("Agenda fechada!")
                    x=False
    
    
menu()
        
         
        


    
