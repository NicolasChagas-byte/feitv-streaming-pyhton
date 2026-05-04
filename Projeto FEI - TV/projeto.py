def cadastrar():
    print('Então vamos criar-la...')
    nome = str(input('Digite seu nome: '))
    sobrenome = str(input('Digite seu sobrenome: '))
    telefone = int(input('Digite seu telefone: '))
    telefone_usuario = str(telefone)
    email = str(input('Digite seu email: '))
    senha_usuario = str(input('Digite sua senha: '))
    print('Ok. Conta criada com sucesso')
    
    arquivo = open('cadastrando_usuarios.txt', 'a')
    arquivo.write(nome + '|' + sobrenome + '|' + telefone_usuario + '|' + email + '|' + senha_usuario + '\n')
    arquivo.close()
    
def login():
    email = str(input('Digite seu email: '))
    senha_usuario = str(input('Digite sua senha: '))
    
    arquivo = open('cadastrando_usuarios.txt', 'r')
    for linha in arquivo:
        partes = linha.strip().split('|')
        if partes[3] == email and partes[4] == senha_usuario:
            print('Acesso Liberado!\n')
            menu_pos_login(email)
    arquivo.close()
        
def sair():
    print('Ok! Até logo')
    
def menu_pos_login(email):
    while True:
        print('1. Buscar filmes')
        print('2. Listar filmes')
        print('3. Like / Dislike')
        print('4. Favoritos')
        print('0. Sair')
        opcao = str(input('O que deseja fazer: '))
        
        if opcao == '1':
            print('Buscando filmes...')
            print('Achei!')
            buscar_filmes()
        elif opcao == '2':
            print('Listando filmes...')
            print('Achei!')
            listar_filmes()
        elif opcao == '3':
            print('Like / Dislike..')
            print('Achei!')
            like_dislike()
        elif opcao == '4':
            print('Favoritos...')
            favoritos(email)
        elif opcao == '0':
            print('Saindo...')
            break

def buscar_filmes():
    while True:
        nome_buscado = str(input('Digite o nome do filmes: '))
        
        if nome_buscado == '0':
            break
        
        arquivo = open('filmes.txt', 'r')
        for linhas in arquivo:
            partes = linhas.split('|')
            if nome_buscado.lower() in partes[1].lower():
                print('=======================')
                print(f'Titulo: {partes[1]}')
                print(f'Genero: {partes[2]}')
                print(f'Ano: {partes[3]}')
                print(f'Sinopse: {partes[4]}')
                print(f'Curtidas: {partes[5]}')
                print('=======================')
        arquivo.close()
    
def listar_filmes():
    while True:
        print('1. Acao')
        print('2. Comedia')
        print('3. Drama')
        print('4. Terror')
        print('5. Ficcao Cientifica')
        print('6. Animacao')
        print('7. Aventura')
        print('0. Sair')
        opcao = str(input('Escolha o genero de sua preferencia: '))
        
        if opcao == '1':
            genero = 'Acao'
        elif opcao == '2':
            genero = 'Comedia'
        elif opcao == '3':
            genero = 'Drama'
        elif opcao == '4':
            genero = 'Terror'
        elif opcao == '5':
            genero = 'Ficcao Cientifica'
        elif opcao == '6':
            genero = 'Animacao'
        elif opcao == '7':
            genero = 'Aventura'
        elif opcao == '0':
            print('Saindo...')
            break
        
        arquivo = open('filmes.txt', 'r')
        for linha in arquivo:
            partes = linha.split('|')
            if partes [2] == genero:
                print('=======================')
                print(f'Titulo: {partes[1]}')
                print(f'Genero: {partes[2]}')
                print(f'Ano: {partes[3]}')
                print(f'Sinopse: {partes[4]}')
                print(f'Curtidas: {partes[5]}')
                print('=======================')
        arquivo.close()

def like_dislike():
    nome_buscado = str(input('Digite o nome do filmes: '))
    linhas_arquivo = []
    
    arquivo = open('filmes.txt', 'r')
    for linhas in arquivo:
        partes = linhas.strip().split('|')
        if nome_buscado.lower() == partes[1].lower():
            print(f'Filme encontrado: {partes[1]}')
            print('1. Like')
            print('2. Dislike')
            opcao = str(input('O que voce deseja fazer? '))
            if opcao == '1':
                partes[5] = str(int(partes[5].replace('.', '')) + 1)
                print(f'Like adicionado com sucesso! Total de curtidas: {partes[5]}')
            elif opcao == '2':
                partes[5] = str(int(partes[5].replace('.', '')) - 1)
                print(f'Dislike adicionado com sucesso! Total de curtidas: {partes[5]}')
        linhas_arquivo.append('|'.join(partes) + '\n')
    arquivo.close()
    
    arquivo = open('filmes.txt', 'w')
    for linhas in linhas_arquivo:
        arquivo.write(linhas)
    arquivo.close()

def favoritos(email):
    while True:
        print('1. Criar listas')
        print('2. Editar o nome da lista')
        print('3. Excluir lista')
        print('4. Adicionar filme na lista')
        print('5. Remover filme na lista')
        print('0. Sair')
        opcao = str(input('O que deseja fazer: '))
        
        if opcao == '1':
            print('Criando uma lista...')
            print('Criei!')
            criar_lista(email)
        elif opcao == '2':
            print('Editando o nome da lista...')
            print('Editei!')
            editar_nome(email)
        elif opcao == '3':
            print('Excluindo a lista...')
            print('Exclui!')
            excluir_lista(email)
        elif opcao == '4':
            print('Adicionando um filme na lista...')
            print('Adicionei!')
            adicionar_lista(email)
        elif opcao == '5':
            print('Removendo um filme da lista...')
            print('Removi!')
            remover_lista(email)
        elif opcao == '0':
            print('Saindo...')
            break
        
def criar_lista(email):
    nome_lista = str(input('Digite o nome da lista: '))
    
    arquivo = open('favoritos.txt', 'a')
    arquivo.write(email + '|' + nome_lista + '|' + '\n')
    arquivo.close()
    
    print('Lista criada com sucesso!')

def editar_nome(email):
    nome_novo = str(input('Digite o novo nome da lista: '))
    nome_antigo = str(input('Digite o nome atual da lista: '))
    linhas_arquivo = []
    
    arquivo = open('favoritos.txt', 'r')
    for linha in arquivo:
        partes = linha.strip().split('|')
        if partes[0] == email and partes[1] == nome_antigo:
            partes[1] = nome_novo
        linhas_arquivo.append('|'.join(partes) + '\n')
    arquivo.close()
    
    arquivo = open('favoritos.txt', 'w')
    for linha in linhas_arquivo:
        arquivo.write(linha)
    arquivo.close()
    
    print('Lista renomeada com sucesso!')
    
def excluir_lista(email):
    nome_lista = str(input('Digite o nome da lista que quer excluir: '))
    linhas_arquivo = []
    
    arquivo = open('favoritos.txt', 'r')
    for linha in arquivo:
        partes = linha.strip().split('|')
        if partes[0] == email and partes[1] == nome_lista:
            pass
        else:
            linhas_arquivo.append(linha)
    arquivo.close()
    
    arquivo = open('favoritos.txt', 'w')
    for linha in linhas_arquivo:
        arquivo.write(linha)
    arquivo.close()
    
    print('Lista excluída com sucesso!')
    
def adicionar_lista(email):
    nome_lista = str(input('Digite o nome da lista: '))
    nome_filme = str(input('Digite o nome do filme: '))
    linhas_arquivo = []
    
    arquivo = open('favoritos.txt', 'r')
    for linha in arquivo:
        partes = linha.strip().split('|')
        if partes[0] == email and partes[1] == nome_lista:
            partes[2] = partes[2] + ',' + nome_filme
        linhas_arquivo.append('|'.join(partes) + '\n')
    arquivo.close()
    
    arquivo = open('favoritos.txt', 'w')
    for linha in linhas_arquivo:
        arquivo.write(linha)
    arquivo.close()
        
    print('Filme adicionado com sucesso!')
    
def remover_lista(email):
    nome_lista = str(input('Digite o nome da lista: '))
    nome_filme = str(input('Digite o nome do filme: '))
    linhas_arquivo = []
    
    arquivo = open('favoritos.txt', 'r')
    for linha in arquivo:
        partes = linha.strip().split('|')
        if partes[0] == email and partes[1] == nome_lista:
            filmes = partes[2].split(',')
            filmes.remove(nome_filme)
            partes[2] = ','.join(filmes)
        linhas_arquivo.append('|'.join(partes) + '\n')
    arquivo.close()
    
    arquivo = open('favoritos.txt', 'w')
    for linha in linhas_arquivo:
        arquivo.write(linha)
    arquivo.close()
    
    print('Filme removido com sucesso!')
    
# Codigo comeca a partir dessa linhna
print('===== Seja bem-vindo ao nosso FEItv!=====\n')

while True:
    print('1. Não tenho cadastro')
    print('2. Login')
    print('0. Sair')
    opcao = str(input('O que deseja fazer: '))
    
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        login()
    elif opcao == '0':
        sair()
        break