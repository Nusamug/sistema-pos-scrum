# Product Backlog - Restaurante POS + KDS

## Bitácora de Decisiones del Product Owner
* **Visión del Negocio:** Enfoque en servicio a la mesa y ruteo a cocina por estaciones[cite: 4, 6].
* **Definición de Salón:** Manejo de zonas (Salón, Terraza, Pets) con estados de mesa (*Libre*, *Ocupada*, *Pendiente de Pago*, *Reservada*, *Fuera de Servicio*) y acciones de mover o juntar mesas[cite: 1].
* **Definición de Cocina (KDS):** Ruteo automático por estaciones (Plancha, Pastas, Ensaladas, Bar) con flujo de estados: `En cola` -> `Preparando` -> `Emplatando` -> `Entregado`[cite: 1].
* **Definición de Caja:** Soporte de precuenta, propina voluntaria y división/fraccionamiento de cuenta[cite: 1].

---

## Épicas y Features Priorizadas

### Épica 1: Usuarios, Roles y Seguridad
* **Prioridad:** Alta[cite: 1, 2]
* **US-01:** Como usuario, quiero autenticarme en el sistema según mi rol (Administrador, Mesero, Cajero, Cocinero)[cite: 1, 2].

### Épica 2: Gestión de Salón, Zonas y Mesas
* **Prioridad:** Alta[cite: 1, 2]
* **US-02:** Como administrador, quiero crear y organizar las zonas del salón (Salón, Terraza, Pets) y sus mesas[cite: 1].
* **US-03:** Como mesero, quiero visualizar el plano del salón interactivo con los estados de las mesas en tiempo real (*Libre*, *Ocupada*, *Pendiente de Pago*)[cite: 1].
* **US-04:** Como mesero, quiero realizar acciones de mover clientes de mesa o juntar mesas[cite: 1].

### Épica 3: Catálogo del Menú y Estaciones de Cocina
* **Prioridad:** Alta[cite: 1, 2]
* **US-05:** Como administrador, quiero estructurar las categorías/subcategorías del menú (Platos, Bebidas, Postres)[cite: 1].
* **US-06:** Como administrador, quiero asignar a cada producto su estación de cocina correspondiente (Plancha, Pastas, Ensaladas, Bar)[cite: 1].

### Épica 4: Toma de Pedidos y Comandas (Módulo Mesero)
* **Prioridad:** Alta[cite: 1, 2]
* **US-07:** Como mesero, quiero seleccionar una mesa y agregar productos del menú a la comanda activa[cite: 1].
* **US-08:** Como mesero, quiero agregar notas u observaciones específicas a cada plato (ej: *"sin cebolla"*)[cite: 1].
* **US-09:** Como mesero, quiero enviar la orden confirmada para que se rutee a las pantallas de cocina y la mesa cambie a *Ocupada*[cite: 1].

### Épica 5: Pantalla de Cocina (KDS) por Estaciones
* **Prioridad:** Media-Alta[cite: 1, 2]
* **US-10:** Como cocinero, quiero visualizar en mi pantalla de estación los ítems pendientes asignados a mi área[cite: 1].
* **US-11:** Como cocinero, quiero cambiar el estado de preparación de los platos (`En cola` -> `Preparando` -> `Emplatando` -> `Entregado`)[cite: 1].

### Épica 6: Caja, Precuenta y Fraccionamiento de Cuenta
* **Prioridad:** Media-Alta[cite: 1, 2]
* **US-12:** Como mesero, quiero solicitar la precuenta de una mesa cambiando su estado a *Pendiente de Pago*[cite: 1].
* **US-13:** Como cajero, quiero procesar pagos totales o permitir el fraccionamiento/división de cuenta entre varios clientes[cite: 1].
* **US-14:** Como cajero, quiero agregar la propina voluntaria, procesar el pago y liberar la mesa a estado *Libre*[cite: 1].