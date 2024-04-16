class Animal:
  def __init__(self, nome, idade, especie): 
    self.nome = nome
    self.idade = idade
    self.especie = especie
  def latir(self):
    return f"{self.latir} está latindo."
 
  def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Espécie: {self.especie}")
        self.emitir_som()


