import sqlite3
from config import DB_PATH

# SQLiteDataAccessObject de venta


class SQLiteDataAccessObjectVenta:
    def insert_venta(self, venta_id, producto_id, cliente_id, importe):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()

                cursor.execute('''
                    INSERT INTO ventas (venta_id, producto_id, cliente_id, importe)
                    VALUES (?, ?, ?, ?);
                ''', (venta_id, producto_id, cliente_id, importe))

                conn.commit()
                print("Venta insertada.")
        except sqlite3.Error as e:
            print("Ha ocurrido un error insertando la venta")

    def update_venta(self, venta_id, producto_id, cliente_id, importe):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            existing_venta = self.query_venta(venta_id)

            if not existing_venta:
                print("Error: La venta no existe.")
                return

            cursor.execute('''
                    UPDATE ventas
                    SET producto_id = ?, cliente_id = ?, importe = ?
                    WHERE venta_id = ?;
                ''', (producto_id, cliente_id, importe, venta_id))

            conn.commit()
            print("Venta actualizada correctamente.")

    def query_venta(self, venta_id):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT *
                    FROM ventas
                    WHERE venta_id = ?;
                ''', (venta_id))

                result = cursor.fetchone()

                if result:
                    return result
                else:
                    return None
        except sqlite3.Error as e:
            print("Ha ocurrido un error buscando la venta")

    def query_todas_las_ventas(self):
        """Muestra todas las ventas."""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM ventas;')
                resultados = cursor.fetchall()
                return resultados
        except sqlite3.Error as e:
            print("Ha ocurrido un error obteniendo todas las ventas")
