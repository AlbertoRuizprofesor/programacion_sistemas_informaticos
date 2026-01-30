 
 USE cursos2026;
SELECT * FROM alumnos 
	WHERE ciudad="Madrid"
	ORDER BY alumnos.ciudad;

SELECT id,nombre,apellidos FROM alumnos
	WHERE nombre LIKE "%l%";

SELECT id, nombre FROM alumnos
	WHERE id>=2 AND nombre="Marta"
	ORDER BY nombre desc;

SELECT id, nombre FROM alumnos
	WHERE id<=2 or nombre="Marta"
	ORDER BY nombre desc;

SELECT id, nombre FROM alumnos
	WHERE id BETWEEN 1 AND 3
	ORDER BY nombre desc;

SELECT  COUNT(id),MAX(id),MIN(id),AVG(id),SUM(id)
	FROM alumnos
	WHERE id>3;

SELECT count(facturas.id_alumno),
		max(facturas.importe), MIN(importe),
		SUM(importe)
		FROM facturas
		WHERE pagado="No";

SELECT * FROM facturas
INNER JOIN alumnos
ON facturas.id_alumno=alumnos.id
WHERE pagado="NO"
ORDER BY apellidos,importe DESC;	