CREATE DATABASE trabalho_db;
USE trabalho_db;

CREATE TABLE Cliente (
	idCliente INT NOT NULl,
    nome VARCHAR(50) NOT NULl,
    telefone VARCHAR(20) NOT NULl,
    email VARCHAR(50) NOT NULl,
    endereco VARCHAR(100) NOT NULl,
    
    PRIMARY KEY(idCliente)
);


CREATE TABLE Pedido (
	idPedido INT NOT NULL,
    dataPedido DATE NOT NULL,
    valorPedido DECIMAL(5, 2) NOT NULL,
	idCliente INT NOT NULL,
    
    PRIMARY KEY (idPedido),
    FOREIGN KEY(idCliente) REFERENCES Cliente(idCliente)
);

CREATE TABLE Editora (
	idEditora INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    
    PRIMARY KEY(idEditora)
);


CREATE TABLE Livro (
	idLivro INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    ano  INT NOT NULL,
    ISBN VARCHAR(20) NOT NULL,
    preco DECIMAL(5, 2) NOT NULL,
    idEditora INT NOT NULL,

	PRIMARY KEY(idLivro),
    FOREIGN KEY(idEditora) REFERENCES Editora(idEditora)
);



CREATE TABLE ItemPedido (
	quantidade INT NOT NULL,
    valorItemPedido DECIMAL(5, 2) NOT NULL,
    idPedido INT NOT NULL,
    idLivro INT NOT NULL,
    
    FOREIGN KEY(idPedido) REFERENCES Pedido(idPedido),
    FOREIGN KEY(idLivro) REFERENCES Livro(idLivro)
);

CREATE TABLE Estoque (
	idLivro INT NOT NULL,
    quantidade INT NOT NULL,
    
    FOREIGN KEY(idLivro) REFERENCES Livro(idLivro)
);






-- Querys
-- 2
SELECT count(idLivro) AS "Quantidade livros" FROM Livro;


-- 3
SELECT nome FROM cliente ORDER BY nome;


-- 4
SELECT  e.nome AS "Nome Editora", l.titulo AS "Titulo Livro"
FROM editora e
INNER JOIN livro l ON e.idEditora = l.idEditora
ORDER BY e.nome DESC;


-- 5 (testado)
select nome, titulo, preco from Livro l  
INNER JOIN Editora e ON e.idEditora = l.idEditora;

select nome, titulo, preco  from Livro l  
INNER JOIN Editora e ON e.idEditora = l.idEditora
ORDER BY e.nome;

-- 5:
SELECT e.nome AS "Nome editora", avg(l.preco) AS "Média preços" from livro l
inner JOIN Editora e ON e.idEditora = l.idEditora
GROUP BY e.nome
ORDER BY e.nome;



-- 6
-- idCliente --> pedido;   idPedido --> ItemPedido
SELECT c.nome, sum(ip.quantidade) as "Quantidade" FROM Cliente c
INNER JOIN Pedido p ON p.idCliente = c.idCliente
INNER JOIN ItemPedido ip ON ip.idPedido = p.idPedido
GROUP BY c.nome
ORDER BY c.nome;



-- TESTE PARA O 6
SELECT 
    c.nome, ip.quantidade, l.titulo
FROM cliente c
JOIN pedido p ON c.idCliente = p.idCliente
JOIN itemPedido ip ON p.idPedido = ip.idPedido
JOIN livro l ON l.idLivro = ip.idLivro
order by nome;


