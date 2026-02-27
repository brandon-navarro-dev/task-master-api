#  Task Master API

##  Descripción del Proyecto

Task Master API es un servicio REST desarrollado con Django y Django REST Framework.

La aplicación permite a usuarios autenticados:

- Crear, consultar, actualizar y eliminar tareas
- Subir imágenes asociadas a las tareas
- Gestionar etiquetas (tags)
- Filtrar tareas por estado y prioridad
- Acceder únicamente a sus propios recursos

La autenticación se realiza mediante JWT (JSON Web Tokens).

---

##  Tecnologías Utilizadas

- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT (Autenticación JWT)
- SQLite
- Docker & Docker Compose

---

##  Instrucciones para Ejecutar el Proyecto

### 1. Construir y levantar los contenedores

```bash
docker compose up --build
```

### 2. Aplicar migraciones 
```bash
docker compose exec backend python manage.py migrate
```

### 3. Crear Superusuario
```bash
docker compose exec backend python manage.py createsuperuser
```

### La aplicación estará disponible en:
```bash
http://localhost:8000/
```
### 4. Obtener Token de Acceso
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"usuario","password":"contraseña"}'

#RESPUESTA ESPERADA
{
  "refresh": "...",
  "access": "TOKEN_DE_ACCESO"
}

#Para acceder a endpoints protegidos en postman

Authorization: Bearer TU_ACCESS_TOKEN


```
### 5. Endpoints Disponibles
Tareas

- GET /api/tasks/

- POST /api/tasks/

- GET /api/tasks/{id}/

- PUT /api/tasks/{id}/

- DELETE /api/tasks/{id}/

Etiquetas

- GET /api/tags/

- POST /api/tags/

### 6. Crear tarea con Imagen
Se debe usar multipart/form-data

```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer TU_ACCESS_TOKEN" \
  -F "title=Tarea con imagen" \
  -F "description=Subiendo archivo" \
  -F "status=pending" \
  -F "priority=high" \
  -F "image=@./imagen.jpg"

#Si la operación es exitossa, el campo image devolverá una URL similar a :
"image": "/media/tasks/archivo.jpg"
  ```

### 7. Características implementadas
- Autenticación JWT

- CRUD completo de tareas

- Relación Many-to-Many con etiquetas

- Subida de imágenes (JPG, PNG, WEBP)

- Validación de tamaño máximo (2MB)

- Permisos basados en propietario (owner-based access)

- Entorno dockerizado

### 8. Decisiones Técnicas

- Se utilizó JWT para mantener autenticación stateless.

- Se implementó control de permisos para que cada usuario solo acceda a sus propios recursos.

- Se validó tipo y tamaño de archivo para garantizar seguridad.

- Se utilizó SQLite por simplicidad para la prueba técnica.

### 9. Consideraciones

- El proyecto está configurado para entorno local.

- No se incluyó configuración para producción (Nginx, Gunicorn, variables de entorno seguras).

- SQLite se utiliza únicamente para simplificar la ejecución de la prueba.

### Autor
Desarrollado por el Ingeniero Brandon González Navarro