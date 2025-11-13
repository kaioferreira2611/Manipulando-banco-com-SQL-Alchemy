CREATE TABLE produtos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
clienteid INTEGER,
produtoid INTEGER, 
quantidade INTEGER,
total REAL,
FOREIGN KEY (clienteid) REFERENCES clientes(id)
FOREIGN KEY (produtoid) REFERENCES produtos(id)