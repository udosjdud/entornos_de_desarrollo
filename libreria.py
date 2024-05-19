import json

class Libreria:
    """Representa una biblioteca de libros."""
    
    def __init__(self):
        """Inicializa una nueva instancia de la clase Libreria."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """Añade un nuevo libro a la biblioteca.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """Busca un libro por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Una lista de libros que coinciden con el título dado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """Busca libros por un autor específico.

        Args:
            autor (str): El nombre del autor a buscar.

        Returns:
            list: Una lista de libros escritos por el autor dado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """Elimina un libro de la biblioteca.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro ha sido eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """Guarda la lista de libros en un archivo JSON.

        Args:
            archivo (str): La ruta del archivo donde se guardará la lista de libros.

        Returns:
            str: Mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """Carga la lista de libros desde un archivo JSON.

        Args:
            archivo (str): La ruta del archivo desde donde se cargarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido cargados correctamente, 
                 o un mensaje de error si el archivo no se encuentra.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros("libreria.json")
print(mi_libreria.cargar_libros("libreria.json"))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
