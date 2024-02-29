menu = dict({
    "Panes-clases": {
        "Producto": list([
            {"nombre": "Baguette", "valor": 5000},
            {"nombre": "Croissant", "valor": 1500},
            {"nombre": "Tarta de frutas", "valor": 8000},
            {"nombre": "Pan de molde", "valor": 4500},
            {"nombre": "Pan integral", "valor": 5500},
            {"nombre": "Pan de centeno", "valor": 6000},
            {"nombre": "Donuts", "valor": 3000},
            {"nombre": "Palmeras de chocolate", "valor": 4000},
            {"nombre": "Tarta de manzana", "valor": 7000},
            {"nombre": "Eclairs", "valor": 2500},
            {"nombre": "Napolitanas de crema", "valor": 3500},
            {"nombre": "Empanadas de carne", "valor": 4000}
        ]),
    "Promociones": list([
        {"indice": 0, "nombre": 'Descuento del 4% en la compra de 3', 'unidades': 3, "Descuento":0.04},
        {"indice": 3, "nombre": "Descuento de campus en la compra de 2 lleve un descuento del 17%", 'unidades': 2, "Descuento":0.17},
        {"indice": 0, "nombre": 'Descuento del 7% en la compra de 6', 'unidades': 6, "Descuento":0.07},
        ])
    
    }
})

# Bienvenida al usuario
print("Bienvenido Punto dulce JM")
print()
print("Seleccione la categoria")

listaCategoria = menu.keys()
listaCategoria = list(listaCategoria)
for i,val in enumerate(listaCategoria):
    print(f"{i}.{val}")
opcionCategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria ])
productosCategoria = datosCategoria["Producto"]

# Menu del usuario
print("Menu de seleccion de productos")
print(f"Seleccione el producto de la categoria {listaCategoria[opcionCategoria ]}")
for i, val in enumerate(productosCategoria ):
    print(f"{i}.{val}")
opcionProducto = int(input())


# Modulo para buscar si el producto tiene promociones segun la categoria del seleccionado
datosCategoria = menu.get(listaCategoria[opcionCategoria ])
promocionesProducto = datosCategoria.get("Promociones")
promocionProductos = list()
for val in promocionesProducto:
    if(val.get("indice") == opcionProducto ):
        promocionProductos.append(val)


# Modulo para saber la lista de promociones que tiene un producto seleccionado segun la categoria
if(len(promocionProductos) == 0):
    producto = datosCategoria.get('Producto')[opcionProducto ]
    nombreProducto = producto.get("nombre")
    productoValor = producto.get("valor")
    cantidad = int(input(f"Usuario cuantos {producto} desea: "))
    valorAPagar = cantidad * productoValor
    print(f"\nUsuario su producto {nombreProducto} tiene un valor de ${productoValor} la cantidad solicitada es de {cantidad} que da un total a pagar de ${valorAPagar} ")
    dinero = int(input("\ningrese la cantidad de dinero disponible: "))
    if(dinero >= valorAPagar):
        vueltos = dinero - valorAPagar
        print(f"\nUsuario sus vueltos son {vueltos}\n, gracias por su compra")
    else: 
        print(f"Usuario el monto es menor al valor total, porfavor busque dinero")
else:
    print(f"Seleccione una promocion del producto {datosCategoria.get('Producto')[opcionProducto ]}")
    for i, val in enumerate(promocionProductos):
        print(f"{i}.{val}")
    print(f"{len(promocionProductos)}. Salir")
    opcionPromocion = int(input())
    if(opcionPromocion !=  2):
        producto = datosCategoria.get('Producto')[opcionProducto ]
        nombreProducto = producto.get("nombre")
        productoValor = producto.get("valor")

        nombrePromocion = promocionProductos[opcionPromocion ].get("nombre")
        descuentoPromocion = promocionProductos[opcionPromocion ].get("descuento")
        unidadesPromocion = promocionProductos[opcionPromocion ].get("unidades")


        valorAPagar = productoValor - ((unidadesPromocion * productoValor)* descuentoPromocion)
        print(f"{nombrePromocion} del producto {datosCategoria.get('Producto')}")
        dinero = int(input("Ingrese la cantidad de dinero disponible "))
        if(dinero >= valorAPagar):
            vueltos = dinero - valorAPagar
            print(f"El valor a pagar es de ${valorAPagar} de la promocion {promocionProductos[opcionPromocion ]}")
            print(f"Usuario sus vueltos son {vueltos}, Gracias por comprar nuestro producto")
        else:
            print(f"Usuario el monto es menor a valor total, porfavor busque plata")
    else:
        producto = datosCategoria.get('Producto')[opcionProducto -1]
        nombreProducto = producto.get("nombre")
        productoValor = producto.get("valor")
        cantidad = int(input(f"Usuario cuantos {producto} desea: "))
        valorAPagar = cantidad * productoValor
        print(f"Usuario su producto {nombreProducto} tiene un valor de ${productoValor} la cantidad solicitada es de {cantidad} que da un total a pagar de ${valorAPagar} ")
        dinero = int(input("Ingrese la cantidad de dinero disponible: "))
        if(dinero >= valorAPagar):
            vueltos = dinero - valorAPagar
            print(f"\nUsuario sus vueltos son {vueltos}\n, gracias por su compra")
        else:
            print("\nUsuario el monto es menor al valor total, porfavor busque mas dinero")

