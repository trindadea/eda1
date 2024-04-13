class Node(): #a classe 'Node' implementa um objeto do tipo nó com os seguintes atributos:
    def __init__(self, id, type):
        self.id = id #nome do nó
        self.type = type #tipo do nó, pode ser 'd' para diretórios ou 'f' arquivos
        self.children = {} #dict cujas chaves são id's dos nós filhos
        
    def __lt__(self, other):
        return self.id < other.id

#---------------------------------------------------------------------------------------------
#FUNÇÕES AUXILIARES
    
def insertNode(parent, node, type):
    parent.children[node] = Node(node, type)

def pathExists(tree, path): #dada uma árvore, a função verifica se um dado caminho existe.
    if path:
        if path[0] in tree.children:
            return pathExists(tree.children[path[0]], path[1:])
    return tree, path #a função retorna o local da memória onde está armazenando o último
#nó existente no caminho dado e uma lista dos nós que não foram encontrados abaixo desse nó.

def isCurrentDir(path, current_dir):
        if not path:
            return current_dir

        if current_dir and path[0] == current_dir[0]:    
            return isCurrentDir(path[1:], current_dir[1:])

        return False
    
def processPath(_input): #a função recebe um caminho em forma de string.
    if ' ' in _input:
        _input = _input.split()
        from_path = _input[0]
        to_path = _input[1]
      
        return processPath(from_path), processPath(to_path)
    
    if _input == '/':
        path = ['']
    else:
        path = _input.split('/')
        
    if path[0] == '':
        path = path[1:]
        
    if '.' in path or '..' in path:
        return dots(path)
        
    return path #após o processamento, ela retorna uma lista que contém os diretórios no caminho dado.

def dots(path): #função auxiliar de processPath para processamento de caminhos com '.' e '..'.
    i = 0
    while i < len(path):
        aux = False
        j = i
        if path[i] == '.':
            path = path[:i] + current_dir + path[i+1:]
            continue
        
        while j < len(path) and path[j] == '..':
            aux = True
            j = j + 1
            
        if aux:
            path = current_dir[:-j] + path[j:]
        else:
            i = i + 1
    
    return path

#---------------------------------------------------------------------------------------------
#FUNÇÕES PRINCIPAIS

def show(node, level = 0):
    print(f'{"---" * level}{node.id}')
    for child in sorted(node.children.values()):
        show(child, level + 1)

def mkdir(path):
    if not path:
        return print('DIRETÓRIO JÁ EXISTE')
    
    global current_dir
    new_dir = path[-1]
    
    parent, make_path = pathExists(tree, path[:-1])
    
    for directory in make_path:
        insertNode(parent, directory, 'd')
        parent = parent.children[directory]
    
    if new_dir in parent.children:
        return print('DIRETÓRIO JÁ EXISTE')
    
    return insertNode(parent, new_dir, 'd')

def mv(from_path, to_path):
    if not from_path:
        return
    
    global current_dir
    file_dir = from_path[-1]
    
    from_parent, from_invalid_path = pathExists(tree, from_path[:-1])
    to_parent, to_invalid_path = pathExists(tree, to_path)
    
    if from_invalid_path or to_invalid_path:
        return print('CAMINHO INVÁLIDO')
        
    if file_dir in from_parent.children:
        if file_dir in to_parent.children:
            del to_parent.children[file_dir]
            
        rem_path = isCurrentDir(from_path, current_dir)
        if rem_path != False:
            current_dir = to_path + [file_dir] + rem_path
            
        aux = from_parent.children[file_dir]
        to_parent.children[file_dir] = aux
        del from_parent.children[file_dir]
        return
            
    return print('ARQUIVO ou DIRETÓRIO não existe')

def rm(path):
    if not path:
        return
    
    global current_dir
    
    to_remove = path[-1]
    
    parent, invalid_path = pathExists(tree, path[:-1])
    
    if invalid_path:
        return print('CAMINHO INVÁLIDO')
    
    if to_remove in parent.children:
        if isCurrentDir(path, current_dir) != False:
            current_dir = ['']
                
        del parent.children[to_remove]
        return
        
    return print('ARQUIVO ou DIRETÓRIO não existe')
    
def touch(path):
    file = path.pop()
    
    parent, invalid_path = pathExists(tree, path)
    
    if not invalid_path:
        if file in parent.children:
            if parent.children[file].type == 'f':
                return print('ARQUIVO JÁ EXISTE')
            else:
                return print('CAMINHO INVÁLIDO')
                
        return insertNode(parent, file, 'f') 
        
    return print('CAMINHO INVÁLIDO')

def cd(path):
    global current_dir
    
    if not path:
        current_dir = ['']
        return
    
    final_dir = path[-1]
    
    parent, invalid_path = pathExists(tree, path[:-1])
    
    if not invalid_path:
        if final_dir in parent.children:
            if parent.children[final_dir].type == 'f':
                return print('COMANDO INVÁLIDO')
            current_dir = path
            return 
            
    return print('CAMINHO INVÁLIDO')
        

def find(c_dir, file_dir, path = ''):  
    if c_dir.id == file_dir:
        print(path)
    
    for child in sorted(c_dir.children.values()):
        find(child, file_dir, path + '/' + child.id)

#---------------------------------------------------------------------------------------------
                            #X-WingFS - Sistemas de Arquivos!        
#ENTRADAS 

tree = Node('/', 'dir_raiz') #inicialização do sistema de arquivos com o diretório raiz '/'.
global current_dir
current_dir = [''] #definição do diretório corrente.

while True:
    _input = input().split(' ', 1)
    command = _input[0]

    if command == 'end':
        break
    
    elif command == 'show':
        show(tree)
        continue
    
    elif command == 'pwd':
        print('/'.join([''] + current_dir)) #current_dir é uma lista que contém o id dos
                                            #diretórios até o diretório corrente em si.
        continue
        
    path = _input[1] #a partir desse ponto, todas as funções recebem um caminho como parâmetro.
    
    if command == 'mkdir':
        mkdir(processPath(path))
        
    elif command == 'mv':        
        mv(*processPath(path))
        
    elif command == 'rm':
        rm(processPath(path))
    
    elif command == 'touch':
        touch(processPath(path))
        
    elif command == 'cd':
        cd(processPath(path))
        
    elif command == 'find':
        c_dir = pathExists(tree, current_dir)[0] #retorna o local em memória do diretório corrente.
        find(c_dir, path) #chama a função 'find' a partir do diretório corrente.

#Arthur Carneiro Trindade - 180098080