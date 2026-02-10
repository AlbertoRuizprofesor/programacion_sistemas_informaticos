SELECT * FROM clientes;


SELECT nombre, direccion, ciudad
	FROM clientes;


SELECT idproducto, nombre_producto
	FROM productos;

SELECT * FROM clientes
	WHERE nombre LIKE 'A%';


SELECT * FROM productos
	WHERE precio > 200;


SELECT * FROM ventas
	WHERE fecha_ventas='2023-01-10';
	

SELECT * FROM clientes 
	WHERE direccion IS NULL OR direccion = '';
	
	
SELECT * FROM productos
	WHERE precio = 499.99;
	

SELECT * FROM productos
	ORDER BY precio desc
	
	
SELECT * FROM productos
	ORDER BY precio desc
	LIMIT 5;
	

SELECT * FROM clientes
	ORDER BY nombre ASC;
	
	
SELECT COUNT(*) AS total_clientes 
FROM clientes; 


SELECT COUNT(*) AS total_productos 
FROM productos; 


SELECT AVG(precio) AS precio_medio 
FROM productos; 


