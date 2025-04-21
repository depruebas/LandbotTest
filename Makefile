#!/bin/bash

# Para ejecutar cualquier acción del fichero Makefile lo hacemos 
# de la siguiente forma:
#	Iniciar contenedores:   make start
#   Parar contenedores:		make stop


# Obtiene el id de usuario que se lo pasaremos a la maquina virtual
# para poder conectar host y docker facilmente
U_ID = $(shell id -u)

# Definimos las llamadas
.PHONY: all nginx create_network

# Define la ruta base del directorio actual
BASE_DIR := $(CURDIR)

# Nombre de la red
NETWORK_NAME := mynetwork

# IPs validas para la red
SUBNET := 172.21.0.0/24

# all: create_network nginx

# crea la red de los contenedores que tenemos en el proyecto
create_network:
	@if ! docker network inspect $(NETWORK_NAME) >/dev/null 2>&1; then \
		echo "Creating network $(NETWORK_NAME) with subnet $(SUBNET)..."; \
		docker network create --subnet=$(SUBNET) $(NETWORK_NAME); \
	else \
		echo "Network $(NETWORK_NAME) already exists."; \
	fi

# Inicia los contendores
start: create_network
	@echo "Starting Nginx container..." 
	cd $(BASE_DIR)/dockers/nginx && UserUID=${U_ID} docker-compose up -d

# Para y elimina los contenedores
down:
	@echo "Destruyendo containers ..."
	cd $(BASE_DIR)/dockers/nginx && UserUID=${U_ID} docker-compose down

# Para los contenedores
stop:
	@echo "Parando containers ..."
	cd $(BASE_DIR)/dockers/nginx && UserUID=${U_ID} docker-compose stop

# Entra en el contenedor de nginx para trabajar desde el propio servvidor 
web:
	@echo "Enter into nginx container..."
	UserUID=${U_ID} docker exec -it --user ${U_ID} flask_nginx bash
  
# Reconstruye los contenedores.
# build se tiene que ejecutar cada vez que el fichero Dockerfile se modifique
build:
	@echo 'Reiniciando containers'
	cd $(BASE_DIR)/dockers/nginx && UserUID=${U_ID} docker-compose build


