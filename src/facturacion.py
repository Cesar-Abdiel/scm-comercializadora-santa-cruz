def calcular_total(monto, descuento=0, impuesto=0):
    subtotal = monto - descuento
    total = subtotal + impuesto
    return total

def aplicar_descuento(monto, porcentaje):
    descuento = monto * porcentaje / 100
    return monto - descuento
