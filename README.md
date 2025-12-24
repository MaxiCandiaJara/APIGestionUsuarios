# API de Gestión de Usuarios – Django REST

API REST desarrollada como proyecto personal para practicar backend con Django REST Framework.
El proyecto está enfocado en autenticación, permisos y manejo de usuarios por roles.

La API no tiene frontend. Se consume mediante herramientas como Postman o desde un frontend externo.

---

## ¿Qué hace esta API?

- Manejo de usuarios personalizados
- Autenticación con JWT
- Roles de usuario (`admin` y `user`)
- Permisos según rol:
  - Admin: CRUD completo
  - User: solo lectura
- Protección de endpoints con permisos personalizados

---

## Tecnologías usadas

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (base de datos por defecto)

---

## Autenticación

La autenticación se realiza mediante JWT.

Flujo básico:
1. El usuario obtiene un token en `/token/`
2. El token `access` se envía en cada request
3. La API valida permisos según el rol del usuario


## Endpoints principales

- `POST /token/` → obtener tokens JWT
- `GET /users/` → listar usuarios (requiere autenticación)
- `POST /users/` → crear usuario (solo admin)
- `PATCH /users/{id}/` → editar usuario (solo admin)
- `DELETE /users/{id}/` → eliminar usuario (solo admin)

---

## Cómo ejecutar el proyecto

```bash
git clone https://github.com/MaxiCandiaJara/nombre-del-repo.git
cd nombre-del-repo
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

