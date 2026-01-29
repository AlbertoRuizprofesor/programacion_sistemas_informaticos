#SQL Phoneland

#Ejercicio 1

SELECT * FROM clientes c
JOIN ventas v
ON c.idclientes=v.idclientes
JOIN productos p
ON v.idproductos=p.nombre_producto
WHERE p.nombre_producto LIKE "%iphone%";



#Ejercicio 2

SELECT * FROM ventas v
JOIN clientes c
ON v.idclientes=c.idclientes
WHERE NOT c.idclientes=3
;


#Ejercicio 3

SELECT * FROM ventas v
JOIN clientes c
ON v.idclientes=c.idclientes
JOIN productos p
ON v.idproductos=p.idproducto
WHERE c.ciudad="%malaga%"
AND p.nombre_producto LIKE "%samsung%"

;


#Ejercicio 4

SELECT productos.nombre_producto, 
COUNT(productos.idproducto) AS unidades_vendidas,
SUM(productos.precio) AS total_ventas,
AVG(productos.precio) AS media_ventas

FROM ventas 
JOIN productos 
ON ventas.idproductos=productos.idproducto
GROUP BY productos.idproducto;

#Ejercicio 5






