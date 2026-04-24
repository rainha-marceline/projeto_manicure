# clientes.py
from datetime import time
from config import TABELA_PRECOS


class Cliente:
    """Representa um cliente comum do salão."""
    def __init__(self, nome: str, horario: time, procedimento: str):
        """Inicializa os dados do cliente e define o preço base."""
        self.nome = nome
        self.horario = horario
        self.procedimento = procedimento
        self._pago = False
        # Busca o valor numérico na tabela, padrão 0 se não encontrado
        self.preco_base = TABELA_PRECOS.get(procedimento.lower(), 0)
        
    def aplicar_taxas(self):
        """Retorna o valor final. Pode ser sobrescrito por subclasses."""
        return self.preco_base
    
    def confirmar_pagamento(self):
        """Altera o status de pagamento para concluído."""
        self._pago = True

    @property
    def status(self):
        """Retorna uma representação visual do status de pagamento."""
        return "✅ Pago" if self._pago else "❌ Pendente"

class ClienteVIP(Cliente):
    """Cliente com benefícios especiais (Ex: Descontos)."""
    
    def aplicar_taxas(self):
        """Polimorfismo: Aplica 10% de desconto sobre o preço base."""
        return self.preco_base * 0.90

class ClienteUrgente(Cliente):
    """Cliente que requer atendimento imediato com taxa extra."""
    
    def aplicar_taxas(self):
        """Polimorfismo: Aplica taxa adicional de R$ 15,00."""
        return self.preco_base + 15.00