from database.accessor_cliente import SQLiteDataAccessObjectCliente
from database.accessor_producto import SQLiteDataAccessObjectProducto
from database.accessor_venta import SQLiteDataAccessObjectVenta
from database.accessor_estadisticas import SQLiteDataAccessObjectEstadisticas
from models.producto import Producto
from models.cliente import Cliente
from models.venta import Venta

venta_accessor = SQLiteDataAccessObjectVenta()
producto_accessor = SQLiteDataAccessObjectProducto()
cliente_accessor = SQLiteDataAccessObjectCliente()
estadisticas_accessor = SQLiteDataAccessObjectEstadisticas()


def menu_principal():
    while True:
        print("\n\nMenú Principal")
        print("1. Cliente")
        print("2. Producto")
        print("3. Venta")
        print("4. Estadísticas")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_producto()
        elif opcion == "3":
            menu_venta()
        elif opcion == "4":
            menu_estadisticas()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


def menu_cliente():
    while True:
        print("\n\nMenú cliente")
        print("1. Consultar todos los clientes")
        print("2. Consultar cliente")
        print("3. Modificar cliente")
        print("4. Insertar cliente")
        print("5. Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados = cliente_accessor.query_todos_los_clientes()
            if resultados:
                for cliente in resultados:
                    print(Cliente(*cliente))
        elif opcion == "2":
            cliente_id = input("Ingresa el ID del cliente: ")
            resultado = cliente_accessor.query_cliente(cliente_id)
            if resultado:
                cliente = Cliente(*resultado)
                print("Cliente encontrado:")
                print(cliente)
            else:
                print("Cliente no encontrado.")
        elif opcion == "3":
            cliente_id = input("Ingresa el ID del cliente a modificar: ")
            nombre = input("Ingresa el nuevo nombre: ")
            edad = input("Ingresa la nueva edad: ")
            email = input("Ingresa el nuevo email: ")
            cliente_accessor.update_cliente(
                cliente_id, nombre, int(edad), email)
        elif opcion == "4":
            cliente_id = input("Ingresa el ID del cliente: ")
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            cliente_accessor.insert_cliente(cliente_id, nombre, int(edad))
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


def menu_producto():
    while True:
        print("\n\nMenú producto")
        print("1. Consultar todos los productos")
        print("2. Consultar producto")
        print("3. Modificar producto")
        print("4. Insertar producto")
        print("5. Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados = producto_accessor.query_todos_los_productos()
            if resultados:
                print("\nTodos los productos:\n")
                for producto in resultados:
                    print(Producto(*producto))
        elif opcion == "2":
            product_id = input("Ingresa el ID del producto: ")
            resultado = producto_accessor.query_producto(product_id)
            if resultado:
                producto = Producto(*resultado)
                print("Producto encontrado:")
                print(producto)
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            product_id = input("Ingresa el ID del producto a modificar: ")
            nombre = input("Ingresa el nuevo nombre: ")
            descripcion = input("Ingresa la nueva descripción: ")
            producto_accessor.update_producto(product_id, nombre, descripcion)
        elif opcion == "4":
            product_id = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre: ")
            descripcion = input("Ingresa la descripción: ")
            producto_accessor.insert_producto(product_id, nombre, descripcion)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


def menu_venta():
    while True:
        print("\n\nMenú venta")
        print("1. Consultar todas las ventas")
        print("2. Consultar venta")
        print("3. Modificar venta")
        print("4. Insertar venta")
        print("5. Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados = venta_accessor.query_todas_las_ventas()
            if resultados:
                print("\nTodos las ventas:\n")
                for venta in resultados:
                    print(Venta(*venta))
        elif opcion == "2":
            venta_id = input("Ingresa el ID de la venta: ")
            resultado = venta_accessor.query_venta(venta_id)
            if resultado:
                venta = Venta(*resultado)
                print("Venta encontrada:")
                print(venta)
            else:
                print("Venta no encontrada.")
        elif opcion == "3":
            venta_id = input("Ingresa el ID de la venta a modificar: ")
            producto_id = input("Ingresa el nuevo ID del producto: ")
            cliente_id = input("Ingresa el nuevo ID del cliente: ")
            importe = input("Ingresa el nuevo importe: ")
            venta_accessor.update_venta(
                venta_id, producto_id, cliente_id, float(importe))
        elif opcion == "4":
            venta_id = input("Ingresa el ID de la venta: ")
            producto_id = input("Ingresa el ID del producto: ")
            cliente_id = input("Ingresa el ID del cliente: ")
            importe = input("Ingresa el importe: ")
            venta_accessor.insert_venta(
                venta_id, producto_id, cliente_id, float(importe))
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


def menu_estadisticas():
    while True:
        print("\n\nEstadísticas")
        print("1. Productos más vendidos")
        print("2. Clientes con mayor número de compras")
        print("3. Clientes sin compras")
        print("4. Ingresos totales por ventas")
        print("5. Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados = estadisticas_accessor.obtener_productos_mas_vendidos()
            print("\nProductos más vendidos:")
            for producto in resultados:
                print(
                    f"Producto ID: {producto[0]}, Nombre: {producto[1]}, Ventas: {producto[2]}")
        elif opcion == "2":
            resultados = estadisticas_accessor.clientes_mayor_numero_compras()
            print("\nClientes con mayor número de compras:")
            for cliente in resultados:
                print(
                    f"Cliente ID: {cliente[0]}, Nombre: {cliente[1]}, Compras: {cliente[2]}")
        elif opcion == "3":
            resultados = estadisticas_accessor.clientes_sin_compras()
            print("\nClientes sin compras:")
            if resultados:
                for cliente in resultados:
                    print(f"Cliente ID: {cliente[0]}, Nombre: {cliente[1]}")
        elif opcion == "4":
            resultado = estadisticas_accessor.calcular_ingresos_totales()
            ingresos_totales = resultado[0] if resultado[0] else 0
            print(
                f"\nIngresos totales obtenidos por ventas: {ingresos_totales}")
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
