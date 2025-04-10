from service_enrollment import ServiceEnrollment
import unittest


class TesteDaClasseServiceEnrollment(unittest.TestCase):
    def test_deve_criar_uma_turma(self):
        self.criarTurma = ServiceEnrollment()
        self.criarTurma.CriarTurma()


        
if __name__ == '__main__':
    unittest.main(verbosity=2)