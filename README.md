# Sistema Web - Comercializadora Santa Cruz S.R.L.

[![CI/CD](https://github.com/Cesar-Abdiel/scm-comercializadora-santa-cruz/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Cesar-Abdiel/scm-comercializadora-santa-cruz/actions/workflows/ci-cd.yml)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![SCM](https://img.shields.io/badge/SCM-GitFlow-success)

Repositorio acad�mico para documentar el Plan de Gesti�n de la Configuraci�n del Software SCM aplicado a un sistema web de Comercializadora Santa Cruz S.R.L.

## Descripci�n del proyecto

El sistema simulado permite gestionar clientes, productos, pedidos, facturaci�n y reportes comerciales.  
Este repositorio se utiliza como evidencia del proceso SCM, incluyendo control de versiones, l�nea base, gesti�n de cambios, releases y automatizaci�n CI/CD.

## M�dulos simulados

- Clientes
- Productos
- Pedidos
- Facturaci�n
- Reportes

## Estructura del proyecto

- docs: documentaci�n del plan SCM.
- src: c�digo fuente simulado del sistema.
- tests: pruebas b�sicas.
- config: archivos de configuraci�n.
- database: scripts de base de datos.
- .github/workflows: configuraci�n del pipeline CI/CD.

## Flujo de trabajo

El proyecto utiliza Git Flow con las siguientes ramas:

- main
- develop
- feature/clientes-crud
- release/v1.1.0
- hotfix/facturacion-descuento
