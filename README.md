# Proyecto XXX
descripcion

## instalacion global de virtualenv
pip install virtualenv

## verificar que este instalado
virtualenv --version   

## en la carpeta del proyecto correr el siguiente comando para crear entorno virtual
virtualenv -p python3 env

## inicializar maquina virtual
.\env\Scripts\activate
source env/bin/activate

## correr archivo raiz
python .\index.py

## detener maquina virtual
deactivate

## crear archivo de dependencias de desarrollo si no sea creado
pip freeze > packages.txt

## instalar dependencia ya creadas
pip install -r ./packages.txt

## ver lista de dependencias instaladas
pip list

## instalacion flask
pip install Flask  

## crear ignore para no suvir la maquina virtual
.gitignore
env/

## version de pip
pip --version

## desigtalar flask
pip uninstall Flask