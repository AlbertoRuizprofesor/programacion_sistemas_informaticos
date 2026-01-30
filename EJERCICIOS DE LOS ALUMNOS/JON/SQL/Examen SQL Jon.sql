#Examen SQL

#Ejercicio 1
SELECT * FROM alumno a
WHERE a.apellidos LIKE "%A%"
AND a.nombre LIKE "%o%"
ORDER BY apellidos
;

#Ejercicio 2
SELECT * FROM facturas f
WHERE f.pagado="no"
ORDER BY f.importe DESC
;

#Ejercicio 3
SELECT * FROM alumnos a
JOIN asistencia asi
ON a.id=asi.id_alumno
JOIN cursos c
ON c.id=asi.id_curso
;


#Ejercicio 3 BIS

SELECT * FROM alumnos a
JOIN asistencia asi
ON asi.id_alumno=a.id
JOIN cursos c
ON c.id=asi.id_curso
WHERE c.nombre_curso="entorno desarrollo"
OR c.nombre_curso="seguridad informatica"
OR c.nombre_curso="redes informaticas"
;


#Ejercicio 4
SELECT* FROM alumnos
JOIN facturas
ON alumnos.id=facturas.id_alumno
WHERE facturas.id_factura between 5 AND 10;




SELECT a.id,a.nombre,a.apellidos,
SUM(f.importe) AS total,f.pagado
FROM alumnos a
JOIN facturas f
ON a.id=f.id_alumno
WHERE f.pagado="no"
GROUP BY a.id
ORDER BY importe DESC
;





#SELECT * from facturas WHERE pagado LIKE "no" ORDER BY importe DESC;
