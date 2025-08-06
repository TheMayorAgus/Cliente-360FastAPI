# 📘 API Flow - cliente360-api

Guía lógica y funcional del backend para gestión de clientes.  
Sin código, solo el flujo conceptual para mantener claridad durante el desarrollo.

---

## 🧩 Objetivo general

Construir una API REST que permita a una PyME manejar clientes:  
crear, ver, actualizar, eliminar y dejar notas internas.

---

## 🗂 Entidad principal

### Cliente
- `id`: identificador único
- `nombre`: nombre completo (obligatorio)
- `email`: correo electrónico (obligatorio, único)
- `teléfono`: número de contacto (opcional)
- `empresa`: nombre de empresa asociada (opcional)
- `notas`: comentarios internos (opcional)

---

## 🚦 Endpoints

### `GET /clientes`
- Trae todos los clientes registrados.
- Útil para listados generales.

### `GET /clientes/{id}`
- Muestra los datos de un cliente por ID.
- Si no existe → 404.

### `POST /clientes`
- Crea un nuevo cliente.
- Verifica si el email ya existe.
- Si existe → 409 Conflict.
- Si no → crea y devuelve el nuevo cliente (201).

### `PUT /clientes/{id}`
- Reemplaza completamente los datos de un cliente.
- Si no existe → 404.
- Todos los campos deben venir en el request.

### `DELETE /clientes/{id}`
- Elimina el cliente indicado.
- Si no existe → 404.
- Si existe → elimina y devuelve 204 No Content.

---

## 🔧 Lógica por operación

### Crear cliente
- Validar campos obligatorios (nombre, email).
- Buscar por email → si existe, rechazar.
- Crear objeto Cliente.
- Guardar en la base.
- Devolver cliente creado (201).

### Obtener cliente
- Buscar por ID.
- Si no existe → error 404.
- Si existe → devolver.

### Actualizar cliente
- Buscar cliente por ID.
- Si no existe → 404.
- Sobrescribir todos los campos.
- Guardar cambios.
- Devolver cliente actualizado.

### Eliminar cliente
- Buscar cliente por ID.
- Si no existe → 404.
- Eliminar y confirmar (204).

---

## 🧠 Reglas de negocio

- El `email` debe ser único por cliente.
- No se pueden guardar clientes sin `nombre` o `email`.
- Las `notas` son opcionales.
- Cliente eliminado → eliminación total (no soft delete).
- No se requiere autenticación por ahora.

---

## 📌 Ideas futuras

- Autenticación por JWT
- Registro de logs (auditoría)
- Búsqueda por nombre, empresa, teléfono
- Soporte para múltiples notas por cliente
- Agregado de timestamps: fecha de creación / modificación

---
