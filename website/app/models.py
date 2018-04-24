
class Categ:#Categoria
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Prod: #Produto
    def __init__(self, id, nome, preco, data, descr, status, notifq, id_categ):
        self.id = id
        self.nome = nome # input text
        self.preco = preco # input text
        self.data = data # input datetime
        self.descr = descr
        self.status = status
        self.notifq = notifq
        self.id_categ = id_categ # select
        # descricao (textarea)
        # status do produto radio Disponivel / Indisponivel
        # Pronta entrega (checkbox)
        
class Estoq: #Estoque

    def __init__(self, id, qtde, id_prod):
         self.id = id
         self.qtde = qtde
         self.id_prod = id_prod
