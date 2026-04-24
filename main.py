# main.py
from agenda import Agenda
from clientes import Cliente

def rodar_sistema():
    # 1. Ligamos a agenda (ela vai conectar no salao_oficial.db)
    minha_agenda = Agenda()

    # 2. Apenas mostramos o que já está guardado
    minha_agenda.exibir_tudo()

# --- ESTA É A CHAVE QUE FALTOU! ---
if __name__ == "__main__":
    rodar_sistema()