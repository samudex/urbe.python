# CoworkReserveAPITest

REST API para Sistema de Reservaciones de Coworking

## Descargar/Clonar Proyecto

Si posees una cuenta de GitHub, clona el proyecto de la siguiente manera en la línea de comando (CMD):

```$
git clone https://github.com/itsronalds/CoworkReserveAPITest.git
```

## Importación de la Base de Datos

En la carpeta **database** existe un archivo llamado **coworking_db.sql**, ese archivo lo deberán importar en el programa de **Workbench** o **XAMPP**, dependiendo de lo que utilicen.

## Crear Entorno Virtual

Luego de clonar el proyecto, ingresa a la raíz del proyecto y escribe el siguiente comando:

```$
python -m venv venv
```

## Activar/Desactivar Entorno Virtual

Cuando se termine el proceso de creación del **venv**, activaremos nuestro entorno virtual tecleando el siguiente comando en la raíz del proyecto:

```$
venv\scripts\activate
```

**NOTA**: No es necesario crear el entorno virtual múltiples veces, si ya lo tienes no ejecutes una y otra vez el paso previo de **Crear Entorno Virtual**.

Si deseas desactivar el entorno virtual ejecuta el siguiente comando:

```$
venv\scripts\deactivate
```

## Instalar Dependencias

**Luego de activar nuestro entorno virtual**, debemos instalar las dependencias del proyecto:

```$
pip install -r requirements.txt
```

## Inicializar Proyecto

Luego de instalar las dependencias y teniendo activo nuestro entorno virtual, ejecutamos el siguiente comando:

```$
uvicorn app:app --reload --port 8000
```

**El puerto puede ser el que ustedes quieran**
