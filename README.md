INTRODUCCION
* Este proyecto es una aplicación de consola que funciona como un sistema de gestión y análisis de datos geográficos y demográficos por paises. Su objetivo principal es permitir el control sobre un registro de países, ofreciendo herramientas interactivas para administrar la información de forma centralizada.

USO DEL PROGRAMA
* El script está estructurado bajo un menu principal que posee diferentes opciones, las cuales el usuario puede elegir introduciendo el numero de la opcion deseada en la consola. Cada opcion e ingreso de datos posee su propia verificacion y validacion, evitando asi campos erroneos o incompletos.
* El flujo de funcionamiento del programa esta explicado en el propio codigo, mediante mensajes en consola que describen la accion permitida que el usuario puede realizar
  
LOGICA DEL SISTEMA
Como se menciona anteriormente, todo el programa se basa en un menu de 7 opciones elegibles. Cuya repeticion esta controlada mediante un while loop.
1. 'Agregar Pais': Opcion que permite al usuario ingresar un nuevo elemento 'pais'. Una vez pasadas las validaciones, se agrega en el archivo CSV
2. 'Actualizar Datos Pais': Opcion que busca un pais especificado por el usuario, y permitiendole actualizar sus campos en el archivo CSV
3. 'Buscar Pais': Opcion donde se busca/an elemento/os dentro del archivo CSV, que coincida con la solicitud establecida por el usuario
4. 'Aplicar Filtros': Filtra los elementos del archivo CSV por el rango de busqueda establecido por el usuario, y los muestra en pantalla
5. 'Aplicar Ordenes': Ordena todos los elementos del archivo CSV, por algunos de los tres campos (Superficie, Continente, Poblacion) que haya elegido el usuario
6. 'Mostrar Estadisticas': Opcion que muestra una serie de estadisticas básicas, tales como 'pais con mayor poblacion' o 'promedio de poblacion'
7. 'Salir': Es la opcion que le indica al while loop que deje de ejecutarse

ARCHIVO CSV
Los datos se almacenan en un archivo 'archivo.csv' con codificación 'utf-8' para soportar caracteres especiales. Cada fila representa un país con la siguiente estructura de índices:
* '[0]' - Nombre (String, clave de identificación)
* '[1]' - Población (Entero)
* '[2] - Superficie en $km^2$ (Entero)
* '[3]' - Continente (String validado mediante lista estática)

ESTRUCTURA DEL REPOSITORIO
* 'archivo.csv' - Arhivo de texto plano donde se almacenan los datos del programa(simula una base de datos)
* 'TrabajoIntegradorProgramacion.py' - Archivo  donde se almmacena todo el codigo y la logica del programa, en lenguaje Python

* Los ejemplos de salidas/entradas y la evidencia de errores se encuentran en el pdf principal, en el apartado 'Simulacion de Codigo e identificacion de errores', para una mejor organizacion

