from Filme import Filme
from Cliente import Cliente

class Locadora():
    
    def __init__(self):
        self.lista_filme=[]
        self.lista_cliente=[]
        self.filme={}
        self.cliente={}
        

    def adicionar_filme(self, filme):
        self.filme=dict(Título=filme.titulo,Ano=filme.ano, Gênero=filme.genero, Disponibilidade=filme.disponibilidade)
        self.lista_filme.append(self.filme)

        
    def adicionar_cliente(self, cliente):
        self.cliente=dict(Id=cliente.id, Nome=cliente.nome)
        self.lista_cliente.append(self.cliente)

    def alugar_filme(self, cliente, filme):
        for x in self.lista_cliente:
            if cliente == x['Nome']:
                for y in self.lista_filme:
                    if filme == y['Título']:
                        if y['Disponibilidade'] is not 'alugado' or y['Disponibilidade'] == 'disponível':
                            print(f'O Filme {filme} foi alugado com sucesso por {cliente}!')
                            y['Disponibilidade'] = 'alugado'
                            break
                    else:
                            print("Filme não existe")
                            break  
                break
            else:
                print("Usuário Não Existe!")


    def listar_filmes_disponiveis(self):
        for y in self.lista_filme:
            if y['Disponibilidade'] is not 'alugado' or y['Disponibilidade'] == 'disponível':
                print(y)

    def listar_filmes_alugados(self):
        for y in self.lista_filme:
            if y['Disponibilidade'] == 'alugado':
                print(y)


    def listar_clientes(self):
        print(self.lista_cliente)
