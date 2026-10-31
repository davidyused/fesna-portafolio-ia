# -*- coding: utf-8 -*-
"""
Script generador del documento Word (.docx) para el EXAMEN FINAL - FESNA.
Cubre las 4 Areas Profesionales por Ciclos Propedeuticos (24 Actividades con IA):
1. Administracion de Empresas
2. Contaduria Publica
3. Ingenieria de Sistemas
4. Marketing y Publicidad
Estudiante: David Yused Pulido Pardo
Programa: Ingenieria de Sistemas - 10. Semestre
Docente: Fredy Osbaldo Lemus Solano
"""

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
    if accent_hex == "921AA3":
        r_badge.font.color.rgb = RGBColor(146, 26, 163)
    elif accent_hex == "1A7C3B":
        r_badge.font.color.rgb = RGBColor(20, 108, 49)
    elif accent_hex == "D43B27":
        r_badge.font.color.rgb = RGBColor(179, 35, 25)
    else:
        r_badge.font.color.rgb = RGBColor(21, 135, 119)

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
        rn_lbl = p_notes.add_run("Elaboración técnica y resultado integrado: ")
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
    r_b = p_badge.add_run("FUNDACIÓN DE EDUCACIÓN SUPERIOR NUEVA AMÉRICA — FESNA\nEXAMEN FINAL — PORTAFOLIO DIGITAL Y CAMPAÑA PUBLICITARIA MULTIMODAL CON IA")
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
        "(HeyGen, CapCut, Gemini, Gemini Canvas y Antigravity) y Sustentación Teórica de la Campaña "
        "Institucional Multipágina para FESNA"
    )
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(17.5)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(13, 59, 102)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(28)
    r_sub = p_sub.add_run(
        "Cuatro Áreas Desarrolladas por Ciclos Propedéuticos (24 Actividades con IA):\n"
        "Administración de Empresas • Contaduría Pública • Ingeniería de Sistemas • Marketing y Publicidad\n"
        "(Sustentación Teórica, Metodología de Elaboración, Ética Algorítmica y Referencias en Normas APA 7.ª Edición)"
    )
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(90, 100, 115)

    cover_rows = [
        ["Estudiante / Autor:", "David Yused Pulido Pardo"],
        ["Programa Académico:", "Ingeniería de Sistemas — 10.º Semestre"],
        ["Docente Titular:", "Fredy Osbaldo Lemus Solano"],
        ["Institución:", "Fundación de Educación Superior Nueva América (FESNA) — SNIES 4719 — Vigilada MinEducación"],
        ["Enlace Web Público:", "https://davidyused.github.io/fesna-portafolio-ia/"],
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
        "El presente documento constituye la memoria técnica, metodológica y teórica integral del Examen Final para el portal "
        "web interactivo y la campaña publicitaria transmedia desarrollada para la Fundación de Educación Superior Nueva América "
        "(FESNA), publicada en línea en https://davidyused.github.io/fesna-portafolio-ia/. El propósito central del proyecto "
        "consistió en diseñar, producir, programar y documentar veinticuatro (24) productos comunicativos, analíticos y tecnológicos "
        "asistidos por Inteligencia Artificial —distribuidos en las cuatro (4) áreas profesionales por ciclos propedéuticos de la "
        "institución: Administración de Empresas, Contaduría Pública, Ingeniería de Sistemas y Marketing y Publicidad—, "
        "respetando el 100 % de fidelidad frente a los códigos SNIES y las Resoluciones de Registro Calificado otorgadas por el "
        "Ministerio de Educación Nacional (MEN)."
    )

    add_formatted_heading(doc, "1.1. Estructura Multipágina del Sitio Web Publicado", level=2, color_rgb=(21, 135, 119))
    add_body_p(
        doc,
        "El sitio web fue diseñado bajo una arquitectura multipágina limpia y responsiva, interconectada mediante una barra de "
        "navegación superior y un menú lateral desplegable a la izquierda (drawer menu) que conserva la identidad cromática "
        "oficial de cada facultad:"
    )

    add_bullet_p(
        doc,
        "1. Página Principal Institucional (index.html): ",
        "Inicia con la Sección 1 obligatoria de Introducción y Presentación Personal del estudiante (David Yused Pulido Pardo, "
        "Ingeniería de Sistemas, 10.º semestre, objetivos de aprendizaje, propósito del sitio web y resumen del recorrido del curso), "
        "seguida de la reseña histórica y jurídica de FESNA (https://www.nuevaamerica.edu.co/), el directorio interactivo de los "
        "12 programas por ciclos propedéuticos y el botón de descarga directa del presente documento Word."
    )
    add_bullet_p(
        doc,
        "2. Área de Administración (administracion.html — Paleta Turquesa #36B59E / #1FA08B / #158777): ",
        "Consolida las 6 actividades de IA: Técnica Profesional en Procesos Administrativos Empresariales (Video explicativo IA + "
        "Infografía institucional IA), Tecnología en Gestión Administrativa (Reel promocional IA + Spot publicitario con voz IA) y "
        "Administración de Empresas (Video institucional IA + Motion Graphics inteligente a 60 FPS en HTML5 Canvas)."
    )
    add_bullet_p(
        doc,
        "3. Área de Contaduría Pública (contaduria.html — Paleta Morada #AA38B9 / #921AA3 / #74187E): ",
        "Consolida las 6 actividades de IA: Técnica Profesional en Procesos Contables (Serie de Reels con subtítulos morados + "
        "Cuña radial IA), Tecnología en Gestión Contable y Financiera (Podcast 'Conoce FESNA' a dos voces + Animación 2D Full HD "
        "generada en Gemini Canvas) y Contaduría Pública (Testimonio recreado con Avatar IA Valeria Mendoza en HeyGen + Podcast institucional)."
    )
    add_bullet_p(
        doc,
        "4. Área de Ingeniería de Sistemas (sistemas.html — Paleta Verde Esmeralda #1A7C3B / #146C31 / #0D5625): ",
        "Consolida las 6 actividades de IA: Técnica Profesional en Procesos de Programación de Software (Reel 9:16 sobre fundamentos "
        "de programación + Infografía interactiva con simulador de algoritmos en vivo), Tecnología en Gestión de Software y Sistemas "
        "(Podcast técnico asistido por IA sobre SDLC y metodologías ágiles + Video explicativo Full HD sobre arquitectura y DevOps) "
        "e Ingeniería de Sistemas (Proyecto de solución tecnológica interactivo en vivo 'FESNA AI CodeGuard v2.4' para auditoría "
        "de ciberseguridad OWASP Top 10 + Podcast de análisis prospectivo sobre IA e ingeniería de sistemas)."
    )
    add_bullet_p(
        doc,
        "5. Área de Marketing y Publicidad (marketing.html — Paleta Roja / Vinotinto #D43B27 / #B32319 / #7B1F17): ",
        "Consolida las 6 actividades de IA: Técnica Profesional en Procesos de Comercialización y Comunicación Publicitaria "
        "(Galería de 2 piezas gráficas comerciales generadas con IA + Simulador en vivo de atención al cliente mediante Chatbot "
        "conversacional entrenado con IA), Tecnología en Gestión Comercial y Publicidad (Creación de Buyer Persona 'Camila Rojas' "
        "y matriz interactiva de copys AIDA, PAS y Storytelling + Simulador y auditor en tiempo real de campañas de pauta digital "
        "con cálculo de Impresiones, Clics, Leads, CPA y ROAS) y Marketing y Publicidad (Plan de marketing predictivo y análisis "
        "de 4 macrotendencias + Pitch Deck interactivo de 6 diapositivas ejecutivas para lanzamiento de marca global)."
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

    ia_rows = [
        [
            "1. Antigravity\n(Agente de Ingeniería de Software & Síntesis Neural)",
            "• Arquitectura web multipágina HTML5/CSS3/JS.\n"
            "• Motores interactivos en vivo (CodeGuard, Chatbot, Simulador Ads, Pitch Deck, Motion Graphics).\n"
            "• Síntesis de voz neural (edge-tts) y Python Pillow.",
            "Permitió programar todos los módulos interactivos funcionales del portafolio, sintetizar 6 productos sonoros MP3 "
            "con voces neurales colombianas y latinoamericanas libres de ruido, postprocesar infografías con precisión tipográfica "
            "y desplegar el proyecto en GitHub Pages."
        ],
        [
            "2. Google Gemini &\nGemini Canvas\n(IA Multimodal y Animación Programática)",
            "• Estructuración de guiones, copys y Buyer Persona.\n"
            "• Generación de ilustraciones y piezas gráficas comerciales.\n"
            "• Exportación de videos Full HD en Gemini Canvas.",
            "Se empleó para redactar guiones verificados contra las Resoluciones MEN y para generar en Gemini Canvas tres (3) "
            "producciones animadas en Full HD capturadas a 60 FPS vía MediaRecorder API (Animación 2D de Contaduría, Video Explicativo "
            "de Sistemas 16:9 y Reel de Programación 9:16)."
        ],
        [
            "3. CapCut\n(Suite de Producción Audiovisual con IA)",
            "• Montaje de videos explicativos e institucionales.\n"
            "• Creación de Reels verticales (9:16).\n"
            "• Subtitulado dinámico automático por colores.",
            "Fundamental para la edición rítmica de los videos del Área de Administración y la Serie de Reels de Contaduría Pública, "
            "aplicando subtítulos automáticos sincronizados con las paletas cromáticas institucionales de FESNA."
        ],
        [
            "4. HeyGen\n(Plataforma de Avatares Digitales con IA)",
            "• Recreación de testimonio con avatar hiperrealista.\n"
            "• Sincronización labial (lip-sync) y gestualidad.\n"
            "• Cumplimiento ético de identidad sintética.",
            "Utilizado en el Nivel 3 de Contaduría Pública para dar vida a la egresada virtual 'Valeria Mendoza', presentando un "
            "testimonio ejecutivo sobre NIIF y Revisoría Fiscal sin clonar ni suplantar la identidad de personas reales (Regla #7)."
        ]
    ]
    add_styled_table(
        doc,
        ["Herramienta de IA", "Funciones Ejecutadas en el Proyecto", "Justificación Técnica y Valor Agregado"],
        ia_rows,
        header_bg="0D3B66"
    )

    doc.add_page_break()

    # =========================================================================
    # SECCION 3: PROCESO DETALLADO Y PROMPTS DE LAS 24 ACTIVIDADES (4 AREAS)
    # =========================================================================
    add_formatted_heading(
        doc,
        "3. Proceso Detallado de Elaboración y Prompts Principales por Área y Nivel (24 Actividades)",
        level=1,
        color_rgb=(13, 59, 102)
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
            "Nivel Operativo:\nArchivo, flujo documental, atención al cliente y ofimática."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión Administrativa",
            "Presencial: 111385\nVirtual: 111386",
            "Res. 010896 del 16/JUN/2022\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(87 créditos)",
            "Nivel Táctico:\nSupervisión, gestión del talento humano, logística e indicadores."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Administración de Empresas",
            "Presencial: 111357\nVirtual: 111750",
            "Res. 010897 del 16/JUN/2022\n(Vigencia 7 años)",
            "+4 períodos / 9 acumulados\n(155 créditos)",
            "Nivel Estratégico:\nAlta dirección, liderazgo, RSE y planes de negocio."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Pedagógico"],
        admin_norm_rows,
        header_bg="158777"
    )

    add_prompt_box(
        doc,
        "Actividad 1.1 (Admin): Video Explicativo con IA (Archivo: assets/video-tppae.mp4)",
        "Gemini + CapCut IA",
        "Actúa como director creativo de marketing educativo para FESNA. Redacta un guion audiovisual explicativo de 45 segundos sobre la 'Técnica Profesional en Procesos Administrativos Empresariales' (SNIES 111383 / 111384, Res. MEN 010895 de 2022, 3 períodos, 53 créditos), explicando paso a paso los procesos operativos empresariales: archivo, flujo de documentos y atención al cliente.",
        "Guion estructurado en Gemini y producido en CapCut con secuencias empresariales modernas, locución sintética y subtítulos dinámicos a 720p HD.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2 (Admin): Infografía Institucional con IA (Archivo: assets/infografia-ia-tppae-final.png)",
        "Gemini Imagen + Antigravity (Python Pillow)",
        "Generate a clean corporate infographic illustration for 'FESNA - Técnica Profesional en Procesos Administrativos Empresariales'. Flat vector + 3D isometric icons in navy blue (#0D3B66), teal (#00897B), and orange (#F36F21). Show 3 connected operational workflow stages: 1. Gestión Documental, 2. Flujo de Operaciones, 3. Atención al Cliente.",
        "Se combinó la ilustración generativa con un script de postprocesamiento en Python (Pillow) que maquetó con nitidez perfecta el encabezado institucional y los códigos SNIES 111383/111384.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 2.1 (Admin): Reel Promocional con IA (Archivo: assets/reel-tga.mp4)",
        "Gemini + CapCut IA (Formato 9:16)",
        "Diseña un guion dinámico para un Reel vertical (9:16) de 30 segundos promocionando la 'Tecnología en Gestión Administrativa' de FESNA (SNIES 111385 / 111386, Res. MEN 010896 de 2022, 5 semestres acumulados, 87 créditos), destacando supervisión táctica, gestión del talento humano y logística.",
        "Producido en formato móvil vertical 9:16 con cortes rítmicos, transiciones modernas y textos resaltados para redes sociales.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2 (Admin): Spot Publicitario con Voz IA (Archivo: assets/spot-tga-voz-ia.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-GonzaloNeural)",
        "Escribe un spot publicitario radial de 30 segundos para la Tecnología en Gestión Administrativa de FESNA con tono ejecutivo y motivador, mencionando los códigos SNIES 111385 y 111386 y la Resolución MEN 010896 de 2022.",
        "Sintetizado mediante el motor neuronal de Microsoft Azure (edge-tts) con la voz masculina colombiana 'es-CO-GonzaloNeural' e integrado con visualizador de barras de audio en vivo.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 3.1 (Admin): Video Institucional Generado con IA (Archivo: assets/video-institucional-ae.mp4)",
        "Gemini + CapCut IA",
        "Elabora el guion maestro para el Video Institucional del programa profesional 'Administración de Empresas' de FESNA (SNIES 111357 / 111750, Res. MEN 010897 de 2022, 9 períodos acumulados, 155 créditos), enfocado en comunicación estratégica, visión directiva, liderazgo y responsabilidad social empresarial.",
        "Integrado en alta definición (fesna_video_institucional_final.mp4) mostrando la culminación exitosa de los tres ciclos propedéuticos.",
        accent_hex="1FA08B"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2 (Admin): Motion Graphics Inteligente (Motor HTML5 Canvas en app.js)",
        "Antigravity (HTML5 Canvas API a 60 FPS)",
        "Programa en JavaScript nativo un motor interactivo de Motion Graphics vectorial en HTML5 Canvas a 60 FPS con 4 escenas sincronizadas: 1) Ruta Propedéutica de 3 Títulos, 2) Pilares Estratégicos y KPIs, 3) Modalidades SNIES 111357/111750 y 4) Respaldo Res. 010897 de 2022.",
        "Ejecutado en tiempo real dentro de administracion.html con controles interactivos de pausa, reinicio y salto directo entre escenas.",
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
            "Nivel Operativo Contable:\nAsientos contables, caja menor, archivo tributario y nómina."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión Contable y Financiera",
            "Presencial: 111391\nVirtual: 111392",
            "Res. 009956 del 03/JUN/2022\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(86 P / 87 V créditos)",
            "Nivel Táctico Financiero:\nEstados financieros, presupuestos, liquidez y tributaria intermedia."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Contaduría Pública",
            "Presencial: 111387\nVirtual: 111388",
            "Res. 009957 del 03/JUN/2022\n(Vigencia 7 años)",
            "+4 períodos / 9 acumulados\n(155 P / 159 V créditos)",
            "Nivel Estratégico y Fe Pública:\nNIIF/NIC, auditoría, revisoría fiscal y análisis macrofinanciero."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Pedagógico"],
        conta_norm_rows,
        header_bg="74187E"
    )

    add_prompt_box(
        doc,
        "Actividad 1.1 (Contaduría): Serie de Reels con Guion IA (Archivo: assets/reel-tppc-contaduria.mp4)",
        "Gemini + CapCut IA (Subtítulos Morados)",
        "Crea una serie de guiones de Reels verticales (9:16) para la 'Técnica Profesional en Procesos Contables' (SNIES 111389 / 111390, Res. MEN 009955 de 2022) con cápsulas sobre registro de asientos contables, manejo de caja menor, archivo tributario y liquidación básica de nómina.",
        "Editado en CapCut (fesna_reel_subtitulos_morados.mp4) con subtítulos dinámicos resaltados en morado (#AA38B9).",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2 (Contaduría): Cuña Radial Generada con IA (Archivo: assets/cuna-radial-tppc.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-SalomeNeural)",
        "Redacta una cuña radial de 30 segundos para la Técnica Profesional en Procesos Contables de FESNA destacando facturación electrónica, nómina y soportes contables en 3 períodos (SNIES 111389 / 111390).",
        "Sintetizada con la voz neural femenina colombiana 'es-CO-SalomeNeural' con ritmo comercial ágil.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 2.1 (Contaduría): Podcast 'Conoce FESNA' con IA (Archivo: assets/podcast-conoce-fesna-tgcf.mp3)",
        "Gemini + Antigravity (edge-tts: DaliaNeural & SebastianNeural)",
        "Escribe el guion de un episodio del podcast conversacional 'Conoce FESNA' entre dos anfitriones (Valeria y Mateo) explicando el análisis de estados financieros, presupuestos e indicadores de liquidez en la Tecnología en Gestión Contable y Financiera (SNIES 111391 / 111392, Res. 009956 de 2022).",
        "Generado mediante síntesis multipista en Python uniendo las voces neurales 'es-MX-DaliaNeural' y 'es-VE-SebastianNeural' con pausas naturales.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2 (Contaduría): Animación 2D Asistida por IA (Archivo: assets/animacion2d-tgcf-contaduria.mp4)",
        "Google Gemini con Canvas (Full HD 1920x1080)",
        "Crea en Gemini Canvas una aplicación HTML5 Canvas Full HD (1920x1080, 60 FPS) que reproduzca y exporte en video una Animación 2D de 30 segundos (5 escenas) sobre la Tecnología en Gestión Contable y Financiera de FESNA (paleta morada #74187E, #921AA3, #AA38B9) con botón MediaRecorder.",
        "Exportado directamente en Full HD (FESNA_Tecnologia_Gestion_Contable_Financiera_FullHD.mp4) e integrado en contaduria.html.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 3.1 (Contaduría): Testimonio Recreado con Avatar IA (Archivo: assets/testimonio-avatar-cp.mp4)",
        "HeyGen Avatar IA + Gemini",
        "Avatar corporativo femenino 'Valeria Mendoza' en HeyGen. Guion: 'Hola, soy Valeria Mendoza... Gracias al modelo por ciclos propedéuticos de FESNA culminé mi título profesional de Contaduría Pública (SNIES 111387 / 111388, Res. 009957 de 2022), dominando NIIF, auditoría, revisoría fiscal y fe pública.'",
        "Producido en HeyGen con sincronización labial hiperrealista y declaración ética explícita de personaje sintético (Regla #7).",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2 (Contaduría): Podcast Institucional Asistido por IA (Archivo: assets/podcast-institucional-cp.mp3)",
        "Gemini + Antigravity (edge-tts: JorgeNeural & CatalinaNeural)",
        "Redacta un podcast institucional directivo entre el Dr. Alejandro Vargas y la Dra. Carolina Méndez sobre Normas Internacionales NIIF/NIC, revisoría fiscal, ética y análisis macrofinanciero en el programa de Contaduría Pública de FESNA.",
        "Sintetizado a dos voces ejecutivas ('es-MX-JorgeNeural' y 'es-CL-CatalinaNeural') con calidad de estudio.",
        accent_hex="921AA3",
        bg_hex="FBF5FC"
    )

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # 3.3 AREA DE INGENIERIA DE SISTEMAS
    # -------------------------------------------------------------------------
    add_formatted_heading(
        doc,
        "3.3. Área de Ingeniería de Sistemas (Paleta Institucional Verde: #1A7C3B / #146C31 / #0D5625)",
        level=2,
        color_rgb=(20, 108, 49)
    )

    sis_norm_rows = [
        [
            "Nivel 1: Técnico Profesional",
            "Técnica Profesional en Procesos de Programación de Software",
            "Presencial: 111395\nVirtual: 111396",
            "Res. 012171 del 28/JUN/2022\n(Vigencia 7 años)",
            "3 períodos\n(52 créditos)",
            "Fundamentos de Código:\nVariables, tipos de datos, condicionales, ciclos, funciones y algoritmos."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión de Software y Sistemas",
            "Presencial: 111397\nVirtual: 111398",
            "Res. 012172 del 28/JUN/2022\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(86 créditos)",
            "Gestión y Arquitectura:\nCiclo de vida SDLC, Scrum/Kanban, bases de datos SQL/NoSQL y arquitectura."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Ingeniería de Sistemas",
            "Presencial: 111393\nVirtual: 111394",
            "Res. 012173 del 28/JUN/2022\n(Vigencia 7 años)",
            "+4 períodos / 9 acumulados\n(155 créditos)",
            "Solución Tecnológica e IA:\nCiberseguridad, sistemas inteligentes, automatización y transformación digital."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Pedagógico"],
        sis_norm_rows,
        header_bg="0D5625"
    )

    add_prompt_box(
        doc,
        "Actividad 1.1 (Sistemas): Serie de Reels con IA sobre Programación (Archivo: assets/reel-programacion-sistemas.webm)",
        "Google Gemini con Canvas (Formato Vertical 9:16 Full HD 1080x1920)",
        "Actúa como Creador de Motion Graphics Verticales y Desarrollador en HTML5 Canvas. Crea en Gemini Canvas una aplicación que reproduzca y descargue en video vertical Full HD (1080x1920, 60 FPS) un Reel educativo de 25 segundos sobre 'Fundamentos de Programación de Software' para FESNA (SNIES 111395 / 111396, Res. 012171 de 2022): 1) Variables y RAM, 2) Condicionales if/else, 3) Ciclos for/while y 4) Funciones y algoritmos, con subtítulos dinámicos en verde esmeralda (#1A7C3B).",
        "Generado y exportado desde Gemini Canvas en formato 9:16 (FESNA_Reel_Programacion_9x16.webm) e integrado en el reproductor vertical de sistemas.html.",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2 (Sistemas): Infografía Interactiva Generada con IA (Archivo: assets/infografia-sistemas-ia.jpg + Simulador JS)",
        "Gemini Imagen + Antigravity (Simulador Interactivo de Algoritmos)",
        "Generate a clean, high-tech educational infographic illustration for 'FESNA - Técnica Profesional en Procesos de Programación de Software'. Visual theme: software programming fundamentals, structured code, algorithms, flowcharts, logic gates, data structures (variables, loops, conditionals, functions) in emerald green (#1A7C3B) and neon cyan on dark slate (#0a192f).",
        "Se integró la infografía generada con IA junto con un Simulador Interactivo de Algoritmos en sistemas.html que permite alternar en vivo entre 4 pestañas de código Python (Variables, Condicionales, Ciclos y Funciones O(1)).",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    add_prompt_box(
        doc,
        "Actividad 2.1 (Sistemas): Podcast Técnico Asistido por IA (Archivo: assets/podcast-tecnico-tgss.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-GonzaloNeural)",
        "Redacta el guion institucional para el podcast técnico 'TechFESNA' de la Tecnología en Gestión de Software y Sistemas (SNIES 111397 / 111398, Res. MEN 012172 de 2022), analizando la evolución del ciclo de vida del software (SDLC) hacia metodologías ágiles (Scrum/Kanban), integración continua CI/CD, bases de datos SQL vs. NoSQL y arquitectura de microservicios.",
        "Sintetizado mediante script en Python (generate_sistemas_audio.py) con voz neural colombiana de alta definición e integrado con ecualizador animado en sistemas.html.",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2 (Sistemas): Video Explicativo con IA sobre Sistemas y Desarrollo de Software (Archivo: assets/video-explicativo-sistemas.webm)",
        "Google Gemini con Canvas (Full HD 1920x1080 a 60 FPS)",
        "Crea en Gemini Canvas una aplicación HTML5 Canvas Full HD (1920x1080, 60 FPS) que reproduzca y permita descargar como archivo de video el 'Video Explicativo con IA sobre Sistemas y Desarrollo de Software' para la Tecnología en Gestión de Software y Sistemas de FESNA (SNIES 111397 / 111398, Res. 012172 de 2022, 86 créditos), estructurado en 5 escenas: Portada, Ciclo SDLC y Scrum, Arquitectura en 3 Capas, Bases de Datos SQL/NoSQL y Escalera Propedéutica.",
        "Exportado como archivo de video Full HD (FESNA_Video_Explicativo_Sistemas_FullHD.webm) e incrustado directamente en sistemas.html.",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    add_prompt_box(
        doc,
        "Actividad 3.1 (Sistemas): Proyecto de Solución Tecnológica con IA ('FESNA AI CodeGuard v2.4' en sistemas.html)",
        "Antigravity + Gemini (Prototipo Funcional de Auditoría de Ciberseguridad OWASP Top 10)",
        "Diseña e implementa un prototipo funcional interactivo de solución tecnológica con IA llamado 'FESNA AI CodeGuard v2.4' que resuelva la problemática real de vulnerabilidades de seguridad y cuellos de botella en el desarrollo de software. El sistema debe analizar código en vivo, detectar Inyección SQL (CWE-89), Cross-Site Scripting XSS (CWE-79) y complejidad cuadrática O(n²), calcular un puntaje de seguridad de 0 a 100 y generar la refactorización segura bajo Clean Architecture.",
        "Programado como aplicación interactiva en vivo dentro de sistemas.html (app.js): el usuario o evaluador puede cargar 4 escenarios de código o editar el código en el área de texto y ejecutar la auditoría asistida por IA en tiempo real.",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2 (Sistemas): Podcast de Análisis Prospectivo sobre IA e Ingeniería de Sistemas (Archivo: assets/podcast-prospectivo-sistemas.mp3)",
        "Gemini + Antigravity (edge-tts: es-CO-SalomeNeural)",
        "Escribe un guion de análisis prospectivo para el programa profesional de Ingeniería de Sistemas de FESNA (SNIES 111393 / 111394, Res. MEN 012173 de 2022, 9 períodos, 155 créditos) sobre cómo la IA generativa y los agentes autónomos transforman al ingeniero de sistemas en un arquitecto de soluciones resilientes, científicas de datos y ciberseguridad ética.",
        "Sintetizado en alta definición con la voz neural 'es-CO-SalomeNeural' e integrado con visualizador de ondas en sistemas.html.",
        accent_hex="1A7C3B",
        bg_hex="F2FBF5"
    )

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # 3.4 AREA DE MARKETING Y PUBLICIDAD
    # -------------------------------------------------------------------------
    add_formatted_heading(
        doc,
        "3.4. Área de Marketing y Publicidad (Paleta Institucional Roja/Vinotinto: #D43B27 / #B32319 / #7B1F17)",
        level=2,
        color_rgb=(179, 35, 25)
    )

    mkt_norm_rows = [
        [
            "Nivel 1: Técnico Profesional",
            "Técnica Profesional en Procesos de Comercialización y Comunicación Publicitaria",
            "Presencial: 119246\nVirtual: 119247",
            "Res. 011477 del 30/ABR/2026\n(Vigencia 7 años)",
            "3 períodos\n(49 créditos)",
            "Comunicación Comercial:\nVenta directa, piezas gráficas comerciales y protocolos de atención al usuario."
        ],
        [
            "Nivel 2: Tecnológico",
            "Tecnología en Gestión Comercial y Publicidad",
            "Presencial: 119245\nVirtual: 119244",
            "Res. 011476 del 30/ABR/2026\n(Vigencia 7 años)",
            "+2 períodos / 5 acumulados\n(82 créditos)",
            "Mercadeo Digital y Pauta:\nBuyer Persona, copys persuasivos, SEM/SEO y auditoría de métricas (CTR, CPA, ROAS)."
        ],
        [
            "Nivel 3: Profesional Universitario",
            "Marketing y Publicidad",
            "Presencial: 119242\nVirtual: 119243",
            "Res. 011475 del 30/ABR/2026\n(Vigencia 7 años)",
            "+3 períodos / 8 acumulados\n(133 créditos)",
            "Estrategia Global y Predictiva:\nNeuromarketing, macrotendencias analíticas y Pitch Deck de marca internacional."
        ]
    ]
    add_styled_table(
        doc,
        ["Nivel Propedéutico", "Programa Oficial FESNA", "Códigos SNIES", "Resolución MEN", "Duración y Créditos", "Enfoque Pedagógico"],
        mkt_norm_rows,
        header_bg="7B1F17"
    )

    add_prompt_box(
        doc,
        "Actividad 1.1 (Marketing): Diseño de Piezas Gráficas Comerciales Asistidas por IA (Archivos: ad-comercial-mkt.jpg y ad-comercial-mkt-2.jpg)",
        "Gemini Imagen + Antigravity (Galería Interactiva Dual)",
        "1) High-impact university advertising banner for 'FESNA - Marketing y Publicidad', creative agency studio, digital marketing dashboards, deep crimson (#D43B27, #B32319).\n"
        "2) Modern social media commercial advertisement poster for 'FESNA - Técnica Profesional en Procesos de Comercialización y Comunicación Publicitaria', glossy 3D megaphone, social metrics, crimson red and burgundy layout.",
        "Se generaron dos (2) piezas gráficas comerciales de alta conversión y se integraron en marketing.html mediante un conmutador interactivo por pestañas junto con sus metadatos de venta directa.",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
    )

    add_prompt_box(
        doc,
        "Actividad 1.2 (Marketing): Simulación de Atención al Cliente mediante Chat Conversacional Entrenado con IA",
        "Antigravity + Gemini (Chatbot Interactivo en Vivo en marketing.html)",
        "Entrena un asistente virtual conversacional de admisiones y servicio al cliente para el área de Marketing y Publicidad de FESNA. Debe aplicar protocolos de atención cordial, resolver dudas en tiempo real sobre los 3 títulos por ciclos propedéuticos, los códigos SNIES (119246/119247, 119245/119244, 119242/119243), las Resoluciones MEN 011477, 011476 y 011475 del 30 de abril de 2026, los créditos (49, 82 y 133) y las modalidades presencial y virtual.",
        "Implementado como un Chatbot 100 % funcional dentro de marketing.html con chips de consulta rápida y campo de texto libre con motor de respuesta inteligente.",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
    )

    add_prompt_box(
        doc,
        "Actividad 2.1 (Marketing): Creación y Optimización de Buyer Persona y Copys Publicitarios con IA",
        "Gemini + Antigravity (Ficha Camila Rojas + Pestañas AIDA, PAS y Storytelling)",
        "Desarrolla el perfil arquetípico de Buyer Persona (Camila Rojas, 21 años, Bogotá D.C., Community Manager Junior que busca profesionalizarse) para la Tecnología en Gestión Comercial y Publicidad de FESNA (SNIES 119245 / 119244, Res. 011476 de 2026, 82 créditos). Redacta y optimiza 3 copys publicitarios aplicando las fórmulas AIDA (Atención, Interés, Deseo, Acción), PAS (Problema, Agitación, Solución) y Storytelling.",
        "Maquetado en marketing.html con la tarjeta visual del Buyer Persona y un sistema interactivo de pestañas que permite evaluar cada estructura de copywriting.",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
    )

    add_prompt_box(
        doc,
        "Actividad 2.2 (Marketing): Auditoría y Simulación de Campañas de Pauta Digital Asistidas por Analítica de IA",
        "Antigravity + Gemini Analítica (Calculadora y Auditor de KPIs en Tiempo Real)",
        "Diseña un simulador interactivo de pauta digital (Meta Ads / Google Ads) que calcule en tiempo real Impresiones, Clics, Leads Calificados (conversión del 8%), Costo por Adquisición (CPA) y Retorno de la Inversión Publicitaria (ROAS) a partir de controles deslizantes de Presupuesto Mensual ($500.000 a $5.000.000 COP), CPC ($400 a $2.000 COP) y CTR (1.0% a 5.0%), generando un diagnóstico de auditoría automática con IA.",
        "Programado en vivo en marketing.html (función updateAdsSimulator en app.js), actualizando instantáneamente las 5 tarjetas de KPIs y el veredicto analítico de la IA.",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
    )

    add_prompt_box(
        doc,
        "Actividad 3.1 (Marketing): Plan de Marketing Predictivo y Análisis de Macrotendencias con IA Analítica",
        "Gemini Analítica + Antigravity",
        "Elabora un plan de marketing predictivo para el programa profesional de Marketing y Publicidad de FESNA (SNIES 119242 / 119243, Res. 011475 del 30 de abril de 2026, 8 períodos, 133 créditos). Analiza 4 macrotendencias globales: 1) Hiperpersonalización Algorítmica, 2) Neuromarketing Predictivo, 3) Consumo Ético y Propósito en Gen Z, y 4) Omnicanalidad Phygital, incluyendo un modelo predictivo de retención estudiantil (Churn vs. LTV).",
        "Integrado en el Nivel 3 de marketing.html con tarjetas analíticas y cuantificación del incremento en retención (+34.2%) y LTV (+41.8%).",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
    )

    add_prompt_box(
        doc,
        "Actividad 3.2 (Marketing): Pitch Deck de Lanzamiento de Marca Internacional con Narrativa Interactiva",
        "Gemini + Antigravity (Visor Ejecutivo Interactivo de 6 Diapositivas)",
        "Estructura un Pitch Deck ejecutivo de 6 diapositivas con narrativa interactiva para el posicionamiento internacional de FESNA: 1) Visión Global y Disrupción Educativa, 2) Oportunidad de Mercado (+68% demanda de talento digital), 3) Solución Propedéutica de 3 Títulos Acreditados, 4) Estrategia Transmedia y Conversión con IA, 5) Unit Economics (CAC $145K, LTV $8.4M, Ratio 57.9x, ROAS 4.2x) y 6) Llamado a la Acción Global.",
        "Implementado como un presentador interactivo de diapositivas dentro de marketing.html con navegación Anterior/Siguiente e indicadores de progreso.",
        accent_hex="D43B27",
        bg_hex="FEF5F4"
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

    ethics_rows = [
        [
            "Datos Académicos y Normativos (Reglas #1, #2 y #4)",
            "Resoluciones MEN 010895, 010896, 010897, 009955, 009956, 009957, 012171, 012172 y 012173 de 2022; Resoluciones MEN 011477, 011476 y 011475 del 30 de abril de 2026; Portal www.nuevaamerica.edu.co.",
            "Fidelidad del 100 %. No se inventaron costos, requisitos ni duraciones no suministradas en los documentos oficiales."
        ],
        [
            "Identidad Sintética y Avatar IA (Regla #7)",
            "HeyGen AI Video Generator (Personaje ficticio: 'Valeria Mendoza').",
            "Cumplimiento ético estricto: no se clonaron voces, rostros ni identidades de personas reales sin autorización. Se declara explícitamente el uso de avatar virtual."
        ],
        [
            "Producción Sonora y Podcasts Neurales (6 Audios MP3)",
            "Motor Microsoft Azure Neural TTS vía librería abierta edge-tts (Python) y guiones originales.",
            "Obras sonoras de autoría académica propia (David Yused Pulido Pardo), libres de restricciones de copyright comercial."
        ],
        [
            "Videos, Reels y Animaciones 2D (8 Archivos MP4/WebM + Motores Canvas)",
            "CapCut, Google Gemini Canvas (HTML5 Canvas API) y Antigravity.",
            "Creación original para el portafolio académico del curso, verificada en computador y dispositivos móviles (Regla #6)."
        ],
        [
            "Infografías y Piezas Gráficas Comerciales (4 Imágenes)",
            "Gemini Imagen + Postprocesamiento tipográfico con Python Pillow.",
            "Ilustraciones generadas con IA bajo prompts documentados (Reglas #3 y #8) con atribución explícita de autoría estudiantil."
        ]
    ]
    add_styled_table(
        doc,
        ["Categoría del Recurso", "Fuente / Tecnología de Generación", "Licencia, Autoría y Cumplimiento Ético"],
        ethics_rows,
        header_bg="0D3B66"
    )

    # =========================================================================
    # SECCION 5: SUSTENTACION TEORICA (PUNTO 4 DEL EXAMEN FINAL)
    # =========================================================================
    add_formatted_heading(
        doc,
        "5. Sustentación Teórica Integral del Proyecto (Punto 4: Fundamentación Académica)",
        level=1,
        color_rgb=(13, 59, 102)
    )

    add_formatted_heading(
        doc,
        "5.1. Jerarquía Organizacional y Niveles de la Administración (Operativo, Táctico y Estratégico)",
        level=2,
        color_rgb=(21, 135, 119)
    )
    add_body_p(
        doc,
        "Desde la teoría neoclásica de la administración formulada por Chiavenato (2019) y Robbins y Coulter (2018), las organizaciones "
        "estructuran su proceso administrativo (planeación, organización, dirección y control) en tres niveles jerárquicos: el nivel "
        "operativo o técnico (ejecución estandarizada de tareas y procesos cotidianos), el nivel táctico o intermedio (coordinación "
        "departamental, gestión del talento humano y control de indicadores) y el nivel estratégico o institucional (visión de largo "
        "plazo, liderazgo directivo y toma de decisiones globales). Este modelo teórico fundamenta de manera exacta la progresión "
        "comunicativa diseñada para el Área de Administración de FESNA a través de sus tres programas acreditados."
    )

    add_formatted_heading(
        doc,
        "5.2. El Modelo de Formación por Ciclos Propedéuticos en la Educación Superior Colombiana",
        level=2,
        color_rgb=(21, 135, 119)
    )
    add_body_p(
        doc,
        "Conforme a la Ley 749 de 2002 y el Decreto Único Reglamentario 1075 de 2015 del Ministerio de Educación Nacional (MEN), "
        "la formación por ciclos propedéuticos organiza la educación superior en etapas secuenciales, complementarias e "
        "interdependientes (técnica profesional, tecnológica y profesional universitaria). Este diseño curricular democratiza el "
        "acceso a la educación superior al otorgar tres titulaciones oficiales a lo largo de la trayectoria formativa, permitiendo "
        "la inserción laboral temprana desde el tercer período académico y reduciendo la deserción estudiantil."
    )

    add_formatted_heading(
        doc,
        "5.3. Ciencia Contable, Normas Internacionales de Información Financiera (NIIF) y Fe Pública",
        level=2,
        color_rgb=(146, 26, 163)
    )
    add_body_p(
        doc,
        "En el Área de Contaduría Pública, la campaña se fundamentó en la evolución epistemológica y legal que va desde el registro "
        "transaccional y la teneduría de libros hasta el aseguramiento de la información y la fe pública. De acuerdo con la Ley 43 "
        "de 1990 y la Ley 1314 de 2009 (convergencia hacia estándares internacionales NIIF/NIC y normas de aseguramiento NAI), el "
        "profesional contable garantiza la transparencia financiera y la confianza pública (Horngren, Sundem & Elliott, 2010), "
        "articulando la operación contable (Nivel 1), la gestión tributaria y financiera (Nivel 2) y la auditoría y revisoría fiscal (Nivel 3)."
    )

    add_formatted_heading(
        doc,
        "5.4. Ingeniería de Software, Arquitecturas Limpias y Ciberseguridad Defensiva (OWASP)",
        level=2,
        color_rgb=(20, 108, 49)
    )
    add_body_p(
        doc,
        "Para el Área de Ingeniería de Sistemas, los productos desarrollados se sustentan en los principios de la ingeniería de "
        "software moderna (Pressman & Maxim, 2021; Sommerville, 2016). El Nivel 1 aborda la algoritmia, las estructuras de datos "
        "y la complejidad computacional (notación Big O); el Nivel 2 incorpora el Ciclo de Vida del Desarrollo de Software (SDLC) "
        "bajo marcos ágiles (Scrum y Kanban), la persistencia políglota (SQL y NoSQL) y la integración continua (DevOps CI/CD); "
        "mientras que el Nivel 3 materializa la seguridad desde el diseño (DevSecOps) mediante el prototipo 'FESNA AI CodeGuard', "
        "orientado a mitigar vulnerabilidades críticas del estándar OWASP Top 10 (como Inyección SQL CWE-89 y Cross-Site Scripting CWE-79)."
    )

    add_formatted_heading(
        doc,
        "5.5. Marketing Digital, Neuromarketing, Buyer Persona y Narrativa Transmedia",
        level=2,
        color_rgb=(179, 35, 25)
    )
    add_body_p(
        doc,
        "En el Área de Marketing y Publicidad, la estrategia se apoyó en la dirección de marketing de Kotler y Keller (2016), la "
        "planificación de imagen corporativa de Capriotti (2013) y las narrativas transmedia de Scolari (2013). El diseño de piezas "
        "comerciales y el chatbot conversacional (Nivel 1) aplican protocolos de venta directa y atención omnicanal; la construcción "
        "del Buyer Persona, los frameworks persuasivos (AIDA y PAS) y el simulador de métricas CTR, CPC, CPA y ROAS (Nivel 2) "
        "responden al marketing de rendimiento basado en datos (Performance Marketing); y el análisis de macrotendencias junto al "
        "Pitch Deck internacional (Nivel 3) integran el neuromarketing y los Unit Economics (CAC vs. LTV) para la alta gerencia de marca."
    )

    add_formatted_heading(
        doc,
        "5.6. Inteligencia Artificial Generativa, Ingeniería de Prompts y Enfoque Human-in-the-Loop",
        level=2,
        color_rgb=(13, 59, 102)
    )
    add_body_p(
        doc,
        "Finalmente, desde la teoría de agentes inteligentes de Russell y Norvig (2021), la co-inteligencia de Mollick (2024) y las "
        "directrices éticas de la UNESCO (2023), el proyecto implementó un protocolo de supervisión humana activa (Human-in-the-Loop) "
        "y anclaje documental (Grounding). Cada prompt suministrado a Gemini, CapCut, HeyGen y Antigravity incorporó explícitamente "
        "los datos verificados de las Resoluciones del MEN, evitando alucinaciones algorítmicas y demostrando un dominio técnico, "
        "conceptual y ético de la Inteligencia Artificial."
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

    apa_refs = [
        "American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000",
        "Bytedance Ltd. (2026). CapCut: Plataforma de edición de video y subtitulado asistido por inteligencia artificial [Software]. https://www.capcut.com/",
        "Capriotti, P. (2013). Planificación estratégica de la imagen corporativa (4.ª ed.). Instituto de Investigación en Relaciones Públicas (IIRP).",
        "Chiavenato, I. (2019). Introducción a la teoría general de la administración (10.ª ed.). McGraw-Hill Interamericana.",
        "Congreso de la República de Colombia. (1990, 13 de diciembre). Ley 43 de 1990. Por la cual se adiciona la Ley 145 de 1960, reglamentaria de la profesión de Contador Público y se dictan otras disposiciones. Diario Oficial n.º 39.602.",
        "Congreso de la República de Colombia. (2002, 19 de julio). Ley 749 de 2002. Por la cual se organiza el servicio público de la educación superior en las modalidades de formación técnica profesional y tecnológica. Diario Oficial n.º 44.872.",
        "Congreso de la República de Colombia. (2009, 13 de julio). Ley 1314 de 2009. Por la cual se regulan los principios y normas de contabilidad e información financiera y de aseguramiento de información aceptados en Colombia. Diario Oficial n.º 47.409.",
        "Fundación de Educación Superior Nueva América [FESNA]. (2026). Oferta académica oficial por ciclos propedéuticos: Administración de Empresas, Contaduría Pública, Ingeniería de Sistemas y Marketing y Publicidad. https://www.nuevaamerica.edu.co/",
        "Google DeepMind. (2026). Antigravity: Agente de ingeniería de software y desarrollo asistido por inteligencia artificial [Software].",
        "Google DeepMind. (2026). Google Gemini & Gemini Canvas: Modelo multimodal de lenguaje y entorno de programación interactiva [Software de inteligencia artificial]. https://gemini.google.com/",
        "HeyGen Inc. (2026). HeyGen AI Video Generator: Plataforma de generación de video con avatares digitales e inteligencia artificial [Software]. https://www.heygen.com/",
        "Horngren, C. T., Sundem, G. L., & Elliott, J. A. (2010). Introducción a la contabilidad financiera (9.ª ed.). Pearson Educación.",
        "Kotler, P., & Keller, K. L. (2016). Dirección de marketing (15.ª ed.). Pearson Educación.",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2015, 26 de mayo). Decreto 1075 de 2015. Por medio del cual se expide el Decreto Único Reglamentario del Sector Educación.",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 3 de junio). Resoluciones n.º 009955, 009956 y 009957 de 2022. Registros calificados de los programas de Técnica Profesional en Procesos Contables (SNIES 111389/111390), Tecnología en Gestión Contable y Financiera (SNIES 111391/111392) y Contaduría Pública (SNIES 111387/111388) de la Fundación de Educación Superior Nueva América (FESNA).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 16 de junio). Resoluciones n.º 010895, 010896 y 010897 de 2022. Registros calificados de los programas de Técnica Profesional en Procesos Administrativos Empresariales (SNIES 111383/111384), Tecnología en Gestión Administrativa (SNIES 111385/111386) y Administración de Empresas (SNIES 111357/111750) de la Fundación de Educación Superior Nueva América (FESNA).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2022, 28 de junio). Resoluciones n.º 012171, 012172 y 012173 de 2022. Registros calificados de los programas de Técnica Profesional en Procesos de Programación de Software (SNIES 111395/111396), Tecnología en Gestión de Software y Sistemas (SNIES 111397/111398) e Ingeniería de Sistemas (SNIES 111393/111394) de la Fundación de Educación Superior Nueva América (FESNA).",
        "Ministerio de Educación Nacional de Colombia [MEN]. (2026, 30 de abril). Resoluciones n.º 011477, 011476 y 011475 de 2026. Registros calificados de los programas de Técnica Profesional en Procesos de Comercialización y Comunicación Publicitaria (SNIES 119246/119247), Tecnología en Gestión Comercial y Publicidad (SNIES 119245/119244) y Profesional Universitario en Marketing y Publicidad (SNIES 119242/119243) de la Fundación de Educación Superior Nueva América (FESNA).",
        "Mollick, E. (2024). Co-Intelligence: Living and working with AI. Portfolio / Penguin Random House.",
        "OWASP Foundation. (2021). OWASP Top 10: The Ten Most Critical Web Application Security Risks. https://owasp.org/www-project-top-ten/",
        "Pressman, R. S., & Maxim, B. R. (2021). Ingeniería del software: Un enfoque práctico (9.ª ed.). McGraw-Hill.",
        "Robbins, S. P., & Coulter, M. (2018). Administración (13.ª ed.). Pearson Educación.",
        "Russell, S., & Norvig, P. (2021). Inteligencia artificial: Un enfoque moderno (4.ª ed.). Pearson Educación.",
        "Scolari, C. A. (2013). Narrativas transmedia: Cuando todos los medios cuentan. Deusto.",
        "Sommerville, I. (2016). Software engineering (10th ed.). Pearson.",
        "UNESCO. (2023). Guía para el uso de IA generativa en educación e investigación. Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura. https://unesdoc.unesco.org/"
    ]

    for ref in apa_refs:
        add_apa_reference(doc, ref)

    out_project = r"C:\Users\david\.gemini\antigravity\scratch\fesna-portafolio-ia\DOCUMENTACION_SUSTENTACION_CAMPANA_FESNA_DAVID_PULIDO.docx"
    out_downloads = r"C:\Users\david\Downloads\DOCUMENTACION_SUSTENTACION_CAMPANA_FESNA_DAVID_PULIDO.docx"

    doc.save(out_project)
    shutil.copy2(out_project, out_downloads)
    print(f"Documento del Examen Final generado exitosamente en:\n1) {out_project}\n2) {out_downloads}")


if __name__ == "__main__":
    build_document()
