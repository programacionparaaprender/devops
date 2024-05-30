
# cursos
>- https://www.udemy.com/course/aws-cognito-avanzado-autenticacion-con-amazon-web-services/learn/lecture/43561016#overview

## Sección 1: Introducción

### 1. Introducción y vista general del curso


### 2. Repositorio GitHub del curso
>- https://github.com/cordev-developer/aws-cognito


### 3. Sobre la valoración del curso

### 4. Actualización - Sobre la documentación de AWS
>- https://docs.amplify.aws/react/

## Sección 2: Servicios de autenticación y autorización


### 5. Introducción

### 6. Autenticación vs Autorización

### 7. Servicios de autenticación: Definición y Métodos
>- Mecanismo que identifica a un usuario o un servicio
>- Consta básicamente de dos procesos, el proceso de identificación y el proceso propiamente dicho de autenticación que verifica la identidad del usuario.
>- El ejemplo típico más común es la autenticación mediante usuario/contraseña.
>- Para añadir más seguridad en los sistemas usuario/contraseña se pueden añadir autenticación multifactor (MFA), proceso mediante el cual se realiza una verificación de dos pasos. Por ejemplo sería primero mediante usuario/contraseña y posteriormente se añade una autenticación mediante SMS al teléfono móvil del usuario. Se puede hacer también la verificación mediante correo electrónico.

### 8. Servicios de autorización: Definición y Métodos
>- La autorización es lo que define a qué recursos del sistem el usuario autorizado podrá acceder.
>- Normalmente definiremos a qué recursos específicos queremos conceder acceso a los usuarios.
>- Por ejemplo a un usuario le podríamos conceder permisos sólo para acceder a S3 (por ejemplo subir objetos), también para acceder a una instancia de EC2, o para acceder a nuestra API. En general, habrá diferentes tipos de usuarios con diferentes tipos de permisos que determinarán a qué recursos del sistema pueden acceder.

#### servicios de autorización

>- Autorización HTTP (usuario/contraseña codificados se envían en el encabezado de una petición HTTP)
>- Autorización API (se genera una clave API que actúa como un token).
>- OAuth 2.0 (framework, estándar abierto de autorización). Basado en diferentes flujos de autorización (para aplicaciones de escritorio/móviles).

## Sección 3: Criptografía y encriptación

### 9. Introducción

### 10. Criptografía simétrica

### 11. Criptografía asimétrica
>- Trabaja con una codificación de información basada en dos claves: una privada y na pública.
>- Proporciona confidencialidad, integridad y autenticidad (mediante los certificados y firmas digitales).
>- Clave Pública: la clave pública puede encriptar mensajes que sólo se descifran con la clave privada.
>- Clave Privada: usada para descifrar la información que ha sido cifrada con la clave pública. También se usa en sistemas de autenticación, ya que se usa la clave privada para firmar y la pública para validar la firma del autor del mensaje.

### 12. Criptografía simétrica vs asimétrica

### 13. Actualización. Protocolos de comunicación segura


