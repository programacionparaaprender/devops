
# Sección 1: Introducción

### 1. Introducción

### 2. Costos y beneficios

### 3. Valoración previa del curso

### 4. Infraestructura como código y AWS CloudFormation

#### Infraestructura como código
>- Es el proceso de manejar y provisionar recursos de un data center a través de la definición de archivos.
>- Existen dos métodos:
>-- Pull
>-- Push
>- Tipos de enfoques:
>-- Declarativo (funcional).
>-- Imperativo (procedimental).
>- Tipo de herramienta:
>-- Manejo de configuración
>-- Aprovisionamiento
>- Infraestructuras:
>-- Mutable
>-- Inmutable
#### ¿Que es CloudFormation?
>- Es un servicio que te permite provisionar recursos a través de plantillas JSON y YAML.
>- No necesitas crear los recursos de manera individual.
>- CF permite crear, actualizar y eliminar todos los recursos en conjunto o de manera individual.

### 5. Recursos del curso
>- https://github.com/MaxCloud101/course-cloudformation

### 6. Laboratorio introductorio

### 7. Conceptos básicos
>- Stacks:
>-- Es el manejo de los recursos definidos por el template como una unidad.
>-- Un stack es creado a partir de un template.
>-- Puedes crear, actualizar y eliminar los recursos del stack o el stack completo.
>- Change sets:
>-- Es un resumen de los cambios propuestos que vamos a realizar a un stack
>-- Permite visualizar los cambios que vamos a realizar y el impacto sobre nuestros recursos


### 8. Json vs Yaml
>- JSON y YAML son lenguajes que puedes usar para crear tu template en CloudFormation.
>- YAML posee mucha mejor legibilidad
>- JSON to YAML
>-- https://www.json2yaml.com/
>- YAML valitador
>-- https://www.yamllint.com/

## Sección 2: Creación, actualización y borrado de un Stack

### 9. Creación de un recurso
>- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.html


### 10. Actualización de un recurso
>- Actualización sin interrupción
>- Actualización con alguna interrupción
>- Reemplazo
>-- Genera un nuevo id físico

### 11. Eliminación de un recurso

## Sección 3: Parámetros

### 12. ¿Que son los parámetros?
>- Los parámetros permiten introducir valores personalizados a un template cada vez que se crea o actualiza un stack.
>- Puedes definir hasta 60 parámetros en un template.
>- Cada parámetro tiene un logical name (tambipen llamado logical ID)
>- Los parámetros son asignados en tiempo de ejecución por CloudFormation
>- Los parámetros son declarados y referenciados dentro de un template
>- Usaremos la función intrínseca Fn::Ref para enlazar el valor a un recurso

### 13. Laboratorio: Parámetros

## Sección 4: Recursos

### 14. Recursos

### 15. Recursos: Laboratorio

## Sección 5: Mappings

### 16. Mappings

### 17. Mappings: Laboratorio

## Sección 6: OutPuts

### 18. OutPuts

### 19. OutPuts: Laboratorio

## Sección 7: Conditions

### 20. Conditions

### 21. Conditions: Laboratorio

## Sección 8: Metadata

### 22. Metadata

## Sección 9: User Data y CloudFormation init

### 23. User Data

### 24. User Data: Laboratorio

### 25. User Data en CloudFormation

### 26. User Data en CloudFormation: Laboratorio

### 27. CloudFormation Helper Scripts

### 28. CloudFormation init: Laboratorio

















