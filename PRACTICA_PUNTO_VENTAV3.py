import os
import json
import sqlite3

class Transaccion:
    def __init__(self, id_transaccion, tipo, productos, fecha, entidad):
        self.id_transaccion = id_transaccion
        self.tipo = tipo  # "venta" o "compra"
        self.productos = productos
        self.fecha = fecha
        self.entidad = entidad  # Cliente o Proveedor
        self.total = 0
        self.detalles_adicionales = {}

    def calcular_total(self):
        self.total = sum(item['cantidad'] * item['precio_unitario'] for item in self.productos)
        if self.tipo == "venta" and 'descuento' in self.detalles_adicionales:
            self.total -= self.detalles_adicionales['descuento']
        return self.total

    def actualizar_stock(self, inventario):
        for item in self.productos:
            if self.tipo == "venta":
                inventario.reducir_stock(item['producto'], item['cantidad'])
            elif self.tipo == "compra":
                inventario.incrementar_stock(item['producto'], item['cantidad'])

    def registrar(self, nombre_archivo='transacciones.json'):
        datos_transaccion = {
            'ID': self.id_transaccion,
            'Tipo': self.tipo,
            'Productos': self.productos,
            'Fecha': self.fecha,
            'Entidad': self.entidad,
            'Total': self.total
        }

        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                datos_transacciones = json.load(archivo)
            datos_transacciones.append(datos_transaccion)
        else:
            datos_transacciones = [datos_transaccion]

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_transacciones, archivo, indent=4)
        print('Transacciones registradas en JSON')

    def generar_reporte(self, datos_venta, datos_compra, id_reporte, id_fecha, id_entidad, nombre_de_archivo='reporte.json'):
        for producto in datos_venta:
            producto['total'] = producto['cantidad'] * producto['precio_unitario']
    
        for compra in datos_compra:
            compra['total'] = compra['cantidad'] * compra['precio_unitario']
    
        reporte = {
            'id_reporte': id_reporte,
            'fecha': id_fecha,
            'entidad': id_entidad,
            'ventas': datos_venta,
            'compras': datos_compra,
        }

        with open(nombre_de_archivo, 'w') as archivo:
            json.dump(reporte, archivo, indent=4)
        print('Reporte generado en JSON')

    def opcion_transaccion(self):
        opcion = input('¿Desea realizar una venta o compra? (V/C): ')
        if opcion.upper() == 'V':
            self.realizar_venta()
        elif opcion.upper() == 'C':
            self.realizar_compra()
        else:
            print("Opción inválida")

    def obtener_informacion(self):
        return {
            "ID": self.id_transaccion,
            "Tipo": self.tipo,
            "Fecha": self.fecha,
            "Entidad": self.entidad,
            "Total": self.calcular_total(),
            "Productos": self.productos
        }

    def aplicar_descuento(self, descuento):
        if self.tipo == "venta":
            self.detalles_adicionales['descuento'] = descuento
        else:
            self.detalles_adicionales['descuento'] = 0

    def validar_transaccion(self, tipo, fecha, total, id_transacciones_existentes, lista_entidades, descuento):
        self.validar_id_transaccion(id_transacciones_existentes)
        self.validar_tipo(tipo)
        self.validar_fecha(fecha)
        self.validar_entidad(lista_entidades)
        self.validar_productos(inventario)
        self.validar_total(total)
        self.validar_descuento(descuento)
        return True

    def validar_id_transaccion(self, id_transacciones_existentes):
        if self.id_transaccion in id_transacciones_existentes:
            raise ValueError("ID de Transacción ya existe.")
        if not isinstance(self.id_transaccion, str) or not self.id_transaccion.strip():
            raise ValueError("ID de Transacción no puede ser vacío.")
        if len(self.id_transaccion) > 20:
            raise ValueError("ID de Transacción no puede tener más de 20 caracteres.")
        if not self.id_transaccion.isalnum():
            raise ValueError("ID de Transacción solo puede contener letras y números.")
        if self.id_transaccion.islower():
            raise ValueError("ID de Transacción debe tener al menos una mayúscula.")
        if self.id_transaccion.isupper():
            raise ValueError("ID de Transacción debe tener al menos una minúscula.")
        if self.id_transaccion.isdigit():
            raise ValueError("ID de Transacción no puede ser únicamente numérico.")
        if self.id_transaccion.isspace():
            raise ValueError("ID de Transacción no puede ser únicamente espacio.")
        if self.id_transaccion == " ":
            raise ValueError("ID de Transacción no puede ser únicamente espacio.")
        if self.id_transaccion == "":
            raise ValueError("ID de Transacción no puede ser vacío.")
        if self.id_transaccion is None:
            raise ValueError("ID de Transacción no puede ser vacío.")

class Inventario:
    def __init__(self, nombre_db='Inventario.db'):
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        self.creacion_nuevo_inventario()

    def creacion_nuevo_inventario(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS INVENTARIO (
                id TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        self.conexion.commit()

    def reducir_stock(self, producto, cantidad):
        self.cursor.execute('''
            UPDATE INVENTARIO
            SET stock = stock - ?
            WHERE id = ?
        ''', (cantidad, producto))
        self.conexion.commit()

    def incrementar_stock(self, producto, cantidad):
        self.cursor.execute('''
            UPDATE INVENTARIO
            SET stock = stock + ?
            WHERE id = ?
        ''', (cantidad, producto))
        self.conexion.commit()

class Cliente:
    def __init__(self, id_cliente, nombre_cliente, telefono_cliente, direccion_cliente):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.telefono_cliente = telefono_cliente
        self.direccion_cliente = direccion_cliente

    def agregar_cliente(self, id_Cliente_db='Cliente.db'):
        conexion = sqlite3.connect(id_Cliente_db)
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()

class Producto:
    def __init__(self, id_producto, nombre_producto, cantidad, precio_unitario):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
