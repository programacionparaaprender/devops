
## curso
https://www.udemy.com/course/la-guia-de-jenkins-de-cero-a-experto/

## Sección 1: Introducción

### 1. Mapa del curso

### 2. Introducción al curso

### 3. Archivos EXTRA
>- https://github.com/macloujulian/cursojenkins

## Sección 2: La necesidad de la integración continua

### 4. Los problemas de ANTES

### 5. ¿Qué es la integración continua?
>- Es una práctica de desarrollo que requiere a los desarrolladores integrar el código en el que trabajan, actualizan y modifican a un repositorio COMPARTIDO, varias veces al día.
>- Server CI -> Construcción / Build -> Pruebas / Tests -> Resultados al Equipo

### Examen de prueba 1: Test sección

## Sección 3: Instalación y Teoria de Jenkins

### 6. ¿De qué formas podemos instalar Jenkins?
1. Instalación de jenkins de forma LOCAL com VM (VirtualBox)
2. En la Nube utilizando Docker (AWS, Digital Ocean, Google Cloud, Azure)
>- https://www.digitalocean.com/
>- https://portal.azure.com/#home
>- https://cloud.google.com/
>- https://aws.amazon.com/es/

3. Vagrant
>- https://www.vagrantup.com/

4. Instalar Docker para Windows/Mac

### 7. Sugerencia próxima clase
>- https://ubuntu.com/download/server

### 8. Instalación de VirtualBox y máquina virtual


### 9. Preparación de la máquina virtual
>- https://iterm2.com/
>- https://www.putty.org/

### 10. ALARACIÓN: ¿Cómo utilizar Putty?

### 11. (Opcional) Instalación de Cmder terminal en Windows
>- https://cmder.app/


### 12. (Opcional) Instalación de Iterm2 terminal en Mac

### 13. Etapas para lograr la Integración Continua y sus beneficios

### 14. Entrega y Despliegue Continuo

### 15. Instalación de Docker

### 16. Introducción de Jenkins

### 17. Instalación Jenkins

### 18. docker-compose.yml

### 19. Aclaración de la próxima clase (Instalación de Visual Studio Code)

### 20. (Opcional) Instalación de Visual Studio Code

### 21. (Opcional) IP dinámica a IP estática

### Cuestionario 1: Exámen de la sección

## Sección 4: ¡Empecemos con Jenkins!

### inicial
>- jenkins.io
>- https://www.jenkins.io/download/thank-you-downloading-windows-installer-stable/
>- C:\ProgramData\Jenkins\.jenkins\workspace\

### plugins
```
Maven integration
Maven integration pipeline
NodeJS Plugin
CloudBees Docker Build and Publish plugin
Role-based Authorization Strategy
Job DSL
```


### Job DSL
```
https://github.com/macloujulian/cursojenkins/blob/main/JenkinsJobDSL/Script%20a%20utilizar%20en%20la%20secci%C3%B3n
https://jenkinsci.github.io/job-dsl-plugin/#
```

### Aprobar los scripts
http://192.168.1.36:8080/scriptApproval/

### Source Control Management
```
https://github.com/macloujulian/jenkins.job.parametrizado
https://jenkinsci.github.io/job-dsl-plugin/#

```


### configuraciones de seguridad
http://192.168.1.36:8080/configureSecurity/

### equipo donde se instalo jenkins
http://localhost:2530/computer/

### Configuración
http://localhost:2530/configure


### variables de entorno
http://localhost:2530/env-vars.html/


### instalación y actualización de plugins
http://localhost:2530/updateCenter/

### enlaces
´´´
https://github.com/macloujulian/cursojenkins
https://putty.org/
https://www.virtualbox.org/
https://www.osboxes.org/ubuntu/#ubuntu20-04-vbox
https://lubuntu.me/downloads/
´´´

## comandos a ejecutar
´´´
sudo apt-get install openssh-server
sudo apt-get install net-tools
ip a
sudo systemctl status ssh #hace que no funcionen las redes luego de ejecutarlo y cancelarlo
´´´


