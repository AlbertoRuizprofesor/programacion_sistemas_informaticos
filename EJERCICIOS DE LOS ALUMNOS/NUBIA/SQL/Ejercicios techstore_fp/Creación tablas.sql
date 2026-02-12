CREATE TABLE clientes( 
  id_cliente INT AUTO_INCREMENT PRIMARY KEY, 
  nombre VARCHAR(60) NOT NULL, 
  email VARCHAR(80), 
  telefono VARCHAR(15), 
  ciudad VARCHAR(40), 
  fecha_alta DATE NOT NULL 
  ); 

CREATE TABLE categorias( 
  id_categoria INT AUTO_INCREMENT PRIMARY KEY, 
  nombre VARCHAR(40) NOT NULL UNIQUE
  ); 

CREATE TABLE productos( 
  id_producto INT AUTO_INCREMENT PRIMARY KEY, 
  nombre VARCHAR(80) NOT NULL, 
  precio DECIMAL(10,2) NOT NULL, 
  stock INT NOT NULL DEFAULT 0, 
  id_categoria INT NOT NULL
  ); 

CREATE TABLE ventas( 
  id_venta INT AUTO_INCREMENT PRIMARY KEY, 
  fecha DATE NOT NULL, 
  id_cliente INT NOT NULL, 
  metodo_pago ENUM('EFECTIVO','TARJETA','BIZUM') NOT NULL
  ); 

 

CREATE TABLE detalle_venta( 
  id_venta INT NOT NULL, 
  id_producto INT NOT NULL, 
  cantidad INT NOT NULL CHECK (cantidad > 0), 
  precio_unitario DECIMAL(10,2) NOT NULL
  ); 


