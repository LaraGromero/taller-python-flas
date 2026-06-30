# Investigación y Desarrollo con Python y Flask
## Descripción
Este proyecto reúne la investigación y los ejemplos prácticos correspondientes a los 28 puntos del taller de Python y Flask.

Durante su desarrollo se estudiaron los fundamentos del lenguaje Python, el desarrollo de aplicaciones web con Flask, el uso de bases de datos SQLite, el manejo de Git y GitHub, así como las buenas prácticas para organizar un proyecto profesional.

Cada punto incluye una explicación teórica y un ejemplo funcional que permite comprender el tema tratado.

## Temas desarrollados
### Python
- Variables y tipos de datos.
- Operadores.
- Condicionales.
- Funciones.
- Listas, tuplas y diccionarios.
- Manejo de archivos.
- Manejo de excepciones.
- Programación Orientada a Objetos (POO).

### Flask
- Instalación de Flask.
- Primera aplicación web.
- Rutas y decoradores.
- Plantillas HTML con Jinja2.
- Formularios HTML y método POST Y GET.
- Variables de URL y parámetros de consulta.
- Archivos estáticos (CSS, JavaScript e imágenes).
- Herencia de plantillas.
- Redireccionamiento y uso de `url_for()`.
- Manejo de errores 404 y 500.
- Sesiones.
- API REST con respuestas JSON.

### Bases de datos
- SQLite con Python.
- Integración de Flask con SQLite (CRUD básico).

### Herramientas de desarrollo
- Entornos virtuales (`venv`).
- Git.
- GitHub.
- Organización profesional de proyectos Flask.
- Archivo `.gitignore`.
- Documentación con `README.md`.

## Tecnologías utilizadas
- Python 3
- Flask 3.1.2
- SQLite
- HTML5
- CSS3
- Jinja2
- Git
- GitHub
- Visual Studio Code

## Estructura del proyecto

```text
taller-python-flask/
│
├── parte1_python/
│   ├── 01_variables.py
│   ├── 02_condicionales.py
│   ├── 03_ciclos.py
│   ├── 04_funciones.py
│   ├── 05_ManejoArchivos.py
│   ├── 06_exepciones.py
│   ├── 07_exepciones.py
│   ├── 08_POO.py
│   └── estudiantes.txt
│
├── parte2_flask/
│   ├── templates/
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── base.html
│   │   ├── form.html
│   │   ├── index.html
│   │   └── pagina.html
│   │
│   ├── 09_variables.py
│   ├── 10_condicionales.py
│   ├── 11_ciclos.py
│   ├── 12_funciones.py
│   ├── 13_ManejoArchivos.py
│   ├── 14_exepciones.py
│   ├── 15_exepciones.py
│   ├── 16_POO.py
│   ├── 17_rendiccionamiento.py
│   ├── 18_manejo de errores.py
│   ├── 19_sesiones.py
│   └── 20_apirest.py
│
├── parte3_bd_git/
│   ├── templates/
│   │   └── estudiantes.html
│   │
│   ├── 21_sqlite.py
│   ├── 22_crud.py
│   ├── 23_venv.py
│   ├── 24_git.py
│   ├── 25_github.py
│   ├── 26_estructura.py
│   ├── 27_gitgnore.py
│   └── colegio.bd
├── proyecto_final/
│   ├── static/
│   │   ├── ccs/
│   │   │  └──estilos.css
│   │   │
│   │   └──img/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── contactos.html
│   │   ├── formulario.html
│   │   └── inicio
│   │
│   ├── app.py
│   └── agenda.bd
├── requirements.txt
├── .gitignore
├── README.md
└── investigación.md
```

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/LaraGromero/taller-python-flas
```

2. Crear un entorno virtual.

```bash
python -m venv venv
```

3. Activar el entorno virtual.

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

4. Instalar las dependencias.

```bash
pip install -r requirements.txt
```

5. Ejecutar la aplicación.

```bash
python app.py
```



## Objetivo
El objetivo de este proyecto es fortalecer los conocimientos fundamentales de Python y Flask mediante el desarrollo de ejemplos prácticos, comprendiendo el funcionamiento de aplicaciones web, el manejo de bases de datos, el control de versiones con Git y la organización profesional de proyectos.


## Autor

**Laura Gonzalez Romero**

Estudiante de Bachillerato y aprendiz de Programación de Software en Centro de Biotecnologia Industrial, Regional Valle (SENA).
