# 🧾 Plan de Versionado – CINEMÁTER

**Proyecto:** Cinema Universitario CineMáter  
**Curso:** Algoritmia y Programación – 2025-II  
**Equipo:** Carlas V • Isabella P • Andrés C  

Este documento describe la evolución del software CINEMÁTER a través de sus diferentes versiones.  
El objetivo es registrar, de forma resumida, los cambios funcionales y técnicos más relevantes en cada iteración.

---

## 🔖 Versión 1 – Estructura inicial del sistema

**Archivos principales:**  
- `menu_cinema.py`  
- `funciones.py`  
- `variables.py`  

**Descripción de cambios:**

En esta primera versión se definió la **arquitectura básica del sistema** y la separación por módulos.  
Se creó el menú principal en consola y se establecieron las primeras estructuras de datos para manejar usuarios y salas del cinema. El enfoque estuvo en disponer de un flujo inicial de interacción con el usuario, sin incluir aún todas las validaciones ni funciones avanzadas de reserva o administración.

---

## 🔖 Versión 2 – Lógica de negocio y flujo de reservas

**Archivos principales:**  
- `menu_cinema.py`  
- `funciones.py`  
- `variables.py`  

**Descripción de cambios:**

En la segunda versión se **refinó la lógica de negocio** y se amplió el menú principal para incluir un flujo más completo de registro de usuarios y manejo de reservas.  
Se organizaron mejor las variables globales en `variables.py` y se mejoraron las funciones de apoyo en `funciones.py`, preparando el sistema para trabajar con múltiples funciones de cine durante el fin de semana. También se corrigieron errores detectados en la versión inicial y se fortaleció la interacción por consola para hacerla más clara para el usuario.

---

## 🔖 Versión 3 – Validaciones robustas, manejo de salas y nuevas funcionalidades

**Archivos principales:**  
- `funciones.py` 
- `menu_cinema.py` 

**Descripción de cambios:**

En la versión 3 se consolidó la arquitectura del sistema, agregando funciones de validación robustas (`validar_int`, `validar_str`, `validar_asiento`) y una función genérica para crear salas de cine mediante una matriz de 11x11 asientos (`crear_cine`). También se implementó `imprimir_cine` para mostrar de forma visual y ordenada el estado de cada sala, y `contar_sillas_disponibles` para calcular en tiempo real la cantidad de asientos libres en cada función. 

En `menu_cinema.py` se definieron todas las salas asociadas a las películas del fin de semana (Interstellar, Oppenheimer y The Imitation Game), así como la lista estructurada de funciones con día, hora y sala. Se fortaleció el **registro de usuarios**, el **registro de reservas** (incluyendo selección de película, horario y asiento con validación de ocupación), y se añadió la opción de **cancelar reservas** revirtiendo el estado del asiento en la sala correspondiente. Además, se incorporó una opción de **consulta de cartelera** que muestra un resumen de funciones y la disponibilidad de asientos usando `contar_sillas_disponibles`, dejando preparado el menú para el módulo de administración.  

---

## 🔖 Versión 4 – Preparación del Módulo Administrador y Ajustes Intermedios

**Archivos:**  
- `funciones3.py`  
- `menu_cinema3.py`  

**Descripción:**  
Se migraron funciones a un módulo más organizado, racionalizando la separación entre validaciones, asientos, reportes y utilidades. Se incorporaron funciones para manejo estadístico del cinema y se mejoró la estructura del menú administrador, aunque sin persistencia de datos aún. También se mejoraron los mensajes y el formato visual de las salas.

---

## 🔖 Versión 5 – Versión Final con Módulo Administrador y Persistencia de Datos

**Archivos:**  
- `funciones.py (versión final)`  
- `menu_cinema.py (versión final)`  
- `Informacion_Usuarios`  

**Descripción:**  
En esta versión se implementó la persistencia de datos mediante archivos y se integró completamente el módulo administrador. Se incluyeron reportes financieros, estadísticas, manejo de usuarios, factura de reserva y mejoras visuales. El sistema de reservaciones quedó completo, robusto y apto para la entrega final.

---
## 🏁 Conclusión

La evolución del proyecto muestra una transición clara desde una estructura básica hasta un sistema robusto con persistencia, administración y una experiencia completa para el usuario. Este documento resume la transformación del proyecto CINEMÁTER hacia su versión final como software funcional para entrega académica.
