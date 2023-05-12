# Tercera-pre-entregaHdezVelaSuarez
Proyecto WEB Django con patrón MVT
Este proyecto es una aplicación web Django que utiliza el patrón Modelo-Vista-Templa (MVT). Incluye lo siguiente:

Herencia HTML: Se utilizó la herencia de plantillas para mantener la consistencia en el diseño de la aplicación.

Tres clases en models: Se definieron tres clases en el archivo models.py: MiModelo, SegundoModelo y TercerModelo. Cada una de estas clases tiene sus propios campos, que pueden ser accedidos mediante el ORM de Django.

Formularios para insertar datos: Se creó un formulario para cada una de las clases de modelos definidas en el proyecto (MiModeloForm, SegundoModeloForm y TercerModeloForm). Estos formularios permiten al usuario agregar nuevos datos a la base de datos.

Formulario de búsqueda: Se incluyó un formulario de búsqueda que permite al usuario buscar datos específicos en la base de datos.

Orden de las funcionalidades: Para utilizar la aplicación, se debe seguir el siguiente orden:

Primero, se deben agregar datos a través de los formularios de inserción.
Luego, se puede utilizar el formulario de búsqueda para encontrar datos específicos en la base de datos.
Instrucciones de instalación y uso
Clona este repositorio a tu máquina local.
Abre una terminal y navega hasta la carpeta del proyecto.
Instala las dependencias necesarias con el siguiente comando: pip install -r requirements.txt
Configura la base de datos en el archivo settings.py.
Crea las migraciones necesarias con el comando: python manage.py makemigrations
Realiza las migraciones con el comando: python manage.py migrate
Inicia el servidor con el comando: python manage.py runserver
Abre tu navegador y visita la siguiente URL: http://localhost:8000/
Estructura del proyecto
hugo_proyecto/: Carpeta principal del proyecto.
hugo_app/: Carpeta de la aplicación web Django.
templates/: Carpeta que contiene las plantillas HTML utilizadas en la aplicación.
models.py: Archivo que contiene las definiciones de los modelos utilizados en la aplicación.
views.py: Archivo que contiene las definiciones de las vistas utilizadas en la aplicación.
forms.py: Archivo que contiene las definiciones de los formularios utilizados en la aplicación.
manage.py: Archivo de Django para manejar comandos.
README.md: Archivo que estás leyendo actualmente.

Contribuciones
Si deseas contribuir a este proyecto, eres más que bienvenido. Solo asegúrate de seguir estas pautas:

Haz un fork del repositorio.
Crea una rama para tus cambios: git checkout -b feature/nombre-del-cambio.
Realiza los cambios necesarios y haz commit de tus cambios: git commit -m "Descripción del cambio".
Haz push de tus cambios a tu fork: git push origin feature/nombre-del-cambio.
Crea un pull request en este repositorio con tus cambios. Describre detalladamente qué cambios realizaste y por qué son importantes.
