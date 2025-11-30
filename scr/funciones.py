def validar_int(numero):
    '''
    Funcion que permite recibir un valor númerico para validar si este contiene letras o caracteres especiales.

    Args:
        numero , int
    
    Return:
        numero , int
    '''
    while True:
        if numero.isnumeric():
            numero=int(numero)
            break
        else:
            print('EL DATO SOLO PUEDE SER NÚMERICO')
            numero = input('INTENTE DE NUEVO CON UN DATO VÁLIDO\n--------> ')
            continue
    return numero
            
#-------------------------------------------- VALIDAR VALORES NUMÉRICOS  --------------------------------------------------------

def validar_str(texto,longitud):
    '''
    Funcion que permite recibir una cadena de texto para validar si esta contiene valores númericos y/o una longitud menor a la solicitada.

    Args:
        texto , str
        longitud , int
    
    Return:
        boolean
    '''
    bandera=0
    numeros=['1','2','3','4','5','6','7','8','9','0'] 
    for i in texto:
        if i in numeros:
            print('\nLA INFORMACIÓN NO DEBE DE CONTENER VALORES NÚMERICOS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n')
            bandera=1
            break
    if len(texto)<longitud:
        print(f'\nLA INFORMACIÓN DEBE DE TENER POR LO MENOS {longitud} LETRAS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n')
        bandera=bandera+1
    if bandera==0:
        return True
    else:
        return False

#-------------------------------------------- VALIDAR ASIENTO  -----------------------------------------------------

def validar_asiento(texto):
    '''
    Funcion que permite recibir un asiento del cine para validar que exista.

    Args:
        texto , str
    
    Return:
        boolean
    '''
    bandera=0
    letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    if texto not in letras:
        print('\nEL DATO INGRESADO NO EXISTE\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n')
        bandera=1
    if bandera==0:
        return True
    else:
        return False
    
#-------------------------------------------- CREAR SALA DE CINE -----------------------------------------------------

def crear_cine(): 
    '''
    Funcion que permite crear una sala de cine a traves de listas.

    Args:
        none
    
    Return:
        asientos , list
    '''
    asientos=[]
    for i in range(11):
        fila=[]
        for j in range(11):
            fila.append('O')
        asientos.append(fila)
    return asientos 

#-------------------------------------------- IMPRIMIR SALA DE CINE -----------------------------------------------------
 
def imprimir_cine(lista,nombre,horario):
    '''
    Funcion que permite imprimir una sala de cine mostrando la película de la función y los asientos disponibles que tiene.

    Args:
        lista , list
        nombre , str
        horario , str
    
    Return:
        str
    '''
    letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    print(f'{nombre}') 
    print(f'{horario}')
    print('Disponible (O) Ocupado (X)\n') 
    print(' '*4, end='')
    for l in letras:
        print(l, end='    ')
    print()
    for i,j in enumerate(lista):
        print(letras[i],end=' ')
        print(j)
    print('='*80)
    return '\n'
        
#-------------------------------------------- SILLAS DISPONIBLES  -----------------------------------------------------    

def contar_sillas_disponibles(sala):
    ''' 
    Función que permite contar cuántas sillas se encuentran disponibles en una sala de cine.
    
    Args:
        sala (list): Matriz que representa la sala, donde cada fila contiene asientos marcados con
                     'O' para disponible o 'X' para ocupado.
    
    Return:
        int: Cantidad total de asientos disponibles en la sala.
    '''
    disponibles = 0
    for fila in sala:
        for asiento in fila:
            if asiento == 'O':
                disponibles += 1
    return disponibles


#--------------------------------------------  FUNCIONES PARA EL PERFIL DE ADMINISTRADOR --------------------------------------------


def total_reservas(usuarios):
    total = 0
    for datos in usuarios.values():
        total += max(0, len(datos) - 4)
    return total


def total_tiquetes_vendidos(usuarios):
    return total_reservas(usuarios)


def total_pago(usuarios):
    precios = {
        "Estudiante": 7500,
        "Docente": 10000,
        "Administrativo": 8500,
        "Oficial Interno": 7000,
        "Externo": 15000
    }
    total = 0
    for usuario in usuarios.values():
        vinculo = usuario[2]
        reservas = max(0, len(usuario) - 4)
        total += precios[vinculo] * reservas
    return total


def promedio_venta_diaria(usuarios):
    return total_pago(usuarios) / 3 if usuarios else 0


def usuario_mayor_menor_reservas(usuarios):
    mayor = 0
    menor = 0
    max_reserva = -1
    min_reserva = 10**8

    for cc, datos in usuarios.items():
        reservas = max(0, len(datos) - 4)

        if reservas > max_reserva:
            max_reserva = reservas
            mayor = (cc, datos[0], datos[1], reservas)

        if reservas < min_reserva:
            min_reserva = reservas
            menor = (cc, datos[0], datos[1], reservas)

    return mayor, menor
        
#--------------------------------------------  FUNCIONES MANEJO DE ARCHIVO --------------------------------------------
def CrearArchivo(nombre_archivo:str):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write('Documento,Nombre,Apellido,Vinculo,Valor,Reservas\n')
    return None

def GuardarDatos(diccionario:dict, nombre_archivo:str):
    llaves = list(diccionario.keys())
    for llave in llaves:
        datos = diccionario[llave]
        texto = ''
        for dato in datos:
            texto += str(dato)+','
        with open(nombre_archivo, 'a', encoding='utf-8') as f:
            f.write(str(llave)+','+texto[:-1]+'\n')
    return None 

def Usuarios_Guardados(nombre_archivo):
    diccionario={}
    with open(nombre_archivo,'r') as f:
        next(f)
        for linea in f:
            info=linea.strip().split(',')
            documento=info[0]
            #info.remove(documento) #se elimina el documento de la informacion de usuario para volverlo llave
            info = info[1:] #así también se elimina el documento
            info = [dato for dato in info if dato != ''] #acá solucionammos el error de que se cuenten las reservas vacías pues para el sistema "" también es una reserva
            diccionario[documento]=info
    return diccionario
