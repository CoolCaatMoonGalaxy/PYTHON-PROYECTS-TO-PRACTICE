# Importar los módulos necesarios
import csv
import pandas as pd
import os
import plotly.graph_objects as go

# Función para calcular la amortización
def calcular_amortizacion(factor_amortizacion, tasa_de_interes, valor_presente, numero_pagos):
    # Inicializar una lista para almacenar los detalles de cada pago
    detalles_pagos = []
    saldo = valor_presente
    
    # Iterar sobre el número de pagos especificado
    for pago in range(1, numero_pagos + 1):
        # Calcular el interés para este pago
        interes = saldo * tasa_de_interes / 12
        # Calcular la amortización para este pago
        amortizacion = factor_amortizacion * valor_presente
        # Calcular la cuota total para este pago
        cuota = interes + amortizacion
        # Actualizar el saldo restante
        saldo -= amortizacion
        # Agregar los detalles de este pago a la lista
        detalles_pagos.append((pago, cuota, saldo, interes, amortizacion))
    
    # Calcular el interés total pagado durante toda la amortización
    interes_total_pagado = valor_presente * tasa_de_interes * numero_pagos / 12
    # Devolver el interés total pagado y los detalles de cada pago
    return interes_total_pagado, detalles_pagos

# Función para exportar los detalles de cada pago a un archivo CSV
def exportar_a_csv(detalles_pagos, file_path):
    # Abrir el archivo CSV para escritura
    with open(file_path, mode="w", newline="") as file:
        # Crear un escritor CSV
        writer = csv.writer(file)
        # Escribir la primera fila con los nombres de las columnas
        writer.writerow(["Pago", "Cuota", "Saldo", "Interes", "Amortizacion"])
        # Iterar sobre los detalles de cada pago y escribirlos en el archivo CSV
        for pago, cuota, saldo, interes, amortizacion in detalles_pagos:
            writer.writerow([pago, f"{cuota:.2f}", f"{saldo:.2f}", f"{interes:.2f}", f"{amortizacion:.2f}"])
    
    # Imprimir un mensaje indicando que los detalles se han exportado correctamente
    print(f"Los detalles de cada pago se han exportado a '{file_path}'.")

# Función para graficar los detalles de amortización
def graficar_amortizacion(detalles_pagos):
    # Crear un DataFrame de pandas a partir de los detalles de pago
    df = pd.DataFrame(detalles_pagos, columns=["Pago", "Cuota", "Saldo", "Interes", "Amortizacion"])

    # Crear un objeto de figura de Plotly
    fig = go.Figure(data=[
        go.Bar(name='Cuota', x=df['Pago'], y=df['Cuota'], text=df['Cuota'], textposition='auto'),
        go.Bar(name='Saldo', x=df['Pago'], y=df['Saldo'], text=df['Saldo'], textposition='auto'),
        go.Bar(name='Interes', x=df['Pago'], y=df['Interes'], text=df['Interes'], textposition='auto'),
        go.Bar(name='Amortizacion', x=df['Pago'], y=df['Amortizacion'], text=df['Amortizacion'], textposition='auto'),
    ])

    # Actualizar el diseño de la figura
    fig.update_layout(
        title="Detalles de cada pago",
        xaxis_title="Pago",
        yaxis_title="Cantidad",
        barmode='stack'
    )

    # Mostrar la figura
    fig.show()

# Función para solicitar un número decimal al usuario
def solicitar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El valor debe ser mayor que cero.")
            return valor
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

# Función para solicitar un número entero al usuario
def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError("El valor debe ser mayor que cero.")
            return valor
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

# Función principal del programa
def main():
    try:
        # Solicitar la tasa de interés anual al usuario
        tasa_de_interes = solicitar_numero("Ingrese la tasa de interés anual (en decimal): ")
        # Verificar que la tasa de interés esté dentro del rango permitido
        if not 0 < tasa_de_interes < 1.1:
            raise ValueError("La tasa de interés debe estar entre 0 y 1.")

        # Solicitar el valor presente al usuario
        valor_presente = solicitar_numero("Ingrese el valor presente: ")

        # Solicitar el número de pagos al usuario
        numero_pagos = solicitar_entero("Ingrese el número de pagos: ")
        # Verificar que el número de pagos esté dentro del rango permitido
        if not 0 < numero_pagos <= 12:
            raise ValueError("El número de pagos debe ser mayor que 0 y menor o igual que 12")

        # Calcular la tasa de interés periódica
        tasa_interes_periodica = tasa_de_interes / 12

        # Calcular el factor de amortización
        factor_amortizacion = (1 - (1 + tasa_interes_periodica)**-numero_pagos) / (tasa_interes_periodica * (1 + tasa_interes_periodica)**-numero_pagos)

        # Calcular la amortización y el interés total pagado
        interes_total_pagado, detalles_pagos = calcular_amortizacion(factor_amortizacion, tasa_de_interes, valor_presente, numero_pagos)

        # Imprimir el interés total pagado
        print("Interés total pagado:", interes_total_pagado)

        # Imprimir los detalles de cada pago
        print("Detalles de cada pago:")
        print("Pago\tCuota\tSaldo\tInteres\tAmortizacion")
        for pago, cuota, saldo, interes, amortizacion in detalles_pagos:
            print(f"{pago}\t{cuota:.2f}\t{saldo:.2f}\t{interes:.2f}\t{amortizacion:.2f}")

        # Solicitar el nombre del archivo CSV al usuario
        csv_path = os.path.join(os.getcwd(), input("Ingrese el nombre del archivo:") + '.csv')

        # Exportar los detalles de cada pago a un archivo CSV
        exportar_a_csv(detalles_pagos, csv_path)

        # Graficar los detalles de amortización
        graficar_amortizacion(detalles_pagos)

    except ValueError as e:
        print("Error:", e)

# Ejecutar la función principal si este script se ejecuta como programa principal
if __name__ == "__main__":
    main()
