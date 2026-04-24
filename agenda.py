class Agenda:
    """Gerencia a lista de atendimentos do dia.""" 
    
    def __init__(self):
        self.lista_de_clientes = []

    def salvar(self, ficha_do_cliente):
        """Adiciona um objeto cliente à lista de agendamentos."""
        self.lista_de_clientes.append(ficha_do_cliente)
        print(f"✅ Agendamento de {ficha_do_cliente.nome} salvo com sucesso!")

    def cancelar(self, ficha_do_cliente):
        """Remove um agendamento da lista, caso ele exista."""
        if ficha_do_cliente in self.lista_de_clientes:
            self.lista_de_clientes.remove(ficha_do_cliente)
            print(f"❌ Agendamento de {ficha_do_cliente.nome} cancelado.")
        else:
            print("⚠️ Este cliente não está na agenda.")
        
    def exibir_tudo(self):
        """Imprime o relatório formatado de todos os agendamentos."""
        print("\n--- MEUS AGENDAMENTOS ---")
        for f in self.lista_de_clientes:
            print(f"{f.horario.strftime('%H:%M')} | {f.nome} | {f.procedimento} | R$ {f.aplicar_taxas():.2f} | {f.status}")