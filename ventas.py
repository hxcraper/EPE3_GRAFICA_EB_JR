# -*- coding: utf-8 -*-
import sqlite3
import csv

def crear_tabla():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto TEXT,
        categoria TEXT,
        precio REAL,
        cantidad INTEGER,
        total REAL
    )
    ''')
    conexion.commit()
    conexion.close()

def insertToDb(ventas):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', ventas)
    conexion.commit()
    conexion.close()

def leer_datos():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def buscar_por_fecha(fecha):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas WHERE fecha = ?', (fecha,))
    ventas = cursor.fetchall()
    #devolver diccionario con key nombre del campo:
    ventas = [dict(id=venta[0], fecha=venta[1], producto=venta[2], categoria=venta[3], precio=venta[4], cantidad=venta[5], total=venta[6]) for venta in ventas]
    conexion.close()
    return ventas

def exportar_csv():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    with open('ventas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])
        writer.writerows(ventas)

# Crear la tabla
crear_tabla()

# Datos de ejemplo
ventas = [
    ('2022-06-29', 'Computador Gamer i5', 'Tecnología', 990000, 1, 990000),
    ('2024-04-18', 'Televisor 50" 4K', 'Tecnología', 1500000, 1, 1500000),
    ('2023-12-15', 'Celular Samsung Galaxy S21', 'Tecnología', 1200000, 1, 1200000),
    ('2024-02-23', 'Tablet iPad Air', 'Tecnología', 2000000, 1, 2000000),
    ('2021-01-13', 'Laptop Dell XPS 13', 'Tecnología', 2500000, 1, 2500000),
    ('2024-04-18', 'Audífonos Bluetooth Sony', 'Tecnología', 350000, 1, 350000),
    ('2021-04-26', 'Cámara Canon EOS M50', 'Tecnología', 1800000, 1, 1800000),
    ('2022-04-18', 'Smartwatch Apple Watch Series 7', 'Tecnología', 1300000, 1, 1300000),
    ('2023-06-06', 'Zapatillas Deportivas Nike', 'Ropa', 300000, 2, 600000),
    ('2023-06-09', 'Camiseta Adidas', 'Ropa', 80000, 3, 240000),
    ('2023-03-27', 'Pantalón Levi\'s', 'Ropa', 150000, 1, 150000),
    ('2023-12-06', 'Chaqueta de Cuero', 'Ropa', 350000, 1, 350000),
    ('2020-09-20', 'Vestido de Fiesta', 'Ropa', 200000, 2, 400000),
    ('2022-07-20', 'Set de Sartenes Tefal', 'Cocina', 180000, 1, 180000),
    ('2022-03-23', 'Licuadora Oster', 'Cocina', 250000, 1, 250000),
    ('2022-10-13', 'Microondas Samsung', 'Cocina', 450000, 1, 450000),
    ('2023-03-24', 'Horno Eléctrico', 'Cocina', 300000, 1, 300000),
    ('2024-03-25', 'Cafetera Nespresso', 'Cocina', 350000, 1, 350000),
    ('2024-02-17', 'Juego de Cubiertos', 'Cocina', 120000, 2, 240000),
    ('2023-07-06', 'Refrigerador LG', 'Cocina', 2000000, 1, 2000000),
]

# Insertar los datos de ejemplo en la base de datos
for venta in ventas:
    insertToDb(venta)

# Imprimir ventas del día
print('Ventas del día:')

# Buscar por fecha
ventas_hoy = buscar_por_fecha('2024-05-20')

for venta in ventas_hoy:
    print(int(venta['total']))

# Exportar datos a CSV
exportar_csv()
