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

    def registrar(self):
        # Registra la transacción en la base de datos
        datos_transaccion = {
            'ID':  self.id_transaccion,
            'Tipo': self.tipo,
            'Productos': self.productos,
            'Fecha': self.fecha,
            'Entidad': self.entidad,
            
            
            
            
            'Total': self.total,
            'Productos':  self.productos
            
        }
        #Leer los datos existentes o crear una nueva lista si el archivo no existe
        if os.path.exist(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                datos_transacciones = json.load(archivo)
        else:
            datos_transacciones = []
            datos_transacciones.append(datos_transaccion)
            with open(nombre_archivo, 'w') as archivo:
                json.dump(datos_transacciones, archivo, indent=4)
            print('Transacciones registradas en JSON')
            

    def generar_reporte(self, datos_venta, datos_compra, id_reporte, id_fecha, id_entidad):
        self.datos_venta = datos_venta
        self.datos_compra = datos_compra
        self.id_reporte = id_reporte
        self.id_fecha = id_fecha
        self.id_entidad = id_entidad
    
        # Calcular el total para cada producto en datos_venta
        for producto in self.datos_venta:
            producto['total'] = producto['cantidad'] * producto['precio_unitario']
    
        # Calcular el total para cada producto en datos_compra
        for compra in self.datos_compra:
            compra['total'] = compra['cantidad'] * compra['precio_unitario']
    
        # Crear un resumen del reporte
        reporte = {
            'id_reporte': self.id_reporte,
            'fecha': self.id_fecha,
            'entidad': self.id_entidad,
            'ventas': self.datos_venta,
            'compras': self.datos_compra,
        }
        # generamos el JSON del reporte     
        if os.path.exist(nombre_de_archivo):
            with open(nombre_de_archivo, 'w') as archivo:
                json.dump(reporte, archivo, indent=4)
                print('Reporte generado en JSON')
        



    def anular_transaccion(self):
        # Implementación para anular una transacción
        pass

    def obtener_informacion(self):
        # Retorna la información de la transacción
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

    def validar_transaccion(self,  tipo,  fecha, total,id_transacciones_existentes, lista_entidades, descuento):

        self.validar_id_transaccion(id_transacciones_existentes)
        self.validar_tipo(tipo)
        self.validar_fecha(fecha)
        self.validar_entidad(lista_entidades)
        self.validar_productos(inventario)
        self.validar_total(total)
        self.validar_descuento(descuento)
        return True
    
    def validar_id_transaccion(self,  id_transacciones_existentes):
        if self.id_transaccion in id_transacciones_existentes:
            raise ValueError("ID de Transaccion ya existe.")
        if not isinstance(self.id_transaccion, str) or not self.id_transaccion.strip():
            raise ValueError("ID de Transaccion no puede ser vacio.")
        if len(self.id_transaccion) > 20:
            raise ValueError("ID de Transaccion no puede tener mas de 20 caracteres.")
        if  not self.id_transaccion.isalnum():
            raise ValueError("ID de Transaccion solo puede contener letras y numeros.")
        if  self.id_transaccion.islower():
            raise ValueError("ID de Transaccion debe tener al menos una mayuscula.")
        if   self.id_transaccion.isupper():
            raise ValueError("ID de Transaccion debe tener al menos una minuscula.")
        if   self.id_transaccion.isdigit():
            raise ValueError("ID de Transaccion no puede ser unicamente numerico.")
        if   self.id_transaccion.isspace():
            raise ValueError("ID de Transaccion no puede ser unicamente espacio.")
        if    self.id_transaccion.isspace():
            raise ValueError("ID de Transaccion no puede ser unicamente espacio.")
        if    self.id_transaccion == " ":
            raise ValueError("ID de Transaccion no puede ser unicamente espacio.")
        if    self.id_transaccion == "" :
            raise ValueError("ID de Transaccion no puede ser vacio.")
        if     self.id_transaccion == None :
            raise ValueError("ID de Transaccion no puede ser vacio.")
        
        
class inventario:
    def __init__(self, nombre_db='Inventario.db'):
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        self.creacion_nuevo_inventario()
        
    def creacion_nuevo_inventario(self):
        conexion = sqlite3.conect(self.nombre_db)
        cursor = conexion.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXIST INVENTARIO (
                           id TEXT PRIMARY KEY
                           nombre TEXT NOT NULL
                           precio REAL NOT NULL
                           stock INTEGER NOT NULL
                           )
                        ''')
        conexion.commit()
        conexion.close()
        
        
class  cliente:
    def __init__(self, id_cliente, nombre_cliente, telefono_cliente, direccion_cliente):
        self.id_cliente = id_cliente
        self.nombre_cliente =  nombre_cliente
        self.telefono_cliente = telefono_cliente
        self.direccion_cliente = direccion_cliente
        
    def agregar_cliente(self,id_Cliente_db='Cliente'):
        conexion = sqlite3.connect(id_Cliente_db)
        cursor = conexion.cursor()  
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS clientes (
                           id INTEGER PRIMARY KEY,
                           nombre TEXT NOT NULL,
                           telefono  TEXT NOT NULL,
                           direccion TEXT NOT NULL
                           )
                           ''')
        conexion.commit()
        conexion.close()

class  producto:
    def __init__(self, id_producto, nombre_producto, cantidad, precio_unitario):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        

        


