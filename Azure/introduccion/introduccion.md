
## Curso
>- https://udemy.com/course/introduccion-a-azure/learn/lecture/25483244#overview

## Sección 1: 1. Introducción a Cloud Computing

### 1. 1.1 ¿Que es Cloud Computing?
>- "... es la entrega de servicios informáticos, incluidos servidores, almacenamiento, bases de datos, redes, software, análisis e inteligencia, a través de Internet ("la nube")... Por lo general, solo se paga por los servicios en la nube que se usa, lo que lo ayuda a reducir costos operativos, ejecutar infraestructura de manera más eficiente, y escalar a medida que cambian las necesidades del negocio".

### 2. 1.2 Beneficios de la nube

#### Alta disponibilidad
1. Capacidad para minimizar interrupciones en los servicios de la nube. Esta característica se logra gracias a tres elementos básicos.
>- Redundancia: garantiza que cualquier elemento crítico tenga un componente redundante (copias).
>- Monitoreo: Permite recopilar datos de un sistema en ejecución y detectar cuando un componente falla.
#### Tolerancia a fallos (fault tolerance)
>- Hace referencia a la capacidad de un sistema para seguir funcionando sin interrupciones cuando uno o más de sus componentes fallen, asegurando continuidad en el servicio.
>- La diferencia entre la tolerancia y la alta disponibilidad radica en que este último proporciona una forma para que el sistema se recupere velozmente frente a una falla.
#### Escalabilidad (scalability)
>- Se refiere a la capacidad de aumentar los recursos de la nube según sea necesario para satisfacer una demanda en aumento.
>- Puede ser vertical, lo cual se refiere a la capacidad de aumentar la potencia del hardware o software existente añadiendo recursos.
>- Puede ser horizontal, lo cual se refiere a aumentar la capacidad conectando múltiples entidades de hardware o softawre para que funcionen como una sola unidad.

#### Elasticidad (elasticity)
>- Se refiere a la asignación dinámica y eficiente de los recursos de la nube a proyectos, flujos de trabajo y procesos, permitiendo optimizar el uso de los recursos frente a una mayor o menor demanda.


### 3. 1.3 Modelos de servicios en la nube
1. IaaS: Infraestructura como servicio
>- Infraestructura de computación instantanea, proporcionada y administradad a través de Internet
>- Microsoft Azure, Amazon Web Service, Google Compute Engine

2. PaaS: Plataforma como servicio
>- Porporciona herramientas de hardware y software a través de Internet que los usuarios usan para desarrollar aplicaciones.
>- aws elastic beanstalk, windows azure, google app engine

3. SaaS: Software como servicio
>- Software o cualquier servicio disponible a través de un tercero y basado en la web
>- Google Apps, Dropbox, Microsoft Office 365


### 4. 1.4 Modelos de implementación en la nube
1. Nube privada (Private cloud)
>- Servicios que se ofrecen a través de internet o una red interna privada y solo para usuarios seleccionados. Brindan mayor seguridad para garantizar que las operaciones y datos no sean accesibles

2. Nube pública (Public cloud)
>- Servicios que se ofrecen por proveedores externos a través de Internet de forma pública, poniéndolos a disposición de cualquiera que desee adquirirlos

3. Nube híbrida (Hybrid cloud)
>- Combina una nube pública y una nube privada. Permite que los datos y aplicaciones se compartan entre ambas.


### 5. 1.5 Cloud providers
>- AWS
>- Azure
>- Google Cloud
>- Alibaba Cloud
>- Otros


## Sección 2: 2. Microsoft Azure

### 6. 2.1 ¿Por qué Microsoft Azure?
>- Permite la integración con otros productos de Microsoft.
>- Permite ahorrar mediante otras licencias de Microsoft.
>- Más del 95% de las empresas incluidas en la lista Fortune 500 usan Azure.
>- Permite la implementación de un entorno híbrido de forma sencilla
>- Más regiones globales que cualquier otro proveedor de servicios en la nube.
>- Más de 400 servicios.
>- Azure es 5 veces más barato que AWS cuando se utiliza en conjunto con otros productos de Windows


### 7. 2.2 Arquitectura Azure
>- https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview
>- https://learn.microsoft.com/es-es/azure/azure-resource-manager/management/overview
1. Azure Resource Manager
>- Azure portal
>- Azure powershell
>- Azure cli
>- rest clients

### 8 2.3 Azure Portal y servicios principales (overview)
>- Azure Portal es una consola unificada que proporciona una herramienta en forma de interfaz. Permite ver, administrar y supervisar todas las aplicaciones de Azure en un único espacio, ya sean aplicaciones web, bases de datos, máquinas virtuales, redes virtuales, almacenamiento, etc.


## Sección 3: 3. Azure Portal

### 9. Creación de Cuenta Gratuita y plataforma web (Actualizado)
>- https://portal.azure.com/#home
>- https://learn.microsoft.com/es-mx/azure/cost-management-billing/manage/create-subscription
>- https://learn.microsoft.com/es-mx/azure/cost-management-billing/manage/cancel-azure-subscription
>- https://learn.microsoft.com/es-mx/azure/cost-management-billing/manage/mca-request-billing-ownership

### 10. 3.1 Cuenta gratuita y plataforma web - (Opcional)


## Sección 4: 4. Azure Virtual Machine y Networking

### 11. 4.1 Máquinas virtuales

#### Definición Maquinas virtuales
>- "... es un archivo de computadora que se comporta como una computadora real (imagen)... Cada máquina virtual proporciona su propio hardware virtual... El hardware virtual se asigna al hardware real en la máquina física, lo que ahorra costos al reducir la necesidad de sistemas de hardware físico junto con los costos de mantenimiento asociados, además de reducir la demanda de energía y refrigeración"

#### Azure Networking
>- Los servicios de red en Azure proporcionan una variedad de capacidades de red que se pueden usar juntas o por separado.
>- Virtual networks
>- Public IP addresses
>- Network security groups
>- Network interfaces

### 12. 4.2 Minioroyecto: Crear un Virtual Machine e implementar puertos

## Sección 5: 5. Azure Storage

### 13. 5.1 Almacenamiento
>- Es un servicio que proporciona almacenamiento de alta disponibilidad, seguro, escalable y redundante. Brinda opciones de almacenamiento en línea con la necesidad de los clientes.
>- Containers 
>- Queues
>- File Shares
>- Tables

### 14. 5.2 Miniproyecto: Azure Storage Accounts
>- crear contenedor y agregar archivos

## Sección 6: 6. Security and Identity

### 15. 6.1 Seguridad e Identidad

### 16. 6.2 Miniproyecto, Parte 1: Añadir usuarios y asignar roles

### 17. 6.2.1 Miniproyecto, Parte 1: Añadir usuarios y asignar roles (Actualización)

### 18. 6.3 Miniproyecto, Parte 2: Asignar roles según recurso

## Sección 7: 7. Mobile

### 19. 7.1 Mobile
>- Servicios que permiten desarrollar aplicaciones web escalables de forma rápida y eficiente, así como aplicaciones nativas y multiplataforma para cualquier dispositivo móvil.
>- App Services
>- API Connections 
>- Media Services
>- App Service Domain

## Sección 8: 8.1 Monitoring and Management

## 20. 8.1 Monitoreo

### 21. 8.2 Miniproyecto: Cómo dar seguimiento a mis gastos en Azure (billing)

## Sección 9: 9. Azure Databases

### 22. 9.1 Bases de datos
>- Azure ofrece una selección de bases de datos que presentan las características de escalabilidad, disponibilidad y seguridad
>- Azure SQL
>- MySQL
>- PostgreSQL
>- MariaDB

### 23. 9.2 Miniproyecto 1: Crear una base de datos Azure


### 24. 9.3 Miniproyecto 2, Parte 1: Azure Cosmos DB

#### Azure Cosmos DB
>- Servicio de base de datos MoSQL para el desarrollo de aplicaciones. Tiempo de respuesta muy rápido, alta disponibilidad, escalabilidad automática e instantanea y API de código abierto para MongoDB y Cassandra

### 25. 9.4 Miniproyecto 2, Parte 2: Cosmos DB en Azure


### 26. 9.5 Miniproyecto 2, Paete 3: Cosmos DB en Python


## Sección 10: 10. Azure Analytics


### 27. 10.1 Analytics

### 28. 10.2 Miniproyecto 1: Crear un proyecto de Azure en Databricks

### 29. 10.3 Miniproyecto 2, Parte 1: Azure Data Factories

### 30. 10.4 Miniproyecto 2, Parte 2: Data Factories en Azure Portal

### 31 10.5 Miniproyecto 2, Parte 3: Data Factories & Databricks

## Sección 11: 11. Certificaciones


