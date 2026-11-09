# Sistemas Inteligentes · EASC-336

**Universidad Autónoma de Nayarit (UAN)**  
**Área Económico Administrativo · Licenciatura en Sistemas Computacionales**  
**Unidad de aprendizaje:** Sistemas Inteligentes  
**Academia:** Tratamiento de la Información  
**Modalidad:** curso-taller, obligatoria  
**Actualización curricular:** agosto de 2026

Este repositorio reúne recursos educativos de la materia **Sistemas Inteligentes**, con un enfoque centrado en la resolución de problemas, el diseño de agentes, la representación del conocimiento, la búsqueda, la decisión bajo incertidumbre, la percepción y los fundamentos funcionales de IA generativa.

Su propósito es que el estudiante **represente, experimente, compare, pruebe y explique** sistemas inteligentes, en lugar de limitarse a ejecutar herramientas sin comprender sus principios.

## Portal web de las seis unidades

**[Abrir los laboratorios interactivos](https://angelcaido37.github.io/Sistemas-Inteligentes_UAE/)**

Si la página web no está publicada todavía, consulta directamente los archivos en la carpeta [Interactivos](./Interactivos).

| Unidad | Contenidos principales | Laboratorio interactivo |
|---|---|---|
| I. Fundamentos de IA, sistemas y agentes | Agentes, modelos PEAS, percepciones, reglas y decisiones supervisadas. | [Abrir HTML](./Interactivos/Unidad_1_Agentes_PEAS.html) |
| II. Conocimiento, razonamiento y búsqueda | Sistemas expertos, inferencia, búsqueda en grafos y comparación de BFS, DFS y A*. | [Abrir HTML](./Interactivos/Unidad_2_Inferencia_BFS_DFS_AEstrella.html) |
| III. Decisión bajo incertidumbre | Umbrales, errores, matrices de costo, abstención y revisión humana. | [Abrir HTML](./Interactivos/Unidad_3_Decisiones_Umbrales.html) |
| IV. Percepción y sistemas multimodales | Reconocimiento de voz, errores de transcripción, distancia de edición y WER. | [Abrir HTML](./Interactivos/Unidad_4_Percepcion_WER.html) |
| V. IA generativa, RAG y agentes | Recuperación documental, vigencia de fuentes, fundamentación y seguridad. | [Abrir HTML](./Interactivos/Unidad_5_Recuperacion_RAG.html) |
| VI. Proyecto de sistema inteligente responsable | Integración de componentes, pruebas funcionales, límites y gestión de riesgos. | [Abrir HTML](./Interactivos/Unidad_6_Integracion_Responsable.html) |

## Qué ofrece cada laboratorio

Cada archivo HTML es un recurso autocontenido diseñado para que el estudiante:

1. Explore los fundamentos con explicaciones y ejemplos aplicados.
2. Manipule parámetros y ejecute actividades de simulación o resolución de problemas.
3. Conteste preguntas de autoevaluación con retroalimentación.
4. Utilice las herramientas de la unidad para preparar las evidencias de su tarea.
5. Documente y explique sus procedimientos, errores y resultados.

**Tecnología:** HTML, CSS y JavaScript integrados en cada archivo. No requieren un servidor de aplicaciones ni dependencias de terceros para abrirse. Al descargar un archivo puede utilizarse localmente en el navegador.

## Organización curricular

La unidad de aprendizaje contempla **96 horas**, distribuidas en 22 horas teóricas, 30 horas prácticas y 44 horas de estudio independiente, con valor de **6 créditos**.

### Evaluación de las evidencias curriculares

| Evidencia de aprendizaje | Ponderación |
|---|---:|
| Análisis de caso y diseño mediante PEAS | 10 % |
| Representación, razonamiento y búsqueda | 15 % |
| Política de decisión bajo incertidumbre | 15 % |
| Experiencia perceptiva o multimodal | 15 % |
| Prototipo funcional RAG o agente | 20 % |
| Proyecto integrador y defensa individual | 25 % |
| **Total** | **100 %** |

Los laboratorios interactivos son **materiales de apoyo formativo**, no sustituyen las evidencias anteriores ni constituyen por sí mismos una acreditación.

Según el programa, la acreditación exige al menos 80 % de asistencia, calificación final mínima de 60/100 y aprobación independiente del proyecto integrador y la defensa individual (al menos 60/100 en cada componente). Asimismo, requiere evidencias de autoría y declaración del uso de IA.

## Arquitectura y contenido del repositorio

```text
Sistemas-Inteligentes_UAE/
├── index.html              # Portal público de las seis unidades
├── README.md               # Presentación y documentación académica
├── .nojekyll               # Publicación de contenido estático sin Jekyll
├── Interactivos/
│   ├── Unidad_1_Agentes_PEAS.html
│   ├── Unidad_2_Inferencia_BFS_DFS_AEstrella.html
│   ├── Unidad_3_Decisiones_Umbrales.html
│   ├── Unidad_4_Percepcion_WER.html
│   ├── Unidad_5_Recuperacion_RAG.html
│   └── Unidad_6_Integracion_Responsable.html
└── Anterior/               # Material académico previo conservado
```

## Cómo publicar con GitHub Pages

1. Abre **Settings → Pages** en este repositorio.
2. En **Build and deployment**, selecciona **Deploy from a branch**.
3. Configura **Branch: main** y **Folder: /(root)**; guarda los cambios.
4. Comprueba que la publicación se complete y abre [el portal](https://angelcaido37.github.io/Sistemas-Inteligentes_UAE/).

Las rutas del portal son relativas a la carpeta del repositorio y están preparadas para GitHub Pages bajo `/Sistemas-Inteligentes_UAE/`.

**Nota técnica:** el error `Internal server error` en un despliegue de GitHub Pages puede proceder de los servicios de GitHub, incluso cuando la construcción y la carga del artefacto terminan correctamente. El archivo `.nojekyll` evita el procesamiento de Jekyll, pero **no garantiza** por sí solo la resolución de un error de infraestructura. Reintenta la publicación y consulta [GitHub Status](https://www.githubstatus.com/) si reaparece.

## Uso en Google Classroom

Publica el enlace del portal o de la unidad correspondiente como material de apoyo. Solicita a los estudiantes que realicen las simulaciones y entreguen, según la tarea formal, un informe, capturas, resultados y una explicación técnica del procedimiento.

**Limitaciones importantes:**
- Los HTML no registran automáticamente calificaciones en Classroom ni remiten respuestas al docente.
- Los datos de ejemplo son didácticos y no deben interpretarse como registros administrativos reales.
- El laboratorio de la Unidad V representa principalmente recuperación documental; no debe confundirse con un sistema RAG generativo conectado a un modelo de lenguaje.
- No deben ingresarse datos personales sensibles, contraseñas ni documentos privados.

## Enfoque didáctico

Se fomenta el uso responsable de herramientas de IA y de *vibe coding supervisado*: especificar el problema, generar prototipos, revisar el código, ejecutar pruebas, documentar los errores y justificar las decisiones de diseño. El estudiante mantiene la responsabilidad sobre la corrección de su trabajo.

## Referencias básicas

- Poole, D. L. y Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3.ª ed.). Cambridge University Press. https://doi.org/10.1017/9781009258227
- Russell, S. J. y Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4.ª ed., Global ed.). Pearson.
- National Institute of Standards and Technology. (2023). *AI Risk Management Framework (AI RMF 1.0)*. https://doi.org/10.6028/NIST.AI.100-1

---

**Responsable académico:** Dr. Oscar Gabriel Vizcaíno Monroy  
**Institución:** Universidad Autónoma de Nayarit  
**Uso:** docencia, experimentación y aprendizaje autónomo.
