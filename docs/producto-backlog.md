# Product Backlog - Sistema Restaurante POS + KDS & Ecosistema Integral

## Visión Arquitectónica del Sistema
El ecosistema se divide en 3 grandes bloques modulares escalables[cite: 2]:
1. **Módulo Operativo (POS + KDS):** Servicio a la mesa, comanda táctil, ruteo a pantallas de cocina y cobro/precuenta[cite: 1].
2. **Módulo de Gestión (Backoffice):** Recepción de facturas de mercancía, inventario/stock, recetas/escandallo y compras a proveedores.
3. **Módulo Administrativo, SST y Calidad:** Control de asistencia de personal, reportes de daños de equipos y registro de incidentes laborales[cite: 1].

---

## Épicas en Desarrollo (Sprint 1 en adelante)

### Épica 1: Usuarios, Roles y Asistencia
* **Prioridad:** Alta[cite: 1, 2]
* **US-01:** Autenticación por roles (Administrador, Mesero, Cajero, Cocinero) y registro de asistencia/horas trabajadas[cite: 1, 2].

### Épica 2: Gestión de Salón, Zonas y Mesas
* **Prioridad:** Alta[cite: 1, 2]
* **US-02:** Configuración de zonas (Salón, Terraza, Pets) y registro de mesas por el administrador[cite: 1].
* **US-03:** Plano interactivo del salón en tiempo real (*Libre*, *Ocupada*, *Pendiente de Pago*)[cite: 1].
* **US-04:** Acciones de mover clientes de mesa y juntar mesas[cite: 1].

### Épica 3: Catálogo del Menú y Estaciones de Cocina
* **Prioridad:** Alta[cite: 1, 2]
* **US-05:** Categorías del menú (Platos, Bebidas, Postres) y modificadores/notas por producto[cite: 1].
* **US-06:** Asignación de productos a estaciones de cocina (Plancha, Pastas, Ensaladas, Bar)[cite: 1].

### Épica 4: Toma de Pedidos y Comandas (Módulo Mesero)
* **Prioridad:** Alta[cite: 1, 2]
* **US-07:** Selección de mesa y adición de productos a comanda[cite: 1].
* **US-08:** Notas personalizadas por plato (ej: *"sin cebolla"*)[cite: 1].
* **US-09:** Envío de orden a cocina y actualización automática de mesa a *Ocupada*[cite: 1].

### Épica 5: Pantalla de Cocina (KDS) por Estaciones
* **Prioridad:** Media-Alta[cite: 1, 2]
* **US-10:** Visualización de comandas ruteadas por estación de preparación[cite: 1].
* **US-11:** Flujo de estados del plato (`En cola` -> `Preparando` -> `Emplatando` -> `Entregado`)[cite: 1].

### Épica 6: Caja, Precuenta y Fraccionamiento
* **Prioridad:** Media-Alta[cite: 1, 2]
* **US-12:** Solicitud de precuenta y cambio de mesa a *Pendiente de Pago*[cite: 1].
* **US-13:** Cobro total o fraccionamiento/división de cuenta con propina voluntaria y liberación de mesa[cite: 1].

---

## Roadmap de Expansión / Épicas Futuras

### Épica 7: Módulo de Gestión de Inventarios y Proveedores (Backoffice)
* **Prioridad:** Futura
* **Features:**
  * Carga de facturas de compra para alimentar stock e insumos.
  * Configuración de recetas/escandallo por plato con descuento automático de inventario.
  * Órdenes de compra e historial de proveedores.

### Épica 8: Módulo de Mantenimiento y Equipos
* **Prioridad:** Futura
* **Features:**
  * Reporte de averías o fallas de equipos de cocina/operación (freidoras, refrigeración, impresoras).
  * Programación de mantenimientos preventivos.

### Épica 9: Módulo de Seguridad y Salud en el Trabajo (SST)
* **Prioridad:** Futura
* **Features:**
  * Reporte de incidentes o accidentes laborales dentro del turno.
  * Control de carpetas de SST y normatividad.
```[cite: 1, 2]

Guarda el archivo y haz el commit en la terminal[cite: 2]:

```bash
git add docs/product-backlog.md
git commit -m "docs: add full architecture diagram and future roadmap epics (Backoffice & SST)"
git push
```[cite: 2]

---

### 2. Implementar la US-02: Zonas y Mesas (`apps/salon`)

Con la documentación actualizada, pasamos a programar los modelos de **Zonas y Mesas** del Salón en Django[cite: 1, 2].

#### A. Editar `src/apps/salon/models.py`

Abre `src/apps/salon/models.py` e inserta los siguientes modelos[cite: 1, 2]: