-- Insertar datos de clientes
INSERT INTO clientes (nombre,email,telefono,ciudad,fecha_alta) VALUES 
('Ana Ruiz','ana@correo.com','600111222','Málaga','2025-01-10'), 
('Luis Pérez','luis@correo.com','600222333','Sevilla','2025-02-05'), 
('María Díaz','maria@correo.com','600333444','Málaga','2025-03-12'), 
('Javier Soto',NULL,'600444555','Granada','2025-03-20'), 
('Carmen León','carmen@correo.com','600555666','Cádiz','2025-04-02'); 

-- Insertar datos de categorías
INSERT INTO categorias (nombre) VALUES 
('Smartphones'), 
('Portátiles'), 
('Accesorios'), 
('Componentes'); 

-- Insertar datos de productos
INSERT INTO productos (nombre,precio,stock,id_categoria) VALUES 
('iPhone 13',599.00,10,1), 
('Samsung A54',329.00,15,1), 
('Xiaomi Redmi Note 12',199.00,20,1), 
('Portátil Lenovo i5',749.00,8,2), 
('MacBook Air M1',899.00,5,2), 
('Auriculares Bluetooth',49.90,50,3), 
('Cargador USB-C 65W',29.90,40,3), 
('SSD 1TB',89.90,30,4), 
('RAM 16GB DDR4',59.90,25,4); 

-- Insertar datos de ventas
INSERT INTO ventas (fecha,id_cliente,metodo_pago) VALUES 
('2025-04-10',1,'TARJETA'), 
('2025-04-10',2,'BIZUM'), 
('2025-04-12',1,'EFECTIVO'), 
('2025-04-15',3,'TARJETA'), 
('2025-04-18',5,'TARJETA'); 

-- detalle: (id_venta, id_producto, cantidad, precio_unitario) 
INSERT INTO detalle_venta VALUES 
(1,1,1,599.00), 
(1,6,2,49.90), 
(2,3,1,199.00), 
(2,7,1,29.90), 
(3,2,1,329.00), 
(3,6,1,49.90),
(4,4,1,749.00), 
(4,8,1,89.90), 
(5,5,1,899.00), 
(5,7,2,29.90);