Team name: Los rolos  
Team members:  
David Camelo -  dcamelos  
Frank Medina - striw-ey  
Santiago Pineda - spinedace  
Sergio Reita - sreita  

Para configurar el proyecto ve a la terminal y sigue los siguientes pasos

1) crea el entorno virtual , preferiblemente en la carpeta del repositorio usando el comando
python -m venv STPenv

2)Inicializa el entorno virtual usando el comando
STPenv\Scripts\activate

3)Usa el siguiente comando para instalar los requerimientos en tu entorno virtual
pip install -r requirements.txt

IF: si te suelta un error puedes instalar manualmente usando los comandos 
pip install django 
pip install pillow

4)Usa el siguiente comando para ir a la carpeta del proyecto
   cd StudyTimePro
5)Inica el servidor usando el comando 
python manage.py runserver
te soltara un enlace que usaras en el navegador en mi caso fue http://127.0.0.1:8000/ pero puede variar 

6)si deseas detener el servidor usa control + C en el terminal
7)si deseas salir del entorno virtual usa  el comando deactivate 



