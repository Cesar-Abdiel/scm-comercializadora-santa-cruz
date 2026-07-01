CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    estado VARCHAR(20)
);

CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INTEGER
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    total DECIMAL(10,2),
    estado VARCHAR(20)
);
