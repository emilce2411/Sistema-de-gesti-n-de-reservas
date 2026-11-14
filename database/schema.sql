-- =========================================================================
-- Proyecto: Reserva (Sistema de Reservas de Coworking)
-- Módulo: Base de Datos Relacional (MySQL)
-- Autor: Emilce Agustina Torres
-- =========================================================================

-- 1. Creación de la base de datos con el nombre simplificado
CREATE DATABASE IF NOT EXISTS reserva 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Seleccionar la base de datos a utilizar
USE reserva;

-- 2. Creación de la tabla USUARIO
-- Almacena la información de los clientes y administradores del sistema.
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) DEFAULT 'cliente'
) ENGINE=InnoDB;

-- 3. Creación de la tabla RESERVA
-- Almacena los turnos de la sala de coworking vinculados a un usuario específico.
CREATE TABLE reserva (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    estado VARCHAR(50) DEFAULT 'Confirmada',
    usuario_id INT NOT NULL,
    
    -- Restricción de Clave Foránea para asegurar la integridad referencial
    CONSTRAINT fk_reserva_usuario 
        FOREIGN KEY (usuario_id) 
        REFERENCES usuario(id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
) ENGINE=InnoDB;