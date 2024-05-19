import unittest
import os

from libreria import Libreria 


class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.file_path = "test_libreria.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_anadir_libro(self):
        # Caso típico
        self.assertEqual(self.libreria.anadir_libro("Harry Potter", "J.K. Rowling", "Fantasía", 1997), "Libro añadido")
        
        # Caso extremo: título y autor vacíos
        self.assertEqual(self.libreria.anadir_libro("", "", "Fantasía", 1997), "Libro añadido")

        # Caso extremo: año de publicación futuro
        self.assertEqual(self.libreria.anadir_libro("The Hobbit", "J.R.R. Tolkien", "Fantasía", 2200), "Libro añadido")

    def test_buscar_libro(self):
        # Caso típico
        self.assertEqual(len(self.libreria.buscar_libro("Cien años de soledad")), 1)

        # Caso extremo: título no existente
        self.assertEqual(len(self.libreria.buscar_libro("Harry Potter")), 0)

    def test_buscar_por_autor(self):
        # Caso típico
        self.assertEqual(len(self.libreria.buscar_por_autor("Gabriel García Márquez")), 1)

        # Caso extremo: autor no existente
        self.assertEqual(len(self.libreria.buscar_por_autor("J.K. Rowling")), 0)

    def test_eliminar_libro(self):
        # Caso típico
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")

        # Caso extremo: intentar eliminar un libro que no existe
        self.assertEqual(self.libreria.eliminar_libro("Harry Potter"), "Libro no encontrado")

    def test_guardar_cargar_libros(self):
        # Caso típico
        self.assertEqual(self.libreria.guardar_libros(self.file_path), "Libros guardados")
        self.assertEqual(self.libreria.cargar_libros(self.file_path), "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)

        # Caso extremo: cargar desde un archivo que no existe
        self.assertEqual(self.libreria.cargar_libros("archivo_no_existente.json"), "Archivo no encontrado")


if __name__ == '__main__':
    unittest.main()
