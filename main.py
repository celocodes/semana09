import aluno as a
import turma as t

alunos = [
	a.Aluno('Fabio', 'Teixeira', 8),
	a.Aluno('Fabiano', 'Teixeira', 10),
	a.Aluno('Melissa', 'Teixeira', -1)
]

turmaObject = t.Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print('*' * 30)
if turmaObject.menorNota:
	print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
if turmaObject.maiorNota:
	print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
