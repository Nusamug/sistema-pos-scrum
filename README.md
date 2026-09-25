# Restaurante POS + KDS (Sistema de Gestión y Cocina por Estaciones)

## Visión del Producto
Sistema web integral en Django diseñado para la operación en tiempo real de restaurantes con servicio a la mesa. Permite a los meseros gestionar mesas por zonas (Salón, Terraza, Pets), tomar comandas con observaciones personalizadas por plato, enviar órdenes automáticas a pantallas de cocina ruteadas por estación (KDS: Plancha, Pastas, Ensaladas, Bar), y facilitar a la caja el cobro con precuenta, propinas y fraccionamiento de cuenta[cite: 1, 2].

## Arquitectura Técnica
* **Backend:** Python & Django (Estructura modular de Apps: `usuarios`, `salon`, `menu`, `pedidos`, `facturacion`)
* **Frontend:** HTML5, Tailwind CSS, HTMX / JavaScript[cite: 2]
* **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Producción)[cite: 2]
* **Control de Versiones y Documentación:** Git, GitHub, Markdown[cite: 2]

## Equipo de Desarrollo
* **Desarrollador Único (PO / SM / Dev):** Miguel David Rojas Gonzalez[cite: 2]

## Estructura del Repositorio
* `docs/`: Documentación del proyecto (`product-backlog.md`, `user-stories.md`)[cite: 2].
* `sprints/`: Evidencias y planificación de cada Sprint (`sprint-01/`)[cite: 2].
* `src/`: Código fuente de las aplicaciones en Django[cite: 2].