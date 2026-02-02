SELECT 
    nombre,
    CONCAT(precio, '€') AS euros,
    CONCAT(TRUNCATE(precio * 1.11, 2), '$') AS dolares
FROM producto;
