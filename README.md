# FEItv — Sistema de Streaming em Python

## O que foi feito
Sistema de streaming de filmes via terminal desenvolvido em Python,
com cadastro de usuários, login, busca de filmes, sistema de likes
e gerenciamento de listas de favoritos.

## Funcionalidades

### Acesso
- Cadastro de novo usuário (nome, sobrenome, telefone, email e senha)
- Login com email e senha
- Dados persistidos em arquivo `.txt`

### Pós-login
- **Buscar filmes** — pesquisa por nome com correspondência parcial
- **Listar filmes** — filtra filmes por gênero (Ação, Comédia, Drama, Terror, etc.)
- **Like / Dislike** — adiciona ou remove curtidas de um filme, atualizando o arquivo
- **Favoritos** — gerenciamento completo de listas pessoais de filmes

### Gerenciamento de Favoritos
- Criar lista
- Renomear lista
- Excluir lista
- Adicionar filme à lista
- Remover filme da lista

## Conceitos praticados
- Funções em Python
- Leitura e escrita em arquivos `.txt` com `open()`, modos `'r'`, `'a'` e `'w'`
- Manipulação de strings com `split()`, `strip()` e `join()`
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição com `while True` e `break`
- Entrada de dados com `input()`
- Conversão de tipos com `int()` e `str()`
- Busca com correspondência parcial usando `in` e `.lower()`

## Arquivos
- `projeto.py` — código principal do sistema
- `filmes.txt` — banco de dados com 100 filmes (id, título, gênero, ano, sinopse, curtidas)
- `cadastrando_usuarios.txt` — usuários cadastrados
- `favoritos.txt` — listas de favoritos por usuário

## Como executar
```bash
python projeto.py
```

## Observações
Projeto desenvolvido na matéria de Lógica de Programação — FEI, 1º semestre.
Sistema totalmente via terminal com persistência de dados em arquivos de texto.
