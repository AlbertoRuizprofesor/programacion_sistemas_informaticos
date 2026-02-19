-- EJERCICIOS EXTRA

-- 1) Lista el nombre de todos los productos que hay en la tabla producto.
SELECT nombre FROM productos;


-- 2) Lista los nombres y los precios de todos los productos de la tabla producto.
SELECT nombre, precio FROM productos;


-- 3) Lista todas las columnas de la tabla producto.
SELECT * FROM productos;


-- 4) Lista el nombre de los productos, el precio en euros y el precio en dólares estadounidenses (USD).
SELECT 
	nombre, 
	CONCAT(precio, ' ', '€'),
	CONCAT(truncate(precio*1.11, 2), ' ', '$')
FROM productos;


-- 5)  Lista el nombre de los productos, el precio en euros y el precio en dólares estadounidenses
-- (USD). Utiliza los siguientes alias para las columnas: nombre de producto, euros, dólares.
SELECT
	nombre, 
	CONCAT(precio, ' ', '€') AS euros, 
	CONCAT(truncate(precio*1.11, 2), ' ', '$') AS dólares
FROM productos;


-- 6) Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los
-- nombres a mayúscula.
SELECT upper(nombre), precio FROM productos;


-- 7)  Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los
--  nombres a minúscula.
SELECT lower(nombre), precio FROM productos;


-- 8) Lista el nombre de todos los fabricantes en una columna, y en otra columna obtenga en
-- mayúsculas los dos primeros caracteres del nombre del fabricante.
SELECT nombre, UPPER(LEFT(nombre,2)) FROM fabricante;


-- 9) Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el
-- valor del precio.
SELECT nombre, round(precio) from productos;

-- 10) Lista los nombres y los precios de todos los productos de la tabla producto, truncando el
-- valor del precio para mostrarlo sin ninguna cifra decimal.
SELECT nombre, truncate(precio, 0) FROM productos;

-- 11) Lista el código de los fabricantes que tienen productos en la tabla producto.
