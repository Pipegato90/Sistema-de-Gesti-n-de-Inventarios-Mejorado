import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        productos = []
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    productos.append(producto)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
        return productos

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Ingrese valores válidos para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores válidos para cantidad y precio.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()