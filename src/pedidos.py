pedidos = []

def crear_pedido(cliente, productos, total):
    pedido = {
        "cliente": cliente,
        "productos": productos,
        "total": total,
        "estado": "pendiente"
    }
    pedidos.append(pedido)
    return pedido

def listar_pedidos():
    return pedidos

def cambiar_estado_pedido(indice, nuevo_estado):
    if indice >= 0 and indice < len(pedidos):
        pedidos[indice]["estado"] = nuevo_estado
        return pedidos[indice]
    return None
