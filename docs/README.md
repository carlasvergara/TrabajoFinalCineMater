# 📚 Repositorio de Documentación  
## 🧩 Trabajo Final  
### 🎬 Cinema - CineMáter  

---

## 1. 👥 Integrantes  

### **Carlas Andrea Vergara Romero**  
-  Tengo 25 años, trabajo tiempo completo en la Corporación Parque Explora como auxiliar administrativa y en mis tiempos libres me gusta viajar, generalmente lo hago en mi moto.  
Escucho música gran parte del día mientras trabajo. Sé hablar portugués y amo los gatos.  

---

### **Isabella Pino Mosquera**  
-  Tengo 19 años y casi siempre en mis tiempos libres juego tenis de campo, cocino y resuelvo cubos de rubik. Me gustan mucho los perros y soy fanática del cine.

---

### **Andrés Camilo Cataño**  
X  

---

## 2. 🎓 Vínculos Académicos  

### **Carlas Andrea Vergara Romero**  
- Soy estudiante de Ingeniería Industrial de quinto semestre (aunque estoy viendo una materia de tercer semestre 😅).  
Estudié los seis niveles de portugués que ofrece la universidad en el programa Multilingua, me gusta liderar equipos y mantener una comunicación asertiva con los demás.  

---

### **Isabella Pino Mosquera**  
-  Actualmente soy estoy estudiante de ingeniería industrial de tercer semestre. Estudié inglés en la Universidad Eafit y me gradué con un nivel B1.

---

### **Andrés Camilo Cataño**  
X  

---

## 3. 🎬 Nombre del Proyecto y Detalles  

### **Cine Universitario – CineMáter**  

El **Cinema Universitario – CineMáter** es un proyecto desarrollado en **Python** que busca simular y gestionar de manera eficiente la operación de un cine universitario.  
El sistema permitirá a los usuarios seleccionar libremente entre **121 asientos disponibles**, realizar reservas y generar reportes administrativos.  
Además, gestionará tarifas diferenciadas según el tipo de usuario —estudiantes, docentes, administrativos, personal interno y público externo—, ofreciendo una interfaz de consola intuitiva y funcional.  
Los datos generados se almacenarán y exportarán en formato **CSV**, garantizando un manejo claro y ordenado de la información.  

---

## 4. ⚖️ Licencia del Software  

[CineMáter](https://github.com/carlasvergara/TrabajoFinalCineMater) © 2025 by [Carlas Andrea Vergara Romero](https://github.com/carlasvergara)  
is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)  
![CC](https://mirrors.creativecommons.org/presskit/icons/cc.svg)  
![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg)  
![NC](https://mirrors.creativecommons.org/presskit/icons/nc.svg)  
![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg)  

---

## 5. 🎯 Reporte de Visión – Cinema Universitario “CineMáter”  

El **Cinema Universitario – CineMáter** es un software desarrollado en **Python** que gestiona las funciones básicas de un cine universitario.  
Permite registrar usuarios, realizar y cancelar reservas, aplicar tarifas diferenciadas según el tipo de público y generar reportes administrativos.  
Su propósito es fortalecer las competencias en **programación orientada a objetos**, manejo de datos y trabajo colaborativo.  
A través de una interfaz de consola amigable y la exportación de datos en formato **CSV**, el sistema busca optimizar la administración de la información y facilitar la toma de decisiones en un entorno académico.  

---

## 6. ⚙️ Especificación de Requisitos  

### **Requisitos Funcionales**  

Los requisitos funcionales definen las acciones específicas que el sistema debe ejecutar para cumplir con las necesidades del usuario final.  

#### **Registro de usuarios**  
- El sistema debe permitir registrar nuevos usuarios con los siguientes datos obligatorios: nombre, apellido, documento y tipo de vínculo (estudiante, docente, administrativo, oficial interno o público externo).  
- El programa debe validar los datos ingresados (longitud mínima de nombres, solo letras en nombres y apellidos, y solo números en el documento).  

#### **Gestión de reservas**  
- El sistema debe permitir crear una reserva únicamente para usuarios registrados.  
- El usuario podrá seleccionar un asiento de entre 121 sillas disponibles, representadas visualmente con símbolos (“O” para libre y “X” para ocupado).  
- Una vez seleccionada la silla, el sistema debe actualizar su estado de disponible a reservado.  
- El programa debe mostrar un mensaje de confirmación y generar la factura correspondiente.  

#### **Cancelación de reservas**  
- El sistema debe permitir cancelar una reserva existente solo si el usuario tiene una reserva activa.  
- Al cancelar, el asiento reservado debe volver a marcarse como disponible (“O”).  
- Si el usuario no tiene reservas, el sistema debe mostrar un mensaje informativo.  

#### **Consulta de funciones**  
- El sistema debe mostrar las películas programadas para el próximo fin de semana, organizadas por día y hora.  
- Esta información será proporcionada por el docente y precargada en el sistema.  

#### **Módulo administrativo**  
Debe permitir el acceso mediante usuario y contraseña de administrador y generar reportes que incluyan:  
- Total de reservas registradas.  
- Total de tiquetes vendidos.  
- Total de pagos realizados.  
- Promedio de ventas diarias.  
- Listado de usuarios.  
- Usuario con mayor y menor número de reservas.  

#### **Exportación de datos**  
El sistema debe exportar la información de usuarios, reservas y reportes en archivos **CSV** para su posterior análisis.  

---

### **Requisitos No Funcionales**  

Los requisitos no funcionales establecen los criterios de calidad y desempeño del sistema, más allá de las funciones específicas.  

#### **Usabilidad**  
- El sistema debe ofrecer una interfaz de consola clara, organizada y comprensible para el usuario.  
- Los mensajes de error deben ser informativos y orientar al usuario sobre cómo corregirlos.  

#### **Fiabilidad**  
- Los datos ingresados deben validarse para evitar inconsistencias (por ejemplo, duplicación de documentos o asientos reservados dos veces).  
- El sistema debe garantizar la integridad de los datos exportados a CSV.  

#### **Rendimiento**  
- El programa debe ejecutar sus funciones en un tiempo razonable, sin retardos perceptibles en la selección o reserva de asientos.  
- La carga de datos debe realizarse de forma eficiente, permitiendo la actualización rápida de reportes.  

#### **Seguridad**  
- Solo los administradores deben tener acceso al módulo administrativo mediante credenciales predefinidas.  
- Los archivos CSV deben generarse sin información sensible ni duplicada.  

#### **Compatibilidad**  
- El programa debe ser compatible con sistemas operativos Windows, Linux y macOS con **Python 3.10 o superior** instalado.  
- Los archivos CSV deben poder abrirse con herramientas estándar como **Microsoft Excel** o **Google Sheets**.  

#### **Mantenibilidad**  
- El código debe estar estructurado en módulos (por ejemplo, `usuarios.py`, `reservas.py`, `facturacion.py`, `reportes.py`) para facilitar su revisión, corrección y actualización.  
- La documentación técnica y el manual de usuario deben permitir que futuros desarrolladores comprendan fácilmente el funcionamiento del sistema.  

---

## 7. 🧭 Plan de Proyecto  

### **Actividades, Cronograma y Presupuesto del Proyecto**  

El proyecto **Cinema Universitario – CineMáter** se desarrollará a lo largo de 16 semanas del semestre académico, distribuyendo las tareas entre los tres integrantes del grupo.  
Las actividades se estructuran de acuerdo con las etapas de planeación, desarrollo, documentación y sustentación, garantizando un proceso de trabajo organizado y colaborativo.  

---

### **Actividades del Proyecto**  

| **Etapa** | **Actividad principal** | **Descripción** |
|------------|--------------------------|-----------------|
| **Planeación** | Elaboración de actas (Entendimiento, Colaboración y Responsabilidad) | Definir roles, normas de trabajo y compromisos del grupo. |
| **Análisis y diseño** | Reporte de visión y especificación de requisitos | Identificar objetivos, funciones y estructura del software. |
| **Desarrollo** | Programación en Python | Crear los módulos del sistema: registro, reservas, cancelaciones, facturación y reportes. |
| **Pruebas** | Validación del código y control de errores | Verificar el correcto funcionamiento de cada módulo. |
| **Documentación** | Manual de usuario y guía técnica | Elaborar los documentos de soporte para uso y mantenimiento del software. |
| **Entrega y sustentación** | Presentación final del proyecto | Exponer resultados, evidencias y aprendizajes del proceso. |

---

### **Diagrama de Gantt (Semanal)**  

El siguiente diagrama representa visualmente la planificación semanal del proyecto, con las responsabilidades distribuidas entre los tres integrantes y las entregas señaladas.  

📊 **Archivo:**  
`entregables/graficos/Diagrama_Gantt_Semanal_CinemaUdeA.png`  

---

### **Presupuesto del Proyecto (Tiempo de práctica de formación)**  

De acuerdo con los lineamientos del curso, este proyecto no contempla remuneración económica, sino que se evalúa en función del tiempo de práctica académica invertido por los integrantes.  
El grupo está conformado por **tres estudiantes**, cada uno con una dedicación estimada de **50 horas** durante el semestre, para un total de **150 horas** de práctica formativa.  

| **Actividad** | **Horas por integrante** | **Total grupo (3 integrantes)** |
|----------------|--------------------------|---------------------------------|
| Planeación y elaboración de actas | 6 | 18 |
| Análisis y diseño del sistema | 8 | 24 |
| Desarrollo del código y pruebas | 18 | 54 |
| Validaciones y documentación | 10 | 30 |
| Sustentación y ajustes finales | 8 | 24 |
| **Total estimado** | **50 horas** | **150 horas** |

El tiempo invertido equivale a una práctica profesional valorada en **1 Salario Mínimo Legal Vigente (SMLV)** por estudiante, reconociendo el trabajo académico y técnico desarrollado durante el proyecto.  

