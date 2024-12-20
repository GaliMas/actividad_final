import sqlite3
from config import DB_PATH

# SQLiteDataAccessObject del producto


class SQLiteDataAccessObjectProducto:
    def insert_producto(self, product_id, nombre, descripcion):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO productos (product_id, nombre, descripcion)
                    VALUES (?, ?, ?);
                ''', (product_id, nombre, descripcion))
                conn.commit()
                print("Producto insertado.")
        except sqlite3.Error as e:
            print("Ha ocurrido un error insertando el producto")

    def update_producto(self, product_id, nombre, descripcion):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE productos
                    SET nombre = ?, descripcion = ?
                    WHERE product_id = ?;
                ''', (nombre, descripcion, product_id))
                conn.commit()
                print("Producto actualizado correctamente.")
        except sqlite3.Error as e:
            print("Ha ocurrido un error actualizando el producto")

    def query_producto(self, product_id):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT *
                    FROM productos
                    WHERE product_id = ?;
                ''', (product_id,))
                result = cursor.fetchone()
                if result:
                    return result
                else:
                    return None
        except sqlite3.Error as e:
            print("Ha ocurrido un error buscando el cliente")

    def query_todos_los_productos(self):
        """Muestra todos los productos."""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM productos;')
                resultados = cursor.fetchall()
                return resultados
        except sqlite3.Error as e:
            print("Ha ocurrido un error obteniendo todos los productos")
