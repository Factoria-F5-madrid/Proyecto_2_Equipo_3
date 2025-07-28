# 🍽️ Food5 – App de Gestión para Empresas de Catering

Food5 es una solución web desarrollada para facilitar la administración de empresas de catering. Ofrece funcionalidades completas para manejar productos, pedidos y clientes, integrando una interfaz moderna y una API robusta basada en Django.

---

## ⚙️ Tecnologías Utilizadas

| Frontend        | Backend          | Autenticación       |
|-----------------|------------------|----------------------|
| React           | Django            | Login con JWT        |
| React Router    | Django REST Framework (DRF) | Roles de usuario básicos |
| Axios           | drf_yasg (Swagger / ReDoc) | —                  |

---

## 🧩 Estructura del Proyecto

- `food5-frontend/`: Aplicación cliente en React
- `Food5/`: Proyecto Django principal
- Apps incluidas:
  - `app_user`
  - `app_customer`
  - `app_order`
  - `app_bread`
  - `app_dessert`
  - `app_first_course`
  - `app_second_course`
  - `app_drink`
  - `app_menu`

---

## 🔐 Funcionalidades Principales

- 🚪 Registro y Login de usuarios
- 📦 Listado de productos
- 🍞 CRUD completo para "panes" como demostración
- 📬 Formulario de contacto para empresas interesadas
- 📊 Panel de administración vía `/admin`
- 📄 Exportación de datos a CSV
- 🧾 Documentación automática con Swagger (`/swagger/`) y Redoc (`/redoc/`)

---

## 🚀 Instalación y Ejecución

### 🔧 Backend (Django)

```bash
# Instala dependencias
pip install -r requirements.txt

# Ejecuta el servidor
python manage.py runserver

🖥️ Frontend (React)

# Accede al directorio del frontend
cd food5-frontend

# Instala dependencias
npm install

# Ejecuta la app en desarrollo
npm run dev


🔗 Rutas destacadas (Frontend)
| Ruta | Componente | 
| /login | Login | 
| /register | Registro | 
| /dashboard | Panel de administración | 
| /orders | Pedidos | 
| /productos | Productos | 
| /contacto | Formulario de contacto | 


 Endpoints Principales (API Django)
Ejemplo usando el modelo Dessert:
GET     /dessert/                 # Listar todos los postres
POST    /dessert/crear            # Crear nuevo postre
GET     /dessert/<id>/            # Ver detalle del postre
PUT     /dessert/<id>/            # Actualizar postre
DELETE  /dessert/<id>/            # Eliminar postre



📘 Documentación de la API
La documentación se genera automáticamente con Swagger y ReDoc:
- Swagger UI: 


