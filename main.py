

from fastapi import FastAPI
from datetime import datetime
import sqlite3


app = FastAPI()


# Criar conexão com o banco de dados
conn = sqlite3.connect('chamados.db')
cursor = conn.cursor()

# Criar tabela de CHAMADO se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbChamado (
    ID INTEGER PRIMARY KEY,
    titulo TEXT,
    descricao INTEGER,
    especialidadeID INTEGER,
    data_abertura DATE,
    data_encerramento DATE,
    prioridadeID INTEGER,
    statusID INTEGER,
    computadorID INTEGER,
    departamentoID INTEGER,
    tecnicoID INTEGER,
    usuarioID INTEGER,
    FOREIGN KEY (especialidadeID) REFERENCES tbEspecialidade(ID),
    FOREIGN KEY (prioridadeID) REFERENCES tbPrioridade(ID),
    FOREIGN KEY (statusID) REFERENCES tbStatus(ID),
    FOREIGN KEY (computadorID) REFERENCES tbComputador(ID),
    FOREIGN KEY (departamentoID) REFERENCES tbDepartamento(ID),
    FOREIGN KEY (tecnicoID) REFERENCES tbTecnico(ID),
    FOREIGN KEY (usuarioID) REFERENCES tbUsuario(ID)
)
''')

# Criar tabela de COMPUTADOR se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbComputador (
    ID INTEGER PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    numero_serie TEXT,
    SO_ID INTEGER,
    data_aquisicao DATE,
    departamentoID INTEGER,
    usuarioID INTEGER,
    FOREIGN KEY (SO_ID) REFERENCES tbSO(ID),
    FOREIGN KEY (departamentoID) REFERENCES tbDepartamento(ID),
    FOREIGN KEY (usuarioID) REFERENCES tbUsuario(ID)
)
''')

# Criar tabela de STATUS se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbStatus (
    ID INTEGER PRIMARY KEY,
    status TEXT
)
''')

# Criar tabela de PRIORIDADE se não existir
cursor.execute( '''
CREATE TABLE IF NOT EXISTS tbPrioridade (
    ID INTEGER PRIMARY KEY,
    prioridade TEXT
)
''')

# Criar tabela de TECNICO se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbTecnico (
    ID INTEGER PRIMARY KEY,
    nome_tec TEXT,
    idade INTEGER,
    email TEXT,
    especialidadeID INTEGER,
    FOREIGN KEY (especialidadeID) REFERENCES tbEspecialidade(ID)
)
''')

# Criar tabela de USUARIO se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbUsuario (
    ID INTEGER PRIMARY KEY,
    nome_usuario TEXT,
    idade INTEGER,
    email TEXT,
    departamentoID INTEGER,
    FOREIGN KEY (departamentoID) REFERENCES tbDepartamento(ID)
)
''')

# Criar tabela de DEPARTAMENTO se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbDepartamento (
    ID INTEGER PRIMARY KEY,
    departamento TEXT
)
''')

# Criar tabela de ESPECIALIDADE se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbEspecialidade (
    ID INTEGER PRIMARY KEY,
    especialidade TEXT
)
''')

# Criar tabela de SISTEMA OPERACIONAL se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tbSO (
    ID INTEGER PRIMARY KEY,
    SO TEXT
)
''')

class Chamado:
    def __init__(self, ID, titulo, descricao, especialidade, data_abertura, data_encerramento, prioridade, status, computador, departamento, tecnico, usuario):
        self.ID = ID
        self.titulo = titulo
        self.descricao = descricao
        self.especialidade = especialidade
        self.data_abertura = data_abertura
        self.data_encerramento = data_encerramento
        self.prioridade = prioridade
        self.status = status
        self.computador = computador
        self.departamento = departamento
        self.tecnico = tecnico
        self.usuario = usuario

class Computador:
    def __init__(self, ID, marca, modelo, numero_serie, SO, data_aquisicao, departamento, usuario):
        self.ID = ID
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.SO = SO
        self.data_aquisicao = data_aquisicao
        self.departamento = departamento
        self.usuario = usuario

class Tecnico:
    def __init__(self, ID, nome_tec, idade, email, especialidade):
        self.ID = ID
        self.nome_tec = nome_tec
        self.idade = idade
        self.email = email
        self.especialidade = especialidade

class Usuario:
    def __init__(self, ID, nome_usuario, idade, email, departamento):
        self.ID = ID
        self.nome_usuario = nome_usuario
        self.idade = idade
        self.email = email
        self.departamento = departamento

class Status:
    def __init__(self, ID, status):
        self.ID = ID
        self.status = status

class Prioridade:
    def __init__(self, ID, prioridade):
        self.ID = ID
        self.prioridade = prioridade

class Departamento:
    def __init__(self, ID, departamento):
        self.ID = ID
        self.departamento = departamento

class Especialidade:
    def __init__(self, ID, especialidade):
        self.ID = ID
        self.especialidade = especialidade

class SO:
    def __init__(self, ID, SO):
        self.ID = ID
        self.SO = SO

# Dados dos CHAMADOS
tbChamado = [
    {
        "ID": 1,
        "titulo": "Problema com a impressora",
        "descricao":
        "A impressora não está respondendo quando tento imprimir.",
        "especialidadeID": 1,
        "data_abertura": datetime(2023, 8, 1),
        "data_encerramento": datetime(2023, 8, 2),
        "prioridadeID": 1,
        "statusID": 1,
        "computadorID": 1,
        "departamentoID": 1,
        "tecnicoID": 1,
        "usuarioID": 1
    },
    {
        "ID": 2,
        "titulo": "Erro ao acessar o software",
        "descricao": "Recebo uma mensagem de erro ao tentar abrir o software.",
        "especialidadeID": 2,
        "data_abertura": datetime(2023, 8, 2),
        "data_encerramento": datetime(2023, 8, 3),
        "prioridadeID": 2,
        "statusID": 2,
        "computadorID": 2,
        "departamentoID": 2,
        "tecnicoID": 2,
        "usuarioID": 2
    },
    {
        "ID": 3,
        "titulo": "Computador lento",
        "descricao":
        "Meu computador está demorando muito para iniciar e executar programas.",
        "especialidadeID": 3,
        "data_abertura": datetime(2023,8,3),
        "data_encerramento": datetime(2023,8,4),
        "prioridadeID": 3,
        "statusID": 3,
        "computadorID": 3,
        "departamentoID": 3,
        "tecnicoID": 3,
        "usuarioID": 3
    },
    {
        "ID": 4,
        "titulo": "Problema de conexão à rede",
        "descricao": "Não consigo me conectar à rede Wi-Fi da empresa.",
        "especialidadeID": 4,
        "data_abertura": datetime(2023,8,4),
        "data_encerramento": datetime(2023,8,5),
        "prioridadeID": 4,
        "statusID": 4,
        "computadorID": 4,
        "departamentoID": 4,
        "tecnicoID": 4,
        "usuarioID": 4
    },
    {
        "ID": 5,
        "titulo": "Erro no email corporativo",
        "descricao":
        "Não estou conseguindo enviar ou receber emails pelo cliente de email.",
        "especialidadeID": 1,
        "data_abertura": datetime(2023,8,5),
        "data_encerramento": datetime(2023,8,6),
        "prioridadeID": 5,
        "statusID": 1,
        "computadorID": 5,
        "departamentoID": 5,
        "tecnicoID": 5,
        "usuarioID": 5
    },
    {
        "ID": 6,
        "titulo": "Atualização de software necessária",
        "descricao":
        "Recebi uma notificação sobre uma atualização de software importante.",
        "especialidadeID": 2,
        "data_abertura": datetime(2023,8,6),
        "data_encerramento": datetime(2023,8,7),
        "prioridadeID": 6,
        "statusID": 2,
        "computadorID": 6,
        "departamentoID": 1,
        "tecnicoID": 6,
        "usuarioID": 6
    },
    {
        "ID": 7,
        "titulo": "Tela do laptop quebrada",
        "descricao": "Deixei o laptop cair e agora a tela está quebrada.",
        "especialidadeID": 3,
        "data_abertura": datetime(2023,8,7),
        "data_encerramento": datetime(2023,8,8),
        "prioridadeID": 1,
        "statusID": 3,
        "computadorID": 7,
        "departamentoID": 2,
        "tecnicoID": 7,
        "usuarioID": 7
    },
    {
        "ID": 8,
        "titulo": "Problema com o mouse",
        "descricao":
        "O cursor do mouse não se move na tela, mesmo que o mouse esteja funcionando.",
        "especialidadeID": 4,
        "data_abertura": datetime(2023,8,8),
        "data_encerramento": datetime(2023,8,9),
        "prioridadeID": 2,
        "statusID": 4,
        "computadorID": 8,
        "departamentoID": 3,
        "tecnicoID": 8,
        "usuarioID": 8
    },
    {
        "ID": 9,
        "titulo": "Senha de acesso esquecida",
        "descricao": "Esqueci minha senha de acesso à rede interna.",
        "especialidadeID": 1,
        "data_abertura": datetime(2023,8,9),
        "data_encerramento": datetime(2023,8,10),
        "prioridadeID": 3,
        "statusID": 1,
        "computadorID": 9,
        "departamentoID": 4,
        "tecnicoID": 9,
        "usuarioID": 9
    },
    {
        "ID": 10,
        "titulo": "Erro na instalação do programa",
        "descricao":
        "Estou tendo problemas para instalar um novo programa no meu computador.",
        "especialidadeID": 2,
        "data_abertura": datetime(2023,8,10),
        "data_encerramento": datetime(2023,8,11),
        "prioridadeID": 4,
        "statusID": 2,
        "computadorID": 10,
        "departamentoID": 5,
        "tecnicoID": 10,
        "usuarioID": 10
    },
    {
        "ID": 11,
        "titulo": "Problema com a impressora a laser",
        "descricao":
        "A impressora a laser está apresentando problemas ao imprimir documentos.",
        "especialidadeID": 3,
        "data_abertura": datetime(2023,8,11),
        "data_encerramento": datetime(2023,8,12),
        "prioridadeID": 5,
        "statusID": 1,
        "computadorID": 6,
        "departamentoID": 1,
        "tecnicoID": 6,
        "usuarioID": 6
    },
    {
        "ID": 12,
        "titulo": "Aplicativo travando ao abrir arquivos grandes",
        "descricao":
        "O aplicativo fecha inesperadamente ao tentar abrir arquivos grandes.",
        "especialidadeID": 1,
        "data_abertura": datetime(2023,8,12),
        "data_encerramento": datetime(2023,8,13),
        "prioridadeID": 2,
        "statusID": 2,
        "computadorID": 7,
        "departamentoID": 2,
        "tecnicoID": 7,
        "usuarioID": 7
    },
    {
        "ID": 13,
        "titulo": "Solicitação de redefinição de senha de email",
        "descricao":
        "Esqueci minha senha de email e gostaria de solicitar uma redefinição.",
        "especialidadeID": 4,
        "data_abertura": datetime(2023,8,13),
        "data_encerramento": datetime(2023,8,14),
        "prioridadeID": 3,
        "statusID": 3,
        "computadorID": 8,
        "departamentoID": 3,
        "tecnicoID": 8,
        "usuarioID": 8
    },
    {
        "ID": 14,
        "titulo": "Erro ao acessar a VPN corporativa",
        "descricao":
        "Estou recebendo um erro ao tentar acessar a VPN da empresa.",
        "especialidadeID": 2,
        "data_abertura": datetime(2023,8,14),
        "data_encerramento": datetime(2023,8,15),
        "prioridadeID": 4,
        "statusID": 4,
        "computadorID": 9,
        "departamentoID": 4,
        "tecnicoID": 9,
        "usuarioID": 6
    },
    {
        "ID": 15,
        "titulo": "Dispositivo móvel não está sincronizando emails",
        "descricao":
        "Meu dispositivo móvel não está sincronizando meus emails corporativos corretamente.",
        "especialidadeID": 3,
        "data_abertura": datetime(2023,8,15),
        "data_encerramento": datetime(2023,8,16),
        "prioridadeID": 1,
        "statusID": 1,
        "computadorID": 10,
        "departamentoID": 5,
        "tecnicoID": 10,
        "usuarioID": 7
    },
]

# Dados dos COMPUTADORES
tbComputador = [
    {
        "ID": 1,
        "marca": "Dell",
        "modelo": "Latitude 5500",
        "numero_serie": "SN123456789",
        "SO_ID": 2,
        "data_aquisicao": datetime(2022,1,15),
        "departamentoID": 3,
        "usuarioID": 7
    },
    {
        "ID": 2,
        "marca": "HP",
        "modelo": "EliteBook 840 G7",
        "numero_serie": "SN987654321",
        "SO_ID": 4,
        "data_aquisicao": datetime(2021,6,20),
        "departamentoID": 2,
        "usuarioID": 3
    },
    {
        "ID": 3,
        "marca": "Lenovo",
        "modelo": "ThinkPad X1 Carbon",
        "numero_serie": "SN567891234",
        "SO_ID": 1,
        "data_aquisicao": datetime(2023,3,10),
        "departamentoID": 5,
        "usuarioID": 10
    },
    {
        "ID": 4,
        "marca": "Apple",
        "modelo": "MacBook Pro",
        "numero_serie": "SN345678912",
        "SO_ID": 5,
        "data_aquisicao": datetime(2020,9,5),
        "departamentoID": 1,
        "usuarioID": 1
    },
    {
        "ID": 5,
        "marca": "Dell",
        "modelo": "XPS 15",
        "numero_serie": "SN789123456",
        "SO_ID": 3,
        "data_aquisicao": datetime(2022,11,30),
        "departamentoID": 4,
        "usuarioID": 5
    },
    {
        "ID": 6,
        "marca": "HP",
        "modelo": "Pavilion 14",
        "numero_serie": "SN456789123",
        "SO_ID": 2,
        "data_aquisicao": datetime(2021,3,12),
        "departamentoID": 3,
        "usuarioID": 8
    },
    {
        "ID": 7,
        "marca": "Lenovo",
        "modelo": "IdeaPad 5",
        "numero_serie": "SN234567891",
        "SO_ID": 4,
        "data_aquisicao": datetime(2023,7,18),
        "departamentoID": 2,
        "usuarioID": 2
    },
    {
        "ID": 8,
        "marca": "Acer",
        "modelo": "Aspire 5",
        "numero_serie": "SN891234567",
        "SO_ID": 1,
        "data_aquisicao": datetime(2020,5,3),
        "departamentoID": 5,
        "usuarioID": 9
    },
    {
        "ID": 9,
        "marca": "Dell",
        "modelo": "Inspiron 13",
        "numero_serie": "SN678912345",
        "SO_ID": 5,
        "data_aquisicao": datetime(2022,8,25),
        "departamentoID": 1,
        "usuarioID": 4
    },
    {
        "ID": 10,
        "marca": "Apple",
        "modelo": "MacBook Air",
        "numero_serie": "SN123457890",
        "SO_ID": 3,
        "data_aquisicao": datetime(2021,12,8),
        "departamentoID": 4,
        "usuarioID": 6
    },
]

# Dados dos status
tbStatus = [
    {
        "ID": 1,
        "status": "aberto"
    },
    {
        "ID": 2,
        "status": "solucionado"
    },
    {
        "ID": 3,
        "status": "atrasado"
    },
    {
        "ID": 4,
        "status": "fechado"
    },
]

# Dados dos graus de prioridade
tbPrioridade = [
    {
        "ID": 1,
        "prioridade": "muito baixa"
    },
    {
        "ID": 2,
        "prioridade": "baixa"
    },
    {
        "ID": 3,
        "prioridade": "media"
    },
    {
        "ID": 4,
        "prioridade": "alta"
    },
    {
        "ID": 5,
        "prioridade": "muito alta"
    },
    {
        "ID": 6,
        "prioridade": "critico"
    },
]

# Dados dos técnicos
tbTecnico = [
    {
        "ID": 1,
        "nome_tec": "Ricardo Silva",
        "idade": 27,
        "email": "ricardo@example.com",
        "especialidadeID": 2
    },
    {
        "ID": 2,
        "nome_tec": "Isabela Santos",
        "idade": 22,
        "email": "isabela@example.com",
        "especialidadeID": 3
    },
    {
        "ID": 3,
        "nome_tec": "Fernando Costa",
        "idade": 24,
        "email": "fernando@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 4,
        "nome_tec": "Amanda Rodrigues",
        "idade": 20,
        "email": "amanda@example.com",
        "especialidadeID": 4
    },
    {
        "ID": 5,
        "nome_tec": "André Oliveira",
        "idade": 31,
        "email": "andre@example.com",
        "especialidadeID": 2
    },
    {
        "ID": 6,
        "nome_tec": "Carolina Pereira",
        "idade": 33,
        "email": "carolina@example.com",
        "especialidadeID": 3
    },
    {
        "ID": 7,
        "nome_tec": "Gabriel Fernandes",
        "idade": 30,
        "email": "gabriel@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 8,
        "nome_tec": "Lúcia Almeida",
        "idade": 40,
        "email": "lucia@example.com",
        "especialidadeID": 4
    },
    {
        "ID": 9,
        "nome_tec": "Mário Santos",
        "idade": 24,
        "email": "mario@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 10,
        "nome_tec": "Lara Lima",
        "idade": 26,
        "email": "lara@example.com",
        "especialidadeID": 2
    },
]

# Dados dos tipos de departamentos
tbDepartamento = [
    {
        "ID": 1,
        "departamento": "RH"
    },
    {
        "ID": 2,
        "departamento": "Financeiro"
    },
    {
        "ID": 3,
        "departamento": "TI"
    },
    {
        "ID": 4,
        "departamento": "Marketing"
    },
    {
        "ID": 5,
        "departamento": "Comercial"
    },
]

# Dados dos usuarios
tbUsuario = [
    {
        "ID": 1,
        "idade": 25,
        "nome_usuario": "João Silva",
        "email": "joao@example.com",
        "departamentoID": 1
    },
    {
        "ID": 2,
        "idade": 30,
        "nome_usuario": "Maria Santos",
        "email": "maria@example.com",
        "departamentoID": 2
    },
    {
        "ID": 3,
        "idade": 28,
        "nome_usuario": "Pedro Oliveira",
        "email": "pedro@example.com",
        "departamentoID": 3
    },
    {
        "ID": 4,
        "idade": 22,
        "nome_usuario": "Ana Souza",
        "email": "ana@example.com",
        "departamentoID": 4
    },
    {
        "ID": 5,
        "idade": 32,
        "nome_usuario": "Luiz Pereira",
        "email": "luiz@example.com",
        "departamentoID": 5
    },
    {
        "ID": 6,
        "idade": 27,
        "nome_usuario": "Juliana Costa",
        "email": "juliana@example.com",
        "departamentoID": 1
    },
    {
        "ID": 7,
        "idade": 29,
        "nome_usuario": "Rafael Almeida",
        "email": "rafael@example.com",
        "departamentoID": 2
    },
    {
        "ID": 8,
        "idade": 24,
        "nome_usuario": "Camila Rodrigues",
        "email": "camila@example.com",
        "departamentoID": 3
    },
    {
        "ID": 9,
        "idade": 26,
        "nome_usuario": "Gustavo Carvalho",
        "email": "gustavo@example.com",
        "departamentoID": 4
    },
    {
        "ID": 10,
        "idade": 31,
        "nome_usuario": "Fernanda Lima",
        "email": "fernanda@example.com",
        "departamentoID": 5
    },
]

# Dados dos tipos de especialidades
tbEspecialidade = [
    {
        "ID": 1,
        "especialidade": "Help Desk"
    },
    {
        "ID": 2,
        "especialidade": "Service Desk"
    },
    {
        "ID": 3,
        "especialidade": "Redes e Segurança"
    },
    {
        "ID": 4,
        "especialidade": "Field Service"
    },
]

# Dados dos tipos de sistemas operacionais.
tbSO = [
    {
        "ID": 1,
        "SO": "Windows 10"
    },
    {
        "ID": 2,
        "SO": "Windows 11"
    },
    {
        "ID": 3,
        "SO": "Ubuntu 20.04"
    },
    {
        "ID": 4,
        "SO": "macOS Big Sur"
    },
    {
        "ID": 5,
        "SO": "Chrome OS"
    },
]

# Declaração de Chamados
chamados = []

for i in range(len(tbChamado)):
  
    chamado = Chamado(tbChamado[i]['ID'], tbChamado[i]['titulo'], tbChamado[i]['descricao'], tbChamado[i]['especialidadeID'], tbChamado[i]['data_abertura'], tbChamado[i]['data_encerramento'], tbChamado[i]['prioridadeID'], tbChamado[i]['statusID'], tbChamado[i]['computadorID'], tbChamado[i]['departamentoID'], tbChamado[i]['tecnicoID'], tbChamado[i]['usuarioID'])
  
    chamados.append(chamado)


# Declaração Computadores
computadores = []

for i in range(len(tbComputador)):
  
    computador = Computador(tbComputador[i]['ID'], tbComputador[i]['marca'], tbComputador[i]['modelo'], tbComputador[i]['numero_serie'], tbComputador[i]['SO_ID'], tbComputador[i]['data_aquisicao'], tbComputador[i]['departamentoID'], tbComputador[i]['usuarioID'])
  
    computadores.append(computador)


# Declaração Tecnicos
tecnicos = []

for i in range(len(tbTecnico)):
  
    tecnico = Tecnico(tbTecnico[i]['ID'], tbTecnico[i]['nome_tec'], tbTecnico[i]['idade'], tbTecnico[i]['email'], tbTecnico[i]['especialidadeID'])
  
    tecnicos.append(tecnico)


# Declaração Usuarios
usuarios = []

for i in range(len(tbUsuario)):
  
    usuario = Usuario(tbUsuario[i]['ID'], tbUsuario[i]['nome_usuario'], tbUsuario[i]['idade'], tbUsuario[i]['email'], tbUsuario[i]['departamentoID'])
  
    usuarios.append(usuario)


# Declaração Status
all_status = []

for i in range(len(tbStatus)):
  
    status = Status(tbStatus[i]['ID'], tbStatus[i]['status'])
  
    all_status.append(status)


# Declaração Prioridades
prioridades = []

for i in range(len(tbPrioridade)):
  
    prioridade = Prioridade(tbPrioridade[i]['ID'], tbPrioridade[i]['prioridade'])
  
    prioridades.append(prioridade)


# Declaração Departamentos
departamentos = []

for i in range(len(tbDepartamento)):
  
    departamento = Departamento(tbDepartamento[i]['ID'], tbDepartamento[i]['departamento'])
  
    departamentos.append(departamento)


# Declaração Especialidades
especialidades = []

for i in range(len(tbEspecialidade)):
  
    especialidade = Status(tbEspecialidade[i]['ID'], tbEspecialidade[i]['especialidade'])
  
    especialidades.append(especialidade)


# Declaração Sistemas Operacionais
SOs = []

for i in range(len(tbSO)):
  
    So = SO(tbSO[i]['ID'], tbSO[i]['SO'])
  
    SOs.append(So)


# Inserir dados de chamados
for chamado in tbChamado:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbChamado WHERE ID = ?', (chamado['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbChamado (ID, titulo, descricao, especialidadeID, data_abertura, data_encerramento, prioridadeID, statusID, computadorID, departamentoID, tecnicoID, usuarioID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            chamado['ID'],
            chamado['titulo'],
            chamado['descricao'],
            chamado['especialidadeID'],
            chamado['data_abertura'].strftime('%Y-%m-%d'),
            chamado['data_encerramento'].strftime('%Y-%m-%d'),
            chamado['prioridadeID'],
            chamado['statusID'],
            chamado['computadorID'],
            chamado['departamentoID'],
            chamado['tecnicoID'],
            chamado['usuarioID']
        ))
    else:
        print(f"Chamado com ID {chamado['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Computador
for computador in tbComputador:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbComputador WHERE ID = ?', (computador['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbComputador (ID, marca, modelo, numero_serie, SO_ID, data_aquisicao, departamentoID, usuarioID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            computador['ID'],
            computador['marca'],
            computador['modelo'],
            computador['numero_serie'],
            computador['SO_ID'],
            computador['data_aquisicao'].strftime('%Y-%m-%d'),
            computador['departamentoID'],
            computador['usuarioID']
        ))
    else:
        print(f"Computador com ID {computador['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Tecnico
for tecnico in tbTecnico:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbTecnico WHERE ID = ?', (tecnico['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbTecnico (ID, nome_tec, idade, email, especialidadeID)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            tecnico['ID'],
            tecnico['nome_tec'],
            tecnico['idade'],
            tecnico['email'],
            tecnico['especialidadeID']
        ))
    else:
        print(f"Tecnico com ID {tecnico['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Usuario
for usuario in tbUsuario:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbUsuario WHERE ID = ?', (usuario['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbUsuario (ID, nome_usuario, idade, email, departamentoID)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            usuario['ID'],
            usuario['nome_usuario'],
            usuario['idade'],
            usuario['email'],
            usuario['departamentoID']
        ))
    else:
        print(f"Usuario com ID {usuario['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Status
for status in tbStatus:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbStatus WHERE ID = ?', (status['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbStatus (ID, status)
            VALUES (?, ?)
        ''', (
            status['ID'],
            status['status']
        ))
    else:
        print(f"Status com ID {status['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Prioridade
for prioridade in tbPrioridade:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbPrioridade WHERE ID = ?', (prioridade['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbPrioridade (ID, prioridade)
            VALUES (?, ?)
        ''', (
            prioridade['ID'],
            prioridade['prioridade']
        ))
    else:
        print(f"Prioridade com ID {status['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Departamento
for departamento in tbDepartamento:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbDepartamento WHERE ID = ?', (departamento['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbDepartamento (ID, departamento)
            VALUES (?, ?)
        ''', (
            departamento['ID'],
            departamento['departamento']
        ))
    else:
        print(f"Departamento com ID {departamento['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Especialidade
for especialidade in tbEspecialidade:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbEspecialidade WHERE ID = ?', (especialidade['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbEspecialidade (ID, especialidade)
            VALUES (?, ?)
        ''', (
            especialidade['ID'],
            especialidade['especialidade']
        ))
    else:
        print(f"Especialidade com ID {especialidade['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Inserir dados de Sistema Operacional
for SO in tbSO:
    # Verificar se o ID já existe
    cursor.execute('SELECT ID FROM tbSO WHERE ID = ?', (SO['ID'],))
    existing_ID = cursor.fetchone()
    
    if existing_ID is None:
        cursor.execute('''
            INSERT INTO tbSO (ID, SO)
            VALUES (?, ?)
        ''', (
            SO['ID'],
            SO['SO']
        ))
    else:
        print(f"SO com ID {SO['ID']} já cadastrado. Ignorando inserção.")
        
conn.commit()


# Decorador Default root endpoint
@app.get("/")
async def root():
  return { "API Chamados de TI em funcionamento" }

# Decorador que traz o Json com o dicionário com chamados
@app.get("/chamados/")
async def get_chamados():
    return chamados

# Decorador que traz o Json com o dicionário com computadores
@app.get("/computadores/")
async def get_computadores():
    return computadores

# Decorador que traz o Json com o dicionário com tecnicos
@app.get("/tecnicos/")
async def get_tecnicos():
    return tecnicos

# Decorador que traz o Json com o dicionário com usuarios
@app.get("/usuarios/")
async def get_usuarios():
    return usuarios

# Decorador que traz o Json com o dicionário com status
@app.get("/status/")
async def get_status():
    return all_status

# Decorador que traz o Json com o dicionário com prioridades
@app.get("/prioridades/")
async def get_prioridades():
    return prioridades

# Decorador que traz o Json com o dicionário com departamentos
@app.get("/departamentos/")
async def get_departamentos():
    return departamentos

# Decorador que traz o Json com o dicionário com especialidades
@app.get("/especialidades/")
async def get_especialidades():
    return especialidades

# Decorador que traz o Json com o dicionário com Sistemas Operacionais
@app.get("/SO/")
async def get_SO():
    return SOs


# Função para obter dados de chamados do banco de dados
def get_chamados_from_db():
    conn = sqlite3.connect('chamados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT tbChamado.ID as chamadoID, titulo, descricao, especialidade, data_abertura, data_encerramento, prioridade, status, tbComputador.ID as computadorID, marca, modelo, numero_serie, SO, data_aquisicao, departamento, nome_tec, nome_usuario FROM tbChamado JOIN tbEspecialidade ON tbChamado.especialidadeID = tbEspecialidade.ID JOIN tbPrioridade ON tbChamado.prioridadeID = tbPrioridade.ID JOIN tbStatus ON tbChamado.statusID = tbStatus.ID JOIN tbComputador ON tbChamado.computadorID = tbComputador.ID JOIN tbDepartamento ON tbChamado.departamentoID = tbDepartamento.ID JOIN tbTecnico ON tbChamado.tecnicoID = tbTecnico.ID JOIN tbUsuario ON tbChamado.usuarioID = tbUsuario.ID JOIN tbSO ON tbComputador.SO_ID = tbSO.ID')
    chamado = cursor.fetchall()
    conn.close()
    return chamado

# Decorador para obter informações dos alunos
@app.get("/chamados_sql/")
async def get_chamados_sql():
    chamados_db = get_chamados_from_db()
    
    chamado_info = []
    for chamado in chamados_db:
        ID, titulo, descricao, especialidade, data_abertura, data_encerramento, prioridade, status, computadorID, marca, modelo, numero_serie, SO, data_aquisicao, departamento, nome_tec, nome_usuario = chamado
        chamado_info.append({
            "chamadoID": ID,
            "titulo": titulo,
            "descricao": descricao,
            "especialidade": especialidade,
            "data_abertura": data_abertura,
            "data_encerramento": data_encerramento,
            "prioridade": prioridade,
            "status": status,
            "computadorID": computadorID,
            "marca": marca,
            "modelo": modelo,
            "numero_serie": numero_serie,
            "SO": SO,
            "data_aquisicao": data_aquisicao,
            "departamento": departamento,
            "nome_tec": nome_tec,
            "nome_usuario": nome_usuario
        })
    
    return chamado_info

# Função para obter dados de computadores do banco de dados
def get_computadores_from_db():
    conn = sqlite3.connect('chamados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT tbComputador.ID as computadorID, marca, modelo, numero_serie, SO, data_aquisicao, departamento, nome_usuario FROM tbChamado JOIN tbEspecialidade ON tbChamado.especialidadeID = tbEspecialidade.ID JOIN tbPrioridade ON tbChamado.prioridadeID = tbPrioridade.ID JOIN tbStatus ON tbChamado.statusID = tbStatus.ID JOIN tbComputador ON tbChamado.computadorID = tbComputador.ID JOIN tbDepartamento ON tbChamado.departamentoID = tbDepartamento.ID JOIN tbUsuario ON tbChamado.usuarioID = tbUsuario.ID JOIN tbSO ON tbComputador.SO_ID = tbSO.ID')
    computador = cursor.fetchall()
    conn.close()
    return computador

# Decorador para obter informações dos computadores
@app.get("/computadores_sql/")
async def get_computadores_sql():
    computadores_db = get_computadores_from_db()
    
    computador_info = []
    for computador in computadores_db:
        computadorID, marca, modelo, numero_serie, SO, data_aquisicao, departamento, nome_usuario = computador
        computador_info.append({
            "computadorID": computadorID,
            "marca": marca,
            "modelo": modelo,
            "numero_serie": numero_serie,
            "SO": SO,
            "data_aquisicao": data_aquisicao,
            "departamento": departamento,
            "nome_usuario": nome_usuario
        })
    
    return computador_info


# Função para obter dados de usuarios do banco de dados
def get_usuarios_from_db():
    conn = sqlite3.connect('chamados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT tbUsuario.ID as usuarioID, nome_usuario, idade, email, departamento FROM tbUsuario JOIN tbDepartamento ON tbUsuario.departamentoID = tbDepartamento.ID')
    usuario = cursor.fetchall()
    conn.close()
    return usuario

# Decorador para obter informações dos Usuarios
@app.get("/usuarios_sql/")
async def get_usuarios_sql():
    usuarios_db = get_usuarios_from_db()
    
    usuario_info = []
    for usuario in usuarios_db:
        usuarioID, nome_usuario, idade, email, departamento = usuario
        usuario_info.append({
            "usuarioID": usuarioID,
            "nome_usuario": nome_usuario,
            "idade": idade,
            "email": email,
            "departamento": departamento
        })
    
    return usuario_info


# Função para obter dados de usuarios do banco de dados
def get_tecnicos_from_db():
    conn = sqlite3.connect('chamados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT tbTecnico.ID as tecnicoID, nome_tec, idade, email, especialidade FROM tbTecnico JOIN tbEspecialidade ON tbTecnico.especialidadeID = tbEspecialidade.ID')
    tecnico = cursor.fetchall()
    conn.close()
    return tecnico

# Decorador para obter informações dos Usuarios
@app.get("/tecnicos_sql/")
async def get_tecnicos_sql():
    tecnicos_db = get_tecnicos_from_db()
    
    tecnico_info = []
    for tecnico in tecnicos_db:
        tecnicoID, nome_tec, idade, email, especialidade = tecnico
        tecnico_info.append({
            "tecnicoID": tecnicoID,
            "nome_tec": nome_tec,
            "idade": idade,
            "email": email,
            "especialidade": especialidade
        })
    
    return tecnico_info
