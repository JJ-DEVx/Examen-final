\# 🎓 Aplicación de Gestión de Talleres


\## 📌 Descripción


Aplicación web para gestionar talleres de formación profesional.

Permite a estudiantes visualizar talleres disponibles y registrarse, mientras que los administradores pueden crear, editar y eliminar talleres.


\---



\## 🌍 Demo en línea
(Al abrir los links esperar de 10 a 20seg para que cargue la informacion predeterminada. Y si gusta añadir talleres en el panel de admin)


🔗 Página principal (Estudiantes):

https://jj-devx.github.io/Examen-final/



🔗 Panel de administrador:

https://jj-devx.github.io/Examen-final/admin.html
(contraseña: admin123)



🔗 API (Backend):

https://talleres-api-myx2.onrender.com/workshops



\---



\## ⚙️ Tecnologías utilizadas


\* Backend: Flask (Python)

\* Frontend: HTML, CSS, JavaScript

\* Estilos: Bootstrap

\* Base de datos: SQLite

\* Despliegue:


&#x20; \* Render (backend)

&#x20; \* GitHub Pages (frontend)


\---


\## 🚀 Funcionalidades



\### 👨‍🎓 Estudiantes




\* Ver lista de talleres

\* Ver detalles (fecha, hora, lugar)

\* Registrarse a talleres



\### 👨‍💼 Administrador




\* Crear talleres

\* Editar talleres

\* Eliminar talleres


\---


\## 🔌 API REST



\* GET /workshops → Obtener todos los talleres

\* GET /workshops/{id} → Obtener detalles

\* POST /workshops → Crear taller

\* PUT /workshops/{id} → Actualizar taller

\* DELETE /workshops/{id} → Eliminar taller

\* POST /workshops/{id}/register → Registrar estudiante


\---


\## ▶️ Ejecución local


1\. Ir al backend:

&#x20;  cd backend

2\. Instalar dependencias:

&#x20;  pip install -r requirements.txt

3\. Ejecutar:

&#x20;  python app.py

4\. Abrir:

&#x20;  index.html


\---


\## 📁 Estructura del proyecto


backend/ → API y lógica del sistema

index.html → interfaz de estudiantes

admin.html → panel de administración

script.js → lógica del frontend

styles.css → estilos


\---


\## 👥 Autor
John Vallarino / 3-754-306
Alex Parra / E-8-192592
Rodrigo Camarena / 8-941-1023



Proyecto desarrollado para la asignatura de Programación de computadora 4.


---

# 🧠 Documentación Técnica

## 🏗️ Arquitectura del sistema

La aplicación sigue una arquitectura cliente-servidor:

* **Frontend:** desarrollado con HTML, CSS y JavaScript. Maneja la interfaz de usuario.
* **Backend:** desarrollado con Flask. Implementa una API REST para la gestión de talleres.

El frontend consume la API mediante peticiones HTTP usando `fetch()`.

---

## 🔄 Flujo de funcionamiento

1. El usuario accede al frontend (GitHub Pages)
2. El frontend realiza solicitudes a la API (Render)
3. El backend procesa la solicitud
4. Se consulta o actualiza la base de datos
5. Se devuelve una respuesta en formato JSON
6. El frontend renderiza los datos dinámicamente

---

## 🗄️ Base de datos

Se utiliza SQLite como sistema de almacenamiento.

### Tabla: Workshop

* id
* name
* description
* date
* time
* place
* category

### Tabla: Registration

* id
* student_name
* workshop_id

---

## 🔌 Arquitectura de la API

La API sigue el estilo REST:

* Uso de métodos HTTP (GET, POST, PUT, DELETE)
* Respuestas en formato JSON
* Manejo de códigos de estado HTTP (200, 201, 404, etc.)

---

## 🚀 Despliegue

* Frontend: GitHub Pages
* Backend: Render

Nota: El backend puede tardar unos segundos en responder la primera vez debido al modo gratuito de Render.

---

# 🧪 Extras Implementados

# ✅ Validaciones

* Uso de atributos `required` en formularios
* Validación de nombre en registro de estudiantes
* Verificación básica de datos antes de enviarlos

# Pruebas

Se implementaron pruebas unitarias básicas para validar endpoints principales de la API.

Ejecutar:

cd backend  
python -m unittest discover ../tests

---

# 🎨 Interfaz de usuario

* Uso de Bootstrap para diseño responsivo
* Tarjetas para mostrar talleres
* Tabla para administración
* Formularios estilizados

---

# 🔄 Renderizado dinámico

* Los talleres se cargan desde la API en tiempo real
* Se generan dinámicamente con JavaScript
* No es necesario recargar la página

---

## ⚙️ Buenas prácticas

* Separación de frontend y backend
* Uso de API REST
* Código documentado
* Uso de Git para control de versiones

---

# 🚀 Mejoras futuras

* Migrar a base de datos PostgreSQL
* Agregar pruebas unitarias
* Mejorar validaciones del backend











