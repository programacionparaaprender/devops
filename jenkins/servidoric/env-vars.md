>- BRANCH_NAME
Para un proyecto de varias ramas, esto se establecerá con el nombre de la rama que se está creando, por ejemplo, en caso de que desee implementar en producción desde la rama maestra pero no desde las ramas características; si corresponde a algún tipo de solicitud de cambio, el nombre es generalmente arbitrario (consulte CHANGE_ID y CHANGE_TARGET).
>- BRANCH_IS_PRIMARY
Para un proyecto de varias sucursales, si la fuente SCM informa que la sucursal que se está creando es una sucursal principal, esto se establecerá en "verdadero"; más desarmado. Algunas fuentes de SCM pueden informar más de una sucursal como sucursal principal, mientras que otras pueden no proporcionar esta información.
>- CHANGE_ID
Para un proyecto de varias sucursales correspondiente a algún tipo de solicitud de cambio, esto se establecerá en el ID de cambio, como un número de solicitud de extracción, si es compatible; más desarmado.
>- CHANGE_URL
Para un proyecto de varias sucursales correspondiente a algún tipo de solicitud de cambio, esto se establecerá en la URL de cambio, si es compatible; más desarmado.
>- CHANGE_TITLE
Para un proyecto multirama correspondiente a algún tipo de solicitud de cambio, esto se establecerá en el título del cambio, si es compatible; más desarmado.
>- CHANGE_AUTHOR
Para un proyecto multirama correspondiente a algún tipo de solicitud de cambio, este se establecerá con el nombre de usuario del autor del cambio propuesto, si es compatible; más desarmado.
>- CHANGE_AUTHOR_DISPLAY_NAME
Para un proyecto multirama correspondiente a algún tipo de solicitud de cambio, se establecerá en el nombre humano del autor, si se admite; más desarmado.
>- CHANGE_AUTHOR_EMAIL
Para un proyecto multirama correspondiente a algún tipo de solicitud de cambio, esta se establecerá en la dirección de correo electrónico del autor, si es compatible; más desarmado.
>- CHANGE_TARGET
Para un proyecto de múltiples ramas correspondiente a algún tipo de solicitud de cambio, esto se establecerá en la rama base o de destino a la que se podría fusionar el cambio, si es compatible; más desarmado.
>- CHANGE_BRANCH
Para un proyecto de varias ramas correspondiente a algún tipo de solicitud de cambio, esto se establecerá con el nombre del encabezado real en el sistema de control de fuente, que puede ser diferente o no de BRANCH_NAME. Por ejemplo, en GitHub o Bitbucket esto tendría el nombre de la rama de origen, mientras que BRANCH_NAME sería algo así como PR-24.
>- CHANGE_FORK
Para un proyecto de varias ramas correspondiente a algún tipo de solicitud de cambio, se establecerá en el nombre del repositorio bifurcado si el cambio se origina en uno; más desarmado.
>- TAG_NAME
Para un proyecto de varias ramas correspondiente a algún tipo de etiqueta, se establecerá con el nombre de la etiqueta que se está creando, si es compatible; más desarmado.
>- TAG_TIMESTAMP
Para un proyecto de varias ramas correspondiente a algún tipo de etiqueta, esto se establecerá en una marca de tiempo de la etiqueta en milisegundos desde la época de Unix, si es compatible; más desarmado.
>- TAG_UNIXTIME
Para un proyecto de varias ramas correspondiente a algún tipo de etiqueta, esto se establecerá en una marca de tiempo de la etiqueta en segundos desde la época de Unix, si es compatible; más desarmado.
>- TAG_TIMESTAMP
Para un proyecto de varias ramas correspondiente a algún tipo de etiqueta, esto se establecerá en una marca de tiempo en el formato definido por java.util.Date#toString() (por ejemplo, miércoles 1 de enero a las 00:00:00 UTC de 2020), si es compatible. ; más desarmado.
>- JOB_DISPLAY_URL
URL que redirigirá a un trabajo en una interfaz de usuario preferida
>- RUN_DISPLAY_URL
URL que redirigirá a una compilación en una interfaz de usuario preferida
>- RUN_ARTIFACTS_DISPLAY_URL
URL que redirigirá a artefactos de una compilación en una interfaz de usuario preferida
>- RUN_CHANGES_DISPLAY_URL
URL que redirigirá al registro de cambios de una compilación en una interfaz de usuario preferida
>- RUN_TESTS_DISPLAY_URL
URL que redirigirá a los resultados de la prueba de una compilación en una interfaz de usuario preferida
>- CI
Establecido estáticamente en la cadena "true" para indicar un entorno de ejecución de "integración continua".
>- BUILD_NUMBER
El número de compilación actual, como "153".
>- BUILD_ID
El ID de compilación actual, idéntico a BUILD_NUMBER para compilaciones creadas en 1.597+, pero una marca de tiempo AAAA-MM-DD_hh-mm-ss para compilaciones más antiguas.
>- BUILD_DISPLAY_NAME
El nombre para mostrar de la compilación actual, que es algo así como "#153" de forma predeterminada.
>- JOB_NAME
Nombre del proyecto de esta compilación, como "foo" o "foo/bar".
>- JOB_BASE_NAME
Nombre corto del proyecto de esta compilación eliminando las rutas de las carpetas, como "foo" para "bar/foo".
>- BUILD_TAG
Cadena de "jenkins-${JOB_NAME}-${BUILD_NUMBER}". Todas las barras diagonales ("/") en JOB_NAME se reemplazan por guiones ("-"). Conveniente para colocar en un archivo de recursos, un archivo jar, etc. para una identificación más sencilla.
>- EXECUTOR_NUMBER
El número único que identifica al ejecutor actual (entre los ejecutores de la misma máquina) que está llevando a cabo esta compilación. Este es el número que ve en el "estado del ejecutor de compilación", excepto que el número comienza en 0, no en 1.
>- NODE_NAME
Nombre del agente si la compilación es en un agente, o "integrado" si se ejecuta en el nodo integrado (o "maestro" hasta Jenkins 2.306).
>- NODE_LABELS
Lista de etiquetas separadas por espacios en blanco que se asigna al nodo.

>- WORKSPACE
La ruta absoluta del directorio asignado a la compilación como espacio de trabajo.

>- WORKSPACE_TMP
Un directorio temporal cerca del espacio de trabajo que no será navegable y no interferirá con los pagos de SCM. Puede que inicialmente no exista, así que asegúrese de crearlo.


>- JENKINS_HOME
La ruta absoluta del directorio asignado en el sistema de archivos del controlador para que Jenkins almacene datos.
>- JENKINS_URL
URL completa de Jenkins, como http://server:port/jenkins/ (nota: solo está disponible si la URL de Jenkins está configurada en la configuración del sistema).

>- BUILD_URL
URL completa de esta compilación, como http://server:port/jenkins/job/foo/15/ (se debe configurar la URL de Jenkins).

>- JOB_URL
URL completa de este trabajo, como http://server:port/jenkins/job/foo/ (se debe configurar la URL de Jenkins).

>- GIT_COMMIT
El hash de confirmación que se está comprobando.

>- GIT_PREVIOUS_COMMIT
El hash de la última confirmación creada en esta rama, si la hay.

>- GIT_PREVIOUS_SUCCESSFUL_COMMIT
El hash de la última confirmación creada con éxito en esta rama, si la hay.

>- GIT_BRANCH
El nombre de la sucursal remota, si corresponde.

>- GIT_LOCAL_BRANCH
El nombre de la sucursal local que se está retirando, si corresponde.

>- GIT_CHECKOUT_DIR
El directorio en el que se extraerá el repositorio. Contiene el valor establecido en Checkout en un subdirectorio, si se utiliza.

>- GIT_URL
La URL remota. Si hay varios, serán GIT_URL_1, GIT_URL_2, etc.

>- GIT_COMMITTER_NAME
El nombre del confirmador de Git configurado, si lo hay, que se utilizará para FUTUROS compromisos desde el espacio de trabajo actual. Se lee desde el campo Valor de nombre de usuario de configuración global de la página Configurar sistema de Jenkins.

>- GIT_AUTHOR_NAME
El nombre del autor de Git configurado, si lo hay, que se utilizará para FUTURAS confirmaciones desde el espacio de trabajo actual. Se lee desde el campo Valor de nombre de usuario de configuración global de la página Configurar sistema de Jenkins.

>- GIT_COMMITTER_EMAIL
El correo electrónico del confirmador de Git configurado, si lo hay, que se utilizará para FUTUROS compromisos desde el espacio de trabajo actual. Se lee desde el campo Valor de usuario.correo electrónico de configuración global de la página Configurar sistema de Jenkins.

>- GIT_AUTHOR_EMAIL
El correo electrónico del autor de Git configurado, si lo hay, que se utilizará para FUTURAS confirmaciones desde el espacio de trabajo actual. Se lee desde el campo Valor de usuario.correo electrónico de configuración global de la página Configurar sistema de Jenkins.