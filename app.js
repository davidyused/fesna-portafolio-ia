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

/* ==========================================================================
   INTERACTIVIDAD PARA MARKETING Y PUBLICIDAD (EXAMEN FINAL)
   ========================================================================== */

// 1. Chatbot Conversacional IA FESNA
const mktKnowledgeBase = {
  titulos: "En FESNA te formas bajo el modelo de ciclos propedéuticos y obtienes tres (3) títulos oficiales a lo largo de tu formación: 1) Técnico Profesional en Procesos de Comercialización y Comunicación Publicitaria (3 períodos, 49 créditos), 2) Tecnólogo en Gestión Comercial y Publicidad (5 períodos acumulados, 82 créditos) y 3) Profesional Universitario en Marketing y Publicidad (8 períodos acumulados, 133 créditos).",
  snies: "Nuestros programas cuentan con registros calificados aprobados por el Ministerio de Educación Nacional (MEN) el 30 de abril de 2026: Técnica Profesional (Res. 011477, SNIES Presencial 119246 / Virtual 119247), Tecnología (Res. 011476, SNIES Presencial 119245 / Virtual 119244) y Profesional Universitario (Res. 011475, SNIES Presencial 119242 / Virtual 119243).",
  creditos: "El plan de estudios está estructurado en períodos cuatrimestrales para que avances más rápido: Técnica Profesional (3 períodos, 49 créditos), Tecnología (+2 períodos para 5 acumulados, 82 créditos) y Grado Profesional (+3 períodos para 8 acumulados, 133 créditos).",
  modalidad: "¡Estudia a tu propio ritmo! Todos nuestros ciclos están disponibles en modalidad PRESENCIAL en Bogotá D.C. (Diag. 47A Sur # 53-46, Barrio Venecia) y en modalidad VIRTUAL con acceso a plataforma interactiva 24/7 desde cualquier lugar del país.",
  materias: "El plan de estudios abarca desde Fundamentos de Mercadeo, Diseño Publicitario y Software de Retoque en la Técnica; pasando por Experiencia UX, Redacción Publicitaria y Algoritmos SEM/SEO en la Tecnología; hasta Neuromarketing, Estrategia de Branding y Mercadeo Internacional en el nivel Profesional.",
  costos: "La Fundación de Educación Superior Nueva América cuenta con planes de financiación directa sin intermediarios, descuentos por pronto pago y facilidades de homologación para que tu matrícula sea accesible. Comunícate al PBX (601) 746 8757 o vía WhatsApp al (+57) 317 400 1068 para una cotización personalizada."
};

function handleChatChip(topic) {
  const answer = mktKnowledgeBase[topic];
  if (!answer) return;

  const topicsMap = {
    titulos: "¿Qué títulos obtengo en Marketing por ciclos?",
    snies: "¿Cuáles son los códigos SNIES y resoluciones oficiales?",
    creditos: "¿Cuántos créditos y períodos dura la carrera?",
    modalidad: "¿En qué modalidades puedo estudiar?"
  };

  addChatMessage(topicsMap[topic] || topic, 'user');
  setTimeout(() => {
    addChatMessage(answer, 'bot');
  }, 400);
}

function submitChatInput() {
  const input = document.getElementById('mkt-chat-input');
  if (!input) return;
  const q = input.value.trim();
  if (!q) return;

  addChatMessage(q, 'user');
  input.value = '';

  setTimeout(() => {
    const lower = q.toLowerCase();
    let reply = "¡Gracias por tu consulta! La Fundación de Educación Superior Nueva América (FESNA) ofrece el programa de Marketing y Publicidad por ciclos propedéuticos (Técnica Profesional, Tecnología y Grado Profesional) en modalidades Presencial y Virtual en Bogotá D.C. Comunícate a nuestro PBX (601) 746 8757 o visítanos en www.nuevaamerica.edu.co para asesorarte.";

    if (lower.includes('titulo') || lower.includes('ciclo') || lower.includes('carrera') || lower.includes('homolog')) {
      reply = mktKnowledgeBase.titulos;
    } else if (lower.includes('snies') || lower.includes('resoluc') || lower.includes('men') || lower.includes('legal') || lower.includes('registro')) {
      reply = mktKnowledgeBase.snies;
    } else if (lower.includes('credito') || lower.includes('durac') || lower.includes('semestre') || lower.includes('periodo') || lower.includes('tiempo')) {
      reply = mktKnowledgeBase.creditos;
    } else if (lower.includes('modal') || lower.includes('virtual') || lower.includes('presencial') || lower.includes('donde') || lower.includes('sede')) {
      reply = mktKnowledgeBase.modalidad;
    } else if (lower.includes('materia') || lower.includes('pensum') || lower.includes('asignatura') || lower.includes('estudio')) {
      reply = mktKnowledgeBase.materias;
    } else if (lower.includes('costo') || lower.includes('precio') || lower.includes('valor') || lower.includes('cuanto') || lower.includes('matricula')) {
      reply = mktKnowledgeBase.costos;
    }

    addChatMessage(reply, 'bot');
  }, 450);
}

function addChatMessage(text, sender) {
  const container = document.getElementById('mkt-chat-messages');
  if (!container) return;

  const msgDiv = document.createElement('div');
  msgDiv.className = `chat-msg ${sender}`;

  const avatarDiv = document.createElement('div');
  avatarDiv.className = 'chat-avatar';
  avatarDiv.textContent = sender === 'bot' ? 'NA' : 'TÚ';

  const bubbleDiv = document.createElement('div');
  bubbleDiv.className = 'chat-bubble';
  bubbleDiv.innerHTML = text;

  msgDiv.appendChild(avatarDiv);
  msgDiv.appendChild(bubbleDiv);

  container.appendChild(msgDiv);
  container.scrollTop = container.scrollHeight;
}

// 2. Buyer Persona Copywriting Tabs
function switchCopyTab(tab) {
  const tabs = ['aida', 'pas', 'story'];
  tabs.forEach(t => {
    const panel = document.getElementById(`copy-panel-${t}`);
    if (panel) panel.style.display = (t === tab) ? 'block' : 'none';
  });

  const buttons = document.querySelectorAll('.copy-tab-btn');
  buttons.forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('onclick').includes(tab));
  });
}

// 3. Simulador de Pauta Digital & Auditoría IA
function updateAdsSimulator() {
  const bInput = document.getElementById('sim-budget');
  const cpcInput = document.getElementById('sim-cpc');
  const ctrInput = document.getElementById('sim-ctr');

  if (!bInput || !cpcInput || !ctrInput) return;

  const budget = parseInt(bInput.value, 10);
  const cpc = parseInt(cpcInput.value, 10);
  const ctr = parseFloat(ctrInput.value);

  // Formato de visualización
  const dispBudget = document.getElementById('disp-budget');
  const dispCpc = document.getElementById('disp-cpc');
  const dispCtr = document.getElementById('disp-ctr');

  if (dispBudget) dispBudget.textContent = `$${budget.toLocaleString('es-CO')} COP`;
  if (dispCpc) dispCpc.textContent = `$${cpc.toLocaleString('es-CO')} COP`;
  if (dispCtr) dispCtr.textContent = `${ctr.toFixed(1)}%`;

  // Cálculos de métricas digitales
  const clicks = Math.round(budget / cpc);
  const impressions = Math.round(clicks / (ctr / 100));
  const conversionRate = 0.08; // 8% tasa de conversión estimada
  const leads = Math.max(1, Math.round(clicks * conversionRate));
  const cpa = Math.round(budget / leads);
  const roas = (ctr >= 3.5 ? 4.6 : (ctr >= 2.5 ? 3.8 : 2.5)).toFixed(1);

  // Actualización en DOM
  const kpiImp = document.getElementById('kpi-impressions');
  const kpiClk = document.getElementById('kpi-clicks');
  const kpiLds = document.getElementById('kpi-leads');
  const kpiCpa = document.getElementById('kpi-cpa');
  const kpiRoas = document.getElementById('kpi-roas');

  if (kpiImp) kpiImp.textContent = impressions.toLocaleString('es-CO');
  if (kpiClk) kpiClk.textContent = clicks.toLocaleString('es-CO');
  if (kpiLds) kpiLds.textContent = leads.toLocaleString('es-CO');
  if (kpiCpa) kpiCpa.textContent = `$${cpa.toLocaleString('es-CO')}`;
  if (kpiRoas) kpiRoas.textContent = `${roas}x`;

  // Diagnóstico IA
  const verdictText = document.getElementById('ai-verdict-text');
  const verdictBox = document.getElementById('ai-verdict-box');
  if (verdictText && verdictBox) {
    if (ctr >= 3.2 && cpc <= 1000) {
      verdictBox.style.borderLeftColor = '#22c55e';
      verdictText.innerHTML = `<strong>Rendimiento sobresaliente:</strong> Con un CTR del ${ctr.toFixed(1)}% y un CPC de $${cpc}, el algoritmo de Meta/Google Ads clasifica los anuncios con alta relevancia cualitativa. Proyectas generar <strong>${leads} leads calificados</strong> a un CPA óptimo de <strong>$${cpa.toLocaleString('es-CO')} COP</strong>. Recomendación: Escalar presupuesto a canales de remarketing.`;
    } else if (cpc > 1400) {
      verdictBox.style.borderLeftColor = '#eab308';
      verdictText.innerHTML = `<strong>Atención a costos por clic:</strong> El CPC de $${cpc} es elevado para el segmento educativo universitario. La IA recomienda optimizar la segmentación geográfica hacia Bogotá y Cundinamarca e implementar copys orientados a los 3 títulos propedéuticos para elevar la conversión orgánica.`;
    } else {
      verdictBox.style.borderLeftColor = '#3b82f6';
      verdictText.innerHTML = `<strong>Rendimiento balanceado:</strong> Generarás <strong>${clicks.toLocaleString('es-CO')} visitas cualificadas</strong> al portal institucional y <strong>${leads} aspirantes inscritos</strong>. La IA sugiere realizar pruebas A/B entre el formato de Reel vertical y banners display para mejorar la tasa de clics en un +0.8%.`;
    }
  }
}

// 4. Pitch Deck Interactivo de Marketing Global
const pitchSlides = [
  {
    title: "1. Visión Global: Redefiniendo la Educación Publicitaria",
    subtitle: "FUNDACIÓN DE EDUCACIÓN SUPERIOR NUEVA AMÉRICA (FESNA)",
    body: `
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-top:0.75rem;">
        <div>
          <h5 style="color:#fca5a5; font-size:0.95rem; margin-bottom:0.4rem;">🎯 La Disrupción Educativa</h5>
          <p style="font-size:0.86rem; color:#cbd5e1; line-height:1.5;">
            FESNA rompe el paradigma de la educación superior rígida mediante un ecosistema de ciclos propedéuticos que combina <strong>rigor académico</strong>, <strong>tecnología de Inteligencia Artificial</strong> y <strong>empleabilidad acelerada</strong>.
          </p>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:1rem; border-radius:10px; border-left:3px solid #f87171;">
          <strong style="color:#ffffff; font-size:0.88rem; display:block; margin-bottom:0.25rem;">Nuestra Promesa de Valor:</strong>
          <span style="font-size:0.82rem; color:#94a3b8;">
            Tres títulos oficiales reconocidos por el Ministerio de Educación Nacional (MEN) en un recorrido secuencial de 8 períodos cuatrimestrales.
          </span>
        </div>
      </div>
    `
  },
  {
    title: "2. Oportunidad de Mercado: La Brecha del Talento Digital",
    subtitle: "DEMANDA CRECIENTE DE PUBLICISTAS CON DOMINIO DE IA",
    body: `
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin-top:0.75rem;">
        <div style="background:rgba(255,255,255,0.05); padding:1rem; border-radius:10px; text-align:center;">
          <div style="font-size:1.8rem; font-weight:800; color:#f87171;">+68%</div>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0.3rem 0 0;">Crecimiento en la demanda de creativos con dominio de analítica publicitaria en LATAM.</p>
        </div>
        <div style="background:rgba(255,255,255,0.05); padding:1rem; border-radius:10px; text-align:center;">
          <div style="font-size:1.8rem; font-weight:800; color:#fb923c;">5 Años</div>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0.3rem 0 0;">Tiempo excesivo que exigen las universidades tradicionales para entregar un primer título.</p>
        </div>
        <div style="background:rgba(255,255,255,0.05); padding:1rem; border-radius:10px; text-align:center;">
          <div style="font-size:1.8rem; font-weight:800; color:#4ade80;">3 Títulos</div>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0.3rem 0 0;">La solución FESNA: inserción laboral desde el tercer período académico.</p>
        </div>
      </div>
    `
  },
  {
    title: "3. Solución: Ruta Propedéutica de 3 Niveles Acreditados",
    subtitle: "RESPALDO JURÍDICO DEL MINISTERIO DE EDUCACIÓN NACIONAL",
    body: `
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.85rem; margin-top:0.75rem;">
        <div style="background:rgba(212,59,39,0.18); border:1px solid #f87171; padding:0.9rem; border-radius:10px;">
          <span style="font-size:0.72rem; color:#fca5a5; font-weight:800;">NIVEL 1 • 3 PERÍODOS</span>
          <h5 style="color:#ffffff; font-size:0.88rem; margin:0.25rem 0;">Técnica Profesional</h5>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0;">SNIES 119246/119247 • Res. 011477 (49 créditos). Enfoque operativo y venta directa.</p>
        </div>
        <div style="background:rgba(179,35,25,0.18); border:1px solid #f87171; padding:0.9rem; border-radius:10px;">
          <span style="font-size:0.72rem; color:#fca5a5; font-weight:800;">NIVEL 2 • 5 PERÍODOS</span>
          <h5 style="color:#ffffff; font-size:0.88rem; margin:0.25rem 0;">Tecnología en Gestión</h5>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0;">SNIES 119245/119244 • Res. 011476 (82 créditos). Pauta digital SEM/SEO y UX.</p>
        </div>
        <div style="background:rgba(123,31,23,0.25); border:1px solid #f87171; padding:0.9rem; border-radius:10px;">
          <span style="font-size:0.72rem; color:#fca5a5; font-weight:800;">NIVEL 3 • 8 PERÍODOS</span>
          <h5 style="color:#ffffff; font-size:0.88rem; margin:0.25rem 0;">Marketing y Publicidad</h5>
          <p style="font-size:0.78rem; color:#cbd5e1; margin:0;">SNIES 119242/119243 • Res. 011475 (133 créditos). Dirección estratégica y global.</p>
        </div>
      </div>
    `
  },
  {
    title: "4. Estrategia de Expansión Transmedia y Omnicanalidad",
    subtitle: "ECOSISTEMA DE CAPTACIÓN ASISTIDO POR INTELIGENCIA ARTIFICIAL",
    body: `
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.25rem; margin-top:0.75rem;">
        <div>
          <h5 style="color:#fca5a5; font-size:0.92rem; margin-bottom:0.35rem;">🚀 Canales de Atracción Masiva</h5>
          <ul style="padding-left:1.15rem; font-size:0.82rem; color:#cbd5e1; display:grid; gap:0.35rem; margin:0;">
            <li>Publicidad programática display segmentada por intencionalidad de estudio.</li>
            <li>Reels y TikToks nativos con subtitulado y ganchos de micro-aprendizaje.</li>
            <li>Inbound marketing mediante tests de orientación vocacional automatizados.</li>
          </ul>
        </div>
        <div>
          <h5 style="color:#fca5a5; font-size:0.92rem; margin-bottom:0.35rem;">💬 Conversión Conversacional</h5>
          <ul style="padding-left:1.15rem; font-size:0.82rem; color:#cbd5e1; display:grid; gap:0.35rem; margin:0;">
            <li>Asistentes virtuales entrenados con IA en WhatsApp institucional y web.</li>
            <li>Atención en tiempo real con tiempos de respuesta menores a 5 segundos.</li>
            <li>Agendamiento de matrícula y validación inmediata de homologación.</li>
          </ul>
        </div>
      </div>
    `
  },
  {
    title: "5. Unit Economics & Proyección de Retorno Publicitario",
    subtitle: "MÉTRICAS CLAVE DE ADQUISICIÓN Y RETENCIÓN (ROAS & LTV)",
    body: `
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.75rem; margin-top:0.85rem; text-align:center;">
        <div style="background:rgba(255,255,255,0.06); padding:0.85rem; border-radius:8px;">
          <span style="font-size:0.72rem; color:#94a3b8; display:block;">CAC Estimado</span>
          <strong style="font-size:1.2rem; color:#4ade80;">$145.000 COP</strong>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:0.85rem; border-radius:8px;">
          <span style="font-size:0.72rem; color:#94a3b8; display:block;">LTV Alumno</span>
          <strong style="font-size:1.2rem; color:#38bdf8;">$8.4M COP</strong>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:0.85rem; border-radius:8px;">
          <span style="font-size:0.72rem; color:#94a3b8; display:block;">Ratio LTV / CAC</span>
          <strong style="font-size:1.2rem; color:#fbbf24;">57.9x</strong>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:0.85rem; border-radius:8px;">
          <span style="font-size:0.72rem; color:#94a3b8; display:block;">ROAS de Pauta</span>
          <strong style="font-size:1.2rem; color:#f87171;">4.2x</strong>
        </div>
      </div>
      <p style="font-size:0.8rem; color:#94a3b8; text-align:center; margin-top:1rem;">
        *Modelo financiero sustentado en la permanencia del estudiante durante los ciclos propedéuticos consecutivos.
      </p>
    `
  },
  {
    title: "6. Llamado a la Acción & Expansión de Marca FESNA",
    subtitle: "CONSTRUYENDO EL LIDERAZGO COMERCIAL DEL MAÑANA",
    body: `
      <div style="text-align:center; padding:1rem 0;">
        <h4 style="color:#ffffff; font-size:1.25rem; margin-bottom:0.6rem;">
          "Siempre Nueva, Siempre Conectada con el Futuro Global"
        </h4>
        <p style="font-size:0.9rem; color:#cbd5e1; max-width:620px; margin:0 auto 1.25rem; line-height:1.5;">
          FESNA consolida su liderazgo en Bogotá y Colombia, formando publicistas y mercadólogos que transforman marcas con ética, visión analítica y dominio de la inteligencia artificial.
        </p>
        <div style="display:inline-flex; gap:0.75rem; flex-wrap:wrap; justify-content:center;">
          <a href="https://www.nuevaamerica.edu.co" target="_blank" class="btn btn-primary" style="background:#d43b27; border:none; padding:0.6rem 1.4rem;">
            🌐 Visitar Portal www.nuevaamerica.edu.co
          </a>
          <a href="DOCUMENTACION_SUSTENTACION_CAMPANA_FESNA_DAVID_PULIDO.docx" download class="btn btn-outline" style="border-color:#fca5a5; color:#ffffff; padding:0.6rem 1.4rem;">
            📄 Descargar Documentación APA 7
          </a>
        </div>
      </div>
    `
  }
];

let currentPitchIndex = 0;

function renderPitchSlide(idx) {
  currentPitchIndex = idx;
  const slide = pitchSlides[idx];
  if (!slide) return;

  const titleEl = document.getElementById('pitch-slide-title');
  const numEl = document.getElementById('pitch-slide-num');
  const bodyEl = document.getElementById('pitch-slide-body');
  const prevBtn = document.getElementById('pitch-prev-btn');
  const nextBtn = document.getElementById('pitch-next-btn');

  if (titleEl) titleEl.textContent = slide.title;
  if (numEl) numEl.textContent = `${idx + 1} / ${pitchSlides.length}`;
  if (bodyEl) bodyEl.innerHTML = slide.body;

  if (prevBtn) prevBtn.disabled = (idx === 0);
  if (nextBtn) nextBtn.disabled = (idx === pitchSlides.length - 1);

  // Puntos indicadores
  const dots = document.querySelectorAll('.pitch-dot');
  dots.forEach((dot, dIdx) => {
    dot.classList.toggle('active', dIdx === idx);
  });
}

function nextPitchSlide() {
  if (currentPitchIndex < pitchSlides.length - 1) {
    renderPitchSlide(currentPitchIndex + 1);
  }
}

function prevPitchSlide() {
  if (currentPitchIndex > 0) {
    renderPitchSlide(currentPitchIndex - 1);
  }
}

function goToPitchSlide(idx) {
  renderPitchSlide(idx);
}

// Inicialización de componentes de Marketing al cargar el documento
document.addEventListener('DOMContentLoaded', () => {
  // Inicializar simulador de pauta si está en la página
  if (document.getElementById('sim-budget')) {
    updateAdsSimulator();
  }

  // Inicializar pitch deck si está en la página
  if (document.getElementById('pitch-slide-title')) {
    renderPitchSlide(0);
  }
});

