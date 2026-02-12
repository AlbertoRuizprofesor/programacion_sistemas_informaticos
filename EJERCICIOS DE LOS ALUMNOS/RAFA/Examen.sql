# CONSULTA 1

-- Mostrar todos los alumnos y las facturas pagadas ordenadas en orden descendente:
SELECT alumnos.nombre, alumnos.apellidos, sum(facturas.importe) AS total, facturas.pagado FROM alumnos 
JOIN facturas ON alumnos.id = facturas.id_alumno
WHERE facturas.pagado="No"
GROUP BY alumnos.id
ORDER BY facturas.importe DESC;


# CONSULTA 2

-- Mostrar datos de los alumnos, sus cursos y asistencia:
SELECT * FROM alumnos
JOIN asistencia ON asistencia.id_alumno = alumnos.id
JOIN cursos ON cursos.id = asistencia.id;


# CONSULTA 3

-- Todos los alumnos de Entorno de desarrollo /  Seguridad Informática:
SELECT * FROM alumnos
JOIN asistencia ON asistencia.id = alumnos.id
JOIN cursos ON cursos.id = asistencia.id
WHERE cursos.nombre_curso = "Entorno de desarrollo" 
OR cursos.nombre_curso = "Seguridad Informática";


# CONSULTA 4

-- Todos los alumnos cuyos nombres empiecen por A:
SELECT * FROM alumnos
WHERE alumnos.nombre LIKE "A%";


# CONSULTA 5

-- Facturas de la 5 a la 10 con los datos de los alumnos:
SELECT * FROM alumnos
JOIN facturas ON facturas.id_alumno = alumnos.id
WHERE facturas.id_factura BETWEEN 5 AND 10;


# CONSULTA 6

-- Clientes que hayan comprado móvil Iphone.
SELECT * FROM clientes
JOIN ventas ON ventas.idclientes = clientes.idclientes
JOIN productos ON ventas.idproductos = productos.idproducto
WHERE productos.nombre_producto = "Móvil Iphone";


# CONSULTA 7

-- Ventas de todos los clientes menos del 3:
SELECT * FROM clientes
JOIN ventas ON ventas.idclientes = clientes.idclientes
WHERE NOT clientes.idclientes = 3;


# CONSULTA 8

-- Clientes de Málaga y que han comprado móvil Samsung (AND):
SELECT * FROM clientes
JOIN ventas ON ventas.idclientes = clientes.idclientes
JOIN productos ON productos.idproducto = ventas.idproductos
WHERE clientes.ciudad = "Málaga" AND productos.nombre_producto LIKE  "%Samsung%";


# CONSULTA 9

-- Contar cliente con cada uno de los móviles:
SELECT productos.nombre_producto, COUNT(productos.idproducto) AS unidades_vendidas FROM ventas
JOIN productos ON ventas.idproductos = productos.idproducto
GROUP BY productos.idproducto;


# CONSULTA 10

-- Todos los datos de todas las tablas:
SELECT * FROM clientes
JOIN ventas ON ventas.idclientes = clientes.idclientes
JOIN productos ON productos.idproducto = ventas.idproductos
JOIN fabricante ON fabricante.idfabricante = productos.idfabricante;
