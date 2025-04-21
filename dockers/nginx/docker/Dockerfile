# Imagen base oficial de Ubuntu
FROM ubuntu:24.04

# Variables de entorno para evitar interacción durante instalación
ENV DEBIAN_FRONTEND=noninteractive

# Obtine el UID del sistema que se le pasa desde el docker-compose
ARG UID

# Veridicamos que no exista previemante el UID que le pasamos
RUN if id -u ${UID} >/dev/null 2>&1; then \
        userdel $(id -un ${UID}); \
    fi 

# Creamos el usuario con el UID que le pasamos 
# Este es el usuario con el que trabajaremos todo el tiempo
RUN useradd -u ${UID} -m -s /bin/bash devuser

# Seteamos la zona horaria donde estamso
# Cambiar esto a vuestro país / ciudad
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Actualizar e instalar dependencias básicas y aplicaciones necesarias
RUN apt-get update && apt-get install -y \
    openssl openssh-client wget zip curl gcc make perl vim htop \
    libpng-dev zlib1g-dev libzip-dev libxml2-dev libicu-dev build-essential sudo \
    net-tools iproute2 iputils-ping locales \ 
    curl \
    gnupg \
    ca-certificates \
    lsb-release \
    software-properties-common \
    build-essential supervisor \
    python3 python3-pip python3-venv python3-dev libmysqlclient-dev \
    nginx mysql-client libpq-dev postgresql-client zsh \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get upgrade -y

# Seteamos el teclado en español
RUN locale-gen es_ES.UTF-8
RUN echo 'echo "LANG=es_ES" > /etc/default/locale'
ENV LC_ALL=es_ES.UTF-8

# Se añade el usuario a los grupos de sudo y admin
RUN adduser devuser sudo
RUN adduser devuser adm

# Le quitamos el password a sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Crear enlaces simbólicos necesarios para python, supervisor y nginx
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /home/devuser/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
RUN ln -s /home/devuser/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Instalar Node.js (ejemplo: v20.x LTS) cambiar si hay versiones LTS mas recientes
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get update && apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Exponer puertos necesarios
EXPOSE 80 3000

# El contenedor al arrancar lanzará supervisor
# CMD ["nginx", "-g", "daemon off;"]
# CMD ["/usr/bin/supervisord"]
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
