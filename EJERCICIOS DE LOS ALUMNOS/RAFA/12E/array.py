notas=[["mates",10],["historia",9],["lengua",5]]
for asignatura, nota in notas:
    print(f"la nota de {asignatura} es {nota}")
    
nota_media=sum([nota for asignatura, nota in notas])//len(notas)
print("la nota media es :" , nota_media)

print(notas[0][0])
    
print("****************************************")
sueldos=[["profesor",2000],["admtvo",1500],["auxiliar",1200],["becario", 100]]
for profesion, sueldo in sueldos:
    print(f"el sueldo de {profesion} es {sueldo}")
    
print(sueldos[0][0])
    
