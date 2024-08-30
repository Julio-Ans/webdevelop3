from Filme import Filme
from Cliente import Cliente
from Locadora import Locadora

def menu():
    print('1. Adicionar filme')
    print('2. Adicionar cliente')
    print('3. Alugar filme')
    print('4. Listar filmes disponíveis')
    print('5. Listar filmes alugados')
    print('6. Listar clientes')
    print('7. Sair')


locadora=Locadora()
op=0

while op is not "7":
    menu()
    op=input('Digite uma das opções acima:')

    if op == "1":
        titulo=input('Qual o nome do filme?')
        ano=input('Qual o ano do filme?')
        genero=input('Qual o genero do filme?')
        f1=Filme(titulo, ano, genero)
        locadora.adicionar_filme(f1)
        print("Filme Adicionado com Sucesso")

    elif op == "2":
        nome=input('Qual o nome do Cliente?')
        id=input('Qual será o Id do Cliente?')
        c1=Cliente(id, nome)
        locadora.adicionar_cliente(c1)
        print("Cliente Adicionado com Sucesso")
    
    elif op == "3":
        cliente=input('Quem está alugando?')
        filme=input('Qual filme deseja alugar?')
        locadora.alugar_filme(cliente, filme)

    elif op == "4":
        locadora.listar_filmes_disponiveis()
    
    elif op == "5":
        locadora.listar_filmes_alugados()

    elif op == "6":
        locadora.listar_clientes()





    


       



       




        
   

    



# IMPORTANTE:
# Inicialmente, todos os filmes estão disponíveis
# Antes de alugar um filme verifique se está disponível e se o cliente está cadastrado.
# Atualize a disponibilidade do filme após alugá-lo.
 