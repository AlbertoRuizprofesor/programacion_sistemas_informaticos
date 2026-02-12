producto=input("dime un producto: bebida/electrodomestico/curso de informatica")
if producto=="bebida":
    importeBebida=float(input("importeBebida:"))
    print("bebida", importeBebida)
    ivaBebida=importeBebida*0.7
    print("iva es:", ivaBebida)
    print("total es:", importeBebida+ivaBebida)
else:
    if producto=="electrodomestico":
        importeElectrodomestico=int(input("importeElectrodomestico:"))
        print("electrodomestico", importeElectrodomestico)
        ivaElectrodomestico=importeElectrodomestico*0.21
        print("iva es:", ivaElectrodomestico)
        print("total es:", importeBebida+ivaBebida)
    else:
        producto=="CursoInformatica"
        importecursoInformatica=int(input("importecursoInformatica:"))
        print("cursoInformatica", importecursoInformatica)
        ivacursoInformatica=importecursoInformatica*0.0
        print("iva es:", importeBebida+ivaBebida)
