#### Archivo **`sprints/sprint-01/sprint-backlog.md`**
```markdown
# Sprint 1 - Sprint Backlog

## Objetivo del Sprint
Construir la base del sistema en Django implementando la autenticación por roles (US-01), la configuración del salón con zonas y mesas (US-02) y la carga del menú con estaciones de cocina (US-05 y US-06)[cite: 1, 2, 3, 5].

## Duración e Información
* **Duración:** 2 semanas[cite: 2]
* **Puntos Totales:** 13 Puntos[cite: 1, 2]
* **Estado:** En Progreso[cite: 1, 2]

---

## Tareas Seleccionadas

### US-01: Autenticación y Roles (3 Pts)[cite: 1, 2]
* [ ] Crear proyecto Django en `src/` e inicializar app `apps/usuarios`[cite: 2, 4, 6].
* [ ] Definir modelo `CustomUser` con roles (`ADMIN`, `MESERO`, `CAJERO`, `COCINERO`)[cite: 1, 2].

### US-02: Zonas y Mesas (5 Pts)[cite: 1, 2]
* [ ] Crear la app `apps/salon`[cite: 2, 4, 6].
* [ ] Definir modelos `Zona` y `Mesa` con estados (`LIBRE`, `OCUPADA`, `PENDIENTE_PAGO`, `RESERVADA`, `FUERA_SERVICIO`)[cite: 1, 2].

### US-05 y US-06: Menú y Estaciones de Cocina (5 Pts)[cite: 1, 2]
* [ ] Crear la app `apps/menu`[cite: 2, 4, 6].
* [ ] Definir modelos `Categoria`, `EstacionCocina` y `Producto`[cite: 1, 2].