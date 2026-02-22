# Trabajo 2: Programación Orientada a Objetos

## Objetivo
Desarrollar un sistema básico de inventario con POO en Python para gestionar productos y realizar operaciones de inventario.

## Enunciado
Crear un sistema de inventario con clases Producto e Inventario, menú interactivo y manejo de excepciones.

## Estructura del código

### Clase Producto
- **Atributos**: nombre, precio, cantidad
- **Métodos**:
  - `__init__()` - Constructor con validaciones
  - `actualizar_precio(nuevo_precio)` - Modifica precio (≥0)
  - `actualizar_cantidad(nueva_cantidad)` - Modifica cantidad (≥0)
  - `calcular_valor_total()` - Devuelve precio × cantidad
  - `__str__()` - Representación legible

### Clase Inventario
- **Atributos**: lista de productos
- **Métodos**:
  - `agregar_producto(producto)` - Añade producto
  - `buscar_producto(nombre)` - Busca por nombre (insensible a mayúsculas)
  - `calcular_valor_inventario()` - Suma valor total
  - `listar_productos()` - Muestra todos los productos

### Menú interactivo
- 1. Agregar producto
- 2. Buscar producto
- 3. Listar productos
- 4. Calcular valor total
- 5. Salir

## Archivos
- `sistema_inventario.py` - Programa principal

## Uso
```bash
python sistema_inventario.py
```

## Ejemplo de ejecución
```
========================================
      SISTEMA DE INVENTARIO
========================================
1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total del inventario
5. Salir
========================================
Seleccione una opción (1-5): 1

--- Agregar Producto ---
Ingrese el nombre del producto: Laptop
Ingrese el precio: 999.99
Ingrese la cantidad: 5
Producto 'Laptop' agregado al inventario.
```
