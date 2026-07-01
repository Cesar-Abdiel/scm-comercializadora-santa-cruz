clientes = []

def registrar_cliente(nombre, correo, estado):
    cliente = {
        "nombre": nombre,
        "correo": correo,
        "estado": estado
    }
    clientes.append(cliente)
    return cliente

def listar_clientes():
    return clientes

def buscar_cliente(correo):
    for cliente in clientes:
        if cliente["correo"] == correo:
            return cliente
    return None

def actualizar_estado_cliente(correo, nuevo_estado):
    cliente = buscar_cliente(correo)
    if cliente:
        cliente["estado"] = nuevo_estado
    return cliente
