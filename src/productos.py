productos = []

def registrar_producto(nombre, precio, stock):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    return producto

def listar_productos():
    return productos

def actualizar_stock(nombre, nuevo_stock):
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["stock"] = nuevo_stock
            return producto
    return None
