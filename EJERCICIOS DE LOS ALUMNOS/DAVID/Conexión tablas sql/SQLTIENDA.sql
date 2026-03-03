-- 1. PREPARACIÓN DEL ENTORNO
CREATE DATABASE IF NOT EXISTS TIENDA;
USE TIENDA;

-- Borramos las tablas en orden inverso a su creación para evitar errores de claves foráneas
DROP TABLE IF EXISTS producto;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS fabricante;

-- 2. CREACIÓN DE LA TABLA CLIENTES (5 registros solicitados)
CREATE TABLE clientes (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- 3. CREACIÓN DE LA TABLA FABRICANTE (Para marcas como Asus)
CREATE TABLE fabricante (
    codigo INT AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    PRIMARY KEY (codigo)
);

-- 4. CREACIÓN DE LA TABLA PRODUCTO
-- id: Autonumérico
-- nombre: Nombre del artículo
-- precio: Usamos DECIMAL para dinero (8 dígitos en total, 2 decimales)
-- codigo_fabricante: Conecta con la tabla fabricante
CREATE TABLE producto (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(8,2) NOT NULL,
    codigo_fabricante INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo)
);

-- 5. INSERCIÓN DE DATOS EN CLIENTES
INSERT INTO clientes (nombre, ciudad) VALUES 
('Alberto', 'Granada'),
('Ana', 'Madrid'),
('Diego', 'Sevilla'),
('Marta', 'Barcelona'),
('Javier', 'Valencia');

-- 6. INSERCIÓN DE DATOS EN FABRICANTE
INSERT INTO fabricante (nombre) VALUES ('Asus');

-- 7. INSERCIÓN DE DATOS EN PRODUCTO (Mínimo un valor)
-- Usamos el codigo_fabricante = 1 que corresponde a 'Asus'
INSERT INTO producto (nombre, precio, codigo_fabricante) 
VALUES ('Monitor 24 pulgadas Full HD', 155.99, 1);

