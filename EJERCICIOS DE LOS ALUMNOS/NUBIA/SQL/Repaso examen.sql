-- id,  nombre, id factura e importe
SELECT alumnos.id, alumnos.nombre, alumnos.apellidos, facturas.id_factura, facturas.importe FROM alumnos
JOIN facturas ON facturas.id_alumno = alumnos.id;

-- todos los cursos y todos los alumnos
SELECT * FROM alumnos
JOIN asistencia ON asistencia.id_alumno = alumnos.id
JOIN cursos ON cursos.id = asistencia.id_curso;

-- buscar un apellido que contenga "o"
SELECT * FROM alumnos
WHERE apellidos LIKE "%o%";

-- Facturas con importe entre 200 y 500 (las he ordenado por importe desc)
SELECT * FROM facturas
WHERE importe BETWEEN 200 AND 500
AND pagado = "No"
ORDER BY importe DESC;

-- Agrupar por ciudad y contamos la cantidad de cada uno
SELECT ciudad, COUNT(ciudad) FROM alumnos
GROUP BY ciudad;

SELECT importe, FORMAT(@iva:=importe*0.21,2) AS iva, FORMAT(importe+@iva,2) AS total, NOW()
FROM facturas;