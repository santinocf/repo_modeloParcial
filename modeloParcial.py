# funcion de mostrar el menu
def menu():
    print("Menú Principal, elegi una opcion indicando su número:")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto más caro y más barato")
    print("5. Mostrar productos con precio mayor a 15000")
    print("6. Salir")


# funcion de cargar inventario
def cargar_inventario(inventario):
    nombre=""
    while nombre.lower() != "salir":
        nombre = input("Ingrese el nombre del producto, si desea salir, ingrese 'salir'")
        if nombre.lower() == "salir":
            break
        precio = float(input("Ingrese el precio del producto"))
        cantidad = int(input("Ingrese la cantidad de productos"))
        inventario.append([nombre, precio, cantidad])
# funcion para buscar producto
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in inventario:
        if (
            producto[0].lower() == nombre.lower()
        ):  # Comparar sin importar mayúsculas/minúsculas
            encontrado = True
            print(
                f"Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}"
            )
            break
    if not encontrado:
        print("Producto no encontrado en el inventario.")


# funcion cargar producto mayor a 15000
def mostrar_producto_mayor_15000(inventario):
    for producto in inventario:
        if producto[1] > 15000:
            print(
                f"Producto: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}"
            ) 


# funcion de ordenar
def ordenar_inventario_seleccion(inventario):
    n = len(inventario)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if inventario[j][1] < inventario[min_index][1]:
                min_index = j
        inventario[i], inventario[min_index] = inventario[min_index], inventario[i]
    print("Inventario ordenado por precio (algoritmo de selección):")
    for producto in inventario:
        print(
            f"Producto: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}"
        )


# mas caro y mas barato
def mostrar_producto_mas_caro_y_barato(inventario):
    producto_mas_caro = inventario[0]
    producto_mas_barato = inventario[0]
    for producto in inventario:
        if producto[1] > producto_mas_caro[1]:  # Comparar precios
            producto_mas_caro = producto
        if producto[1] < producto_mas_barato[1]:
            producto_mas_barato = producto
    print(
        f"Producto más caro: {producto_mas_caro[0]} con precio de {producto_mas_caro[1]} y cantidad de {producto_mas_caro[2]}."
    )
    print(
        f"Producto más barato: {producto_mas_barato[0]} con precio de {producto_mas_barato[1]} y cantidad de {producto_mas_barato[2]}."
    )

inventario = []
# funcion de elegir la opcion
opcion = input("Ingrese la opción")
while opcion==6:
    menu()
    match opcion:
        case "1":
            print("Cargar producto/s")
            # logica para cargar productos
            inventario=cargar_inventario(inventario)
        case "2":
            print("Buscar producto")
            # Lógica para buscar productos
            buscar_producto(inventario)
        case "3":
            print("Ordenar inventario")
            # Lógica para ordenar inventario
            ordenar_inventario_seleccion(inventario)
        case "4":
            print("Mostrar producto más caro y más barato")
            # Lógica para mostrar productos
            mostrar_producto_mas_caro_y_barato(inventario)
        case "5":
            print("Mostrar productos con precio mayor a 15000")
            # Lógica para mostrar productos
            mostrar_producto_mayor_15000(inventario)
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")
