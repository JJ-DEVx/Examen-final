# 🎓 Sistema de Gestión de Talleres

Aplicación web desarrollada con Flask para gestionar talleres de formación profesional. Permite a estudiantes ver talleres disponibles y registrarse, y a administradores crear, editar y eliminar talleres.

## 🚀 Tecnologías utilizadas

- **Backend:** Flask (Python)
- **Base de datos:** SQLite con SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Estilos:** Bootstrap
- 

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd workshops-app
Crear entorno virtual:
python -m venv venv
venv\Scripts\activate
Instalar dependencias:
pip install -r requirements.txt

▶️ Ejecución
Ir a la carpeta backend y ejecutar:
cd backend
python app.py
El servidor se ejecutará en: http://127.0.0.1:5000

🌐 Uso de la aplicación
👨‍🎓 Estudiantes
Ver lista de talleres
Registrarse en talleres

Abrir en el navegador:

frontend/index.html
👨‍💼 Administradores
Crear talleres
Editar talleres
Eliminar talleres

Abrir en el navegador:

frontend/admin.html
🔌 API REST
Método	Endpoint	Descripción
GET	/workshops	Obtener todos los talleres
GET	/workshops/{id}	Obtener un taller específico
POST	/workshops	Crear un nuevo taller
PUT	/workshops/{id}	Actualizar un taller
DELETE	/workshops/{id}	Eliminar un taller
POST	/workshops/{id}/register	Registrar un estudiante

🗄️ Base de datos
Se utiliza SQLite con SQLAlchemy.

Modelo Workshop
id
name
description
date
time
place
category

Modelo Registration
id
student_name
workshop_id

🏗️ Arquitectura
La aplicación sigue una arquitectura cliente-servidor:
Frontend → Interfaz de usuario (HTML, CSS, JS)
Backend → API REST con Flask
Base de datos → SQLite

👥 Autores

Proyecto desarrollado como parte del examen final
John Vallarino / 3-754-306
-----
-----
