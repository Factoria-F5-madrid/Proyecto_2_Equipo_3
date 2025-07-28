# Proyecto_2_Equipo_3
Scrum Master = Andrés Lázaro

Product Owner = Ignacio Castillo

API = [Django](https://www.djangoproject.com/) version 5.2.4

negocio = comida

gestion del proyecto [aquí](https://github.com/orgs/Factoria-F5-madrid/projects/25)


# 🚀 Proyecto: Sistema de Gestión Personalizado

![Banner Proyectos](https://github.com/user-attachments/assets/94ecebe4-ceba-47ae-8f3c-af14bdfe8606)

# 📄 Retrospectiva del Proyecto – Food5

## 1. Información General
- **Nombre del proyecto:** Food5. Proyecto 2 del bootcamp de IA de F5  
- **Fecha de este documento:** 28-07-2025  
- **Duración del proyecto:** 3 semanas  
- **Equipo participante:** Ignacio Castillo, Andrés Lázaro, Mónica Gómez, Ümit Güngör, Teo Ramos

---

## 2. Objetivos del Proyecto
El objetivo del proyecto fue desarrollar un sistema destinado a ayudar al dueño de una microempresa de catering a gestionar su operación de forma más eficiente.  
El sistema debía permitir, a través de una **base de datos estructurada**, realizar todas las operaciones **CRUD** necesarias para manejar el inventario de la empresa, incluyendo entidades clave como **platos, menús, pedidos y clientes**.  
Esta base de datos serviría como núcleo del sistema, permitiendo almacenar, consultar, modificar y relacionar correctamente toda la información del negocio, y facilitando así una administración ágil, segura y estructurada.

---

## 3. Resultados Alcanzados
El proyecto alcanzó una implementación funcional con múltiples características avanzadas:

- ✅ Backend modular construido en Django  
- ✅ API REST bien estructurada, documentada con **Swagger**  
- ✅ Frontend desacoplado y conectado desde la carpeta `food5-frontend`  
- ✅ Estructura de base de datos sólida y coherente  
- ✅ Implementación de **tests automáticos**  
- ✅ Integración con base de datos remota **Supabase**  
- ✅ Funcionalidad para **exportar datos a CSV**, útil para reportes, backups o migración de información

---

## 4. ¿Qué funcionó bien?

- ✅ **Modularidad del sistema:** Separación por apps facilitó el trabajo en paralelo y la organización del código  
- ✅ **API documentada con Swagger:** Facilita consumo e integración por otros desarrolladores  
- ✅ **Exportación a CSV:** Permite extracción útil para análisis o informes  
- ✅ **Conexión con Supabase:** Aporta escalabilidad y arquitectura moderna  
- ✅ **Tests automáticos:** Aseguran calidad y permiten refactorizaciones con confianza  
- ✅ **Arquitectura desacoplada (frontend/backend):** Permite independencia en desarrollo y despliegue

---

## 5. ¿Qué no funcionó tan bien?

 ⚠️ **Exceso de fragmentación de apps:** Crear una app por tipo de plato (`bread`, `dessert`, etc.) generó redundancia y duplicación de lógica  
 ⚠️ **Dificultades técnicas con relaciones de modelos:**  
  Django no permite, dentro de sus modelos, mantener una lista de objetos de diferente tipo que hereden de una clase común (`Dish`), como sí lo permite Python.  
  Esto se debe a que los modelos de Django también representan **tablas en bases de datos relacionales**, por lo que fue necesario crear un modelo adicional con una `ForeignKey` hacia la tabla `Order`, 
  donde se deseaba almacenar dicha lista.  
 ⚠️ **Dificultades con migraciones:** Al trabajar cada desarrollador en ramas diferentes, se generaron conflictos en migraciones que costó resolver  
 ⚠️ **Desperdicio de abstracciones reutilizables:** La lógica compartida entre tipos de platos pudo haberse centralizado en una sola app más genérica

---

## 6. Lecciones Aprendidas

 📌 Documentar APIs con Swagger desde el principio mejora la comunicación técnica  
 📌 La exportación de datos es una funcionalidad muy útil para usuarios reales y debe considerarse desde el diseño inicial  
 📌 La modularidad es valiosa, pero debe mantenerse con equilibrio para evitar sobreestructuración  
 📌 El uso de herramientas externas (Supabase, Swagger, CSV, tests) eleva el nivel profesional del proyecto, pero requiere integración coherente desde el diseño

---

## 7. Acciones a Tomar / Plan de Mejora

 🔄 **Unificar modelos de platos:** Consolidar apps similares en una sola (`app_dish`), diferenciando con un campo `tipo`  
 🧪 **Aumentar cobertura de tests**, especialmente para escenarios más complejos  
 📚 **Documentar el uso de Supabase y exportación a CSV** en una guía técnica  
 🔍 **Revisar relaciones complejas en ORM Django:** Considerar uso de `Abstract Models`, `GenericForeignKey` o `Proxy Models` para mayor flexibilidad

---

## 8. Conclusión
El proyecto **Food5** se desarrolló con una arquitectura moderna, buenas prácticas de desarrollo y herramientas profesionales.  
La combinación de **Django, React, Supabase, API REST, Swagger, testing y exportación a CSV** demuestra un enfoque sólido, funcional y preparado para escalar.  
A pesar de algunos problemas en el modelado inicial, el sistema alcanzó un estado robusto y deja al equipo con aprendizajes clave para futuras implementaciones.

---
