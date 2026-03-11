# Teste Prático para Kodland

Teste prático para a empresa Kodlang

## Função do bot
- é um bot simples que comando de !pay

## Stack usadas
- Python 3.12 (3.12.10)
- Sqlite3

## Como Testar
O teste está contando que você já baixou o projeto e o python.

Nota: O database.db não tem sistema de migrations para criar as tabelas, então eu deixei o arquivo já pronto.
Nota: Como o projeto foi desenvolvido rapidamente para o teste, o código não implementa o fechamento das conexões com o banco de dados. (O conexão é com o próprio tempo mínimo de conexão.)

- Troque o nome do `env` para `.env` e preencha as informações.
- Use `python3 app.py` no terminal do seu editor de código
- Entre no discord e use !help

## Nota

Por ser um teste, eu fiz a classe Database de forma rápida (não é um ORM), e o service faz todas as requisições. Sei que não é a maneira mais profissional, mas é a mais simples.