import sqlite3
from config import DB_PATH

# SQLiteDataAccessObject del cliente


class SQLiteDataAccessObjectCliente:
    def insert_cliente(self, cliente_id, nombre, edad, email):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO clientes (cliente_id, nombre, edad, email)
                    VALUES (?, ?, ?, ?);
                ''', (cliente_id, nombre, edad, email))
                conn.commit()
                print("Cliente insertado.")
        except sqlite3.Error as e:
            print("Ha ocurrido un error insertando el cliente")

    def update_cliente(self, cliente_id, nombre, edad, email):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE clientes
                    SET nombre = ?, email = ?, edad = ?
                    WHERE cliente_id = ?;
                ''', (nombre, email, edad, cliente_id))
                conn.commit()
                print("Cliente actualizado correctamente.")
        except sqlite3.Error as e:
            print("Ha ocurrido un error actualizando el cliente")

    def query_cliente(self, cliente_id):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT *
                    FROM clientes
                    WHERE cliente_id = ?;
                ''', (cliente_id,))
                result = cursor.fetchone()
                if result:
                    return result
                else:
                    return None
        except sqlite3.Error as e:
            print("Ha ocurrido un error buscando el cliente")

    def query_todos_los_clientes(self):
        """Muestra todos los clientes."""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM clientes;')
                resultados = cursor.fetchall()
                return resultados
        except sqlite3.Error as e:
            print("Ha ocurrido un error obteniendo todos los clientes")
