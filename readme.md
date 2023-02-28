## Trabajo Práctico Integrador - METODO ANALÍTICO

## Cátedra Modelo y Simulacion

## Licenciatura en sistemas de Información - Universidad Nacional de Misiones

### Pasos Previos

Python

- Verificar que tenemos instalado python en nuestro sistema operativo

Creamos Entorno virtual

- En linux ejecutar: python3 -m venv venv
- En windows ejecutar: py -m venv venv

Activamos entorno virtual

- En linux ejecutar:source venv/bin/activate
- En windows ejecutar: .\venv\script\activate

Instalamos dependencias

- pip install numpy
- pip install ipython
- pip install ipykernel
- pip install plotly
- pip install matplotlib 
- pip install nbformat
- pip install scipy
- pip install pandas

Configuraciones finales

- Una vez instalado todo, desactivar el entorno virtual ingresando en la terminal "deactivate"
- Luego volver a activar el entorno virtual.
- crear el kernel para ejecutar los comandos: ipython kernel install --user --name=venv
- reiniciamos el Jupyter Notebook
- Seleccionar el kernel utilizado en el entorno virtual y no el nativo del sistema operativo, desde VSCODE en la zona superior derecha.

Pasos para la ejecución.

- Borrar los documentos de textos ("datos_extraidos_diferencia_humedad.txt", "datos_extraidos_humedad.txt", "datos_extraidos_promedios_humedad.txt")
- Ejecutar el archivo depuracionDatos.py
- Abrir y ejecutar los pasos del Notebook de Jupyter "MetodoAnalitico.ipynb"