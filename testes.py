import unittest
import aluno as a
import turma as t

class turmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = [
            a.Aluno('Fabio', 'Teixeira', 10),
            a.Aluno('Fabiano', 'Teixeira', 8),
            a.Aluno('Melissa', 'Teixeira', 6),
            a.Aluno('Angela', 'Teixeira', 7)
        ]
        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota')

    def testMenor(self):
        self.assertEqual(6, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota')

    def testIntervalo(self):
        print('Testar se o intervalo de notas está correto.')
        for aluno in self.turmaObject.turma:
            self.assertTrue(0 <= aluno.nota <= 10, f"Nota inválida encontrada: {aluno.nota}")

    def testNotaInvalida(self):
        aluno_invalido = a.Aluno('João', 'Silva', -1)
        self.turmaObject.cadastrarAlunos([aluno_invalido])
        self.assertNotIn(aluno_invalido, self.turmaObject.turma, "Aluno com nota inválida foi cadastrado.")

if __name__ == "__main__":
    unittest.main()
