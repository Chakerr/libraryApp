# 📚 library_app

`library_app` es una aplicación de consola desarrollada en Python como parte del parcial final de la materia **Sistemas Operativos**.  
Permite gestionar miembros, libros y préstamos en una biblioteca usando SQLite como base de datos local, con una interfaz por terminal.  
Está diseñada para ser liviana, modular y fácil de ejecutar en cualquier entorno con Python 3.

---

## 📦 Requisitos

- Python 3.8 o superior
- pip
- bash (para ejecutar `setup.sh` en Linux/macOS)
- En Windows, usar Git Bash o ejecutar manualmente los pasos del script

---

## ⚙️ Instalación y ejecución rápida

Puedes usar el siguiente comando para configurar automáticamente todo el entorno virtual, instalar dependencias y ejecutar el programa:

```bash
bash setup.sh
```

Este script hace lo siguiente:

1. Crea un entorno virtual en `.venv`
2. Activa el entorno
3. Instala las dependencias necesarias (`tabulate`, `rich`)
4. Asegura permisos de la base de datos (solo en Linux/macOS)
5. Ejecuta el programa principal `run.py`

---

## 🗂️ Estructura del proyecto

```
library_app/
├── data/                 # Carpeta donde se crea la base de datos SQLite
│   └── library.db
├── .venv/                # Entorno virtual (excluido en .gitignore)
├── db.py                 # Inicializa y crea las tablas de la base de datos
├── operations.py         # Lógica de negocio (CRUD, préstamos, devoluciones)
├── run.py                # Interfaz interactiva del usuario (menú en consola)
├── setup.sh              # Script para configurar y lanzar la app
├── requirements.txt      # Dependencias del entorno
├── README.md             # Documentación del proyecto
└── library.log           # Archivo de registro de operaciones (logging)
```

---

## 🧠 ¿Qué hace cada archivo?

- `db.py`: Crea las tablas `members`, `books` y `loans` si no existen. Usa SQLite como sistema de base de datos local.
- `operations.py`: Implementa las funciones principales del sistema (registrar miembros/libros, prestar, devolver, ver vencidos). Registra todo en `library.log`.
- `run.py`: Muestra el menú interactivo. Usa `rich` para mejorar la presentación. Captura `Ctrl + C` para salir ordenadamente.
- `setup.sh`: Automatiza la instalación y configuración del entorno.
- `library.log`: Archivo generado automáticamente que registra todas las operaciones importantes (miembros registrados, préstamos, devoluciones).
- `.gitignore`: Excluye el entorno virtual, la base de datos y archivos temporales del control de versiones.

---

## 📌 Funcionalidades

- 📥 Registrar nuevos miembros con nombre y email (verifica duplicados).
- 📚 Registrar nuevos libros, con cantidad de copias disponibles.
- 📖 Realizar préstamos (verifica si hay copias).
- ✅ Registrar devoluciones y actualizar inventario.
- 🕒 Ver préstamos vencidos automáticamente.
- 📋 Visualización elegante con `rich`.
- 📜 Registro de acciones en `library.log`.
- ⌨️ Salida limpia al presionar `Ctrl + C`.

---

## 📝 Ejemplo de ejecución

```bash
$ bash setup.sh

--- MENÚ PRINCIPAL ---
1. Registrar miembro
2. Listar miembros
3. Registrar libro
4. Listar libros
5. Prestar libro
6. Devolver libro
7. Ver préstamos vencidos
0. Salir
Seleccione una opción:
```

---

## 🪪 Licencia

Este proyecto se publica bajo la licencia MIT. Puedes modificarlo, reutilizarlo o adaptarlo para fines educativos.

---

## 👤 Autor

**Luis Gabriel Romero**  
Estudiante de Ingeniería de Sistemas  
Universidad Piloto de colombia
