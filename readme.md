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

Pasos finales

- Una vez instalado todo, desactivar el entorno virtual ingresando en la terminal "deactivate"
- Luego volver a activar el entorno virtual.
- crear el kernel para ejecutar los comandos: ipython kernel install --user --name=venv
- reiniciamos el Jupyter Notebook
- Seleccionar el kernel utilizado en el entorno virtual y no el nativo del sistema operativo, desde VSCODE en la zona superior derecha.