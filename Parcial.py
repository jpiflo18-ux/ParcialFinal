# Parcial-Final 

#Karen Prieto
productos = {
    1: ("Cafe", 3000, 20),
    2: ("Jugo natural", 5000, 15),
    3: ("Sandwich", 8000, 10),
    4: ("Empanada", 2500, 25),
    5: ("Hamburguesa", 12000, 8)
}

#Juana Pineda
pedido = []

#Karen Prieto
def mostrar_productos(productos):
    print("Codigo - Producto - Precio - Existencias")
    for codigo in productos:
        info = productos[codigo]
        print(codigo, "-", info[0], "-", info[1], "-", info[2])

#Juana Pineda
def registrar_producto(productos, pedido, codigo, cantidad):
    if codigo not in productos:
        print("Producto no encontrado.")
    elif cantidad <= 0:
        print("Cantidad no valida.")
    elif cantidad > productos[codigo][2]:
        print("No hay suficientes unidades disponibles.")
    else:
        nombre = productos[codigo][0]
        precio = productos[codigo][1]
        existencias = productos[codigo][2]
        subtotal = precio * cantidad
        pedido.append((codigo, nombre, cantidad, subtotal))
        productos[codigo] = (nombre, precio, existencias - cantidad)
        print("Producto agregado al pedido.")

#Karen Prieto
def calcular_total(pedido):
    total = 0
    for item in pedido:
        total = total + item[3]
    return total

opcion = 0
while opcion != 3:
    print("========== CAFETERIA ==========")
    print("1. Mostrar productos")
    print("2. Agregar producto al pedido")
    print("3. Finalizar pedido")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        mostrar_productos(productos)
    elif opcion == 2:
        codigo = int(input("Codigo del producto: "))
        cantidad = int(input("Cantidad: "))
        registrar_producto(productos, pedido, codigo, cantidad)
    elif opcion == 3:
        print("Finalizando pedido...")
    else:
        print("Opcion no valida.")

#Juana Pineda
total = calcular_total(pedido)

if total >= 50000:
    descuento = int(total * 0.10)
else:
    descuento = 0

total_final = total - descuento

#Karen Prieto
print("========== RESUMEN DEL PEDIDO ==========")
print("     Producto  Cantidad  Subtotal       ")
print("-----------------------------------------")
for item in pedido:
    print(item[1], " ", item[2], " ", item[3])
print("-----------------------------------------")
print("Total : $", total)
print("Descuento : $", descuento)
print("TOTAL A PAGAR : $", total_final)
print("========================================")
