from coneccao import Session 
from bd import Loja

with Session as session:
     Loja (nome = "Kaio", endereco = 164 , gerente = "pedro")
     session.add(Loja)
     session.commit()
     print("deu certo")
    
