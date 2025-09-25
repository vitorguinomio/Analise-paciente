# 1. Objetivo

Esta documeto detalha a estrutura, as tecnologias e os objetivos do projeto. O prorpósito central é pesquisar e a aplicar práticas de DevOps em um contexto de Ciência de Dados (DataOps/MLOps), visando criar um sistema eficiente de de baixo custo para o gerenciamento de dados na triagem de pacientes em ambiente hospitalar.

# 2. Visão geral do Projeto
O Projeto visa otimizar o processo de triagem hospitais por meio de uma gestão de dados e preliminares de LLM. Atualmente, a coleta de informações dos pacientes é um processo manual, onde os dados são dividos em duas categorais principais:

+ Dados Voláteis (ou de Curto Prazo) Informações que mudam rapidamente, geralmente em um intervalo de até 24 horas.
	+ Exemplos: Pressão arterial, temperatura corporal, frequência cardiaca, saturação de oxigênio.
+ Dados Estáveis(ou de longo Prazo): Informações que permanecem constantes por longos períodos, mais que podem ser atualizados pontualmente.
	+ Exemplos: Altura, peso, tipo sanguíneo, nacionalidade, data de nascimento e histórico de alergias

O principal desafio é grantir que os dados estáveis, como peso e altura, sejam validados e, se necessário atualizados pela equipe de enfermagem durante a triagem, sem criar gargalos no processo. O sistema proposto buscará automatizar e captura e a organização dessas informações, permitindo que a equipe foque na análise clínica e a na tomada de decisão


# Estrutura de pasta
## Database
Pasta com todos os codigos referente a banco de dados. Todos vão ser escritos em SQL e PL/pgsql será usado o banco postgresql.
## Docs
Pasta com todos os arquivos markadown com toda documentação sobre resoluções e anotações do do projeto.
## Src
Tem a finalidade de separar o codigo-fonte ele reforça que e uma instalação editavel so e capaz de impota arquivos que devem ser realmente importados.
## Back
A pas