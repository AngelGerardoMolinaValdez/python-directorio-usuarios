# ***Sistema de Gestión de Clientes***

Este archivo describe el proyecto y proporciona instrucciones para ejecutar la aplicación.


# ***Descripción general***

El "Sistema de Gestión de Clientes" es una aplicación de línea de comandos que permite a un usuario gestionar los clientes de una empresa. El usuario puede agregar, eliminar y actualizar información de los clientes, y también puede ver una lista de todos los clientes existentes.

La aplicación consta de cuatro componentes principales:

- `model`: define la estructura de datos de un cliente y proporciona funciones para agregar, eliminar y actualizar clientes.
- `inputs`: proporciona funciones para obtener información de los usuarios, como el nombre y la dirección de un nuevo cliente.
- `errors`: define excepciones personalizadas que se lanzan cuando se producen errores durante la ejecución de la aplicación.
- `main`: contiene la lógica principal de la aplicación, como el bucle principal que muestra el menú de opciones y maneja las entradas del usuario.


# ***Requisitos***

- [Python](https://www.python.org/downloads/) (3.11)
- [prettytable](https://pypi.org/project/prettytable/)
- [pyfiglet](https://pypi.org/project/pyfiglet/)


## ***Instalación***

- `pip install prettytable`


- `pip install pyfiglet`

Para instalar python:
- [Mac](https://docs.python.org/es/3/using/mac.html)
- [Linux](https://docs.python.org/es/3/using/unix.html)
- [Windows](https://docs.python.org/es/3/using/windows.html)


# ***Ejecutar la aplicación***

Para ejecutar la aplicación, ejecute el archivo `main.py` en la línea de comandos.

```sh
python main.py
```

Esto mostrará un menú de opciones al usuario, donde puede seleccionar una acción para realizar.


# ***Ejecutar pruebas***

Las pruebas unitarias para la aplicación se encuentran en el directorio `tests`. Para ejecutar las pruebas, ejecute cada archivo de prueba utilizando el siguiente comando:

```sh
python test_suite.py
```
