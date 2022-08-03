#Solucion reto2 ↓

informacion={
    "id_cliente": 4,
    "nombre": "Johana Fernandez",
    "edad": 8,
    "primer_ingreso": True
}


def cliente(informacion: dict):
    
    id_cliente = informacion['id_cliente']
    nombre_cliente = informacion['nombre']
    edad_cliente = informacion['edad']
    primer_ingreso_cliente = informacion['primer_ingreso']
    
    if edad_cliente > 18:
        atraccion = 'X-Treme'
        apto = True
        if primer_ingreso_cliente == True:
            total_boleta = 20000 - (20000 * 0.05)
        else:
            total_boleta = 20000
    elif edad_cliente >= 15 and edad_cliente <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if primer_ingreso_cliente == True:
            total_boleta = 5000 - (5000 * 0.07)
        else:
            total_boleta = 5000
    elif edad_cliente >= 7 and edad_cliente < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if primer_ingreso_cliente == True:
            total_boleta = 10000 - (10000 * 0.05)
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'
    
    diccionario_respuesta = {
        'nombre': nombre_cliente,
        'edad': edad_cliente,
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': primer_ingreso_cliente,
        'total_boleta': total_boleta
    }
    
    return diccionario_respuesta

print(cliente(informacion))