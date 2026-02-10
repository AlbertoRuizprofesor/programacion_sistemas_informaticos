-- --------------------------------------------------------
-- Host: 127.0.0.1
-- Versión del servidor: 8.0.31 - MySQL Community Server - GPL
-- HeidiSQL Versión: 12.5.0.6677
-- --------------------------------------------------------

-- Volcando estructura de base de datos para phoneland
CREATE DATABASE IF NOT EXISTS `phoneland_SUPERALBERTRON`;
USE `phoneland_SUPERALBERTRON`;

-- --------------------------------------------------------
-- TABLAS
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `proveedores` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre_proveedor` varchar(30) NOT NULL,
  `tlf_proveedor` varchar(10) NOT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=9;

CREATE TABLE IF NOT EXISTS `clientes` (
  `Id_CLIENTES` int NOT NULL,
  `fecha_de_alta` varchar(255) DEFAULT NULL,
  `cif_nif` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `CP` int DEFAULT NULL,
  `ciudad` varchar(255) DEFAULT NULL,
  `provincia` varchar(255) DEFAULT NULL,
  `empresa` varchar(255) DEFAULT NULL,
  `como_nos_conocio` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id_CLIENTES`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `productos` (
  `id_PRODUCTO` int NOT NULL,
  `id_proveedor` int NOT NULL,
  `NOMBRE` varchar(58) DEFAULT NULL,
  `FABRICANTE` varchar(7) DEFAULT NULL,
  `PRECIO` varchar(8) DEFAULT NULL,
  `PVP` decimal(10,2) DEFAULT NULL,
  `Descripcion` varchar(50) DEFAULT NULL,
  `fecha_entrada` date DEFAULT NULL,
  PRIMARY KEY (`id_PRODUCTO`),
  KEY `id_proveedor` (`id_proveedor`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedor`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `ventas` (
  `Id_VENTAS` int NOT NULL,
  `id_PRODUCTOS` int DEFAULT NULL,
  `Id_CLIENTES` int DEFAULT NULL,
  `FECHA_DE_VENTA` varchar(9) DEFAULT NULL,
  `UNIDADES` int DEFAULT NULL,
  `FEMISION` date DEFAULT NULL,
  PRIMARY KEY (`Id_VENTAS`),
  KEY `id_PRODUCTOS` (`id_PRODUCTOS`),
  KEY `Id_CLIENTES` (`Id_CLIENTES`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_PRODUCTOS`) REFERENCES `productos` (`id_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`Id_CLIENTES`) REFERENCES `clientes` (`Id_CLIENTES`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- --------------------------------------------------------
-- VOLCADO DE DATOS (EJEMPLOS)
-- --------------------------------------------------------

INSERT INTO `proveedores` (`id_proveedor`, `nombre_proveedor`, `tlf_proveedor`) VALUES
	(1, 'Apple', '123456789'), (3, 'XIOAMI', '1212323'), (5, 'SAMSUNG', '2323');

INSERT INTO `clientes` (`Id_CLIENTES`, `nombre`, `ciudad`) VALUES
	(1, 'ANA PEREZ', 'GRANADA'), (3, 'ALBERTO GONZALEZ', 'MALAGA'), (4, 'MARIO VARGAS', 'MALAGA');

INSERT INTO `productos` (`id_PRODUCTO`, `id_proveedor`, `NOMBRE`, `FABRICANTE`, `PRECIO`, `fecha_entrada`) VALUES
	(1, 3, 'XIAOMI IMI10LITE5G', 'XIOAMI', '220.00', '2023-10-18'),
	(3, 1, 'APPLE Iphone 11', 'APPLE', '650.00', '2023-10-18');

-- --------------------------------------------------------
-- FUNCIONES Y PROCEDIMIENTOS (LIMPIOS)
-- --------------------------------------------------------

DELIMITER //

CREATE FUNCTION `calcular_iva`(`precio` DECIMAL(10,2), `fabricante` VARCHAR(50)) RETURNS decimal(10,2)
DETERMINISTIC
BEGIN
    DECLARE iva DECIMAL(10,2);
    IF fabricante <> 'XIAOMI' THEN SET iva = precio * 0.21;
    ELSE SET iva = 0;
    END IF;
    RETURN iva;
END//

CREATE PROCEDURE `CalcularIvaYTotal`()
BEGIN
    SELECT nombre, precio, precio * 0.21 AS iva, precio * 1.21 AS total FROM productos; 
END//

DELIMITER ;