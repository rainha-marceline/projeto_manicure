from banco import sessao, motor, Base
from clientes import Cliente

class Agenda:
    """Classe responsável pela comunicação entre o Python e o SQLite."""
    
    def __init__(self):
        # Base.metadata cria o arquivo .db e as tabelas se não existirem
        Base.metadata.create_all(motor)

    def salvar(self, ficha):
        """Persiste os dados de um objeto Cliente no banco de dados."""
        sessao.add(ficha)
        sessao.commit()
        print(f"✅ {ficha.nome} guardada no Banco de Dados!")

    def cancelar(self, nome_cliente):
        """Busca e remove um registro pelo nome."""
        alvo = sessao.query(Cliente).filter_by(nome=nome_cliente).first()
        if alvo:
            sessao.delete(alvo)
            sessao.commit()
            print(f"❌ Agendamento de {nome_cliente} removido!")

    def exibir_tudo(self):
        """Recupera todos os registros e exibe formatado."""
        lista = sessao.query(Cliente).all()
        print("\n--- RELATÓRIO DO BANCO DE DADOS ---")
        for f in lista:
            # Note que agora usamos o f.status e f.horario_str salvo
            print(f"{f.horario_str} | {f.nome:10} | {f.procedimento:15} | {f.status}")