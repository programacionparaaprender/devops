
## Curso
>- https://www.udemy.com/course/draft/3574995/learn/lecture/22811709?start=0#overview

### enlaces
>- https://learn.microsoft.com/es-es/sql/linux/quickstart-install-connect-docker?view=sql-server-ver16&pivots=cs1-bash

## Sección 1

### 1. Bienvenida del curso

### 2. Instalar Docker Desktop para windows

### 3. Bajar imagenes de SQL Server
>- docker pull mcr.microsoft.com/mssql/server:2017-latest
>- docker pull mcr.microsoft.com/mssql/server:2019-latest

### 4. Crear contenedores SQL Server
>- docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=980Parace12tamol%&" -p 14033:1433 --name sqll -h sqll -d mcr.microsoft.com/mssql/server:2019-latest
>- colocar para poder acceder al servidor .,14033
>- 824a40ea663702c1f0b2b7225b078bab2207bd35802f41b97315234c27fa04b6
>- docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=PasswOrd" -p 14034:1433 --name sql2 -h sql2 -d mcr.microsoft.com/mssql/server:2017-latest
>- 235eefcca8c101ac137e3cdccccefc63075646044b063b4a7143b3e97565c451
>- docker-compose build
>- docker-compose up -d
>- docker-compose down

### 5. Copiar y restaurar base de datos dentro del contenedor
>- docker cp E:\tmp\docker\AdventureWorks2017.bak conteiner_id:/var/opt/mssql/data
>- docker cp C:\Users\luis1\Downloads\AdventureWorks2017.bak 824a40ea6637:/var/opt/mssql/data

### 6. Como cambiar parámetros de instancia
>- ejecutamos comandos.sql
>- docker ps
>- docker restart 824a40ea6637

### 7. Persistir datos fuera del contenedor
>- borrar contenedor para volver a crearlo
>- docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=980Parace12tamol%&" -p 14033:1433 -v c:/Users/luis1/Downloads/sqlserver/data:/var/opt/mssql/data -v c:/Users/luis1/Downloads/sqlserver/log:/var/opt/mssql/log -v c:/Users/luis1/Downloads/sqlserver/log:/var/opt/mssql/secrets -d mcr.microsoft.com/mssql/server:2019-latest
>- 0662d23d58cdcf607f1e1f0e2f650c109f61776b39c9f5b0ecbc5f2941ee2103
>- docker ps
>- docker cp C:\Users\luis1\Downloads\AdventureWorks2017.bak 0662d23d58cd:/var/opt/mssql/data

### 8. Aplicar parches de SQL en un contenedor
>- docker pull mcr.microsoft.com/mssql/server:2019-CU1-ubuntu-16.04
>- docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=980Parace12tamol%&" -p 14033:1433 -v c:/Users/luis1/Downloads/sqlserver/data:/var/opt/mssql/data -v c:/Users/luis1/Downloads/sqlserver/log:/var/opt/mssql/log -v c:/Users/luis1/Downloads/sqlserver/log:/var/opt/mssql/secrets -d mcr.microsoft.com/mssql/server:2019-latest
>- actualizar data usando las mismas ubicaciones de los volumenes

### 9. Crear una imagen personalizada con Dockerfile
>- https://github.com/microsoft/mssql-docker
>- 