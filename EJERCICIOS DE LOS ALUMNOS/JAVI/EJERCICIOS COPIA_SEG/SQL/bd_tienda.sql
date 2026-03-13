-- Crear base de datos
CREATE DATABASE tienda;
USE tienda;

-- ============================
-- TABLA FABRICANTE
-- ============================
CREATE TABLE fabricante (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO fabricante (nombre) VALUES
('Samsung'),
('Lenovo'),
('Sony'),
('Asus'),
('HP'),
('Logitech'),
('Acer'),
('Xiaomi'),
('Dell'),
('Huawei');

-- ============================
-- TABLA PRODUCTO
-- ============================
CREATE TABLE producto (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    codigo_fabricante INT,
    FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo)
);

INSERT INTO producto (nombre, precio, codigo_fabricante) VALUES
('Portátil Lenovo IdeaPad', 599.99, 2),
('Monitor Samsung 24"', 149.99, 1),
('Ratón Logitech M185', 14.99, 6),
('Teclado Mecánico Asus', 49.99, 4),
('Auriculares Sony WH-CH510', 39.99, 3),
('Portátil HP Pavilion', 799.00, 5),
('Monitor Acer Nitro 27"', 219.00, 7),
('Altavoz Xiaomi Mi Speaker', 29.99, 8),
('Portátil Dell Inspiron', 699.00, 9),
('Monitor Huawei MateView', 399.00, 10),
('Webcam Logitech C920', 89.99, 6),
('Teclado HP Classic', 19.99, 5),
('Monitor Sony Bravia 32"', 499.00, 3),
('Portátil Asus ZenBook', 999.00, 4),
('Auriculares Samsung Buds', 129.00, 1);
