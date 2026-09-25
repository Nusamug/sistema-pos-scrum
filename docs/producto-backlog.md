# Product Backlog - Sistema de Inventario y Punto de Venta (POS)

## Bitácora de Uso de Inteligencia Artificial
* **Prompt utilizado:** *"Actúa como un Product Owner experto en Scrum. Toma el listado de 14 actividades de un Sistema POS y organízalo en Épicas y Features, definiendo códigos identificadores (US-XX) para cada historia de usuario."*[cite: 4, 6]
* **Ajustes del equipo:** Se decidió unificar el módulo de pagos y comprobantes dentro del flujo directo de la caja registradora para optimizar la atención en el POS[cite: 4, 6]. Se ajustaron las prioridades poniendo en primer lugar la seguridad (autenticación) e inventario básico, antes de habilitar el punto de venta y reportes[cite: 4, 6].

---

## 1. Épicas y Features Priorizadas

### Épica 1: Gestión de Usuarios y Seguridad
* **Prioridad:** Alta
* **Justificación:** Es la base de seguridad para garantizar el acceso controlado al sistema y diferenciar entre el rol de Administrador y Cajero[cite: 4, 6].

#### Feature 1.1: Autenticación y Control de Acceso
* **US-01:** Como usuario, quiero registrarme e iniciar sesión para acceder a la plataforma de forma segura.
* **US-02:** Como administrador, quiero gestionar perfiles de empleados y asignar permisos según el rol (Administrador / Cajero)[cite: 1].

---

### Épica 2: Gestión de Inventario y Catálogo
* **Prioridad:** Alta[cite: 1, 2]
* **Justificación:** Sin un catálogo cargado y un stock registrado, no es posible operar la caja registradora[cite: 4, 6].

#### Feature 2.1: Administración del Catálogo de Productos
* **US-03:** Como administrador, quiero crear, editar y eliminar productos con su precio y código de barras para mantener el catálogo actualizado[cite: 1].
* **US-04:** Como administrador, quiero gestionar categorías de productos para organizarlos eficientemente[cite: 1].

#### Feature 2.2: Control de Stock y Consultas
* **US-05:** Como usuario, quiero consultar y filtrar el inventario en tiempo real para verificar la disponibilidad de productos[cite: 2].
* **US-06:** Como administrador, quiero definir alertas de stock mínimo para recibir notificaciones cuando un producto esté por agotarse[cite: 1].

---

### Épica 3: Punto de Venta (POS) y Procesamiento de Pagos
* **Prioridad:** Alta[cite: 1, 2]
* **Justificación:** Corresponde al núcleo operativo del negocio para atender clientes y facturar compras[cite: 4, 6].

#### Feature 3.1: Módulo de Caja Registradora
* **US-07:** Como cajero, quiero buscar productos rápidamente por código o nombre para agilizar la atención[cite: 2].
* **US-08:** Como cajero, quiero agregar productos al carrito de compras para estructurar la venta activa[cite: 1].
* **US-09:** Como cajero, quiero visualizar el cálculo automático del total, impuestos y cambio a entregar para evitar errores de cobro[cite: 1].

#### Feature 3.2: Procesamiento de Pago y Comprobantes
* **US-10:** Como cajero, quiero procesar pagos en efectivo, tarjeta o transferencia para completar la transacción[cite: 1].
* **US-11:** Como cliente, quiero recibir un recibo digital de la compra para contar con un soporte del pago[cite: 1].

---

### Épica 4: Historial de Transacciones y Gestión de Ventas
* **Prioridad:** Media[cite: 1, 2]
* **Justificación:** Permite realizar seguimiento, auditorías y corrección de operaciones registradas durante la jornada[cite: 4, 6].

#### Feature 4.1: Control y Anulación de Transacciones
* **US-12:** Como usuario, quiero consultar el historial de ventas por fechas o jornadas laborales[cite: 1].
* **US-13:** Como administrador, quiero anular o cancelar una venta errónea para corregir el registro del inventario y la caja[cite: 1].

---

### Épica 5: Dashboard y Reportes Administrativos
* **Prioridad:** Media-Baja[cite: 1, 2]
* **Justificación:** Otorga valor analítico para la toma de decisiones, aunque no bloquea la operación básica de venta diaria[cite: 4, 6].

#### Feature 5.1: Métricas de Negocio
* **US-14:** Como administrador, quiero visualizar un dashboard con las métricas clave de ventas diarias y productos más vendidos[cite: 1].