import sqlite3
from config import DB_PATH


class SQLiteDataAccessObjectEstadisticas:
    def __init__(self):
        self.db_path = DB_PATH

    def obtener_productos_mas_vendidos(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.product_id, p.nombre, COUNT(v.venta_id) AS ventas
                FROM ventas v
                INNER JOIN productos p ON v.producto_id = p.product_id
                GROUP BY p.product_id, p.nombre
                ORDER BY ventas DESC
                LIMIT 5;
            ''')
            resultados = cursor.fetchall()
            return resultados

    def clientes_mayor_numero_compras(self):
        """Obtiene los clientes con mayor número de compras."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.cliente_id, c.nombre, COUNT(v.venta_id) AS compras
                FROM ventas v
                INNER JOIN clientes c ON v.cliente_id = c.cliente_id
                GROUP BY c.cliente_id, c.nombre
                ORDER BY compras DESC
                LIMIT 5;
            ''')
            resultados = cursor.fetchall()
            return resultados

    def clientes_sin_compras(self):
        """Identifica los clientes que nunca han realizado una compra."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.cliente_id, c.nombre
                FROM clientes c
                LEFT JOIN ventas v ON c.cliente_id = v.cliente_id
                WHERE v.venta_id IS NULL;
            ''')
            resultados = cursor.fetchall()
            if resultados:
                return resultados
            else:
                print("Todos los clientes han realizado al menos una compra.")

    def calcular_ingresos_totales(self):
        """Calcula los ingresos totales obtenidos por ventas."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT SUM(importe) AS ingresos_totales
                FROM ventas;
            ''')
            resultado = cursor.fetchone()
            return resultado
