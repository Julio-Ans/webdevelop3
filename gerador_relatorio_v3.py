#Trata os dados do txt
def TrataDados():
        with open('texto.txt','r', encoding='utf-8') as arquivo:
                lista=str(arquivo.read())
                lista=lista.replace('\n', ',')
                lista2=lista.split(',')

        categoria_dicionario=['Data', 'Nome Produto', 'Quantidade', 'Preço']
        conteudo=[]
        dicionario_lista=[]

        j=4
        z=0       
        
        while j <= len(lista2):
                conteudo=lista2[z:z+4]
                j+=4
                z+=4
                dicionario=dict(list(zip(categoria_dicionario, conteudo)))
                dicionario_lista.append(dicionario)
                
        return dicionario_lista


# Alogritmo

dados = TrataDados()


def CalculaTotalProduto(dados):
        total_por_produto = {}
        for item in dados:
                produto = item['Nome Produto']
                total_venda = float(item['Quantidade']) * float(item['Preço'])
                
                # Total por Produto
                if produto in total_por_produto:
                        total_por_produto[produto] += total_venda
                else:
                        total_por_produto[produto] = total_venda
                        
        return total_por_produto
        

def CalculaTotalDia(dados):
        total_por_dia = {}
        for item in dados:
                data = item['Data']
                total_venda = float(item['Quantidade']) * float(item['Preço'])
        # Total por Dia
                if data in total_por_dia:
                        total_por_dia[data] += total_venda
                else:
                        total_por_dia[data] = total_venda
                
        return total_por_dia


with open('relatorio.txt','a', encoding='utf-8') as relatorio:
        relatorio.write("\nTotal de Vendas por Produto: \n"+str(CalculaTotalProduto(dados)))
        relatorio.write("\nTotal de Vendas por Dia: \n"+str(CalculaTotalDia(dados)))

print("\nTotal de Vendas por Produto: \n"+str(CalculaTotalProduto(dados)))
print("\nTotal de Vendas por Dia: \n"+str(CalculaTotalDia(dados)))



     