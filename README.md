# 💅 Sistema de Gestão de Salão (Versão Database)

Este projeto é uma evolução do sistema de agendamento, agora utilizando **Persistência de Dados** com SQLite e SQLAlchemy. O sistema permite salvar, listar e deletar agendamentos de forma permanente.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **SQLAlchemy**: ORM para comunicação com o banco de dados.
- **SQLite**: Banco de dados leve e local (arquivo `salao_oficial.db`).

## 🏗️ Arquitetura de Arquivos
- `banco.py`: Configuração da conexão e sessão do banco.
- `config.py`: Tabela de preços fixa para os serviços.
- `clientes.py`: Modelos de dados (ORM) com lógica de Herança e Polimorfismo.
- `agenda.py`: Métodos de CRUD (Criar, Ler e Deletar) no banco.
- `main.py`: Ponto de entrada do sistema.

## 💻 Conceitos Aplicados
- **ORM (Object-Relational Mapping):** Transformamos classes Python em tabelas de banco de dados.
- **Herança e Polimorfismo:** Diferentes tipos de clientes (VIP, Urgente) calculam preços de forma única, mas são salvos na mesma tabela.
- **Persistência:** Os dados não são perdidos ao fechar o programa.

## 🚀 Como Usar
1. Instale o SQLAlchemy: `pip install sqlalchemy`
2. Execute o arquivo `main.py`.
3. Para adicionar novos clientes, utilize o método `salvar()` da classe `Agenda`.

```python
# Exemplo de inserção no banco:
from agenda import Agenda
from clientes import ClienteVIP
from datetime import time

agenda = Agenda()
novo_vip = ClienteVIP("Beatriz", time(16,0), "Manicure")
agenda.salvar(novo_vip)