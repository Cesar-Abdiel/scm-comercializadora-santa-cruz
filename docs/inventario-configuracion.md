# Inventario de ítems de configuración

| Código | Elemento | Descripción | Estado |
|---|---|---|---|
| LB-001 | Estructura del repositorio | Carpetas base, README.md y documentación inicial | Aprobado |
| LB-002 | Plan SCM | Documento principal del plan de gestión de configuración | Aprobado |
| LB-003 | Scripts de base de datos | Archivo schema.sql con estructura inicial | Aprobado |
| LB-004 | Workflow CI/CD | Archivo ci-cd.yml para automatización en GitHub Actions | En revisión |
| LB-005 | Código fuente | Archivos simulados de clientes, productos, pedidos y facturación | Aprobado |

## Línea base inicial

La línea base inicial del proyecto contiene la estructura mínima necesaria para controlar los ítems de configuración del sistema web de Comercializadora Santa Cruz S.R.L.

## Responsables de la configuración

| Rol | Responsabilidad |
|---|---|
| Administrador SCM | Controlar la línea base y versiones |
| Desarrollador | Crear ramas feature y commits convencionales |
| Revisor CCB | Aprobar solicitudes de cambio |
| Responsable CI/CD | Verificar pipeline y despliegue a staging |

## Criterios de control

- Todo cambio debe estar asociado a un commit.
- Los cambios importantes deben pasar por Pull Request.
- Las versiones se documentan en CHANGELOG.md.
- Las ramas principales son main y develop.
