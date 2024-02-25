
## curso
>- https://udemy.com/course/jenkins-servidor-de-ic/learn/lecture/27273986#overview

## Sección 1: Prólogo y herramientas

### 1. Prólogo

### 2. Instrucciones curso de Udemy

### 3. Descargar Jenkins
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
>- sudo apt-get install openssh-server
>- sudo apt-get install net-tools
>- ip a
>- sudo systemctl status ssh #hace que no funcionen las redes luego de ejecutarlo y cancelarlo

### 4. Comprobar MV Java

### 5. Descargar MV Java

### 6. Instalar Java

### 7. Instalar Jenkins

### 8. Comprobar jenkins

### 9. Explorando jenkins

## Sección 2: Entendiendo DevOps

### 10. Fase 1: Repositorio de código

### 11. Fase 2: Gestor de dependencias

### 12. Fase 3: Repositorio de artefactos

### 13. Fase 4: Servidor de IC

### 14. Fase 5: Testing

### 15. Fase 6: Calidad

### 16. Fase 7: Comunicación

### 17. Fase 8: Entornos

## Sección 3: Jenkins

### 18. Primera revisión Jenkins

### 19. Reiniciar Jenkins
>- http://localhost:2530/restart
>- preguntara si estamos seguros

### 20. Problemas de traducciones

### 21. Primer Job - Console

### 22. Entendiendo CRON
>- https://crontab.guru/
>- * * * * *
>- 15 3 3 1,2 1-5
>- 15 3 * 1,2 1-5


### 23. Trigger de CRON

### 24. Variables de Jenkins
>- http://localhost:2530/env-vars.html/
>- echo Hello_World
>- echo "%GIT_AUTHOR_EMAIL% %JOB_NAME%"

### 25. Jobs parametrizados


### 26. Trigger remoto con y sin parámetros
>- http://localhost:2530/job/03-job-parameters/build?token=fer
>- http://localhost:2530/job/03-job-parameters/buildWithParameters?token=fer&pais=FRA&admin=true

### 27. Triggers entre Jobs: Parte 1

### 28. Triggers entre Jobs: Parte 2

### 29. Folders
>- permite agrupar los proyectos
>- http://localhost:2530/manage/pluginManager/installed


### 30. Views
>- agrupar proyectos a los que tiene acceso el usuario

### 31. Users
>- http://localhost:2530/securityRealm/addUser

### 32. Autorización
>- http://localhost:2530/configureSecurity

### 33. Matrix

### 34. Roles
>- http://localhost:2530/configureSecurity
>- http://localhost:2530/role-strategy/manage-roles
>- http://localhost:2530/role-strategy/list-macros

### 35. Configuración de Maven y JDK
>- http://localhost:2530/configureTools

### 36. Comprobar versión Maven

### 37. Administrar Plugins

### 38. Configuración MV Java en Jenkins
>- http://localhost:2530/systemInfo

### 39. Instalando Plugins
>- http://localhost:2530/pluginManager/available

### 40. Descargar código Git con Job


### 41. Trigger repo Git


### 42. Instalar Git


### 43. Descargar GitHub Mvn


### 44. Descargar Tomcat


### 45. Configurando Tomcat


### 46. Configuración Jenkins - Tomcat
>- plugin deploy to container


### 47. Configuración varios Jenkins Tomcat


## Sección 4: Jenkins con Pipelines y Groovy

### 48. Página oficial de jenkins
>- https://www.jenkins.io/doc/book/pipeline/
>- Pipeline: Step API
>- Pipeline: API
>- Pipeline: Job
>- Pipeline: Groovy
>- Pipeline: Nodes and Processes
>- Pipeline: Basic Steps
>- Pipeline: Stage Step
>- Pipeline: Input Step
>- Pipeline: Multibranch
>- Pipeline: Build Step
>- Pipeline: Shared Groovy Libraries
>-  Pipeline: Graph Analysis
>-  Pipeline: Model API
>-  Pipeline: REST API
>-  Pipeline: Stage View
>-  Pipeline: Declarative
>-  Pipeline


### 49. Plugins de pipeline y primer pipeline


### 50. Script de node


### 51. Script con programación Groovy


### 52. Pipeline y posts


### 53. Pipeline options


### 54. Pipeline y parameters


### 55. Pipeline y triggers


### 56. Pipeline y tools


### 57. Pipeline e inputs


### 58. Pipeline plugins


### 59. Pipeline externos


## Sección 5: Master y Slaves
































































