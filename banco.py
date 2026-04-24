# banco.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria o arquivo do banco
motor = create_engine('sqlite:///salao_oficial.db')
Sessao = sessionmaker(bind=motor)
sessao = Sessao()
Base = declarative_base()