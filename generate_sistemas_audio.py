# -*- coding: utf-8 -*-
"""
Generador de Podcasts Neurales en MP3 para el Área de Ingeniería de Sistemas - FESNA.
Estudiante: David Yused Pulido Pardo
Programa: Ingeniería de Sistemas - 10.º Semestre
"""

import asyncio
import os
import edge_tts

OUT_DIR = r"C:\Users\david\.gemini\antigravity\scratch\fesna-portafolio-ia\assets"

PODCAST_TECNICO_SCRIPT = (
    "Bienvenidos a TechFESNA, el podcast oficial de la Tecnología en Gestión de Software y Sistemas de la Fundación de Educación Superior Nueva América. "
    "Hoy analizamos las claves del desarrollo moderno. "
    "Primero: el ciclo de vida del software ha evolucionado. Ya no trabajamos en cascada tradicional; hoy dominamos metodologías ágiles como Scrum y Kanban, "
    "integrando pipelines de integración y entrega continua CI/CD para desplegar código seguro y escalable. "
    "Segundo: en gestión de datos, articulamos bases de datos relacionales SQL con motores NoSQL orientados a documentos y analítica en tiempo real. "
    "Y tercero: formamos líderes con visión de arquitectura de software, patrones de microservicios y computación en la nube. "
    "Fórmate en 5 cuatrimestres bajo la Resolución MEN 012172 de 2022 con códigos SNIES 111397 en presencial y 111398 en virtual, "
    "y continúa hacia tu título profesional en Ingeniería de Sistemas en La Nueva América, siempre nueva."
)

PODCAST_PROSPECTIVO_SCRIPT = (
    "Análisis Prospectivo FESNA: El futuro de la Ingeniería de Sistemas en la era de la Inteligencia Artificial. "
    "La ingeniería de software experimenta su mayor transformación histórica. La inteligencia artificial generativa y los sistemas de agentes autónomos "
    "no reemplazan al ingeniero de sistemas; potencian su capacidad estratégica para diseñar arquitecturas resilientes, modelar datos a gran escala "
    "y auditar ciberseguridad con aprendizaje automático. "
    "En la Fundación de Educación Superior Nueva América formamos profesionales capaces de liderar la transformación digital con sentido ético, "
    "soluciones en la nube y visión directiva, culminando los tres ciclos propedéuticos con título profesional en Ingeniería de Sistemas, "
    "respaldado por la Resolución MEN 012173 de 2022 y códigos SNIES 111393 presencial y 111394 virtual. "
    "El futuro inteligente se construye en FESNA."
)

async def generate():
    os.makedirs(OUT_DIR, exist_ok=True)
    
    # 1. Podcast Técnico Nivel 2
    f1 = os.path.join(OUT_DIR, "podcast-tecnico-tgss.mp3")
    print(f"Generando Podcast Técnico en {f1}...")
    communicate1 = edge_tts.Communicate(
        text=PODCAST_TECNICO_SCRIPT,
        voice="es-CO-GonzaloNeural",
        rate="+4%",
        pitch="+0Hz"
    )
    await communicate1.save(f1)
    print("Podcast Técnico generado con éxito.")

    # 2. Podcast Prospectivo Nivel 3
    f2 = os.path.join(OUT_DIR, "podcast-prospectivo-sistemas.mp3")
    print(f"Generando Podcast Prospectivo en {f2}...")
    communicate2 = edge_tts.Communicate(
        text=PODCAST_PROSPECTIVO_SCRIPT,
        voice="es-CO-SalomeNeural",
        rate="+3%",
        pitch="+2Hz"
    )
    await communicate2.save(f2)
    print("Podcast Prospectivo generado con éxito.")

if __name__ == "__main__":
    asyncio.run(generate())
