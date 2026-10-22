// ============================================================================
// PORTAFOLIO DIGITAL Y CAMPAÑA PUBLICITARIA FESNA
// Menú Lateral Izquierdo + Reproductores IA (Administración y Contaduría)
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  initLeftSidebar();
  initCurriculumToggles();
  initAllAudioVisualizers();
  initInstitutionalVideoAE();
  initMotionGraphicsEngine();
  initContaduriaReelsSeries();
  initContaduriaAnimacion2D();
  initContaduriaAvatarTestimonial();
});

// 1. Menú Lateral Desplegable a la Izquierda (Disponible en todas las páginas)
function initLeftSidebar() {
  const sidebar = document.getElementById('left-sidebar');
  const overlay = document.getElementById('sidebar-overlay');
  const openBtns = document.querySelectorAll('.open-sidebar-btn');
  const closeBtn = document.getElementById('close-sidebar-btn');

  if (!sidebar || !overlay) return;

  function openMenu() {
    sidebar.classList.add('open');
    overlay.classList.add('open');
  }

  function closeMenu() {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
  }

  openBtns.forEach((btn) => btn.addEventListener('click', openMenu));
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  overlay.addEventListener('click', closeMenu);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

// 2. Desplegable del Plan de Estudios Oficial por Nivel
function initCurriculumToggles() {
  const toggles = document.querySelectorAll('.toggle-curriculum-btn');
  toggles.forEach((btn) => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      const panel = document.getElementById(targetId);
      if (!panel) return;
      const isOpen = panel.classList.toggle('open');
      btn.textContent = isOpen
        ? 'Ocultar Plan de Estudios ▲'
        : 'Ver Plan de Estudios por Períodos ▼';
    });
  });
}

// 3. Ecualizadores de Audio para todos los Spots, Cuñas y Podcasts IA
function initAllAudioVisualizers() {
  const pairs = [
    { audioId: 'spot-audio-element', visId: 'spot-visualizer' },
    { audioId: 'cuna-tppc-audio', visId: 'cuna-tppc-visualizer' },
    { audioId: 'podcast-tgcf-audio', visId: 'podcast-tgcf-visualizer' },
    { audioId: 'podcast-cp-audio', visId: 'podcast-cp-visualizer' }
  ];

  pairs.forEach(({ audioId, visId }) => {
    const audio = document.getElementById(audioId);
    const vis = document.getElementById(visId);
    if (!audio || !vis) return;
    audio.addEventListener('play', () => vis.classList.add('playing'));
    audio.addEventListener('pause', () => vis.classList.remove('playing'));
    audio.addEventListener('ended', () => vis.classList.remove('playing'));
  });
}

// 4. Video Institucional Administración de Empresas (Si usa canvas fallback)
function initInstitutionalVideoAE() {
  const canvas = document.getElementById('canvas-video-ae');
  const audio = document.getElementById('audio-video-ae');
  if (!canvas || !audio) return;
}

// 5. Motion Graphics Inteligente (Administración de Empresas)
function initMotionGraphicsEngine() {
  const canvas = document.getElementById('canvas-motion-ae');
  const modeBtn = document.getElementById('mode-motion-ae');
  const uploadInput = document.getElementById('upload-motion-ae');
  const customVideo = document.getElementById('custom-motion-ae');

  if (!canvas) return;
  canvas.width = 960;
  canvas.height = 540;
  const ctx = canvas.getContext('2d');

  let running = true;
  let viewMode = 0;
  let startTime = performance.now();

  const cyclesData = [
    {
      label: 'Ciclo 1: Técnica Profesional',
      snies: 'SNIES 111383 / 111384',
      periods: 3,
      credits: 53,
      color: '#36b59e',
      res: 'Res. 010895 (2022)'
    },
    {
      label: 'Ciclo 2: Tecnología',
      snies: 'SNIES 111385 / 111386',
      periods: 5,
      credits: 87,
      color: '#1fa08b',
      res: 'Res. 010896 (2022)'
    },
    {
      label: 'Ciclo 3: Administración de Empresas',
      snies: 'SNIES 111357 / 111750',
      periods: 9,
      credits: 155,
      color: '#f36f21',
      res: 'Res. 010897 (2022)'
    }
  ];

  const kpiData = [
    { name: 'Estrategia y Prospectiva (Per. 6-7)', pct: 95, color: '#36b59e' },
    { name: 'Plan de Negocio y Finanzas (Per. 6-7)', pct: 92, color: '#f36f21' },
    { name: 'Responsabilidad Social y Ambiental (Per. 8-9)', pct: 96, color: '#1fa08b' },
    { name: 'Gerencia Logística y Proyectos (Per. 8-9)', pct: 94, color: '#38bdf8' }
  ];

  function drawMotion(now) {
    const elapsed = (now - startTime) / 1000;
    const animFactor = Math.min(1, (elapsed % 6) / 2.2);
    const w = canvas.width;
    const h = canvas.height;

    const grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#041222');
    grad.addColorStop(1, '#0b4f44');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
    roundRect(ctx, 45, 28, w - 90, 52, 10, true, false);

    ctx.fillStyle = '#f36f21';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('MOTION GRAPHICS • RUTA PROPEDÉUTICA Y ESTRATEGIA DIRECTIVA FESNA', 65, 52);

    ctx.fillStyle = '#cbd5e1';
    ctx.font = '13px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.fillText('SNIES Presencial: 111357 | Virtual: 111750 • Res. 010897 del 16 de junio de 2022 • 155 Créditos', 65, 70);

    if (viewMode === 0) {
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 22px "Plus Jakarta Sans", Arial, sans-serif';
      ctx.fillText('Tu Crecimiento Profesional en FESNA: 3 Niveles = 3 Títulos', 50, 118);

      const baseY = 435;
      const maxH = 240;

      cyclesData.forEach((c, i) => {
        const colX = 110 + i * 280;
        const barH = (c.credits / 155) * maxH * easeOutCubic(animFactor);
        const barY = baseY - barH;

        ctx.fillStyle = c.color;
        roundRect(ctx, colX, barY, 160, barH, 12, true, false);

        ctx.fillStyle = '#ffffff';
        ctx.font = '800 24px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`${Math.round(c.credits * easeOutCubic(animFactor))} Créd.`, colX + 80, barY - 32);

        ctx.fillStyle = '#5eead4';
        ctx.font = 'bold 15px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.fillText(`${c.periods} Períodos`, colX + 80, barY - 10);

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 15px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.fillText(c.label, colX + 80, baseY + 26);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '13px monospace';
        ctx.fillText(c.snies, colX + 80, baseY + 46);
        ctx.fillText(c.res, colX + 80, baseY + 64);
      });
    } else {
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 22px "Plus Jakarta Sans", Arial, sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Competencias Directivas y Planes de Negocio (Períodos 6.º al 9.º)', 50, 120);

      kpiData.forEach((k, idx) => {
        const y = 160 + idx * 78;
        ctx.fillStyle = '#e2e8f0';
        ctx.font = 'bold 16px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(k.name, 55, y);

        ctx.fillStyle = 'rgba(255,255,255,0.12)';
        roundRect(ctx, 55, y + 12, 740, 26, 8, true, false);

        const fillW = 740 * (k.pct / 100) * easeOutCubic(animFactor);
        ctx.fillStyle = k.color;
        roundRect(ctx, 55, y + 12, Math.max(20, fillW), 26, 8, true, false);

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 15px monospace';
        ctx.fillText(`${Math.round(k.pct * easeOutCubic(animFactor))}%`, 815, y + 30);
      });
    }

    if (running) {
      requestAnimationFrame(drawMotion);
    }
  }

  requestAnimationFrame(drawMotion);

  if (modeBtn) {
    modeBtn.addEventListener('click', () => {
      viewMode = viewMode === 0 ? 1 : 0;
      startTime = performance.now();
    });
  }

  if (uploadInput && customVideo) {
    uploadInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      running = false;
      canvas.style.display = 'none';
      customVideo.style.display = 'block';
      customVideo.src = URL.createObjectURL(file);
      customVideo.play();
    });
  }
}

// 6. Contaduría Nivel 1: Serie de Reels con Guion IA (4 Cápsulas Interactivas + Soporte MP4)
function initContaduriaReelsSeries() {
  const canvas = document.getElementById('canvas-reels-tppc');
  const nextBtn = document.getElementById('next-reel-tppc');
  const uploadInput = document.getElementById('upload-reel-tppc');
  const customVideo = document.getElementById('custom-reel-tppc');

  if (!canvas) return;
  canvas.width = 540;
  canvas.height = 960;
  const ctx = canvas.getContext('2d');

  let currentTip = 0;
  let startTime = performance.now();
  let running = true;

  const tips = [
    {
      num: 'CÁPSULA 1 DE 4 • ASIENTOS CONTABLES',
      title: 'Registro de\nAsientos Contables',
      desc: 'Todo hecho económico se registra por partida doble: Débito = Crédito.\nAprende Contabilidad de Activos, Pasivos y Patrimonio desde 1.er período.',
      pill1: 'Partida Doble Exacta',
      pill2: 'Software Contable Aplicado',
      pill3: 'SNIES 111389 / 111390',
      accent: '#aa38b9'
    },
    {
      num: 'CÁPSULA 2 DE 4 • CAJA MENOR',
      title: 'Manejo Eficiente\nde Caja Menor',
      desc: 'Controla gastos urgentes de baja cuantía con soportes legales, arqueos periódicos y reembolsos oportunos.',
      pill1: 'Arqueo y Control Interno',
      pill2: 'Soportes Contables Válidos',
      pill3: 'Res. 009955 (03/JUN/2022)',
      accent: '#f36f21'
    },
    {
      num: 'CÁPSULA 3 DE 4 • ARCHIVO TRIBUTARIO',
      title: 'Organización de\nArchivo Tributario',
      desc: 'Clasifica facturas electrónicas, retenciones y declaraciones según el Procedimiento Tributario colombiano.',
      pill1: 'Procedimiento Tributario',
      pill2: 'Trazabilidad Documental',
      pill3: '3 Períodos • 51/52 Créditos',
      accent: '#921aa3'
    },
    {
      num: 'CÁPSULA 4 DE 4 • NÓMINA BÁSICA',
      title: 'Liquidación Básica\nde Nómina',
      desc: 'Domina devengados, deducciones, seguridad social y prestaciones sociales con Derecho Laboral y Excel Financiero.',
      pill1: 'Derecho Laboral + Excel',
      pill2: 'Seguridad Social y Aportes',
      pill3: '¡Inscríbete en FESNA!',
      accent: '#d946ef'
    }
  ];

  function drawReel(now) {
    const elapsed = (now - startTime) / 1000;
    if (elapsed > 6.5) {
      currentTip = (currentTip + 1) % tips.length;
      startTime = now;
    }
    const tip = tips[currentTip];
    const w = canvas.width;
    const h = canvas.height;
    const padX = 38;

    const grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#2a0630');
    grad.addColorStop(0.5, '#581063');
    grad.addColorStop(1, '#74187e');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Top stories progress bars
    const segW = (w - padX * 2 - 18) / 4;
    for (let i = 0; i < 4; i++) {
      ctx.fillStyle = 'rgba(255,255,255,0.22)';
      roundRect(ctx, padX + i * (segW + 6), 28, segW, 6, 3, true, false);
      if (i < currentTip) {
        ctx.fillStyle = '#f5d0fe';
        roundRect(ctx, padX + i * (segW + 6), 28, segW, 6, 3, true, false);
      } else if (i === currentTip) {
        const p = Math.min(1, elapsed / 6.5);
        ctx.fillStyle = '#f36f21';
        roundRect(ctx, padX + i * (segW + 6), 28, segW * p, 6, 3, true, false);
      }
    }

    // Header badge
    ctx.fillStyle = 'rgba(255,255,255,0.12)';
    roundRect(ctx, padX, 54, w - padX * 2, 44, 10, true, false);
    ctx.fillStyle = '#f5d0fe';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('FESNA • PROCESOS CONTABLES', padX + 14, 81);
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'right';
    ctx.fillText('SNIES 111389/111390', w - padX - 14, 81);

    // Capsule tag
    ctx.fillStyle = tip.accent;
    roundRect(ctx, padX, 138, w - padX * 2, 34, 8, true, false);
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.fillText(tip.num, w / 2, 160);

    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 36px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    let y = 235;
    tip.title.split('\n').forEach((line) => {
      ctx.fillText(line, padX, y);
      y += 44;
    });

    // Description box
    ctx.fillStyle = 'rgba(0,0,0,0.28)';
    roundRect(ctx, padX, y + 10, w - padX * 2, 175, 14, true, false);
    ctx.fillStyle = '#f8fafc';
    ctx.font = '600 18px "Plus Jakarta Sans", Arial, sans-serif';
    wrapText(ctx, tip.desc, padX + 20, y + 48, w - padX * 2 - 40, 28);

    // 3 Feature pills
    const pills = [tip.pill1, tip.pill2, tip.pill3];
    pills.forEach((pText, idx) => {
      const py = 540 + idx * 72;
      ctx.fillStyle = 'rgba(255,255,255,0.12)';
      ctx.strokeStyle = '#f5d0fe';
      ctx.lineWidth = 1.5;
      roundRect(ctx, padX, py, w - padX * 2, 54, 12, true, true);
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 17px "Plus Jakarta Sans", Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(`✔ ${pText}`, w / 2, py + 33);
    });

    // Bottom subtitle
    ctx.fillStyle = 'rgba(20, 4, 24, 0.9)';
    roundRect(ctx, padX, h - 110, w - padX * 2, 64, 10, true, false);
    ctx.fillStyle = '#fef08a';
    ctx.font = 'bold 15px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Serie de Reels con Guion IA • Técnica Profesional FESNA', w / 2, h - 72);

    if (running) requestAnimationFrame(drawReel);
  }

  requestAnimationFrame(drawReel);

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      currentTip = (currentTip + 1) % tips.length;
      startTime = performance.now();
    });
  }

  if (uploadInput && customVideo) {
    uploadInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      running = false;
      canvas.style.display = 'none';
      customVideo.style.display = 'block';
      customVideo.src = URL.createObjectURL(file);
      customVideo.play();
    });
  }
}

// 7. Contaduría Nivel 2: Animación 2D Asistida por IA (Tecnología en Gestión Contable y Financiera)
function initContaduriaAnimacion2D() {
  const canvas = document.getElementById('canvas-anim2d-tgcf');
  const switchBtn = document.getElementById('switch-anim2d-tgcf');
  const uploadInput = document.getElementById('upload-anim2d-tgcf');
  const customVideo = document.getElementById('custom-anim2d-tgcf');

  if (!canvas) return;
  canvas.width = 960;
  canvas.height = 540;
  const ctx = canvas.getContext('2d');

  let running = true;
  let slideIdx = 0;
  let startTime = performance.now();

  function drawAnim2D(now) {
    const elapsed = (now - startTime) / 1000;
    const f = easeOutCubic(Math.min(1, (elapsed % 6) / 2.0));
    const w = canvas.width;
    const h = canvas.height;

    const grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#27072c');
    grad.addColorStop(1, '#61126b');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    ctx.fillStyle = 'rgba(255,255,255,0.1)';
    roundRect(ctx, 45, 26, w - 90, 52, 10, true, false);
    ctx.fillStyle = '#f5d0fe';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('ANIMACIÓN 2D ASISTIDA POR IA • TECNOLOGÍA EN GESTIÓN CONTABLE Y FINANCIERA', 65, 50);
    ctx.fillStyle = '#e2e8f0';
    ctx.font = '13px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.fillText('SNIES Presencial: 111391 | Virtual: 111392 • Res. 009956 (03/JUN/2022) • 5 Semestres • 86/87 Créditos', 65, 68);

    if (slideIdx === 0) {
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 22px "Plus Jakarta Sans", Arial, sans-serif';
      ctx.fillText('Exposición Didáctica: Estados Financieros, Liquidez y Presupuestos', 50, 118);

      const cards = [
        { title: '1. Estados Financieros', sub: 'Contabilidad Financiera y NIIF', val: '100%', col: '#d946ef', h: 210 },
        { title: '2. Indicadores Liquidez', sub: 'Razón Corriente y Capital Trabajo', val: '1.8x', col: '#f36f21', h: 185 },
        { title: '3. Presupuestos y Costos', sub: 'Costos Estándar y por Procesos', val: '95%', col: '#a855f7', h: 195 },
        { title: '4. Tributaria Intermedia', sub: 'Impuestos Nal., Deptal. y Mpal.', val: 'DIAN', col: '#38bdf8', h: 205 }
      ];

      cards.forEach((c, i) => {
        const x = 55 + i * 218;
        const barH = c.h * f;
        const y = 415 - barH;

        ctx.fillStyle = c.col;
        roundRect(ctx, x, y, 185, barH, 12, true, false);

        ctx.fillStyle = '#ffffff';
        ctx.font = '800 26px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(c.val, x + 92, y - 14);

        ctx.font = 'bold 15px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.fillText(c.title, x + 92, 445);

        ctx.fillStyle = '#f5d0fe';
        ctx.font = '12.5px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.fillText(c.sub, x + 92, 468);
      });
    } else {
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 22px "Plus Jakarta Sans", Arial, sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('Ruta Curricular del Tecnólogo (Períodos 4.º y 5.º – 86/87 Créditos)', 50, 118);

      const items = [
        { name: 'Contabilidad Financiera y Normas Internacionales', pct: 96, col: '#d946ef' },
        { name: 'Indicadores Contables Financieros y Planeación Financiera', pct: 94, col: '#f36f21' },
        { name: 'Impuestos Nacionales, Departamentales y Municipales', pct: 95, col: '#a855f7' },
        { name: 'Costos Estándar y por Procesos + Estadística Inferencial', pct: 92, col: '#38bdf8' }
      ];

      items.forEach((it, idx) => {
        const y = 160 + idx * 78;
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 16px "Plus Jakarta Sans", Arial, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(it.name, 55, y);

        ctx.fillStyle = 'rgba(255,255,255,0.14)';
        roundRect(ctx, 55, y + 12, 740, 26, 8, true, false);

        ctx.fillStyle = it.col;
        roundRect(ctx, 55, y + 12, Math.max(24, 740 * (it.pct / 100) * f), 26, 8, true, false);

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 15px monospace';
        ctx.fillText(`${Math.round(it.pct * f)}%`, 815, y + 30);
      });
    }

    if (running) requestAnimationFrame(drawAnim2D);
  }

  requestAnimationFrame(drawAnim2D);

  if (switchBtn) {
    switchBtn.addEventListener('click', () => {
      slideIdx = slideIdx === 0 ? 1 : 0;
      startTime = performance.now();
    });
  }

  if (uploadInput && customVideo) {
    uploadInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      running = false;
      canvas.style.display = 'none';
      customVideo.style.display = 'block';
      customVideo.src = URL.createObjectURL(file);
      customVideo.play();
    });
  }
}

// 8. Contaduría Nivel 3: Testimonio Recreado con Avatar IA (Valeria Mendoza - Egresada Ficticia)
function initContaduriaAvatarTestimonial() {
  const canvas = document.getElementById('canvas-avatar-cp');
  const audio = document.getElementById('audio-avatar-cp');
  const playBtn = document.getElementById('play-avatar-cp');
  const uploadInput = document.getElementById('upload-avatar-cp');
  const customVideo = document.getElementById('custom-avatar-cp');

  if (!canvas || !audio) return;
  canvas.width = 960;
  canvas.height = 540;
  const ctx = canvas.getContext('2d');
  let animFrame = null;

  function drawAvatarFrame() {
    const w = canvas.width;
    const h = canvas.height;
    const speaking = !audio.paused;
    const t = Date.now() * 0.008;

    const grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#240529');
    grad.addColorStop(1, '#581063');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Header
    ctx.fillStyle = 'rgba(255,255,255,0.12)';
    roundRect(ctx, 45, 28, w - 90, 44, 10, true, false);
    ctx.fillStyle = '#f5d0fe';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('TESTIMONIO RECREADO CON AVATAR IA • CONTADURÍA PÚBLICA FESNA', 65, 55);
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'right';
    ctx.fillText('SNIES 111387 / 111388 • RES. 009957', w - 65, 55);

    // Left Avatar Illustration Circle
    const cx = 210;
    const cy = 265;
    if (speaking) {
      ctx.strokeStyle = 'rgba(243, 111, 33, 0.55)';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(cx, cy, 105 + Math.sin(t) * 8, 0, Math.PI * 2);
      ctx.stroke();
    }

    ctx.fillStyle = '#aa38b9';
    ctx.beginPath();
    ctx.arc(cx, cy, 94, 0, Math.PI * 2);
    ctx.fill();

    // Stylized Vector Avatar Face & Suit
    ctx.fillStyle = '#fde68a';
    ctx.beginPath();
    ctx.arc(cx, cy - 18, 36, 0, Math.PI * 2);
    ctx.fill();

    // Hair
    ctx.fillStyle = '#1e1b4b';
    ctx.beginPath();
    ctx.arc(cx, cy - 26, 38, Math.PI, Math.PI * 2);
    ctx.fill();

    // Eyes
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(cx - 12, cy - 20, 3.5, 0, Math.PI * 2);
    ctx.arc(cx + 12, cy - 20, 3.5, 0, Math.PI * 2);
    ctx.fill();

    // Animated Mouth synced with speech
    ctx.fillStyle = '#be123c';
    const mouthOpen = speaking ? 4 + Math.abs(Math.sin(t * 1.8)) * 9 : 3;
    ctx.beginPath();
    ctx.ellipse(cx, cy - 4, 10, mouthOpen, 0, 0, Math.PI * 2);
    ctx.fill();

    // Suit shoulders
    ctx.fillStyle = '#0a2e52';
    roundRect(ctx, cx - 52, cy + 24, 104, 52, 22, true, false);

    // Avatar Name Tag
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 17px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Valeria Mendoza (Avatar IA)', cx, cy + 125);
    ctx.fillStyle = '#f5d0fe';
    ctx.font = '13px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.fillText('Egresada Virtual • Contadora Pública FESNA', cx, cy + 146);

    // Right Speech Bubble & Topics
    ctx.fillStyle = 'rgba(255,255,255,0.1)';
    roundRect(ctx, 360, 105, 550, 315, 16, true, false);

    ctx.fillStyle = '#f36f21';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('PERSPECTIVA DE EGRESADA VIRTUAL (PERSONAJE FICTICIO IA)', 385, 138);

    ctx.fillStyle = '#ffffff';
    ctx.font = '800 24px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.fillText('"3 Títulos Profesionales en 9 Períodos"', 385, 174);

    const quote =
      '"Gracias a los ciclos propedéuticos de FESNA me titulé como Técnica en Procesos Contables, Tecnóloga en Gestión Contable y Financiera, y Contadora Pública (155/159 créditos). Hoy lidero procesos de Normas Internacionales (NIIF/NIC), Auditoría Forense, Revisoría Fiscal y Análisis Macrofinanciero con ética profesional."';
    ctx.fillStyle = '#f1f5f9';
    ctx.font = '16px "Plus Jakarta Sans", Arial, sans-serif';
    wrapText(ctx, quote, 385, 212, 500, 26);

    // Bottom status bar
    ctx.fillStyle = 'rgba(0,0,0,0.45)';
    roundRect(ctx, 45, h - 68, w - 90, 44, 8, true, false);
    ctx.fillStyle = '#fef08a';
    ctx.font = 'bold 14px "Plus Jakarta Sans", Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(
      speaking
        ? '🔊 Reproduciendo Testimonio de Avatar IA (Sin clonación de rostros ni voces reales)'
        : '▶ Haz clic en "Reproducir Testimonio Avatar IA" para escuchar a la egresada virtual',
      w / 2,
      h - 41
    );

    if (speaking) {
      animFrame = requestAnimationFrame(drawAvatarFrame);
    }
  }

  drawAvatarFrame();

  if (playBtn) {
    playBtn.addEventListener('click', () => {
      if (audio.paused) {
        audio.play();
        playBtn.textContent = '⏸ Pausar Testimonio IA';
        animFrame = requestAnimationFrame(drawAvatarFrame);
      } else {
        audio.pause();
        playBtn.textContent = '▶ Reproducir Testimonio Avatar IA';
        cancelAnimationFrame(animFrame);
        drawAvatarFrame();
      }
    });
  }

  audio.addEventListener('ended', () => {
    if (playBtn) playBtn.textContent = '▶ Reproducir Testimonio Avatar IA';
    cancelAnimationFrame(animFrame);
    drawAvatarFrame();
  });

  if (uploadInput && customVideo) {
    uploadInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      audio.pause();
      cancelAnimationFrame(animFrame);
      canvas.style.display = 'none';
      customVideo.style.display = 'block';
      customVideo.src = URL.createObjectURL(file);
      customVideo.play();
    });
  }
}

function wrapText(ctx, text, x, y, maxWidth, lineHeight) {
  const words = text.split(' ');
  let line = '';
  let curY = y;
  for (let n = 0; n < words.length; n++) {
    const testLine = line + words[n] + ' ';
    const metrics = ctx.measureText(testLine);
    if (metrics.width > maxWidth && n > 0) {
      ctx.fillText(line, x, curY);
      line = words[n] + ' ';
      curY += lineHeight;
    } else {
      line = testLine;
    }
  }
  ctx.fillText(line, x, curY);
}

function easeOutCubic(x) {
  return 1 - Math.pow(1 - x, 3);
}

function roundRect(ctx, x, y, width, height, radius, fill, stroke) {
  ctx.beginPath();
  ctx.moveTo(x + radius, y);
  ctx.lineTo(x + width - radius, y);
  ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
  ctx.lineTo(x + width, y + height - radius);
  ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
  ctx.lineTo(x + radius, y + height);
  ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
  ctx.lineTo(x, y + radius);
  ctx.quadraticCurveTo(x, y, x + radius, y);
  ctx.closePath();
  if (fill) ctx.fill();
  if (stroke) ctx.stroke();
}
