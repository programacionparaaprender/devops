## cursos
>- https://udemy.com/course/cicd-para-testers-jenkins-github-actions-a-fondo/learn/lecture/29279010#learning-tools

## Sección 1: Introducción

### 1. Introducción 

### 2. ¿ Qué es CI por qué se usa ?
>- jenkins.io
>- https://www.jenkins.io/download/thank-you-downloading-windows-installer-stable/
>- C:\ProgramData\Jenkins\.jenkins\workspace\
1. Continuous Integration (CI) build -> test -> merge
2. Continuous Delivery (CD) Liberación automatica al repositorio
3. Continuous Deployment (CD) Despliegue automatico hacia producción

### 3. ¿Cómo se intregra Testinf en este concepto?
>- Pruebas para que no continue con el pipeline

### 4. ¿Sirve saber CI a la hora de buscar trabajo como Tester ?
>- 

### 5. ¿ Cuáles son las herramientas y lenguajes más usados ?
>- Github actions
>- https://docs.github.com/es/actions

## Sección 2: Jenkins: Instalación y configuración inicial.

### 6. Jenkins: ¿ Qué es ?
>- Es una aplicación para correr casos de prueba, pipeline, triggers.

### 7. Instalación
>- jenkins.io
>- download lts windows

### 8. Opcional: Instalar jenkins con un volumen persistente en Docker
>- docker image pull jenkins/jenkins:lts
>- docker volume create mijenkins
>- docker container run -d -p 2530 -v mijenkins --name jenkins-local jenkins/jenkins:lts
>- b3acef7b9d98583f941427f1ea9f354e5a294d211304a32555f624ef24e3d668
>- docker-compose build
>- docker-compose up
>- docker-compose down

#### https://github.com/jvalentino/example-docker-jenkins/blob/main/docker-compose.yaml
>- https://www.youtube.com/watch?v=i1ySYuQ2ASg
>- docker-compose up -d
>- debe realizarse en una carpeta donde se pueda crear el jenkins_home

### 9. ¿Qué componentes tiene jenkins?
>- jobs
>- vistas

### 10. Agentes, nodos y ejecutores.
1. Agentes
<p>dentro de los nodos y correr las tareas en los ejecutores</p>

2. Nodos
<p>Maquina virtual donde va a estar corriendo jenkins</p>

3. Ejecutores
<p>Donde se ejecuta la VI</p>

### 11. Configuración.
>- configurar el jdk
>- https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz