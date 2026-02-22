"""
Sistema de inventario con POO.
Gestión de productos con operaciones de inventario.
"""

from typing import Optional


class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, nombre: str, precio: float, cantidad: int):
        """
        Constructor de Producto.
        Valida que los datos sean correctos.
        """
        # Validar nombre
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        # Validar precio
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        # Validar cantidad
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio: float) -> None:
        """Modifica el precio validando que sea mayor o igual a cero."""
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = float(nuevo_precio)
        print(f"Precio de '{self.nombre}' actualizado a ${self.precio:.2f}")

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        """Modifica la cantidad validando que sea mayor o igual a cero."""
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = int(nueva_cantidad)
        print(f"Cantidad de '{self.nombre}' actualizada a {self.cantidad}")

    def calcular_valor_total(self) -> float:
        """Devuelve el valor total (precio × cantidad)."""
        return self.precio * self.cantidad

    def __str__(self) -> str:
        """Muestra la información del producto de forma legible."""
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor: ${self.calcular_valor_total():.2f}"


class Inventario:
    """Clase que gestiona una colección de productos."""

    def __init__(self):
        """Constructor que inicializa una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, producto: Producto) -> None:
        """Añade un objeto de tipo Producto a la lista."""
        if not isinstance(producto, Producto):
            raise TypeError("Debe ser un objeto de tipo Producto.")
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al inventario.")

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """
        Busca un producto por su nombre.
        Búsqueda exacta, insensible a mayúsculas/minúsculas.
        Devuelve el producto si lo encuentra o None si no existe.
        """
        nombre_lower = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_lower:
                return producto
        return None

    def calcular_valor_inventario(self) -> float:
        """Suma el valor total de todos los productos."""
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total

    def listar_productos(self) -> None:
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("\nEl inventario está vacío.")
            return

        print("\n" + "=" * 60)
        print("LISTADO DE PRODUCTOS")
        print("=" * 60)
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")
        print("=" * 60)


def mostrar_menu() -> None:
    """Muestra las opciones del menú."""
    print("\n" + "=" * 40)
    print("      SISTEMA DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Listar productos")
    print("4. Calcular valor total del inventario")
    print("5. Salir")
    print("=" * 40)


def obtener_datos_producto() -> Producto:
    """
    Solicita los datos de un producto al usuario.
    Returns: Objeto Producto
    """
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))

            producto = Producto(nombre, precio, cantidad)
            return producto

        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, intente de nuevo.\n")
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Por favor, intente de nuevo.\n")


def menu_principal() -> None:
    """Función principal que muestra el menú y procesa las opciones."""
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            # Agregar producto
            print("\n--- Agregar Producto ---")
            try:
                producto = obtener_datos_producto()
                inventario.agregar_producto(producto)
            except Exception as e:
                print(f"Error al agregar producto: {e}")

        elif opcion == "2":
            # Buscar producto
            print("\n--- Buscar Producto ---")
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            producto = inventario.buscar_producto(nombre)

            if producto:
                print(f"\nProducto encontrado:\n{producto}")
            else:
                print(f"No se encontró ningún producto con el nombre '{nombre}'.")

        elif opcion == "3":
            # Listar productos
            print("\n--- Listar Productos ---")
            inventario.listar_productos()

        elif opcion == "4":
            # Calcular valor total
            print("\n--- Valor Total del Inventario ---")
            total = inventario.calcular_valor_inventario()
            print(f"\nEl valor total del inventario es: ${total:.2f}")

        elif opcion == "5":
            # Salir
            print("\n¡Gracias por usar el sistema de inventario!")
            print("Hasta luego.")
            break

        else:
            print("\nOpción no válida. Por favor, seleccione 1-5.")


if __name__ == "__main__":
    menu_principal()
