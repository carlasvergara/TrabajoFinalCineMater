from funciones import validar_int
from funciones import validar_str
from funciones import validar_asiento
from funciones import crear_cine
from funciones import imprimir_cine
from funciones import contar_sillas_disponibles
from funciones import total_reservas
from funciones import total_tiquetes_vendidos
from funciones import total_pago
from funciones import promedio_venta_diaria
from funciones import usuario_mayor_menor_reservas
from funciones import GuardarDatos
from funciones import Usuarios_Guardados
from funciones import CrearArchivo
from datetime import datetime as dt
import time

#DICCIONARIOS Y VARIABLES IMPORTANTES
nombre_archivo='Informacion_Usuarios'
usuarios=Usuarios_Guardados(nombre_archivo) 
CrearArchivo(nombre_archivo)
admins = {
    "steve wozniak" : "0001",
    "pirlo" : "4200"
}



#SALAS INTERSTELLAR
salaINT_1=crear_cine()
salaINT_2=crear_cine()
salaINT_3=crear_cine() 

#SALAS OPPENHEIMER
salaOPP_1=crear_cine()
salaOPP_2=crear_cine()
salaOPP_3=crear_cine() 

#SALAS MATRIX
salaTIG_1=crear_cine()
salaTIG_2=crear_cine()
salaTIG_3=crear_cine() 

#INFORMACION DE FACTURA
fecha=str(dt.today())
fecha=fecha.split()[0].replace('-','/')

# LISTA DE FUNCIONES DEL FIN DE SEMANA
funciones = [
    [1, 'Viernes', '2pm',  'Interstellar',      'sala_1'],
    [1, 'Viernes', '4pm',  'Interstellar',      'sala_1'],
    [1, 'Viernes', '6pm',  'Interstellar',      'sala_1'],

    [2, 'Sábado',  '2pm',  'Oppenheimer',       'sala_2'],
    [2, 'Sábado',  '4pm',  'Oppenheimer',       'sala_2'],
    [2, 'Sábado',  '6pm',  'Oppenheimer',       'sala_2'],

    [3, 'Domingo', '2pm',  'Matrix','sala_3'],
    [3, 'Domingo', '4pm',  'Matrix','sala_3'],
    [3, 'Domingo', '6pm',  'Matrix','sala_3']
]



#MENU PRINCIPAL
while True:
    print('\n')
    print('='*80) 
    print('📽️  CINEMÁTER 📽️'.center(80))
    print('La pantalla de la UdeA'.center(80))
    print('='*80)
    print('\n')
    print('⭐⭐⭐  MENÚ PRINCIPAL  ⭐⭐⭐\n'.center(80))
    print('1. Registrar Usuario'.center(80))
    print('2. Registrar Reserva'.center(80))
    print('3. Cancelar Reserva'.center(80))
    print('4. Consultar Funciones de Fin de Semana'.center(80))
    print('5. Administrador'.center(80))
    print('6. Salir'.center(80))
    op=validar_int(input('\n--------> '))
    print('='*80)

    match op:
        case 1:
            while True: #CICLO OPCION REGISTRO DE USUARIO
                print('='*80)
                print('\n')
                print('👤 REGISTRO DE USUARIO👤\n'.center(80))
                print('Por favor ingrese los siguientes datos\n')
                while True: #CICLO QUE VALIDA LA VARIABLE NOMBRE 
                    nombre=input('NOMBRE: ')
                    if validar_str(nombre,3):
                        break
                    else:
                        continue
            
                while True: #CICLO QUE VALIDA LA VARIABLE APELLIDO  
                    apellido=input('APELLIDO: ')
                    if validar_str(apellido,3):
                        break
                    else:
                        continue

                while True: #CICLO QUE VALIDA LA VARIABLE DOCUMENTO
                    bandera=0
                    cc=validar_int(input('DOCUMENTO: ' ))
                    cc=str(cc)
                    if len(cc)<3:
                        print('''\nEL DOCUMENTO DEBE DE TENER POR LO MENOS 3 DÍGITOS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n''') 
                        continue
                    elif len(cc)>15:
                        print('''\nEL DOCUMENTO NO DEBE DE TENER MÁS DE 15 DÍGITOS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n''') 
                        continue
                    elif cc in usuarios.keys(): #HACE SABER AL USUARIO QUE YA ESTA REGISTRADO EN EL SISTEMA 
                        print('\n') 
                        print('='*80)
                        print('\n')
                        print('🔴  EL DOCUMENTO YA SE ENCUENTRA REGISTRADO EN CINEMÁTER 🔴'.center(80))
                        print('🔴  REGRESANDO AL MENU PRINCIPAL 🔴'.center(80))     
                        bandera=1
                        break
                    else:
                        break
                if bandera==1: #NO CONTINUA EL CICLO, SALE AL MENU PRINCIPAL
                    break
                                
                while True: #CICLO QUE VALIDA LA VARIABLE VINCULO
                    print('='*80)
                    print('\n')
                    print('TIPO DE VINCULO\n'.center(80))
                    print('1. Estudiantes -----> $7 500'.center(80))
                    print('2. Docentes -----> $10 000'.center(80))
                    print('3. Administrativos -----> $8 500'.center(80))
                    print('4. Oficiales Internos -----> $7 000'.center(80))
                    print('5. Publico Externo -----> $15 000'.center(80))
                    print('\nIngrese un numero segun su tipo de vinculo')                    
                    vin=validar_int(input('--------> '))
                    if vin>5 or vin<1:
                        print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA''') 
                        continue
                    else:
                        break
                match vin: #DECODIFICA LA VARIABLE VINCULO
                    case 1:
                        vinculo='Estudiante'
                        entrada=7500
                    case 2:
                        vinculo='Docente'
                        entrada=10000
                    case 3:
                        vinculo='Administrativo'
                        entrada=8500
                    case 4:
                        vinculo='Oficial Interno'
                        entrada=7000
                    case 5:
                        vinculo='Externo'
                        entrada=15000
                    case _:
                        vinculo='N/A'
                    
                print('\n') 
                print('='*80)
                print('\n')
                
                #GUARDA LOS USUARIOS EN EL DICCIONARIO CON SU DOCUMENTO COMO LLAVE
                usuarios[cc]=[nombre,apellido,vinculo,entrada]
               
                while True: #DA LA OPCION DE REGISTRAR MAS USUARIOS
                    print('👤  USUARIO REGISTRADO EXITOSAMENTE👤\n'.center(80))    
                    print('1. Registrar Otro Usuario'.center(80))
                    print('2. Volver al Menu Principal'.center(80))
                    op2=validar_int(input('\n--------> '))
                    bandera=0
                    match op2:
                        case 1: #PERMITE HACER OTRO REGISTRO Y ROMPE EL CICLO PARA MAS REGISTROS
                            break
                        case 2: #ACTIVA LA BANDERA
                            bandera=1
                            break
                        case _:
                            print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA''') 
                            continue
                if bandera==1: #VE LA BANDERA Y VUELVE AL MENU PRINCIPAL
                    break

        case 2: 
            bandera=0
            while True: #CICLO OPCION REGISTRO DE RESERVA
                if bandera==1:  #VE LA BANDERA Y VUELVE AL MENU PRINCIPAL
                    break
                else:
                    print('='*80)
                    print('\n')
                    print('🎟️  REGISTRO DE RESERVA  🎟️\n'.center(80)) 
                    while True: #VALIDACION DE QUE EL USUARIO ESTE REGISTRADO 
                        print('Ingrese su numero de documento')
                        cc=validar_int(input('--------> '))
                        cc=str(cc)
                        if len(cc)<3:
                            print('''\nEL DOCUMENTO DEBE DE TENER POR LO MENOS 3 DÍGITOS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n''') 
                            continue
                        elif len(cc)>15:
                            print('''\nEL DOCUMENTO NO DEBE DE TENER MÁS DE 15 DÍGITOS\nINTENTE DE NUEVO CON UN DATO VÁLIDO\n''') 
                            continue
                        else:
                            break
                    cc=str(cc)
                    
                    if cc in usuarios.keys(): #EL USUARIO ESTA REGISTRADO
                        print('\n') 
                        print('='*80)
                        print('\n')
                        info_usuario=usuarios[cc]
                        nombre=info_usuario[0]
                        apellido=info_usuario[1]
                        vinculo=info_usuario[2]
                        tarifa=int(info_usuario[3])
                        print(f'HOLA, {nombre.upper()}👋\n'.center(80))
                        print('Para realizar la reserva, seleccione la película que desea ver\n'.center(80))    
                        print('1. Interstellar'.center(80))
                        print('2. Oppenheimer'.center(80))
                        print('3. Matrix'.center(80))
                        print('4. Volver al Menu Principal'.center(80))
                        print('\n*Recuerde que solo puede reservar un asiento por reserva*')
                        while True: 
                            pel=validar_int(input('--------> '))
                            bandera=0
                            match pel:
                                case 1:
                                    pelicula='INTERSTELLAR'
                                    break
                                case 2:
                                    pelicula='OPPENHEIMER'
                                    break
                                case 3:
                                    pelicula='MATRIX'
                                    break
                                case 4: #ACTIVA LA BANDERA
                                    bandera=1
                                    break
                                case _:
                                    print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA''') 
                                    continue
                        if bandera==1: #VE LA BANDERA Y CIERRA EL CICLO DE REGISTRO DE RESERVA
                            break
                        
                        print('FUNCIONES DISPONIBLES PARA'.center(80))
                        print(f'{pelicula}\n'.center(80))     
                        print('1. Viernes 2pm'.center(80))
                        print('2. Viernes 4pm'.center(80))
                        print('3. Viernes 6pm'.center(80))
                        while True: 
                            h=validar_int(input('--------> '))
                            match h:
                                case 1:
                                    horario='Viernes 2pm'
                                    break
                                case 2:
                                    horario='Viernes 4pm'
                                    break
                                case 3:
                                    horario='Viernes 6pm'
                                    break
                                case _:
                                    print('\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA')
                                    continue
                                
                        if pelicula=='INTERSTELLAR' and horario=='Viernes 2pm':
                            sala_elegida=salaINT_1
                        elif pelicula=='INTERSTELLAR' and horario=='Viernes 4pm':
                            sala_elegida=salaINT_2
                        elif pelicula=='INTERSTELLAR' and horario=='Viernes 6pm':
                            sala_elegida=salaINT_3
                            
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 2pm':
                            sala_elegida=salaOPP_1
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 4pm':
                            sala_elegida=salaOPP_2
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 6pm':
                            sala_elegida=salaOPP_3
                        
                        elif pelicula=='MATRIX' and horario=='Viernes 2pm':
                            sala_elegida=salaTIG_1
                        elif pelicula=='MATRIX' and horario=='Viernes 4pm':
                            sala_elegida=salaTIG_2
                        elif pelicula=='MATRIX' and horario=='Viernes 6pm':
                            sala_elegida=salaTIG_3
                        
                        print('\n') 
                        print('='*80)
                        print('\n')
                        while True: 
                            imprimir_cine(sala_elegida,pelicula,horario)
                            print('\nIngrese los datos del asiento a reservar')
                            while True:
                                while True:
                                    fila=input('FILA ---> ').upper()
                                    if validar_asiento(fila):
                                        break
                                    else:
                                        continue

                                while True: 
                                    columna=input('COLUMNA --->: ').upper()
                                    if validar_asiento(columna):
                                        break
                                    else:
                                        continue

                                letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
                                f=letras.index(fila)
                                c=letras.index(columna)
                                fila_sel=sala_elegida[f]
                                if fila_sel[c]=='O':
                                    fila_sel[c]='X'
                                    # 🔴 AQUÍ FALTABA EL TERCER PARÁMETRO (horario)
                                    imprimir_cine(sala_elegida,pelicula,horario)
                                    break
                                else:
                                    print('\nEL ASIENTO QUE DESEA RESERVAR SE ENCUENTRA OCUPADO\nPOR FAVOR REVISE SU ELECCION')
                                    continue
                                
                            #SE GUARDA LA RESERVA
                            reserva=f'(Película ---> {pelicula}) - (Funcion ---> {horario}) - (Asiento ---> Fila: {fila} Columna: {columna})'
                            info_usuario.append(reserva)
                            print(f'\nFila seleccionada: {fila}\nColumna seleccionada: {columna}')
                            silla=fila+columna
                            print('\n')
                            print('🟩 RESERVA REGISTRADA EXITOSAMENTE 🟩\n'.center(80))    
                            bandera=1
                            
                            #SE MUESTRA LA FACTURA
                            print('*'*80)
                            print('\n')
                            print('📽️  CINEMÁTER 📽️'.center(80))
                            print('La pantalla de la UdeA'.center(80))
                            print('\n')
                            print('CALLE 67 #53-108, ARANJUEZ, MEDELLIN'.center(80))
                            print('TEL (604) 219 8332'.center(80))
                            print('\n')
                            print('FACTURA DE SU BOLETO CINEMÁTER'.center(80))
                            print('\n')
                            print(f'Cliente: {nombre} {apellido}'.ljust(80))
                            print(f'Documento: {cc}'.ljust(80))
                            print(f'Vinculo: {vinculo}'.ljust(80))
                            print(f'Fecha: {fecha}'.ljust(80))
                            print('\n'*2)
                            print('CANT'.center(20), 'PELÍCULA'.center(20), 'FUNCIÓN'.center(20), 'SILLA'.center(20))
                            print('1'.center(20), format(pelicula).center(18), format(horario).center(20), format(silla).center(20)) 
                            print('\n'*2)
                            print('METODO DE PAGO: CONTADO') 
                            print(f"VALOR A PAGAR {tarifa:,}$")
                            print('\n')
                            print('⭐⭐⭐  GRACIAS POR SU COMPRA  ⭐⭐⭐'.center(80))
                            print('\n')
                            print('*'*80)
                            
                            if bandera==1: #VUELVE AL MENU PRINCIPAL
                                break
                    else: #EL USUARIO NO ESTA REGISTRADO
                        print('\n') 
                        print('='*80)
                        print('\n')
                        print('🔴  EL DOCUMENTO QUE INGRESÓ NO SE ENCUENTRA REGISTRADO EN CINEMÁTER 🔴\n'.center(80))    
                        print('1. Corregir'.center(80))
                        print('2. Volver al Menu Principal'.center(80))
                        while True: #OPCION PARA CORREGIR EL DOCUMENTO
                            op2=validar_int(input('\n--------> '))
                            bandera=0
                            match op2:
                                #PERMITE CORRIGIR EL DOCUMENTO
                                case 1:
                                    break
                                #ACTIVA LA BANDERA
                                case 2:
                                    bandera=1
                                    break
                                case _:
                                    print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA''') 
                                    continue
                        
                        if bandera==1: #VE LA BANDERA Y VUELVE AL MENU PRINCIPAL
                            break

        case 3:
            print('='*80)
            print('\n❌ CANCELAR RESERVA ❌\n')
            
            cc = validar_int(input('INGRESE SU DOCUMENTO: '))
            cc = str(cc)
            
            # Validar usuario
            if cc not in usuarios.keys():
                print('\nEL DOCUMENTO NO SE ENCUENTRA REGISTRADO EN CINEMÁTER\n')
            
            else:
                info = usuarios[cc]      # [nombre, apellido, vinculo, tarifa, reservas...]
                reservas = info[4:]      # desde índice 4 empiezan las reservas
                
                if len(reservas) == 0:
                    print('\nUSTED NO TIENE RESERVAS ACTIVAS\n')
                
                else:
                    print('\nESTAS SON SUS RESERVAS ACTIVAS:\n')
                    for i, r in enumerate(reservas, start=1):
                        print(f'{i}. {r}')
                    
                    # elegir reserva
                    num = validar_int(input('\nNÚMERO DE RESERVA A CANCELAR: '))
                    if 1 <= num <= len(reservas):
                    
                        reserva = reservas[num - 1]
                        
                        # extraer datos de la reserva
                        # Formato: (Película ---> XXX) - (Funcion ---> HORA) - (Asiento ---> Fila: F Columna: C)
                        pelicula = reserva.split('Película --->')[1].split(')')[0].strip()
                        horario = reserva.split('Funcion --->')[1].split(')')[0].strip()
                        fila = reserva.split('Fila:')[1].split()[0].strip()
                        columna = reserva.split('Columna:')[1].split(')')[0].strip()
                        
                        # escoger sala según película y horario (igual que en la reserva)
                        if pelicula=='INTERSTELLAR' and horario=='Viernes 2pm':
                            sala = salaINT_1
                        elif pelicula=='INTERSTELLAR' and horario=='Viernes 4pm':
                            sala = salaINT_2
                        elif pelicula=='INTERSTELLAR' and horario=='Viernes 6pm':
                            sala = salaINT_3
                        
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 2pm':
                            sala = salaOPP_1
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 4pm':
                            sala = salaOPP_2
                        elif pelicula=='OPPENHEIMER' and horario=='Viernes 6pm':
                            sala = salaOPP_3
                        
                        elif pelicula=='MATRIX' and horario=='Viernes 2pm':
                            sala = salaTIG_1
                        elif pelicula=='MATRIX' and horario=='Viernes 4pm':
                            sala = salaTIG_2
                        elif pelicula=='MATRIX' and horario=='Viernes 6pm':
                            sala = salaTIG_3
                        else:
                            sala = None
                        
                        if sala is not None:
                            letras = ['A','B','C','D','E','F','G','H','I','J','K']
                            f = letras.index(fila)
                            c = letras.index(columna)
                            
                            sala[f][c] = 'O'
                            info.remove(reserva)
                            
                            print('\n ✅ RESERVA CANCELADA EXITOSAMENTE\n')
                        else:
                            print('\nNO SE ENCONTRÓ LA SALA ASOCIADA A ESA RESERVA\n')
                    
                    else:
                        print('\nOPCIÓN NO VÁLIDA\n')

        case 4:
            # Total de funciones
            total_funciones = len(funciones)
        
            # Películas únicas en cartelera
            peliculas_unicas = []
            for func in funciones:
                nombre_peli = func[3]
                if nombre_peli not in peliculas_unicas:
                    peliculas_unicas.append(nombre_peli)
            total_peliculas = len(peliculas_unicas)
            
            print('='*80)
            print('📽️  CARTELERA DE CINEMÁTER  📽️'.center(80))
            print('='*80)
            print()
            # Resumen
            print(f'📅 Total de funciones programadas: {total_funciones}')
            print(f'📀 Películas en cartelera: {total_peliculas}')
            print()
        
            # Listado de películas
            print('🎞️ PELÍCULAS EN CARTELERA:')
            print('-------------------------------------')
            for peli in peliculas_unicas:
                print(f'• {peli}')
            print()
        
            # Horarios y disponibilidad
            print('🪑 HORARIOS Y DISPONIBILIDAD:')
            print('---------------------------------------------------------------------')
            # Encabezados alineados
            print(
                'IdPelicula'.ljust(10),
                'Día'.ljust(10),
                'Hora'.ljust(10),
                'Película'.ljust(22),
                'Disponibles'
            )
        
            # Filas de la tabla
            for func in funciones:
                idp = func[0]
                dia = func[1]
                hora = func[2]
                peli = func[3]
        
                # Seleccionar sala según película y hora
                if peli == 'Interstellar':
                    if hora == '2pm':
                        sala = salaINT_1
                    elif hora == '4pm':
                        sala = salaINT_2
                    else:  # 6pm
                        sala = salaINT_3
                
                elif peli == 'Oppenheimer':
                    if hora == '2pm':
                        sala = salaOPP_1
                    elif hora == '4pm':
                        sala = salaOPP_2
                    else:
                        sala = salaOPP_3
                
                else:  # The Imitation Game
                    if hora == '2pm': 
                        sala = salaTIG_1
                    elif hora == '4pm':
                        sala = salaTIG_2
                    else:
                        sala = salaTIG_3
        
                disp = contar_sillas_disponibles(sala)
        
                print(
                    str(idp).ljust(10),
                    dia.ljust(10),
                    hora.ljust(10),
                    peli.ljust(22),
                    str(disp)
                )
        
            print()

        case 5:
            print('='*80)
            print('\n🔐 MÓDULO ADMINISTRADOR 🔐\n')

            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            if usuario not in admins or admins[usuario] != contraseña:
                print("\n❌ ACCESO DENEGADO ❌\n")
                time.sleep(0.8)
                continue
            
            # ACCESO CORRECTO
            while True:
                print('='*80)
                print("\n📊 MENÚ ADMINISTRADOR 📊\n")
                print("1. Total de reservas registradas")
                print("2. Total de tiquetes vendidos")
                print("3. Total pago realizado")
                print("4. Promedio de venta diario del cine")
                print("5. Lista de usuarios")
                print("6. Usuario con mayor y menor cantidad de reservas")
                print("7. Volver al menú principal\n")

                opAd = validar_int(input("\n--------> "))

                match opAd:
                    case 1:
                        print("\n📌 TOTAL DE RESERVAS:")
                        print(total_reservas(usuarios))
                    
                    case 2:
                        print("\n🎟 TOTAL DE TIQUETES VENDIDOS:")
                        print(total_tiquetes_vendidos(usuarios))

                    case 3:
                        print("\n💰 TOTAL PAGADO:")
                        print(f"${total_pago(usuarios):,}")

                    case 4:
                        print("\n📆 PROMEDIO DE VENTA DIARIO:")
                        print(f"${promedio_venta_diaria(usuarios):,}")

                    case 5:
                        print("\n👥 LISTA DE USUARIOS REGISTRADOS:")
                        for cc, datos in usuarios.items():
                            nombre, apellido, vinculo = datos[:3]
                            print(f"- {cc}: {nombre} {apellido} ({vinculo})")

                    case 6:
                        mayor, menor = usuario_mayor_menor_reservas(usuarios)
                        print("\n🏆 USUARIO CON MÁS RESERVAS:")
                        print(mayor)

                        print("\n📉 USUARIO CON MENOS RESERVAS:")
                        print(menor)

                    case 7:
                        break

                    case _:
                        print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA\n''') 
                        continue

        case 6:
            if not usuarios:
                print("")
                print("QUÉ TROSTE, NADIE NOS VISITÓ :((((((\n".center(80))
                print("CHAU MÁS BIEN\n".center(80))
                print("😢"*40)
                print("")
            else:
                print("")
                print("GRACIAS POR VISITAR ✨CINEMÁTER✨ ESPERAMOS HAYAS TENIDO LA MEJOR EXPERIENCIA\n\n".center(1000))
                print("🤑"*40)
                print("\n")
            break 
        
        case _: 
            print('''\nLA OPCIÓN INGRESADA NO EXISTE\nINTENTE DE NUEVO CON UNA OPCIÓN VÁLIDA\n''') 
            continue

GuardarDatos(usuarios,nombre_archivo)
