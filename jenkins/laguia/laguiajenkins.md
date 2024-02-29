
## curso
https://www.udemy.com/course/la-guia-de-jenkins-de-cero-a-experto/

## Sección 1: Introducción

### 1. Mapa del curso

### 2. Introducción al curso
>- jenkins.io
>- https://www.jenkins.io/download/thank-you-downloading-windows-installer-stable/
>- C:\ProgramData\Jenkins\.jenkins\workspace\
>- http://localhost:2530/scriptApproval/
>- http://localhost:2530/configureSecurity/
>- http://localhost:2530/computer/
>- http://localhost:2530/configure
>- http://localhost:2530/env-vars.html/
>- http://localhost:2530/updateCenter/
>- http://localhost:2530/manage/pluginManager/installed
>- http://localhost:2530/securityRealm/addUser
>- http://localhost:2530/view/all/builds

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

#### Beneficios de la integración continua
1. Reducción de tiempo en volver atrás para descubrir los errores.
2. Como ahorramos tiempo en corregir errores, tenemos más tiempo para añadir características nuevas.
3. Reducción de problemas de integración permitiendo entregar software más rápidamente.

#### ETAPAS
1. Automatizar el proceso de build o compilación
2. Optimizar el build para que se auto testee
3. Mantener un solo source repository
4. No complicar las cosas para el resto
5. La visibilidad de qué está sucediendo
6. Despliegue Automático

#### ¿Cómo lo logramos?
1. Los desarrolladores deben  trabajar en su propio espacio de trabajo
2. Cuando finalizan o realizan algún cambio significativo deben confirmar los cambios en el repositorio
3. Deben configurar el server CI que se va a encargar de controlar el repositorio y chequear los cambios cuando estos ocurran
4. Configurar el server CI para compile o realice el "build" del Proyecto y que ejecute las pruebas unitarias, llamadas en inglés unit and integration tests
5. El server CI se encarga de desplegar los artefactos para la prueba, en inglés conocido como deployable artefacts
6. El server CI asigna un build label, o número de compilación a la versión de código ejecutable que se acaba de realizar

#### ¡Jenkins es el encargado de fabricar el CI server para llevar a cabo todas estas tareas!

#### La integración continua también tiene responsabilidad de EQUIPO

#### Responsabilidades de equipo
1. Check in frecuentemente
2. No realizar un check in con código erróneo (broken code)
3. No realizar un check in en código que no fue testeado
4. No realizar un check in cuando el build no funciona

### 14. Entrega y Despliegue Continuo
>- La entrega continua de código a un entorno específico una vez que el código está listo y preparado para ser entregado
>- CI / CD (Continuous integration / Continuous Deployment)


### 15. Instalación de Docker
>- https://hub.docker.com/
>- https://docs.docker.com/engine/install/ubuntu/

### 16. Introducción de Jenkins
>- https://code.visualstudio.com/
>- Es una herramienta CI/CD de fuente abierta escrita en Java
>-  Es una herramiena de automatización utilizada para construir (Build) y entregar (Deliver) software
>- Fue bifurcado (Forked) de otro proyecto llamado Hudson
>- Es una aplicación basada en servidor y requiere un servidor web como Apache Tomcat
>- ¿Por qué utilizar Jenkins para la integración continua?
#### alternativas a jenkins
>- Drone CI
>- Circle CI
>- Teamcity
>- CodeShip
>- Wercker


### 17. Instalación Jenkins


### 18. docker-compose.yml


### 19. Aclaración de la próxima clase (Instalación de Visual Studio Code)


### 20. (Opcional) Instalación de Visual Studio Code


### 21. (Opcional) IP dinámica a IP estática


### Cuestionario 1: Exámen de la sección


## Sección 4: ¡Empecemos con Jenkins!

### 22. Arquitectura de Jenkins
>- https://github.com/macloujulian/cursojenkins/blob/main/%C2%A1EmpecemosconJenkins!/Job%20v2.0%20script
>- Tareas ejecutables que son supervisadas y controladas por Jenkins

#### Tareas del Maestro
1. Es el encargado de programar el Build
2. Envía la compilación al esclavo para que se haga efectiva la ejecución del job
3. Supervisar el trabajo del esclavo y registrar los resultados del Build
4. Ejecutar los Build jobs que el maestro le ha enviado

#### Jenkins Slave
>- Los esclavos son máquinas programadas para construir los proyectos que el maestro le requiere.

### Jenkins Executor
>- Un ejecutor es una secuencia separada de compilaciones que se ejecutarán en un nodo en paralelo

### Un plugin de Jenkins es una parte de software adicional a la funcionalidad básica del Jenkins Server

### 23. Conociendo Jenkins
>- http://localhost:2530/view/all/builds

### 24. Primer Job de Jenkins
>- disparadores de ejecuciones
>- Github hook trigger for GitScm polling


### 25. ¡Tu reseña es MUY importante para mi!

### 26. Primer Job de Jenkins (Parte 1)

### 27. ¡Agregando variables a nuestro Job!

### 28. Job v2.0
>- http://localhost:2530/view/all/builds


### 29. Job v2.0: Script desde el contenedor

### Cuestionario 2: Exámen de la sección

## Sección 5: Parametrizando Jenkins Jobs

### 30. Agregando parámetros

### 31. Parámetro de elección

### 32. Parámetro de booleano
>- https://github.com/macloujulian/cursojenkins/blob/main/ParametrizandoJenkinsJobs/Par%C3%A1metro%20booleano%20script

### Cuestionario 3: Exámen de la sección

## Sección 6: Integración Email y Slack

### 33. ¿Para qué las necesitamos?

### 34. Instalación del Email Plugin

### 35. Email con Gmail

### 36. Email con Mailtrap

### 37. Integración de Slack

### Cuestionario 4: Exámen de la sección

## Sección 7: Java Maven App

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


