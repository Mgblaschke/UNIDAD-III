#ejemplo tipos de datos e identificadores

# Buen identificador para una variable que almacena las ventas en una clase
ventas_efectivas = 7

# Buen identificador para una función que registra datos
def registar_datos(calle, cedula):
    datos_cliente = {'calle': calle, 'cedula': cedula}
    return datos_cliente

# Buen identificador para una variable que almacena el valor a pagar por medio de un deposito
valor_deposito = 13.80

# Uso de los identificadores en un contexto de código
print(f"Ventas efectivas: {ventas_efectivas}")
usuario = registar_datos("calicuchima&quisquis1989", 000000000)
print(f"Datos registrados: {usuario['calle']} con id {usuario['cedula']}")
print(f"Valor a pagar mediante deposito: {valor_deposito}")