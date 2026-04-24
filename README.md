# 💅 Sistema de Gestão de Salão de Beleza

Este projeto é um sistema de agendamento desenvolvido em Python, focado em organizar o fluxo de clientes e atendimentos de um salão de beleza. O código foi estruturado utilizando **Programação Orientada a Objetos (POO)** e modularização de arquivos para facilitar a manutenção e escalabilidade.

## 🚀 Funcionalidades

- **Agendamento Dinâmico:** Cadastro de clientes com busca automática de preços em tabela configurável.
- **Diferenciação de Categorias via Polimorfismo:**
  - **Cliente Comum:** Preço padrão da tabela.
  - **Cliente VIP:** Aplicação automática de 10% de desconto.
  - **Cliente Urgente:** Adição de taxa fixa de urgência (R$ 15,00).
- **Controle de Pagamentos:** Gestão de status (Pago/Pendente) com indicadores visuais.
- **Relatório de Agenda:** Exibição organizada contendo horário, nome, procedimento, valor final calculado e status.

## 🏗️ Estrutura do Projeto

O projeto está dividido em módulos para seguir as melhores práticas de desenvolvimento:

1.  **`config.py`**: Centraliza a `TABELA_PRECOS`, facilitando reajustes de valores sem mexer na lógica.
2.  **`clientes.py`**: Contém a lógica de negócio dos clientes, aplicando **Herança** e **Polimorfismo**.
3.  **`agenda.py`**: Gerencia a lista de atendimentos (Salvar, Cancelar e Exibir).
4.  **`main.py`**: Arquivo de execução onde os objetos são criados e os métodos chamados.

## 💻 Conceitos de POO Aplicados

O sistema demonstra o uso prático dos quatro pilares da POO:
- **Abstração:** Modelagem das entidades do mundo real (`Cliente` e `Agenda`).
- **Encapsulamento:** Proteção do atributo `_pago` e uso de `@property` para exposição segura de dados.
- **Herança:** Reuso de código onde `ClienteVIP` e `ClienteUrgente` herdam da classe base `Cliente`.
- **Polimorfismo:** O método `aplicar_taxas` se adapta ao tipo de objeto, permitindo que a `Agenda` processe diferentes cálculos de forma genérica.

## 🛠️ Como Executar

1.  Certifique-se de que os arquivos `config.py`, `clientes.py` e `agenda.py` estão na mesma pasta.
2.  Crie um arquivo chamado `main.py` e utilize o exemplo abaixo:

```python
from datetime import time
from agenda import Agenda
from clientes import Cliente, ClienteVIP, ClienteUrgente

# 1. Instanciar a Agenda
minha_agenda = Agenda()

# 2. Criar Clientes (Normal, VIP e Urgente)
c1 = Cliente("Ana Silva", time(14, 0), "manicure")
c2 = ClienteVIP("Beatriz Oliveira", time(15, 30), "manicure e pedicure")
c3 = ClienteUrgente("Carla Souza", time(17, 0), "pedicure")

# 3. Salvar na Agenda
minha_agenda.salvar(c1)
minha_agenda.salvar(c2)
minha_agenda.salvar(c3)

# 4. Confirmar Pagamento
c2.confirmar_pagamento()

# 5. Exibir Relatório
minha_agenda.exibir_tudo()