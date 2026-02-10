pagoInicial=float(input("Introduce el pago inicial: "))
descuento=pagoInicial * 30 / 100
print(f"Le devolvemos {descuento}€ por el desceunto")
print(f"El cliente solo tuvo que pagar en total: {pagoInicial - descuento}")