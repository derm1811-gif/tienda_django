# Tienda Django

Aplicación web desarrollada con Django para registrar, editar, eliminar y listar productos almacenados en una base de datos SQLite.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Git y GitHub

## Funcionalidades implementadas

- Registro de productos
- Visualización de productos en una tabla
- Detalle de cada producto
- Edición de información
- Eliminación de productos
- Redirección desde la raíz del proyecto a la vista de productos

## Requisitos

- Python 3.x
- Django
- Git

## Ejecución

1. Crear un entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install django
```

4. Ejecutar migraciones:

```bash
python manage.py migrate
```

5. Iniciar el servidor:

```bash
python manage.py runserver
```

6. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Estructura del proyecto

```text
tienda/
├── manage.py
├── tienda/
├── productos/
├── templates/
├── db.sqlite3
├── README.md
└── .gitignore
```

## Notas

La aplicación permite registrar productos, guardarlos en SQLite y luego listarlos desde la interfaz web creada con Django.
