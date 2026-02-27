# Task Master API

## Descripción del Proyecto

Task Master API es un servicio REST desarrollado con Django y Django REST Framework.

La aplicación permite a usuarios autenticados:

- Crear, consultar, actualizar y eliminar tareas
- Subir imágenes asociadas a las tareas
- Gestionar etiquetas (tags)
- Filtrar tareas por estado y prioridad
- Acceder únicamente a sus propios recursos

La autenticación se realiza mediante JWT (JSON Web Tokens).

---

## Tecnologías Utilizadas

- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT (Autenticación JWT)
- SQLite
- Docker & Docker Compose

---

##  Instrucciones para Ejecutar el Proyecto

###  1.- Construir y levantar los contenedores

```bash
docker compose up --build

### 2.- Aplicar migraciones

```bash
docker compose exec backend python manage.py migrate

### 3.- Crear superusuario

```bash
docker compose exec backend python manage.py createsuperuser

### La aplicación estará disponible en 

http://localhost:8000/

---

## Autenticación(JWT)
###Para poder obtener el TOKEN de acceso 

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"usuario","password":"contraseña"}'

##La respuesta esperada 
```JSON
{
  "refresh": "...",
  "access": "AQUI ESTA EL TOKEN QUE SE USA PARA PODER ACCEDER A LOS ENDPOINTS"
}

##Para acceder a los endpoints protegidos
```Dentro de POSTMAN 
Authorization: Bearer TU_ACCESS_TOKEN (O la información obtenida en access)

### Endpoints Disponibles
##Tareas

GET /api/tasks/

POST /api/tasks/

GET /api/tasks/{id}/

PUT /api/tasks/{id}/

DELETE /api/tasks/{id}/

Etiquetas

GET /api/tags/

POST /api/tags/

----

###Crear Tarea con Imagen
##Usa multipart/form-data en POSTMAN
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer TU_ACCESS_TOKEN" \
  -F "title=Tarea con imagen" \
  -F "description=Subiendo archivo" \
  -F "status=pending" \
  -F "priority=high" \
  -F "image=@./imagen.jpg"

#Si la operación es exitosa, el campo image devolverá una URL similar a:
"image": "/media/tasks/archivo.jpg"

###Características Implementadas

Autenticación JWT

CRUD completo de tareas

Relación Many-to-Many con etiquetas

Subida de imágenes (JPG, PNG, WEBP)

Validación de tamaño máximo (2MB)

Permisos basados en propietario (owner-based access)

Entorno completamente dockerizado

### Decisiones Técnicas

Se utilizó JWT para autenticación stateless.

Se implementó control de permisos para que cada usuario solo pueda acceder a sus propias tareas.

Se validó el tipo y tamaño del archivo para garantizar la seguridad en la carga de imágenes.

Se dockerizó el proyecto para facilitar su ejecución en cualquier entorno.

###Autor
##Desarrollado por el Ingenierio en Datos e Inteligencia Organizacional: 
##Brandon González Navarro