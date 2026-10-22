# -*- coding: utf-8 -*-
"""
Script generador del documento Word (.docx) para el Punto 4 y la Documentacion
Tecnica Completa del Examen de Segundo Corte - FESNA.
Estudiante: David Yused Pulido Pardo
Programa: Ingenieria de Sistemas - 10. Semestre
"""

import os
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn


def set_cell_background(cell, fill_hex):
    """Aplica color de fondo hexadecimal a una celda de tabla en Word."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    """Configura margenes internos (padding) de una celda en twips."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_formatted_heading(doc, text, level=1, color_rgb=(13, 59, 102)):
    """Agrega un encabezado estilizado con color corporativo."""
    h = doc.add_heading(level=level)
    h.paragraph_format.space_before = Pt(16 if level == 1 else 12)
    h.paragraph_format.space_after = Pt(6)
    run = h.add_run(text)
    run.font.name = 'Calibri'
    run.font.bold = True
    if level == 1:
        run.font.size = Pt(16)
    elif level == 2:
        run.font.size = Pt(13.5)
    else:
        run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(*color_rgb)
    return h


def add_body_p(doc, text, bold_prefix=None, italic_prefix=None, space_after=6, justify=True):
    """Agrega un parrafo de cuerpo con formato limpio."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name = 'Calibri'
        rb.font.size = Pt(11)
        rb.font.bold = True
        rb.font.color.rgb = RGBColor(20, 35, 60)
    if italic_prefix:
        ri = p.add_run(italic_prefix)
        ri.font.name = 'Calibri'
        ri.font.size = Pt(11)
        ri.font.italic = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(35, 35, 35)
    return p


def add_bullet_p(doc, bold_prefix, text):
    """Agrega un elemento de lista con prefijo en negrita."""
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name = 'Calibri'
        rb.font.size = Pt(11)
        rb.font.bold = True
        rb.font.color.rgb = RGBColor(13, 59, 102)
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(35, 35, 35)
    return p


def add_prompt_box(doc, title, tool_badge, prompt_text, script_or_notes=None, accent_hex="0D3B66", bg_hex="F4F7FB"):
    """Crea un recuadro estilizado (tabla de 1x1) para mostrar un Prompt y su Guion/Resultado."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    # Borde izquierdo grueso de color acento
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{accent_hex}"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

    p_head = cell.paragraphs[0]
    p_head.paragraph_format.space_after = Pt(4)
    r_title = p_head.add_run(f"{title} ")
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(11)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(13, 59, 102)

    r_badge = p_head.add_run(f"[{tool_badge}]")
    r_badge.font.name = 'Calibri'
    r_badge.font.size = Pt(10)
    r_badge.font.bold = True
    r_badge.font.color.rgb = RGBColor(146, 26, 163) if accent_hex == "921AA3" else RGBColor(21, 135, 119)

    p_prompt_lbl = cell.add_paragraph()
    p_prompt_lbl.paragraph_format.space_after = Pt(2)
    rl = p_prompt_lbl.add_run("Prompt principal ejecutado:")
    rl.font.name = 'Calibri'
    rl.font.size = Pt(10)
    rl.font.bold = True
    rl.font.color.rgb = RGBColor(60, 60, 60)

    p_prompt = cell.add_paragraph()
    p_prompt.paragraph_format.space_after = Pt(6 if script_or_notes else 2)
    p_prompt.paragraph_format.line_spacing = 1.1
    rp = p_prompt.add_run(f"\"{prompt_text}\"")
    rp.font.name = 'Consolas'
    rp.font.size = Pt(9.5)
    rp.font.italic = True
    rp.font.color.rgb = RGBColor(30, 41, 59)

    if script_or_notes:
        p_notes = cell.add_paragraph()
        p_notes.paragraph_format.space_after = Pt(2)
        p_notes.paragraph_format.line_spacing = 1.12
        rn_lbl = p_notes.add_run("Elaboración técnica y extracto del guion/resultado: ")
        rn_lbl.font.name = 'Calibri'
        rn_lbl.font.size = Pt(10)
        rn_lbl.font.bold = True
        rn_lbl.font.color.rgb = RGBColor(13, 59, 102)

        rn = p_notes.add_run(script_or_notes)
        rn.font.name = 'Calibri'
        rn.font.size = Pt(10)
        rn.font.color.rgb = RGBColor(45, 45, 45)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(4)


def add_styled_table(doc, headers, rows, header_bg="0D3B66"):
    """Crea una tabla con encabezados coloreados y filas alternadas."""
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.style = 'Table Grid'

    # Encabezados
    hdr_cells = tbl.rows[0].cells
    for idx, h_text in enumerate(headers):
        cell = hdr_cells[idx]
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Filas de datos
    for r_idx, row_data in enumerate(rows):
        row_cells = tbl.rows[r_idx + 1].cells
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row_cells[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=110, right=110)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(13, 59, 102)
            else:
                r.font.color.rgb = RGBColor(40, 40, 40)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(4)
    return tbl


def add_apa_reference(doc, ref_text):
    """Agrega una referencia bibliografica con sangria francesa (hanging indent) de 1.27 cm (0.5 in) segun APA 7."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.5
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(ref_text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(30, 30, 30)
    return p


def build_document():
    doc = Document()

    # Configurar margenes de pagina (Normas APA: 2.54 cm = 1 pulgada en todos los lados)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # =========================================================================
    # PORTADA FORMAL (NORMAS APA 7.a EDICION)
    # =========================================================================
    for _ in range(2):
        doc.add_paragraph()

    p_badge = doc.add_paragraph()
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_b = p_badge.add_run("FUNDACIÓN DE EDUCACIÓN SUPERIOR NUEVA AMÉRICA — FESNA\nEXAMEN DE SEGUNDO CORTE — PORTAFOLIO Y CAMPAÑA MULTIMEDIA CON IA")
    r_b.font.name = 'Calibri'
    r_b.font.size = Pt(11)
    r_b.font.bold = True
    r_b.font.color.rgb = RGBColor(21, 135, 119)

    doc.add_paragraph()

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(12)
    r_t = p_title.add_run(
        "Documentación Técnica, Ingeniería de Prompts, Ecosistema de Inteligencia Artificial "
        "(HeyGen, CapCut, Gemini y Antigravity) y Sustentación Teórica de la Campaña "
        "Institucional Multipágina para FESNA"
    )
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(18)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(13, 59, 102)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(36)
    r_sub = p_sub.add_run(
        "Áreas Desarrolladas por Ciclos Propedéuticos: Administración de Empresas y Contaduría Pública\n"
        "(Punto 4: Sustentación Teórica, Metodología de Elaboración y Referencias en Normas APA 7.ª Edición)"
    )
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(90, 100, 115)

    # Tabla resumen de datos de portada
    cover_rows = [
        ["Estudiante / Autor:", "David Yused Pulido Pardo"],
        ["Programa Académico:", "Ingeniería de Sistemas — 10.º Semestre"],
        ["Docente Titular:", "Fredy Osbaldo Lemus Solano"],
        ["Institución:", "Fundación de Educación Superior Nueva América (FESNA) — Personería Jurídica Res. 6208 de 2009 MEN"],
        ["Ecosistema IA Empleado:", "Antigravity (Agente IA & Neural TTS) • Google Gemini & Gemini Canvas • CapCut IA • HeyGen Avatar IA"],
        ["Fecha de Entrega:", "Octubre de 2026 — Bogotá D.C., Colombia"]
    ]
    add_styled_table(doc, ["Campo Institucional", "Información Oficial del Proyecto"], cover_rows, header_bg="0D3B66")

    doc.add_page_break()

    # =========================================================================
    # SECCION 1: INTRODUCCION Y ARQUITECTURA GENERAL DEL PROYECTO
    # =========================================================================
    add_formatted_heading(
        doc,
        "1. Introducción y Arquitectura General del Proyecto Web e Institucional",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "El presente documento constituye el soporte técnico, metodológico y teórico (Punto 4 del Examen de Segundo Corte) "
        "del portal web interactivo y la campaña publicitaria transmedia desarrollada para la Fundación de Educación Superior "
        "Nueva América (FESNA). El objetivo central del proyecto consistió en diseñar, producir e integrar doce (12) productos "
        "comunicativos asistidos por Inteligencia Artificial —seis (6) para el Área de Administración y seis (6) para el Área "
        "de Contaduría Pública—, respetando de manera rigurosa el modelo educativo por ciclos propedéuticos de la institución "
        "(Nivel 1: Técnico Profesional, Nivel 2: Tecnológico y Nivel 3: Profesional Universitario) y garantizando el 100 % de "
        "fidelidad frente a los códigos SNIES y las Resoluciones de Registro Calificado otorgadas por el Ministerio de Educación "
        "Nacional (MEN)."
    )

    add_formatted_heading(doc, "1.1. Estructura Multipágina y Separación entre Portal Publicitario y Sustentación", level=2, color_rgb=(21, 135, 119))
    add_body_p(
        doc,
        "Siguiendo los criterios de diseño y experiencia de usuario (UX/UI) definidos durante el desarrollo, se estableció una "
        "arquitectura web limpia y modular donde el sitio web actúa como una plataforma institucional y publicitaria real de FESNA, "
        "mientras que el presente documento Word concentra toda la memoria técnica, los prompts ejecutados, la justificación de "
        "herramientas y la fundamentación teórica en normas APA 7.ª edición. La plataforma web se compone de cinco (5) páginas "
        "interconectadas mediante un menú lateral desplegable a la izquierda (drawer menu):"
    )

    add_bullet_p(
        doc,
        "1. Página Principal Institucional (index.html): ",
        "Inicia con la Sección 1 obligatoria de Introducción y Presentación Personal del estudiante (David Yused Pulido Pardo, "
        "Ingeniería de Sistemas, 10.º semestre, objetivos de aprendizaje, propósito del sitio web y recorrido del curso). "
        "A continuación, presenta la identidad corporativa de FESNA (https://www.nuevaamerica.edu.co/), su modelo por ciclos "
        "propedéuticos y el directorio visual de los 12 programas académicos con sus bandas cromáticas oficiales."
    )
    add_bullet_p(
        doc,
        "2. Área de Administración (administracion.html — Paleta Turquesa #36B59E / #1FA08B / #158777): ",
        "Aloja las 6 actividades de IA distribuidas en sus 3 niveles propedéuticos: Técnica Profesional en Procesos Administrativos "
        "Empresariales (Video explicativo IA + Infografía institucional IA), Tecnología en Gestión Administrativa (Reel promocional IA "
        "+ Spot publicitario con voz IA) y Administración de Empresas (Video institucional IA + Motion Graphics inteligente en Canvas)."
    )
    add_bullet_p(
        doc,
        "3. Área de Contaduría Pública (contaduria.html — Paleta Morada #AA38B9 / #921AA3 / #74187E): ",
        "Aloja las 6 actividades de IA de la facultad contable: Técnica Profesional en Procesos Contables (Serie de Reels con guion IA "
        "+ Cuña radial IA), Tecnología en Gestión Contable y Financiera (Podcast 'Conoce FESNA' a dos voces + Animación 2D Full HD "
        "asistida por IA) y Contaduría Pública (Testimonio recreado con Avatar IA Valeria Mendoza en HeyGen + Podcast institucional ejecutivo)."
    )
    add_bullet_p(
        doc,
        "4. Áreas Complementarias del Menú Desplegable (sistemas.html y marketing.html): ",
        "Páginas dedicadas a Ingeniería de Sistemas (paleta verde #1A7C3B) y Marketing y Publicidad (paleta roja/vinotinto #D43B27) "
        "con sus respectivos códigos SNIES y estructura de ciclos propedéuticos, garantizando una navegación institucional completa."
    )

    # =========================================================================
    # SECCION 2: ECOSISTEMA DE HERRAMIENTAS DE IA UTILIZADAS
    # =========================================================================
    add_formatted_heading(
        doc,
        "2. Ecosistema de Herramientas de Inteligencia Artificial Utilizadas y Justificación Técnica",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "Para alcanzar un acabado profesional, nítido y coherente en todos los formatos exigidos por el examen (video horizontal 16:9, "
        "Reels verticales 9:16, avatar hablante con sincronización labial, animación 2D vectorial, infografía corporativa y producción "
        "sonora multipista), se integró un flujo de trabajo apoyado en cuatro (4) plataformas especializadas de Inteligencia Artificial: "
        "Antigravity, Google Gemini (con Gemini Canvas), CapCut y HeyGen."
    )

    ia_rows = [
        [
            "1. Antigravity\n(Agente de Ingeniería de Software & Síntesis Neural)",
            "• Arquitectura web HTML5, CSS3 y JavaScript.\n"
            "• Motor de Motion Graphics a 60 FPS.\n"
            "• Generación de voces neurales (edge-tts).\n"
            "• Postprocesamiento gráfico con Python Pillow.",
            "Permitió construir desde cero la estructura multipágina con menú lateral desplegable, programar el lienzo interactivo "
            "del Nivel 3 de Administración y sintetizar audios MP3 de alta definición (24 kHz) con voces neurales colombianas y "
            "latinoamericanas diferenciadas para cada spot, cuña y podcast a dos voces."
        ],
        [
            "2. Google Gemini &\nGemini Canvas\n(IA Multimodal y Código Animado)",
            "• Ingeniería y validación de guiones.\n"
            "• Animación 2D en Full HD (1920x1080).\n"
            "• Generación de ilustración base para infografía.",
            "Se utilizó para estructurar los guiones adaptados al nivel jerárquico de cada programa y, mediante Gemini Canvas, "
            "generar y exportar en video la Animación 2D del Nivel 2 de Contaduría Pública (Tecnología en Gestión Contable y Financiera) "
            "con gráficos vectoriales nítidos y captura MediaRecorder."
        ],
        [
            "3. CapCut\n(Suite de Producción Audiovisual con IA)",
            "• Edición de videos explicativos e institucionales.\n"
            "• Creación de Reels verticales (9:16).\n"
            "• Subtitulado dinámico automático y efectos.",
            "Fundamental para el montaje rítmico de los videos del Área de Administración y la Serie de Reels del Nivel 1 de "
            "Contaduría Pública (fesna_reel_subtitulos_morados.mp4), aplicando subtítulos dinámicos sincronizados con la paleta "
            "morada (#AA38B9) y turquesa (#36B59E) de FESNA."
        ],
        [
            "4. HeyGen\n(Plataforma de Avatares Digitales con IA)",
            "• Recreación de testimonio con avatar hiperrealista.\n"
            "• Sincronización labial (lip-sync) y gestualidad.\n"
            "• Cumplimiento ético de identidad sintética.",
            "Se empleó en el Nivel 3 de Contaduría Pública para dar vida a 'Valeria Mendoza' (Valeria Mendoza — Contaduría Pública FESNA.mp4), "
            "un avatar digital ejecutivo que presenta un testimonio realista sobre NIIF y Revisoría Fiscal sin clonar ni suplantar a "
            "ninguna persona real (cumpliendo la Regla General #7 del examen)."
        ]
    ]
    add_styled_table(
        doc,
        ["Herramienta de IA", "Funciones Ejecutadas en el Proyecto", "Justificación Técnica y Valor Agregado"],
        ia_rows,
        header_bg="0D3B66"
    )

    add_formatted_heading(doc, "2.1. Detalle de Cómo Interactuaron las 4 Herramientas en Nuestro Flujo de Trabajo", level=2, color_rgb=(21, 135, 119))
    add_body_p(
        doc,
        "1. En Google Gemini analizamos primero los documentos oficiales suministrados (Resoluciones MEN 010895, 010896, 010897 para "
        "Administración; Resoluciones MEN 009955, 009956, 009957 y brochures oficiales para Contaduría Pública). Con base en esa "
        "información verificada, redactamos los guiones técnicos y generamos en Gemini Canvas la Animación 2D Full HD."
    )
    add_body_p(
        doc,
        "2. En CapCut importamos los guiones y secuencias visuales para producir los videos explicativos, el video institucional final "
        "y los Reels promocionales verticales (9:16), añadiendo subtítulos dinámicos resaltados en los colores institucionales de cada "
        "facultad (turquesa en Administración y morado en Contaduría)."
    )
    add_body_p(
        doc,
        "3. En HeyGen configuramos el avatar virtual femenino de perfil corporativo ('Valeria Mendoza'), cargamos el guion testimonial "
        "del Nivel Profesional de Contaduría Pública y generamos la pieza audiovisual con sincronización labial precisa y entonación "
        "profesional colombiana."
    )
    add_body_p(
        doc,
        "4. En Antigravity integramos todos los activos multimedia dentro de la arquitectura web multipágina, refinamos la infografía "
        "institucional mediante un script de Python (Pillow) para que los códigos SNIES y textos se vieran 100 % nítidos, programamos "
        "el motor de Motion Graphics en HTML5 Canvas y ejecutamos scripts de síntesis neural (edge-tts) para producir los cuatro (4) "
        "productos sonoros con voces neurales diferenciadas y calidad de estudio."
    )

    doc.add_page_break()

    # =========================================================================
    # SECCION 3: COMO ELABORAMOS LAS COSAS PASO A PASO Y PROMPTS UTILIZADOS
    # =========================================================================
    add_formatted_heading(
        doc,
        "3. Proceso Detallado de Elaboración y Prompts Principales por Área y Nivel",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "A continuación, se documenta de forma exhaustiva cómo se elaboró cada una de las doce (12) actividades exigidas en el "
        "Examen de Segundo Corte, incluyendo la tabla de verificación normativa previa, los prompts exactos suministrados a las "
        "herramientas de Inteligencia Artificial (Gemini, CapCut, HeyGen y Antigravity), los guiones producidos y el procedimiento "
        "técnico de integración."
    )

    # -------------------------------------------------------------------------
    # 3.1 AREA DE ADMINISTRACION
    # -------------------------------------------------------------------------
    add_formatted_heading(
        doc,
        "3.1. Área de Administración (Paleta Institucional Turquesa: #36B59E / #1FA08B / #158777)",
        level=2,
        color_rgb=(21, 135, 119)
    )

    admin_norm_rows = [
        [
            "Nivel 1: Técnico Profesional",
            "Técnica Profesional en Procesos Administrativos Empresariales",
            "Presencial: 111383\nVirtual: 111384",
            "Res. 010895 del 16/JUN/2022\n(Vigencia 7 años)",
            "3 períodos\n(53 créditos)",
            "Nivel Operativo:\nEjecución documental, archivo, servicio al cliente y apoyo administrativo."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión Administrativa",
            "Presencial: 111385\nVirtual: 111386",
            "Res. 010896 del 16/JUN/2022\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(87 créditos)",
            "Nivel Táctico / Intermedio:\nCoordinación de áreas, control de indicadores y optimización de recursos."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Administración de Empresas",
            "Presencial: 111357\nVirtual: 111750",
            "Res. 010897 del 16/JUN/2022\n(Vigencia 7 años)",
            "+4 períodos / 9 acumulados\n(155 créditos)",
            "Nivel Estratégico / Directivo:\nAlta gerencia, toma de decisiones, planeación global y emprendimiento."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Comunicativo"],
        admin_norm_rows,
        header_bg="158777"
    )

    # Nivel 1 Administracion
    add_formatted_heading(
        doc,
        "A. Nivel 1 — Técnica Profesional en Procesos Administrativos Empresariales",
        level=3,
        color_rgb=(21, 135, 119)
    )

    add_prompt_box(
        doc,
        "Actividad 1.1: Video Explicativo con IA (Archivo: assets/video-tppae.mp4)",
        "Gemini + CapCut IA",
        "Actúa como un director creativo de marketing educativo para la Fundación de Educación Superior Nueva América (FESNA). "
        "Redacta un guion audiovisual explicativo de 45 segundos y su estructura de escenas para CapCut sobre el programa "
        "'Técnica Profesional en Procesos Administrativos Empresariales' (SNIES Presencial 111383, Virtual 111384, Resolución MEN "
        "010895 del 16 de junio de 2022). El enfoque debe ser 100% operativo y práctico: destaca que en solo 3 períodos académicos "
        "(53 créditos) el estudiante domina la gestión documental, atención al cliente, ofimática empresarial y soporte a procesos "
        "internos. Incluye subtítulos dinámicos y llamado a la acción a www.nuevaamerica.edu.co.",
        "Se estructuró el guion en Gemini dividido en 4 bloques (Gancho operativo, Formación práctica en 3 semestres, Respaldo legal "
        "SNIES 111383/111384 y Cierre). Posteriormente, en CapCut se realizó el montaje con secuencias de entorno empresarial moderno, "
        "locución clara y subtítulos automáticos sincronizados a 720p HD.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2: Infografía Institucional con IA (Archivo: assets/infografia-ia-tppae-final.png)",
        "Gemini Imagen + Antigravity (Python Pillow)",
        "Generate a clean, modern corporate infographic illustration for a Colombian university business administration program "
        "('FESNA - Técnica Profesional en Procesos Administrativos Empresariales'). Visual style: flat vector infographic combined "
        "with 3D isometric icons, corporate colors matching FESNA identity: deep navy blue (#0D3B66), vibrant teal/emerald (#00897B), "
        "and warm orange accents (#F36F21) on a clean light background. Show 3 connected operational workflow stages with clear visual "
        "icons: 1. Gestión Documental y Archivo, 2. Flujo de Documentos y Operaciones, 3. Atención al Cliente y Ofimática.",
        "Para garantizar que ningún texto ni código SNIES sufriera distorsiones típicas de los generadores de imagen, aplicamos un "
        "proceso híbrido en Antigravity: generamos la ilustración isométrica base con IA y luego programamos un script en Python "
        "con la librería Pillow (postprocess_infografia.py) que maquetó el encabezado institucional de FESNA, las etiquetas nítidas "
        "de los 3 ejes operativos y el pie de página con los códigos SNIES 111383/111384 y la Resolución 010895 de 2022.",
        accent_hex="1FA08B"
    )

    # Nivel 2 Administracion
    add_formatted_heading(
        doc,
        "B. Nivel 2 — Tecnología en Gestión Administrativa",
        level=3,
        color_rgb=(21, 135, 119)
    )

    add_prompt_box(
        doc,
        "Actividad 2.1: Reel Promocional con IA (Archivo: assets/reel-tga.mp4)",
        "Gemini + CapCut IA (Formato 9:16)",
        "Diseña un guion dinámico para un Reel vertical (9:16) de 30 segundos dirigido a jóvenes y técnicos que buscan ascender "
        "al nivel táctico empresarial con la 'Tecnología en Gestión Administrativa' de FESNA (SNIES Presencial 111385, Virtual 111386, "
        "Resolución MEN 010896 de 2022, 5 semestres acumulados, 87 créditos). Estructura el Reel en: 1) Hook visual en los primeros "
        "3 segundos ('¿Ya eres técnico o quieres coordinar equipos de alto rendimiento?'), 2) Cuerpo sobre supervisión táctica, "
        "indicadores de gestión y optimización de recursos, y 3) CTA invitando a homologar o avanzar por ciclos propedéuticos.",
        "Se produjo el video vertical en CapCut empleando cortes rápidos cada 2.5 segundos, transiciones dinámicas y texto en pantalla "
        "resaltando el paso del nivel operativo al nivel táctico en solo 2 semestres adicionales tras el ciclo técnico.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2: Spot Publicitario con Voz IA (Archivo: assets/spot-tga-voz-ia.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-GonzaloNeural)",
        "Escribe un spot publicitario radial de 30 segundos para la Tecnología en Gestión Administrativa de FESNA. El tono debe ser "
        "ejecutivo, motivador y enfocado en el liderazgo táctico: coordinación de talento humano, control presupuestal e indicadores "
        "de gestión. Incluye los códigos SNIES 111385 (Presencial) y 111386 (Virtual), Resolución MEN 010896 de 2022 y el portal "
        "www.nuevaamerica.edu.co.",
        "Una vez validado el guion, se sintetizó el audio en Antigravity utilizando el motor neuronal de Microsoft Azure (edge-tts) "
        "con la voz masculina colombiana 'es-CO-GonzaloNeural' configurada con ajuste de velocidad (+4%) y entonación cálida para "
        "obtener una locución comercial nítida y libre de artefactos robóticos.",
        accent_hex="1FA08B"
    )

    # Nivel 3 Administracion
    add_formatted_heading(
        doc,
        "C. Nivel 3 — Administración de Empresas (Nivel Profesional Universitario)",
        level=3,
        color_rgb=(21, 135, 119)
    )

    add_prompt_box(
        doc,
        "Actividad 3.1: Video Institucional Generado con IA (Archivo: assets/video-institucional-ae.mp4)",
        "Gemini + CapCut IA",
        "Elabora el guion maestro para el Video Institucional del programa profesional 'Administración de Empresas' de FESNA "
        "(SNIES Presencial 111357, Virtual 111750, Resolución MEN 010897 del 16 de junio de 2022, 9 períodos acumulados, 155 créditos). "
        "El mensaje debe proyectar visión estratégica, alta gerencia, dirección organizacional, innovación corporativa y creación de "
        "empresa, mostrando cómo el estudiante culmina su tercer ciclo propedéutico obteniendo tres títulos en su trayectoria.",
        "El video final (fesna_video_institucional_final.mp4 integrado como assets/video-institucional-ae.mp4) combina narrativa "
        "corporativa de alto impacto visual en CapCut con gráficas de crecimiento empresarial, destacando la formación de líderes "
        "estratégicos capaces de transformar organizaciones en Colombia y el mundo.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2: Motion Graphics Inteligente en Tiempo Real (Motor Canvas en app.js)",
        "Antigravity (HTML5 Canvas API a 60 FPS)",
        "Programa en JavaScript nativo un motor interactivo de Motion Graphics vectorial en HTML5 Canvas a 60 fotogramas por segundo "
        "para el Nivel Profesional de Administración de Empresas de FESNA. La animación debe dividirse en 4 escenas sincronizadas con "
        "controles de reproducción, barra de progreso y selector directo de escenas: Escena 1 (Ruta Propedéutica de 3 Títulos), "
        "Escena 2 (Pilares Estratégicos y KPIs Gerenciales), Escena 3 (Modalidades Presencial SNIES 111357 y Virtual SNIES 111750) "
        "y Escena 4 (Respaldo Legal Res. 010897 de 2022).",
        "Desarrollado íntegramente mediante código en Antigravity dentro de app.js. Renderiza partículas dinámicas, nodos conectados, "
        "barras de progreso animadas con funciones de suavizado (easeOutCubic) y tarjetas vectoriales que responden en tiempo real "
        "a la interacción del usuario.",
        accent_hex="1FA08B"
    )

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # 3.2 AREA DE CONTADURIA PUBLICA
    # -------------------------------------------------------------------------
    add_formatted_heading(
        doc,
        "3.2. Área de Contaduría Pública (Paleta Institucional Morada: #AA38B9 / #921AA3 / #74187E)",
        level=2,
        color_rgb=(146, 26, 163)
    )

    conta_norm_rows = [
        [
            "Nivel 1: Técnico Profesional",
            "Técnica Profesional en Procesos Contables",
            "Presencial: 111389\nVirtual: 111390",
            "Res. 009955 del 03/JUN/2022\n(Vigencia 7 años)",
            "3 períodos\n(51 P / 52 V créditos)",
            "Nivel Operativo Contable:\nRegistro de transacciones, causación, facturación electrónica, nómina y soportes."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión Contable y Financiera",
            "Presencial: 111391\nVirtual: 111392",
            "Res. 009956 del 03/JUN/2022\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(86 P / 87 V créditos)",
            "Nivel Táctico y Analítico:\nPresupuestos, costos, estados financieros intermedios, tesorería e impuestos."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Contaduría Pública",
            "Presencial: 111387\nVirtual: 111388",
            "Res. 009957 del 03/JUN/2022\n(Vigencia 7 años)",
            "+4 períodos / 9 acumulados\n(155 P / 159 V créditos)",
            "Nivel Estratégico y Fe Pública:\nAuditoría, Revisoría Fiscal, Estándares Internacionales NIIF/NIA y Gerencia Tributaria."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Comunicativo"],
        conta_norm_rows,
        header_bg="74187E"
    )

    # Nivel 1 Contaduria
    add_formatted_heading(
        doc,
        "A. Nivel 1 — Técnica Profesional en Procesos Contables",
        level=3,
        color_rgb=(146, 26, 163)
    )

    add_prompt_box(
        doc,
        "Actividad 1.1: Serie de Reels con Guion IA (Archivo: assets/reel-tppc-contaduria.mp4)",
        "Gemini + CapCut IA (Subtítulos Morados)",
        "Actúa como estratega de contenidos digitales para FESNA. Crea una serie de 3 guiones de Reels verticales (9:16) para el "
        "programa 'Técnica Profesional en Procesos Contables' (SNIES Presencial 111389, Virtual 111390, Resolución MEN 009955 del "
        "3 de junio de 2022, 3 períodos académicos, 51 créditos presencial / 52 virtual): "
        "Reel 1 (Mito vs. Realidad): Desmiente que se necesiten 5 años para empezar a trabajar en contabilidad. "
        "Reel 2 (Perfil Laboral): Muestra los cargos reales (Auxiliar Contable, Asistente de Facturación Electrónica y Nómina). "
        "Reel 3 (Ventaja Propedéutica): Explica cómo este primer título se homologa directamente hacia la Tecnología y la Contaduría Pública.",
        "Con el guion estructurado en Gemini, se realizó la producción audiovisual en CapCut (fesna_reel_subtitulos_morados.mp4), "
        "incorporando subtítulos dinámicos resaltados en color morado institucional (#AA38B9), ritmo ágil para TikTok/Instagram Reels "
        "y tarjetas visuales con los códigos SNIES verificados.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2: Cuña Radial Generada con IA (Archivo: assets/cuna-radial-tppc.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-SalomeNeural)",
        "Redacta una cuña radial publicitaria de 30 segundos para la Técnica Profesional en Procesos Contables de FESNA. Debe tener "
        "un tono joven, ágil y convincente, destacando el dominio de software contable, facturación electrónica, nómina y soportes "
        "tributarios en solo 3 semestres. Incluye los códigos SNIES 111389 y 111390 y la Resolución MEN 009955 de 2022.",
        "Para diferenciar la identidad sonora respecto al área de Administración, en Antigravity empleamos la voz neuronal femenina "
        "colombiana 'es-CO-SalomeNeural' con ritmo dinámico (+6% en velocidad y +3Hz en tono), logrando una cuña radial brillante, "
        "natural y de alta recordación.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    # Nivel 2 Contaduria
    add_formatted_heading(
        doc,
        "B. Nivel 2 — Tecnología en Gestión Contable y Financiera",
        level=3,
        color_rgb=(146, 26, 163)
    )

    add_prompt_box(
        doc,
        "Actividad 2.1: Podcast 'Conoce FESNA' con IA a Dos Voces (Archivo: assets/podcast-conoce-fesna-tgcf.mp3)",
        "Gemini + Antigravity (edge-tts: es-MX-DaliaNeural & es-VE-SebastianNeural)",
        "Escribe el guion de un episodio de podcast conversacional titulado 'Conoce FESNA' (duración aproximada 1 minuto y 15 segundos) "
        "entre dos anfitriones: Valeria (conductora principal, cálida y analítica) y Mateo (co-conductor, enfocado en empleabilidad y "
        "finanzas). El episodio debe explicar cómo el estudiante avanza al segundo ciclo propedéutico: 'Tecnología en Gestión Contable "
        "y Financiera' (SNIES Presencial 111391, Virtual 111392, Resolución MEN 009956 del 3 de junio de 2022, 5 semestres acumulados), "
        "destacando competencias en análisis financiero, control presupuestal, estructura de costos y gestión tributaria.",
        "En Antigravity programamos un generador multipista en Python (generate_clean_voices.py) que sintetizó por separado las "
        "intervenciones de Valeria (voz neural 'es-MX-DaliaNeural') y de Mateo (voz neural 'es-VE-SebastianNeural') y luego las "
        "ensambló con pausas acústicas naturales de 250 ms entre turnos de habla. El resultado es un diálogo realista entre dos "
        "locutores distintos y perfectamente nítidos.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2: Animación 2D Asistida por IA (Archivo: assets/animacion2d-tgcf-contaduria.mp4)",
        "Google Gemini con Canvas (Exportación Video Full HD 1920x1080)",
        "Actúa como un experto en Motion Graphics 2D y desarrollador creativo en HTML5 Canvas. Crea en Gemini Canvas una aplicación "
        "autocontenida en un solo archivo HTML que reproduzca una Animación 2D promocional e informativa en resolución Full HD "
        "(1920x1080, 60 FPS) sobre el programa 'Tecnología en Gestión Contable y Financiera' de FESNA (Nivel 2 por Ciclos Propedéuticos). "
        "Usa la paleta morada oficial (#74187E, #921AA3, #AA38B9) con acentos dorados (#F59E0B). Estructura 5 escenas de 6 segundos "
        "(30s en total): Escena 1 (Intro Institucional FESNA), Escena 2 (Progresión Propedéutica del Nivel 1 al Nivel 2 en 5 semestres), "
        "Escena 3 (Competencias Tácticas: Costos, Presupuestos, Tesorería e Impuestos con gráficos animados), Escena 4 (Modalidades "
        "Presencial SNIES 111391 y Virtual SNIES 111392) y Escena 5 (Cierre con Res. MEN 009956 de 2022). Incluye un botón 'Descargar "
        "Video' usando MediaRecorder API a 8 Mbps.",
        "Se ejecutó este prompt especializado en Google Gemini activando la herramienta Canvas. El lienzo renderizó las 5 escenas "
        "vectoriales con barras financieras animadas, tarjetas isométricas y transiciones suaves, permitiendo grabar y descargar "
        "directamente el archivo de video en alta definición (FESNA_Tecnologia_Gestion_Contable_Financiera_FullHD.mp4).",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    # Nivel 3 Contaduria
    add_formatted_heading(
        doc,
        "C. Nivel 3 — Contaduría Pública (Nivel Profesional Universitario)",
        level=3,
        color_rgb=(146, 26, 163)
    )

    add_prompt_box(
        doc,
        "Actividad 3.1: Testimonio Recreado con Avatar IA (Archivo: assets/testimonio-avatar-cp.mp4)",
        "HeyGen Avatar IA + Gemini",
        "Configuración en HeyGen: Seleccionar avatar femenino corporativo latinoamericano ('Valeria Mendoza', vestimenta ejecutiva "
        "formal, encuadre medio de estudio moderno). "
        "Guion y Prompt de voz suministrado al avatar: 'Hola, soy Valeria Mendoza, y hoy quiero contarte cómo la Contaduría Pública "
        "en la Fundación de Educación Superior Nueva América, FESNA, transforma tu visión profesional. Gracias a su modelo por ciclos "
        "propedéuticos, avancé desde el nivel técnico y tecnológico hasta culminar mi título profesional en 9 períodos académicos. "
        "Aquí dominamos las Normas Internacionales de Información Financiera (NIIF), la auditoría integral, la revisoría fiscal y la "
        "gerencia tributaria estratégica, con la responsabilidad ética de dar fe pública. Estudia en modalidad presencial con código "
        "SNIES 111387 o virtual con SNIES 111388, respaldados por la Resolución del Ministerio de Educación 009957 de 2022. "
        "¡Construye tu futuro directivo en FESNA!'",
        "Generado en HeyGen (archivo 'Valeria Mendoza — Contaduría Pública FESNA.mp4'). El motor de IA de HeyGen sincronizó los "
        "movimientos labiales (lip-sync), parpadeos y microexpresiones faciales con la locución testimonial. En la tarjeta del sitio "
        "web se incluyó la nota ética explícita indicando que se trata de una recreación con avatar sintético de IA, cumpliendo la "
        "Regla General #7 del examen.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2: Podcast Institucional Asistido por IA (Archivo: assets/podcast-institucional-cp.mp3)",
        "Gemini + Antigravity (edge-tts: es-MX-JorgeNeural & es-CL-CatalinaNeural)",
        "Redacta un guion de Podcast Institucional de corte directivo y académico (duración 1 minuto y 20 segundos) para el programa "
        "profesional de Contaduría Pública de FESNA (SNIES Presencial 111387, Virtual 111388, Resolución MEN 009957 del 3 de junio de "
        "2022, 9 períodos acumulados, 155 créditos presencial / 159 virtual). Participan dos voces de perfil decano/consultor: el "
        "Dr. Alejandro Vargas y la Dra. Carolina Méndez. Deben dialogar sobre la importancia estratégica del Contador Público de FESNA "
        "en la alta dirección, la aplicación de estándares internacionales NIIF/NIA, la Revisoría Fiscal, la ética de la fe pública y "
        "la ventaja de obtener tres títulos universitarios a lo largo de la carrera.",
        "Para distinguir este podcast directivo del podcast juvenil del Nivel 2, en Antigravity seleccionamos dos voces neurales con "
        "timbre maduro y autoritativo: 'es-MX-JorgeNeural' (Dr. Alejandro Vargas) y 'es-CL-CatalinaNeural' (Dra. Carolina Méndez), "
        "ensamblando sus intervenciones con calidad de estudio.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    # -------------------------------------------------------------------------
    # 3.3 DESAFIOS ENCONTRADOS Y SOLUCIONES
    # -------------------------------------------------------------------------
    add_formatted_heading(
        doc,
        "3.3. Desafíos Técnicos Encontrados Durante la Elaboración y Soluciones Implementadas",
        level=2,
        color_rgb=(13, 59, 102)
    )

    challenges_rows = [
        [
            "1. Legibilidad de textos y códigos SNIES en infografías generadas por IA",
            "Los modelos de difusión de imagen suelen alterar números largos (como SNIES 111383 o Res. 010895) o deformar tipografías pequeñas.",
            "Se implementó un flujo híbrido en Antigravity: la IA generó la ilustración vectorial/isométrica limpia y mediante un script en Python (Pillow) se superpusieron el encabezado institucional y el pie normativo con tipografía 100 % nítida."
        ],
        [
            "2. Naturalidad y diferenciación de voces en Cuñas y Podcasts",
            "Las voces TTS locales del navegador suenan robóticas y no permiten grabar un diálogo fluido entre dos interlocutores distintos.",
            "Se integró la librería 'edge-tts' en Python conectada a las voces neurales de Microsoft Azure, asignando 6 timbres distintos (Salomé, Gonzalo, Dalia, Sebastián, Jorge y Catalina) y uniendo las pistas de diálogo con pausas naturales."
        ],
        [
            "3. Exportación de la Animación 2D en resolución Full HD descargable",
            "Se requería una animación 2D vectorial fluida sobre la Tecnología en Gestión Contable y Financiera que pudiera descargarse como archivo MP4/WebM.",
            "Se diseñó un prompt de ingeniería avanzada para Google Gemini con Canvas a 1920x1080 (60 FPS) incorporando el API MediaRecorder a 8 Mbps para exportar el video directamente en alta definición."
        ],
        [
            "4. Recreación del testimonio con Avatar IA y restricciones de exportación",
            "Las plataformas de avatares presentan límites de exportación en cuentas gratuitas y exigen cuidado ético para no suplantar personas reales.",
            "Se estructuró el guion exacto de 45 segundos para el avatar ficticio 'Valeria Mendoza' en HeyGen y se integró el video MP4 resultante junto con su cláusula de transparencia ética."
        ],
        [
            "5. Coherencia cromática entre 4 facultades en una misma web",
            "Cada área de FESNA posee un color institucional propio (Turquesa, Morado, Verde y Rojo), lo que podía fragmentar la identidad visual.",
            "Se creó un sistema de variables CSS dinámicas en styles.css y un menú lateral desplegable (drawer) que adapta los acentos cromáticos según la página activa sin perder la unidad institucional de FESNA."
        ]
    ]
    add_styled_table(
        doc,
        ["Desafío Identificado", "Causa Técnica", "Solución Implementada por el Estudiante con IA"],
        challenges_rows,
        header_bg="0D3B66"
    )

    doc.add_page_break()

    # =========================================================================
    # SECCION 4: USO RESPONSABLE DE RECURSOS Y DERECHOS DE AUTOR
    # =========================================================================
    add_formatted_heading(
        doc,
        "4. Uso Responsable de Recursos Visuales, Sonoros, Derechos de Autor y Ética en IA",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "En cumplimiento estricto de las ocho (8) Reglas Generales del Examen de Segundo Corte y de los principios de integridad "
        "académica de la Fundación de Educación Superior Nueva América (FESNA), todos los activos audiovisuales, gráficos, sonoros "
        "y de código que conforman este portafolio responden a criterios verificables de propiedad intelectual y uso ético de la "
        "Inteligencia Artificial:"
    )

    ethics_rows = [
        [
            "Datos Académicos y Normativos (Reglas #1, #2 y #3)",
            "Resoluciones MEN 010895, 010896, 010897, 009955, 009956 y 009957 de junio de 2022; Portal oficial www.nuevaamerica.edu.co.",
            "Uso institucional académico con fidelidad del 100 %. No se inventaron costos, convenios ni duraciones fuera de los actos administrativos oficiales."
        ],
        [
            "Identidad Sintética y Avatar IA (Regla #7)",
            "HeyGen AI Video Generator (Personaje ficticio: 'Valeria Mendoza').",
            "Cumplimiento ético total: no se clonó la voz ni el rostro de ningún directivo, docente o estudiante real sin autorización. Se declara explícitamente su naturaleza sintética."
        ],
        [
            "Producción Sonora y Locuciones Neurales (4 Audios MP3)",
            "Motor Microsoft Azure Neural TTS vía librería abierta edge-tts (Python) y guiones propios.",
            "Voces sintéticas generadas a partir de guiones originales redactados y verificados por David Yused Pulido Pardo, libres de reclamaciones de copyright musical."
        ],
        [
            "Videos, Reels y Animaciones 2D (6 Archivos MP4 + 1 Canvas Live)",
            "CapCut, Google Gemini Canvas (HTML5 Canvas API) y Antigravity.",
            "Creación original para fines académicos del curso. Subtítulos, diagramación y secuencias vectoriales de autoría del estudiante."
        ],
        [
            "Infografía Institucional Nivel 1 Administración",
            "Modelo generativo de imagen + postprocesamiento programático con Python Pillow.",
            "Obra derivada de carácter académico con maquetación tipográfica propia para garantizar precisión informativa."
        ]
    ]
    add_styled_table(
        doc,
        ["Categoría del Recurso", "Fuente / Tecnología de Generación", "Licencia, Autoría y Cumplimiento Ético"],
        ethics_rows,
        header_bg="0D3B66"
    )

    # =========================================================================
    # SECCION 5: SUSTENTACION TEORICA (PUNTO 4 DEL EXAMEN)
    # =========================================================================
    add_formatted_heading(
        doc,
        "5. Sustentación Teórica del Proyecto (Punto 4: Fundamentación Académica)",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "El diseño conceptual, comunicativo y tecnológico del sitio web para la Fundación de Educación Superior Nueva América (FESNA) "
        "no se limitó a una ejecución estética o instrumental de herramientas de Inteligencia Artificial; por el contrario, se "
        "fundamentó en cinco (5) pilares teóricos y normativos que articulan las ciencias administrativas, la disciplina contable, "
        "la pedagogía por ciclos propedéuticos, la comunicación estratégica transmedia y la ingeniería de sistemas aplicada a la IA "
        "generativa."
    )

    add_formatted_heading(
        doc,
        "5.1. Jerarquía Organizacional y Niveles de la Administración (Operativo, Táctico y Estratégico)",
        level=2,
        color_rgb=(21, 135, 119)
    )
    add_body_p(
        doc,
        "Desde la teoría neoclásica de la administración expuesta por Chiavenato (2019) y Robbins y Coulter (2018), toda organización "
        "contemporánea estructura su proceso administrativo (planeación, organización, dirección y control) en tres niveles "
        "jerárquicos claramente diferenciados: el nivel operativo o técnico (enfocado en la ejecución estandarizada de tareas y "
        "procedimientos cotidianos), el nivel táctico o intermedio (encargado de la coordinación departamental, la asignación de "
        "recursos y el seguimiento de indicadores) y el nivel estratégico o institucional (orientado a la visión de largo plazo, la "
        "toma de decisiones globales y la relación con el entorno competitivo). "
        "Esta arquitectura teórica fue el eje rector de nuestra campaña para el Área de Administración en FESNA: las piezas del Nivel 1 "
        "(Técnica Profesional en Procesos Administrativos Empresariales, Res. 010895) comunican precisión operativa y gestión "
        "documental; las piezas del Nivel 2 (Tecnología en Gestión Administrativa, Res. 010896) enfatizan la coordinación táctica y el "
        "control de gestión; y los productos del Nivel 3 (Administración de Empresas, Res. 010897) proyectan liderazgo directivo, "
        "innovación y gerencia estratégica."
    )

    add_formatted_heading(
        doc,
        "5.2. El Modelo de Formación por Ciclos Propedéuticos en la Educación Superior Colombiana",
        level=2,
        color_rgb=(21, 135, 119)
    )
    add_body_p(
        doc,
        "De acuerdo con la Ley 749 de 2002 y el Decreto Único Reglamentario del Sector Educación 1075 de 2015 expedido por el "
        "Ministerio de Educación Nacional (MEN), la formación por ciclos propedéuticos organiza la educación superior en tres etapas "
        "secuenciales, complementarias e interdependientes (técnica profesional, tecnológica y profesional universitaria). El componente "
        "propedéutico constituye la fase de profundización que prepara al estudiante para transitar al siguiente nivel sin perder "
        "el tiempo ni los créditos cursados, otorgándole además titulaciones intermedias que facilitan su inserción laboral temprana. "
        "Tanto en la estructura de navegación de nuestro sitio web como en los guiones de los Reels, podcasts y animaciones 2D, este "
        "concepto se tradujo visual y narrativamente como una 'escalera de valor acumulativa': 3 períodos para el primer título "
        "técnico, 5 períodos acumulados para el título tecnológico y 9 períodos acumulados para el título profesional universitario."
    )

    add_formatted_heading(
        doc,
        "5.3. Evolución de la Ciencia Contable: Del Registro Transaccional a las NIIF y la Fe Pública",
        level=2,
        color_rgb=(146, 26, 163)
    )
    add_body_p(
        doc,
        "En el Área de Contaduría Pública, la campaña se sustentó en la distinción epistemológica y legal entre la teneduría de libros, "
        "la contabilidad de gestión y la contaduría pública como profesión liberal investida de fe pública. Conforme a la Ley 43 de "
        "1990 (Estatuto de la Profesión de Contador Público en Colombia) y la Ley 1314 de 2009 (que regula la convergencia hacia las "
        "Normas Internacionales de Información Financiera — NIIF/IFRS y las Normas Internacionales de Aseguramiento de la Información "
        "— NAI), el ejercicio contable abarca desde la captura fidedigna del hecho económico hasta el dictamen independiente de "
        "estados financieros (Horngren, Sundem & Elliott, 2010). "
        "Por ello, en el Nivel 1 (Técnica Profesional en Procesos Contables, Res. 009955) los Reels y la cuña radial se enfocan en "
        "la causación, la facturación electrónica y los soportes contables; en el Nivel 2 (Tecnología en Gestión Contable y Financiera, "
        "Res. 009956) el podcast 'Conoce FESNA' y la animación 2D abordan la contabilidad administrativa, los presupuestos y el "
        "análisis financiero; mientras que en el Nivel 3 (Contaduría Pública, Res. 009957) el testimonio con avatar IA y el podcast "
        "institucional destacan el dominio de las NIIF, la Revisoría Fiscal, la auditoría y la responsabilidad ética de dar fe pública."
    )

    add_formatted_heading(
        doc,
        "5.4. Comunicación Institucional Estratégica, Marketing Educativo y Narrativa Transmedia",
        level=2,
        color_rgb=(13, 59, 102)
    )
    add_body_p(
        doc,
        "Siguiendo los postulados de Kotler y Keller (2016) sobre dirección de marketing y de Capriotti (2013) sobre identidad e "
        "imagen corporativa, la comunicación de una institución de educación superior exige coherencia simbólica (colores, tono de "
        "voz y promesa de valor) combinada con segmentación de formatos según el público objetivo. Asimismo, bajo el paradigma de la "
        "narrativa transmedia de Scolari (2013), un mismo universo institucional se despliega a través de múltiples medios donde cada "
        "formato aporta una experiencia específica: el formato vertical 9:16 (Reels en CapCut) captura la atención inmediata de "
        "audiencias jóvenes mediante micro-narrativas; la infografía y el Motion Graphics sintetizan estructuras curriculares "
        "complejas mediante visualización de datos; el formato sonoro (cuñas y podcasts) genera cercanía cognitiva mediante el "
        "diálogo; y el video institucional y el avatar hiperrealista consolidan la credibilidad y el prestigio académico."
    )

    add_formatted_heading(
        doc,
        "5.5. Inteligencia Artificial Generativa, Ingeniería de Prompts y Supervisión Humana (Human-in-the-Loop)",
        level=2,
        color_rgb=(13, 59, 102)
    )
    add_body_p(
        doc,
        "Desde la perspectiva de la Ingeniería de Sistemas y la Inteligencia Artificial moderna (Russell & Norvig, 2021; Mollick, 2024), "
        "los modelos generativos multimodales (LLMs, síntesis neural de voz y motores de difusión de video) operan mediante "
        "distribuciones probabilísticas condicionadas por el contexto de entrada (prompt). Sin embargo, como advierte la UNESCO (2023) "
        "en sus directrices sobre el uso ético de la IA en la educación superior, los sistemas generativos son susceptibles a "
        "'alucinaciones' (invención de datos no verificados) si no se someten a un protocolo de supervisión humana activa "
        "(Human-in-the-Loop). En este proyecto, la ingeniería de prompts se diseñó bajo restricción de contexto estricto "
        "(Grounding Documental): cada prompt inyectó explícitamente los números de Resolución MEN, los códigos SNIES y el número "
        "exacto de créditos extraídos de los documentos oficiales de FESNA, garantizando cero alucinaciones normativas y un uso "
        "transparente, ético y pedagógicamente riguroso de la tecnología."
    )

    doc.add_page_break()

    # =========================================================================
    # SECCION 6: REFERENCIAS BIBLIOGRAFICAS (NORMAS APA 7.a EDICION)
    # =========================================================================
    add_formatted_heading(
        doc,
        "6. Referencias Bibliográficas (Normas APA 7.ª Edición)",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_body_p(
        doc,
        "A continuación, se presenta el listado formal de referencias bibliográficas, normativas, institucionales y tecnológicas "
        "consultadas y citadas para la fundamentación y elaboración del proyecto, organizadas alfabéticamente con sangría francesa "
        "conforme a los lineamientos de la séptima edición de las normas de la American Psychological Association (APA):"
    )

    apa_refs = [
        "American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000",
        "Bytedance Ltd. (2026). CapCut: Plataforma de edición de video y subtitulado asistido por inteligencia artificial [Software]. https://www.capcut.com/",
        "Capriotti, P. (2013). Planificación estratégica de la imagen corporativa (4.ª ed.). Instituto de Investigación en Relaciones Públicas (IIRP).",
        "Chiavenato, I. (2019). Introducción a la teoría general de la administración (10.ª ed.). McGraw-Hill Interamericana.",
        "Congreso de la República de Colombia. (1990, 13 de diciembre). Ley 43 de 1990. Por la cual se adiciona la Ley 145 de 1960, reglamentaria de la profesión de Contador Público y se dictan otras disposiciones. Diario Oficial n.º 39.602.",
        "Congreso de la República de Colombia. (2002, 19 de julio). Ley 749 de 2002. Por la cual se organiza el servicio público de la educación superior en las modalidades de formación técnica profesional y tecnológica. Diario Oficial n.º 44.872.",
        "Congreso de la República de Colombia. (2009, 13 de julio). Ley 1314 de 2009. Por la cual se regulan los principios y normas de contabilidad e información financiera y de aseguramiento de información aceptados en Colombia. Diario Oficial n.º 47.409.",
        "Fundación de Educación Superior Nueva América [FESNA]. (2026). Oferta académica por ciclos propedéuticos: Áreas de Administración, Contaduría Pública, Ingeniería de Sistemas y Marketing y Publicidad. https://www.nuevaamerica.edu.co/",
        "Google DeepMind. (2026). Google Gemini & Gemini Canvas: Modelo multimodal de lenguaje y entorno de programación interactiva [Software de inteligencia artificial]. https://gemini.google.com/",
        "Google DeepMind. (2026). Antigravity: Agente de ingeniería de software y desarrollo asistido por inteligencia artificial [Software].",
        "HeyGen Inc. (2026). HeyGen AI Video Generator: Plataforma de generación de video con avatares digitales e inteligencia artificial [Software]. https://www.heygen.com/",
        "Horngren, C. T., Sundem, G. L., & Elliott, J. A. (2010). Introducción a la contabilidad financiera (9.ª ed.). Pearson Educación.",
        "Kotler, P., & Keller, K. L. (2016). Dirección de marketing (15.ª ed.). Pearson Educación.",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2015, 26 de mayo). Decreto 1075 de 2015. Por medio del cual se expide el Decreto Único Reglamentario del Sector Educación.",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 3 de junio). Resolución n.º 009955 de 2022. Por medio de la cual se otorga el registro calificado al programa de Técnica Profesional en Procesos Contables de la Fundación de Educación Superior Nueva América (FESNA) en modalidades presencial (SNIES 111389) y virtual (SNIES 111390).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 3 de junio). Resolución n.º 009956 de 2022. Por medio de la cual se otorga el registro calificado al programa de Tecnología en Gestión Contable y Financiera de la Fundación de Educación Superior Nueva América (FESNA) en modalidades presencial (SNIES 111391) y virtual (SNIES 111392).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 3 de junio). Resolución n.º 009957 de 2022. Por medio de la cual se otorga el registro calificado al programa de Contaduría Pública de la Fundación de Educación Superior Nueva América (FESNA) en modalidades presencial (SNIES 111387) y virtual (SNIES 111388).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 16 de junio). Resoluciones n.º 010895, 010896 y 010897 de 2022. Por medio de las cuales se otorgan los registros calificados a los programas de Técnica Profesional en Procesos Administrativos Empresariales (SNIES 111383/111384), Tecnología en Gestión Administrativa (SNIES 111385/111386) y Administración de Empresas (SNIES 111357/111750) de la Fundación de Educación Superior Nueva América (FESNA).",
        "Mollick, E. (2024). Co-Intelligence: Living and working with AI. Portfolio / Penguin Random House.",
        "Robbins, S. P., & Coulter, M. (2018). Administración (13.ª ed.). Pearson Educación.",
        "Russell, S., & Norvig, P. (2021). Inteligencia artificial: Un enfoque moderno (4.ª ed.). Pearson Educación.",
        "Scolari, C. A. (2013). Narrativas transmedia: Cuando todos los medios cuentan. Deusto.",
        "UNESCO. (2023). Guía para el uso de IA generativa en educación e investigación. Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura. https://unesdoc.unesco.org/"
    ]

    for ref in apa_refs:
        add_apa_reference(doc, ref)

    # Guardar en la carpeta del proyecto y en Downloads
    out_project = r"C:\Users\david\.gemini\antigravity\scratch\fesna-portafolio-ia\DOCUMENTACION_SUSTENTACION_CAMPANA_FESNA_DAVID_PULIDO.docx"
    out_downloads = r"C:\Users\david\Downloads\DOCUMENTACION_SUSTENTACION_CAMPANA_FESNA_DAVID_PULIDO.docx"

    doc.save(out_project)
    shutil.copy2(out_project, out_downloads)
    print(f"Documento generado exitosamente en:\n1) {out_project}\n2) {out_downloads}")


if __name__ == "__main__":
    build_document()
