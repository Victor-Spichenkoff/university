use trabalho_db;

select count(idLivro) from livro;

-- 2
select * from Livro;

-- 4
select e.nome, l.titulo from Editora e
inner join livro l on e.idEditora = l.idEditora;



SELECT 
    e.nome AS NomeEditora, 
    l.titulo AS TituloLivro
FROM 
    Editora e
JOIN 
    Livro l ON e.idEditora = l.idEditora
ORDER BY 
    e.nome DESC;



-- 5 
select e.nome, avg(l.preco) from editora e
inner join livro l on e.idEditora = l.idEditora
GROUP  BY e.nome
;
-- teste: 
select e.nome, l.titulo, l.preco from editora e
inner join livro l on e.idEditora = l.idEditora
ORDER BY e.nome
;

-- 6
SELECT 
    c.nome, ip.quantidade, l.titulo
FROM cliente c
JOIN pedido p ON c.idCliente = p.idCliente
JOIN itemPedido ip ON p.idPedido = ip.idPedido
JOIN livro l ON l.idLivro = ip.idLivro
order by nome;