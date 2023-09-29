# Definicao da classe compra, que armazena os dados de uma pessoa
class Pessoa:
  def __init__(self, nome:str , email:str, cpf:str):
    self.nome = nome
    self.email = email
    self.cpf = cpf
