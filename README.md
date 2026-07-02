# Sistema Web - Comercializadora Santa Cruz S.R.L.

[![CI/CD](https://github.com/Cesar-Abdiel/scm-comercializadora-santa-cruz/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Cesar-Abdiel/scm-comercializadora-santa-cruz/actions/workflows/ci-cd.yml)
![Version](https://img.shields.io/badge/version-1.1.1-blue)
![SCM](https://img.shields.io/badge/SCM-GitFlow-success)

Repositorio académico para documentar el Plan de Gestión de la Configuración del Software SCM aplicado a un sistema web de Comercializadora Santa Cruz S.R.L.

## Descripción del proyecto

El sistema simulado permite gestionar clientes, productos, pedidos, facturación y reportes comerciales.

Este repositorio se utiliza como evidencia del proceso SCM, incluyendo control de versiones, línea base, gestión de cambios, releases y automatización CI/CD.

## Módulos simulados

- Clientes
- Productos
- Pedidos
- Facturación
- Reportes

## Estructura del proyecto

- docs: documentación del plan SCM.
- src: código fuente simulado del sistema.
- tests: pruebas básicas.
- config: archivos de configuración.
- database: scripts de base de datos.
- .github/workflows: configuración del pipeline CI/CD.

## Flujo de trabajo Git Flow

El proyecto utiliza las siguientes ramas:

- main
- develop
- feature/clientes-crud
- release/v1.1.0
- hotfix/facturacion-descuento

## Pipeline CI/CD

El workflow de GitHub Actions ejecuta los siguientes jobs:

- build
- test
- lint
- deploy-staging
