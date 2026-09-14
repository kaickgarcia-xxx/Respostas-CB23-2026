import unittest
from P06_3499_pilha_encadeada import PilhaEncadeada
from P06_3499_fila_encadeada import FilaEncadeada


class TestPilhaEncadeada(unittest.TestCase):
    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_ordem_lifo(self):
        self.pilha.push(10)
        self.pilha.push(20)
        self.pilha.push(30)
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(self.pilha.pop(), 20)
        self.assertEqual(self.pilha.pop(), 10)

    def test_excecoes_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_tamanho(self):
        self.assertEqual(len(self.pilha), 0)
        self.assertTrue(self.pilha.esta_vazia())
        self.pilha.push("A")
        self.assertEqual(len(self.pilha), 1)
        self.assertFalse(self.pilha.esta_vazia())
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 0)
        self.assertTrue(self.pilha.esta_vazia())

    def test_valores_diversos_e_duplicados(self):
        self.pilha.push(None)
        self.pilha.push(100)
        self.pilha.push(100)
        self.assertEqual(self.pilha.pop(), 100)
        self.assertEqual(self.pilha.pop(), 100)
        self.assertIsNone(self.pilha.pop())


class TestFilaEncadeada(unittest.TestCase):
    def setUp(self):
        self.fila = FilaEncadeada()

    def test_ordem_fifo(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

    def test_intercalacao_enfileirar_desenfileirar(self):
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.assertEqual(self.fila.desenfileirar(), "A")
        self.fila.enfileirar("C")
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")

    def test_excecoes_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_esvaziar_e_reutilizar(self):
        self.fila.enfileirar(10)
        self.assertEqual(self.fila.desenfileirar(), 10)
        self.assertTrue(self.fila.esta_vazia())

        self.fila.enfileirar(20)
        self.assertEqual(len(self.fila), 1)
        self.assertEqual(self.fila.frente(), 20)


if __name__ == '__main__':
    unittest.main()
