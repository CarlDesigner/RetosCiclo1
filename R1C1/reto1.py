##Solucion del reto1 ↓

def CDT(usuario: str, capital: int, tiempo: int):
    cantidad = capital
    porcentaje_interes = 0.03
    periodo = tiempo
    porcentaje_perder = 0.02

    if periodo <= 2:
        valor_perder = cantidad * porcentaje_perder
        valor_total = cantidad - valor_perder
        mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(
            cantidad) + " para un tiempo de " + str(periodo) + " meses es: " + str(valor_total)
    else:
        valor_intereses = cantidad * porcentaje_interes * periodo / 12
        valor_total = valor_intereses + cantidad
        mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(
            cantidad) + " para un tiempo de " + str(periodo) + " meses es: " + str(valor_total)
    return mensaje

print(CDT("Carlos Fajardo", 1000000, 3))