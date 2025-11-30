![Logo CineMáter](imagencinema.png)


# 🎬 MANUAL DE USUARIO – CINEMÁTER

## CONTENIDO

1. **INTRODUCCIÓN**
   - CineMáter
   - Objetivos
   - Requisitos de uso

2. **OPCIONES DEL SISTEMA**
   1. Registro de usuarios
   2. Registro de reservas
   3. Cancelación de reservas
   4. Consulta de funciones
   5. Menú de administrador
   6. Salir

---

## INTRODUCCIÓN

### CineMáter

CineMáter es un sistema interactivo que permite gestionar usuarios, reservas, consultar cartelera y acceder a reportes de administración. Este sistema se ejecuta desde consola y está diseñado para funcionar con entradas de teclado.

### Objetivo

Simular y gestionar de manera eficiente la operación de un cine universitario.

### Requisitos de uso

- Python 3.8 o superior
- Ejecutar: `python menu_cinema.py`

---

##  OPCIONES DEL SISTEMA

### 1️⃣ Registro de usuarios

La primera opción del menú CineMáter permite registrar el nombre, apellido, documento y vínculo de un usuario en el diccionario principal, para que posteriormente esta información pueda ser guardada en un archivo externo por el sistema. En caso de que el documento de la persona que se intenta registrar en CineMáter ya se encuentre, el sistema se lo hará saber al usuario y lo envía de vuelta al menú principal.

### 2️⃣ Registro de reservas

Al ingresar en esta opción, la consola pide al usuario verificar si se encuentra registrado en CineMáter usando su documento. Al verificar que se encuentre en el sistema, este le permite al usuario crear su propia reserva eligiendo una película, horario y asiento disponible. Las sillas disponibles de cada función se ven reflejadas con una "O", una vez seleccionado el asiento se marca como ocupado con una "X" y se guarda la reserva junto a la información del usuario. Finalmente, se muestra una factura electrónica con la información de la reserva y el total que se debe de pagar.

En caso de que el documento digitado por el usuario no se encuentre en CineMáter, el sistema da la opción de corregirlo o de volver al menú principal.

### 3️⃣ Cancelación de reservas

Al ingresar en esta opción, la consola pide al usuario digitar su documento de identidad para verificar si presenta reservas activas en CineMáter. Al verificar que exista al menos una reserva vinculada al documento ingresado, el sistema muestra en pantalla todas las reservas activas del usuario respectivamente numeradas. Posterior a esto, la consola deja que el usuario pueda digitar el número de la reserva que desea cancelar. Finalmente, cuando se elimina la reserva seleccionada de la información del usuario, se libera el asiento en la sala correspondiente y se imprime un mensaje confirmando el éxito del proceso.

### 4️⃣ Consulta de funciones

En esta opción, el sistema muestra la información guardada en CineMáter con respecto a las funciones. Permite al usuario ver la cantidad de funciones programadas, las películas en cartelera con sus respectivos horarios y los asientos disponibles en cada sala. Luego de mostrar esta información, el sistema se devuelve automáticamente al menú principal.

### 5️⃣ Menú de administrador

Esta opción es de uso exclusivo para los administradores de CineMáter. Al seleccionarla, el sistema realiza un proceso de inicio de sesión, donde si el nombre o el apellido del usuario administrador son digitados incorrectamente, de forma automática se va al menú principal luego de negar el acceso al menú de administrador.

En caso contrario, se ingresa a un menú secundario, que según la opción digitada por el administrador, muestra reportes tales como:

- Total de reservas
- Total de tiquetes vendidos
- Total pago realizado
- Promedio de venta diario
- Lista de usuarios
- Usuario con mayor y menor cantidad de reservas

Al final del menú de administrador, se encuentra una opción que permite volver al menú principal de CineMáter.

### 6️⃣ Salir

Finaliza el programa mostrando agradecimientos.




