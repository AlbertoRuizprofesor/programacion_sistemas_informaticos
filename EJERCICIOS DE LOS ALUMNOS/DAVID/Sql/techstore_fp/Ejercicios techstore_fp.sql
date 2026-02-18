-- 1.1 Lista todos los clientes
SELECT * FROM clientes;

-- 1.2 Muestra nombre y ciudad de los clientes de Málaga
SELECT clientes.nombre, clientes.ciudad FROM clientes
WHERE ciudad="Málaga";

-- 1.3 Lista productos con precio > 300 ordenados de mayor a menor.
SELECT * FROM productos
WHERE precio >300
ORDER BY precio DESC;

-- 1.4 Muestra los 3 productos más baratos
SELECT * FROM productos
ORDER BY precio ASC
LIMIT 3;

-- 1.5 Cuenta cuántos productos hay por categoría
SELECT categorias.nombre, COUNT(*) AS num_productos FROM categorias
JOIN productos ON productos.id_categoria = categorias.id_categoria
GROUP BY categorias.nombre;

-- 1.6 Muestra el stock total (suma de stock) de todos los productos
SELECT SUM(productos.stock) AS stock_total FROM productos;

-- 1.7 Muestra productos cuyo nombre contenga “USB”
SELECT * FROM productos
WHERE nombre LIKE "%USB%";

-- 1.8 Muestra clientes con email NULL
SELECT * FROM clientes 
WHERE email IS NULL;


-- 2.9 Lista ventas con: id_venta, fecha, cliente, método de pago
SELECT ventas.id_venta, ventas.fecha, clientes.nombre, ventas.metodo_pago FROM ventas
JOIN clientes ON clientes.id_cliente = ventas.id_cliente;

-- 2.10 Saca el detalle de una venta: id_venta, producto, cantidad, precio_unitario
SELECT * FROM detalle_venta; 

-- 2.11 Calcula el importe por línea (cantidad * precio_unitario)
SELECT detalle_venta.id_venta, productos.nombre, detalle_venta.cantidad, detalle_venta.precio_unitario,
detalle_venta.cantidad * detalle_venta.precio_unitario AS importe_por_linea
FROM detalle_venta
JOIN productos ON productos.id_producto = detalle_venta.id_producto;

-- 2.12 Calcula el total de cada venta
SELECT ventas.id_venta, detalle_venta.cantidad, detalle_venta.precio_unitario, 
detalle_venta.cantidad * detalle_venta.precio_unitario AS total_venta
FROM detalle_venta
JOIN ventas ON ventas.id_venta = detalle_venta.id_venta;

-- 2.13 Calcula el total gastado por cada cliente. 
SELECT c.id_cliente, c.nombre, SUM(dv.cantidad * dv.precio_unitario) AS gasto_total 
FROM clientes c 
JOIN ventas v ON c.id_cliente = v.id_cliente 
JOIN detalle_venta dv ON v.id_venta = dv.id_venta 
GROUP BY c.id_cliente, c.nombre; 

-- 2.14 Saca el TOP 3 clientes que más han gastado
SELECT clientes.nombre, SUM(detalle_venta.cantidad * detalle_venta.precio_unitario) AS total_gastado
FROM clientes
JOIN ventas ON ventas.id_cliente = clientes.id_cliente
JOIN detalle_venta ON detalle_venta.id_venta = ventas.id_venta
GROUP BY clientes.id_cliente, clientes.nombre
ORDER BY total_gastado desc
LIMIT 3;

-- 2.15 Saca el TOP 3 productos más vendidos (por unidades)
SELECT 
   p.nombre, 
   SUM(dv.cantidad) AS total_unidades
FROM productos p
JOIN detalle_venta dv ON p.id_producto = dv.id_producto
GROUP BY p.id_producto, p.nombre
ORDER BY total_unidades DESC
LIMIT 3;

-- 2.16 Saca la facturación por día
SELECT v.fecha, SUM(dv.cantidad * dv.precio_unitario) AS facturacion_dia  FROM ventas v
JOIN detalle_venta dv on dv.id_venta = v.id_venta
GROUP BY v.fecha
ORDER BY v.fecha;

-- 3.17 Clientes que han comprado al menos una vez
SELECT * FROM clientes
WHERE id_cliente IN (SELECT id_cliente FROM ventas);

-- 3.18 Clientes que NO han comprado nunca
SELECT * FROM clientes
WHERE id_cliente NOT IN (SELECT id_cliente FROM ventas);

-- 3.19 Productos que se han vendido alguna vez 
SELECT * FROM productos
WHERE id_producto IN (SELECT id_producto FROM detalle_venta);

-- 3.20 Productos que NO se han vendido nunca
SELECT * FROM productos
WHERE id_producto NOT IN (SELECT id_producto FROM detalle_venta);

-- 3.21 Productos con precio superior al precio medio
SELECT * FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);

-- 3.22 Ventas con total superior a la media de todas las ventas 
# NO ME SALE
SELECT * FROM ventas
WHERE SUM(cantidad*precio_unitario) AS total > (SELECT AVG(total) FROM detalle_venta);

-- 3.23 Cliente que más ha gastado (una sola fila)
SELECT clientes.id_cliente, clientes.nombre, total.gasto_total FROM clientes
JOIN (
	SELECT ventas.id_cliente, SUM(cantidad*precio_unitario) AS gasto_total
	FROM ventas
	JOIN detalle_venta ON detalle_venta.id_venta = ventas.id_venta
	GROUP BY ventas.id_cliente
	) total ON clientes.id_cliente = total.id_cliente
ORDER BY total.gasto_total DESC
LIMIT 1;

-- 3.24 Productos vendidos en la misma venta que el “iPhone 13”
# NO ME SALE

	