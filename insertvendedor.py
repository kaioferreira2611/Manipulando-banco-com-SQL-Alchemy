from coneccao import Session 
from bd import Vendedor 
from bd import Loja 


with Session() as session:
    vendedor= Vendedor(nome = 'Querio Junior', Loja=1)
    session.add(vendedor)
    session.commit()
    print('registro realizado')

from coneccao import session 
from coneccao import 
from bd import Venda
with Session () as session:

Vendas= Venda(carros = 'bmw x6', preco= 320.000 , comissão = 50.000, vendedor_id = 1)


session.add(Venda)
session.commit()
print("vendas registradads com sucesso")
