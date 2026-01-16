def valorMayor(lista):
	valor = lista[0]
	for cnt in lista:
		if valor < cnt:
			valor = cnt
	return valor


def valorMenor(lista):
	valor = lista[0]
	for cnt in lista:
		if valor > cnt:
			valor = cnt
	return valor
