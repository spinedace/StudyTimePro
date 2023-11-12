Team name: Los rolos  
Team members:  
David Camelo -  dcamelos  
Frank Medina - striw-ey  
Santiago Pineda - spinedace  
Sergio Reita - sreita  

## como configurar el proyecto 

prerequisito:tener python instalado

1.Clona el repositorio usando el comando
```
git clone https://github.com/spinedace/StudyTimePro.git
```
2.Entra en la carpeta usando el comando
```
cd StudyTimePro
```
3.Crea el entorno virtual , preferiblemente en la carpeta del repositorio usando el comando

En macOs y linux (si estas usando python 3 puedes usalo tambien en windows)
```
python3 -m venv venv
```
en windows
```
python -m venv venv
```
4.Activa el entorno virtual

en linux y macOS

```
source venv/bin/activate
```
en windows

```
venv/Scripts\activate
```
5.Instala los requerimientos

```
pip install -r requirements.txt
```
6.Crea las migraciones

```
python manage.py makemigrations
```
7.Aplica las migracion

```
python manage.py migrate
```
8. Crea un super usuario

```
python manage.py createsuperuser
```
despues de ejecutar este comando te pedira correo,usuario y contraseña para crear el super usuario ,puedes omitir rellenar el correo pero no los otros dos campos

9.Correr el servidor

```
python manage.py runserver
```

## Al Finalizar para salir 

1.Usa el control + C para detener el servidor 

2. Para salir de entorno virtual usa el comando 

```
deactivate
```