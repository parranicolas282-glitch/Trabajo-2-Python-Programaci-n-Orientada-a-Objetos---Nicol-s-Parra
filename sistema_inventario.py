# --- Excepciones Personalizadas ---
class ProductoNoEncontradoError(Exception):
    """Excepción lanzada cuando un producto no existe en el inventario."""
    pass


# --- Clases del Sistema ---
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad del producto no puede ser negativa.")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        self.precio = nuevo_precio    

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad del producto no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de la clase Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre_producto: str):
        # Búsqueda insensible a mayúsculas/minúsculas empleando .lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        
        # Si termina el ciclo y no lo encuentra, lanza la excepción explícita
        raise ProductoNoEncontradoError(f"El producto '{nombre_producto}' no existe en el inventario.")

    def calcular_valor_inventario(self):
        valor_total = 0
        for producto in self.productos:
            valor_total += producto.calcular_valor_total()
        return valor_total

    def listar_productos(self):
        return [str(producto) for producto in self.productos]


# --- Interfaz de Usuario ---
def menu_principal(inventario: Inventario):  # Ahora recibe el inventario por parámetro
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Listar productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("¡Producto agregado exitosamente!")
            except ValueError as e:
                print(f"Error: Entrada inválida o restricción rota. ({e})")
                
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            try:
                # Intentamos buscar el producto
                producto = inventario.buscar_producto(nombre_producto)
                print("¡Producto encontrado!")
                print(producto)
            except ProductoNoEncontradoError as e:
                # Capturamos la excepción específica si no se encuentra
                print(f"❌ {e}")
                
        elif opcion == "3":
            valor_total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: {valor_total}")
            
        elif opcion == "4":
            productos_listados = inventario.listar_productos()
            if not productos_listados:
                print("El inventario está vacío.")
            for prod in productos_listados:
                print(prod)
                
        elif opcion == "5":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# --- Sección Principal de Ejecución ---
if __name__ == "__main__":
    # Instanciación del objeto inventario en el bloque principal
    mi_inventario_global = Inventario()
    
    # Se pasa el objeto como argumento al menú principal
    menu_principal(mi_inventario_global)