class Aluno:
  def __init__(self, nome, sobrenome, nota):
      self.nome = nome
      self.sobrenome = sobrenome
      self.nota = nota

  def mostrarAluno(self):
      return f'Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}'
