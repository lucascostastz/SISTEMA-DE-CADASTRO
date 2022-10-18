# SISTEMA-DE-CADASTRO
SISTEMA DE CADASTRO DESENVOLVIDO EM PYTHON

blibliotecas necessárias.

1- sqlite3
2- mysql.connector
3 - tkinter import messagebox
4- time
5- PyQt6
6 - sys


COMANDO PARA CRIAR banco de dados NO BANCO DE DADOS MYSQL:

CREATE DATABASE `teste` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

COMANDO PARA CRIAR tabela NO BANCO DE DADOS MYSQL:

TABELA PACIENTES:

CREATE TABLE `pacientes` (
  `idpacientes` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cpf` varchar(45) DEFAULT NULL,
  `sus` varchar(45) DEFAULT NULL,
  `telefone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `encaminhamento` varchar(45) DEFAULT NULL,
  `especialidade` varchar(45) DEFAULT NULL,
  `acompanhante` varchar(45) DEFAULT NULL,
  `almoco` varchar(45) DEFAULT NULL,
  `local_atendimento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpacientes`),
  UNIQUE KEY `idpacientes_UNIQUE` (`idpacientes`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

TABELA USUÁRIOS: 

CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `senha` varchar(45) NOT NULL,
  PRIMARY KEY (`idusuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;





Sistema desenvolvido para fins didáticos...Repasse seu conhecimento para o próximo.
