import unittest
import os

from libreria import Libreria  # Reemplaza 'tu_modulo' con el nombre real de tu módulo


class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.file_path = "test_libreria.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.anadir_libro("Harry Potter", "J.K. Rowling", "Fantasía", 1997), "Libro añadido")

    def test_buscar_libro(self):
        self.assertEqual(len(self.libreria.buscar_libro("Cien años de soledad")), 1)

    def test_buscar_por_autor(self):
        self.assertEqual(len(self.libreria.buscar_por_autor("Gabriel García Márquez")), 1)

    def test_eliminar_libro(self):
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")

    def test_guardar_cargar_libros(self):
        self.assertEqual(self.libreria.guardar_libros(self.file_path), "Libros guardados")
        self.assertEqual(self.libreria.cargar_libros(self.file_path), "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)


if __name__ == '__main__':
    unittest.main()
