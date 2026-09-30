CREATE DATABASE IF NOT EXISTS oficina_mecanica
DEFAULT CHARSET = utf8mb4;

USE oficina_mecanica;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20)
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS veiculos (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    placa VARCHAR(10) NOT NULL,
    id_cliente INT NOT NULL,

    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
) DEFAULT CHARSET = utf8mb4;