# Configuración

El proyecto esta en un entorno dockerizado y solo probado en Linux, se puede ejetuar desde una maquina virtual linux (ubuntu) siempre que tenga instalado docker y docker-compose

Y todo se controla con un Makefile en el directorio principal

Estructura del proyecto:  



            LandbtotTest\dockers
                        \srv


en el directorio dockers esta el directorio nginx que es el docker de la aplicación. Esta en un docker aparte para poder ir añadiendo entornos MySql, postgreSQL, redis, etc ..

El proyecto se encuentra en src y esta realizado en Flask, es muy simple, recibe un post con este formato:

            {
                "topic": "pricing",
                "description": "Necesito ayuda con el plan empresarial"
            }

a esta url:

            http://172.21.0.50/api/topic

Dependiendo del topic hace una cosa u otra:

- sales envia un mail
- pricing graba en un log la informacion de entrada.

Para que envie mail de verdad se tiene que añadir la configuración del SMTP en el fichero .env

# Como ejecutar el proyecto

Despues de clonar el repo entrar en el directorio LandbtotTest y ejecutar:

- Copiar ./src/app/.env.example a ./src/app/.env y cambiar la configuracion del mail

- **make init**  (este comando solo la primera vez que se instala el proyecto)
Inicializa el entorno instalando el entorno virtual de python para el proyecto y arranca el contenedor

Esto inicializa el proyecto, comprobar que docker ha inicializado bien con **docker ps** y lanzar un POST a

            http://172.21.0.50/api/topic

con el siguiente contenido

            {
                "topic": "pricing",
                "description": "Necesito ayuda con el plan empresarial"
            }

topic puede ser sales 

Otros comandos para manejar el entorno.

- **make web**
(Entra dentro de el contenedor)

- **make start** 
(Inicia el contenedor)

- **make down**
(Para y borra el contenedor)

- **make stop** 
(Para el contenedor)

- **make build** 
(Reconstruye el contenedor, solo utilizar si se cambia el Dockerfile)


# El proyecto
Esta dividido en diferentes ficheros y dirctorios para que puedan añadirse topics.

En el directorio controllers estan las clases de los topics y lo que tienen que hacer

El fichero config.py esta vacio pero es para centralizar las configuraciones y no usar os.getenv() por toda la aplicacion

El fichero routes.py, pues eso.

El topic "sales" envia un mail se configura en .env los datos del SMTP, sino devuelve json con status=false

El topoc "pricing" graba un log, no tenia un slack a mano.


/



