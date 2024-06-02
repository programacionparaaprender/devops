
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

## Sección 4: JWT: JSON Web Tokens

### 14. Introducción

### 15. ¿Qué son los JWT?
>- https://www.iana.org/assignments/jwt/jwt.xhtml
>- https://datatracker.ietf.org/doc/html/rfc7519
>- jwt.io
>- Estándar abierto RFC 7519 basado en JSON para crear tokens.
>- Permite enviar información entre dos partes de forma segura. Su objetivo principal es proporcionar autecticación y/o también autorización.
>- Se suele firmar usando un algoritmo de codificación simétrica o asimétrica, por ejemplo el HS256 (cifrado simétrico) o el RS256 (cifrado asimétrico). De esta manera la información queda firmada por medio de la clave de cifrado.
>- Los tokens firmados permiten verificar la integridad de la información que contienen.
>- La firma también certifica que sólo la parte que posee la clave privada es la que la firmo (caso de criptografía asimétrica).

### 16. Estructura y tipos de JWT
>- https://jwt.io/
>- ID token: este tipo de token usado para autenticar al usuario en un sistema, como por ejemplo AWS Cognito. Es un token de autenticación.
>- Access token: contiene toda la información que el servidor necesita para saber si el usuario o dispositivo puede acceder al recurso. Es un token de autorización.
>- Refresh token: se utiliza para generar nuevos tokens de acceso y autorización. Se usa en casos en los que los tokens expiren su tiempo de utilización.

### 17. JWK (JSON Web Key) y JWKS (JSON Web Key Sets)

## Sección 5: OAuth 2.0

### 18. Introducción

### 19. Definición y flujos autorización OAuth 2.0
>- https://datatracker.ietf.org/doc/html/rfc6749

### 20. Flujo Authorization Code Grant
>- 
>- https://app.diagrams.net/

### 21. Flujo Implicit Grant

### 22. Flujo Client Credentials Grant

### 23. Flujo Authorization Code Grant con PKCE
>- https://app.diagrams.net/
>- https://datatracker.ietf.org/doc/html/rfc7636

## Sección 6: OpenID Connect

### 24. Introducción

### 25. Qué es OpenID Connect
>- https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims
>- https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims

### 26. Cognito ID token

### 27. Cognito: Access token

### 28. Cognito: Refresh token y revocación de tokens

### 29. JWK y JWKS propios de AWS Cognito

## Sección 7: Cognito User Pools o Grupos de Usuarios

### 30. Introducción

### 31. Cognito: Características

### 32. User Pools o grupos de usuarios

### 33. Flujos de autenticación

### 34. Protocolo SRP
>- https://www.incibe.es/incibe-cert/blog/autenticacion-passwords-srp


### 35. Recorrido por User Pools - Parte 1

### 36. Recorrido por User Pools - Parte 2
>- https://docs.aws.amazon.com/es_es/cognito/latest/developerguide/cognito-user-pools-using-import-tool-csv-header.html


### 37. Seguridad Avanzada y Analítica con Pinpoint
>- https://docs.aws.amazon.com/es_es/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html


### 38. Hosted UI o interface predefinida de Cognito

### 39. Dónde guarda la Hosted UI los tokens

### 40. Eliminar User Pools

### 41. Personalizar Hosted UI - Parte 1
>- https://docs.aws.amazon.com/es_es/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html
>- https://docs.aws.amazon.com/es_es/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html

### 42. Personalizar Hosted UI - Parte 2


## Sección 8: Cognito Identity Pools










