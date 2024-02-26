
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
>- https://www.jenkins.io/doc/book/pipeline/syntax/


### 50. Script de node


### 51. Script con programación Groovy


### 52. Pipeline y posts
>- https://www.jenkins.io/doc/book/pipeline/syntax/
>- Ejemplo 3
```
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
            post { 
                always { 
                    echo '¡dentro del stage!'
                }
                failure { 
                    echo '¡Esto se ejecuta si ha fallado stage!'
                }
                success { 
                    echo '¡Caso de exito stage!'
                }
            }
        }
    }
    post { 
        always { 
            echo '¡Esto se ejecuta siempre!'
        }
        failure { 
            echo '¡Esto se ejecuta si ha fallado!'
        }
        success { 
            echo '¡Caso de exito!'
        }
    }
}
```

### 53. Pipeline options
```
pipeline {
    agent any 
    options{
        timeout(time:1, unit:"HOURS")
    }
    stages {
        stage('Ejemplo primero') {
            steps {
                echo 'Hola Caracola'
            }
        }
    }
}
```

### 54. Pipeline y parameters
>- https://www.jenkins.io/doc/book/pipeline/syntax/
>- Example 10. Parameters, Declarative Pipeline
```
pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"

                echo "Biography: ${params.BIOGRAPHY}"

                echo "Toggle: ${params.TOGGLE}"

                echo "Choice: ${params.CHOICE}"

                echo "Password: ${params.PASSWORD}"
            }
        }
    }
}
```

### 55. Pipeline y triggers
>- https://www.jenkins.io/doc/book/pipeline/syntax/
>- Example 11. Triggers, Declarative Pipeline
```
// Declarative //
pipeline {
    agent any
    triggers {
        cron('H */4 * * 1-5')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

### 56. Pipeline y tools
>- https://www.jenkins.io/doc/book/pipeline/syntax/
>- Example 13. Tools, Declarative Pipeline
```
pipeline {
    agent any
    tools {
        maven 'Maven3' 
        jdk: 'Jdk8'
    }
    stages {
        stage('Example') {
            steps {
                bat 'mvn --version'
                bat 'java -version'
            }
        }
    }
}
```

### 57. Pipeline e inputs
>- https://www.jenkins.io/doc/book/pipeline/syntax/
>- Example 14. Input Step, Declarative Pipeline

```
pipeline {
    agent any
    stages {
        stage('Example') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                }
            }
            steps {
                echo "Hello, ${PERSON}, nice to meet you."
            }
        }
    }
}
```

### 58. Pipeline plugins
>- https://www.jenkins.io/doc/book/pipeline/syntax/#agent
```
pipeline {
    agent any
    // options {
        // Timeout counter starts AFTER agent is allocated
       //  timeout(time: 1, unit: 'SECONDS')
    // }
    stages {
        stage('Descargar código del git') {
            steps {
                echo 'Hello World'
                git 'https://github.com/programacionparaaprender/primefaces.git'
            }
        }
        stage('Paquetizar con maven') {
            steps {
                echo 'Hola Caracola'
                bat 'mvn clean package'
            }
        }
    }
}
```

### 59. Pipeline externos
>- https://www.jenkins.io/doc/book/pipeline/syntax/#agent
```
pipeline {
    agent any
    stages {
        stage('Descarga de git') {
            steps {
                git 'https://github.com/programacionparaaprender/Pipeline_Script.git'
            }
        }
        stage('DEPLOY') {
            steps {
                bat 'Deploy.bat'
            }
        }
        stage('UNIT') {
            steps {
                bat 'unit.bat'
            }
        }
    }
}
```

## Sección 5: Master y Slaves

### 60. Explicación Master-Slave


### 61. Agente Mock
>- http://localhost:2530/manage/pluginManager/available
>- Mock Agent
>- http://localhost:2530/manage/
>- http://localhost:2530/computer/

### 62. Monitoring
>- http://localhost:2530/manage/pluginManager/available
>- Monitoring
>- http://localhost:2530/monitoring

### 63. JenkinsFile y Agents

### 64. Jenkins agent con Java JNLP

## Sección 6: Finalizando

### 65. Finalizando




































































