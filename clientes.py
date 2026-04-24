from sqlalchemy import Column, Integer, String, Boolean
from banco import Base
from config import TABELA_PRECOS # Necessário para o cálculo

class Cliente(Base):
    """Classe base que mapeia a tabela 'clientes' no banco de dados."""
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    horario_str = Column(String)
    procedimento = Column(String)
    pago = Column(Boolean, default=False)

    def __init__(self, nome, horario, procedimento):
        """Inicializa o cliente e prepara os dados para o banco."""
        self.nome = nome
        self.horario_str = str(horario)
        self.procedimento = procedimento
        # Definimos o preco_base buscando na tabela de configuração
        self.preco_base = TABELA_PRECOS.get(procedimento.lower(), 0)
        
    def aplicar_taxas(self):
        """Retorna o valor final (Polimorfismo)."""
        return self.preco_base
    
    def confirmar_pagamento(self):
        """Atualiza o status de pagamento."""
        self.pago = True

    @property
    def status(self):
        """Retorna um ícone visual baseado no valor booleano do banco."""
        return "✅ Pago" if self.pago else "❌ Pendente"

class ClienteVIP(Cliente):
    """Subclasse que aplica 10% de desconto via Polimorfismo."""
    def aplicar_taxas(self):
        return self.preco_base * 0.90

class ClienteUrgente(Cliente):
    """Subclasse que aplica taxa de R$ 15,00 via Polimorfismo."""
    def aplicar_taxas(self):
        return self.preco_base + 15.00