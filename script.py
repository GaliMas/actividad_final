import sqlite3
from config import DB_PATH

# Conexión a la base de datos
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()

    # Crear tabla de productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            product_id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL
        );
    ''')

    # Crear tabla de clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            cliente_id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            email TEXT NOT NULL
        );
    ''')

    # Crear tabla de ventas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            venta_id INTEGER PRIMARY KEY,
            producto_id INTEGER NOT NULL,
            cliente_id INTEGER NOT NULL,
            importe REAL NOT NULL,
            FOREIGN KEY (producto_id) REFERENCES productos (product_id),
            FOREIGN KEY (cliente_id) REFERENCES clientes (cliente_id)
        );
    ''')

    # Insertar datos en la tabla de productos
    cursor.executemany('''
        INSERT INTO productos (product_id, nombre, descripcion)
        VALUES (?, ?, ?)
    ''', [
        (1, 'Televisión', 'Televisión LG 60 pulgadas'),
        (2, 'Portátil', 'Portátil windows'),
        (3, 'Auriculares', 'Auriculares bluetooth')
    ])

    # Insertar datos en la tabla de clientes
    cursor.executemany('''
        INSERT INTO clientes (cliente_id, nombre, edad, email)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Juan Pérez', 30, 'juan@perez.com'),
        (2, 'María López', 25, 'maria@lopez.com'),
        (3, 'Carlos García', 35, 'carlos@garcia.com')
    ])

    # Insertar datos en la tabla de ventas
    cursor.executemany('''
        INSERT INTO ventas (venta_id, producto_id, cliente_id, importe)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 1, 1, 750.50),
        (2, 2, 2, 800.99),
        (3, 3, 3, 40.00)
    ])

    conn.commit()

    print("Tablas creadas y datos insertados correctamente.")
