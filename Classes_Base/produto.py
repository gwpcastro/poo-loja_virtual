# Definicao da classe compra, que representa um produto da loja
class Produto:
  def __init__(self,nome:str, preco:float, qtdestoque:float, descpercent:float, categoria:str):
    self.nome = nome
    self.preco = preco
    self.__qtdestoque = 0
    self.__descpercent = 0
    self.categoria = categoria
    
