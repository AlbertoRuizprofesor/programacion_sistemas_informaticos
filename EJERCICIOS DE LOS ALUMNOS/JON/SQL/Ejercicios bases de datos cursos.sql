SELECT * FROM alumnos; 


SELECT nombre, apellidos FROM alumnos;


SELECT * FROM alumnos
	WHERE ciudad="Sevilla";

	
SELECT * FROM alumnos 
	WHERE nombre LIKE 'A%'; 

	
SELECT * FROM alumnos
ORDER BY apellidos ASC;


SELECT * FROM cursos;


SELECT nombre_curso FROM cursos
ORDER BY nombre_curso ASC;


SELECT * FROM cursos
WHERE descripcion LIKE '%bases%';


SELECT COUNT(*) AS total_alumnos FROM alumnos; 


SELECT COUNT(*) AS total_cursos FROM cursos;


USE cursos2026;
SELECT ciudad, COUNT(ciudad) AS nº_alumnos
	FROM alumnos
	GROUP BY ciudad
	ORDER BY alumnos.ciudad;

	
SELECT asistencia.id, cursos.nombre_curso, asistencia.fecha_asistencia
	FROM asistencia
	JOIN cursos ON asistencia.id_curso;
	

SELECT 
   asistencia.id, 
   alumnos.nombre, 
   cursos.nombre_curso, 
   asistencia.fecha_asistencia 
FROM asistencia  
INNER JOIN alumnos 
   ON asistencia.id_alumno = alumnos.id 
INNER JOIN cursos 
   ON asistencia.id_curso = cursos.id 
ORDER BY asistencia.fecha_asistencia DESC;


SELECT facturas.id_factura, alumnos.nombre, alumnos.apellidos, facturas.importe, facturas.pagado
FROM facturas
JOIN alumnos ON facturas.id_alumno=alumnos.id
ORDER BY facturas.id_factura;


SELECT facturas.id_factura, alumnos.nombre, alumnos.apellidos, facturas.importe, facturas.pagado 
FROM facturas
JOIN alumnos  ON facturas.id_alumno = alumnos.id 
ORDER BY facturas.id_factura; 


SELECT al.id, al.nombre, al.apellidos, SUM(f.importe) AS total_facturado 
	FROM facturas f 
	JOIN alumnos al ON f.id_alumno=al.id 
	GROUP BY al.id, al.nombre, al.apellidos 
	ORDER BY total_facturado DESC; 
	
