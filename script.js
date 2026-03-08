document.addEventListener('DOMContentLoaded', () => {
    // ─── PRELOADER CONTROL ──────────────────────────────────────────────────
    const preloader = document.getElementById('preloader');
    if (preloader) {
        // Duración de exactamente 4 segundos (4000ms)
        setTimeout(() => {
            preloader.classList.add('fade-out');
            document.body.classList.remove('loading');

            // Eliminar del DOM después de la transición de fade para optimizar
            setTimeout(() => {
                preloader.remove();
            }, 800);
        }, 1500);
    }


    // ─── NAVBAR SCROLL EFFECT ───────────────────────────────────────────────
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    // ─── MOBILE MENU ────────────────────────────────────────────────────────
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const mobileOverlay = document.getElementById('mobileNavOverlay');
    const mobileClose = document.getElementById('mobileNavClose');

    function openMobileMenu() {
        mobileOverlay.classList.add('open');
        mobileBtn.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeMobileMenu() {
        mobileOverlay.classList.remove('open');
        mobileBtn.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (mobileBtn) mobileBtn.addEventListener('click', openMobileMenu);
    if (mobileClose) mobileClose.addEventListener('click', closeMobileMenu);

    // Close mobile menu when clicking overlay links
    if (mobileOverlay) {
        mobileOverlay.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }

    // ─── SMOOTH SCROLL ──────────────────────────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const navbarHeight = navbar.offsetHeight;
                const targetPos = target.getBoundingClientRect().top + window.scrollY - navbarHeight;
                window.scrollTo({ top: targetPos, behavior: 'smooth' });
            }
        });
    });

    // ─── PARTICLES SYSTEM ───────────────────────────────────────────────────
    const particlesContainer = document.getElementById('particles');
    const particleCount = window.innerWidth < 768 ? 20 : 50;

    for (let i = 0; i < particleCount; i++) {
        createParticle();
    }

    function createParticle() {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        const size = Math.random() * 4 + 1;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}vw`;
        particle.style.setProperty('--duration', `${Math.random() * 20 + 10}s`);
        particle.style.setProperty('--drift', `${(Math.random() - 0.5) * 100}px`);
        particle.style.animationDelay = `-${Math.random() * 20}s`;
        particlesContainer.appendChild(particle);
    }

    // ─── SCROLL REVEAL ──────────────────────────────────────────────────────
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

    revealElements.forEach(el => revealObserver.observe(el));

    // Trigger hero reveals immediately (they're in viewport on load)
    setTimeout(() => {
        document.querySelectorAll('.hero .reveal').forEach(el => {
            el.classList.add('visible');
        });
    }, 100);

    // ─── ANIMATED COUNTERS ──────────────────────────────────────────────────
    const counters = document.querySelectorAll('.metric-number[data-target]');

    // ─── EDUCATION TIMELINE ANIMATION ────────────────────────────────────
    const eduCards = document.querySelectorAll('.edu-card');
    const eduObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const line = entry.target.querySelector('.edu-line');
                if (line) {
                    // Pequeño delay para que se vea el inicio tras el reveal de la card
                    setTimeout(() => {
                        line.classList.add('completed');
                    }, 400);
                }
                eduObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    eduCards.forEach(card => eduObserver.observe(card));

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    function animateCounter(el) {
        const target = parseInt(el.dataset.target);
        const suffix = el.dataset.suffix || '';
        const prefix = el.dataset.prefix || '+';
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            el.textContent = (target > 2 ? prefix : '') + Math.floor(current) + suffix;
        }, 16);
    }

    // ─── FLIP CARDS MOBILE ──────────────────────────────────────────────────
    if (window.matchMedia('(hover: none)').matches) {
        document.querySelectorAll('.flip-card').forEach(card => {
            card.addEventListener('click', () => {
                const inner = card.querySelector('.flip-card-inner');
                inner.classList.toggle('flipped-active');
            });
        });
    }

    // ─── LEAD FORM MAKE WEBHOOK ─────────────────────────────────────────────
    // ⚠️ REEMPLAZA ESTA URL CON TU WEBHOOK DE MAKE
    const MAKE_WEBHOOK_URL = 'https://hook.us2.make.com/ocfah09brrq8gef6ageov2w2dl6mj2do';

    const leadFormMake = document.getElementById('form-servicios-erickddp');
    const formStatusMake = document.getElementById('formStatus');
    const submitBtnMake = leadFormMake ? leadFormMake.querySelector('button[type="submit"]') : null;

    if (leadFormMake && submitBtnMake) {
        leadFormMake.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Validación Or/O: Debe haber WhatsApp o Correo
            const whatsapp = leadFormMake.whatsapp.value.trim();
            const email = leadFormMake.email.value.trim();

            if (!whatsapp && !email) {
                formStatusMake.textContent = 'Por favor, proporciona al menos un medio de contacto (WhatsApp o Correo)';
                formStatusMake.className = 'form-status error';
                return; // Detiene el envío
            }

            // Estado visual "Enviando..."
            const originalBtnText = submitBtnMake.textContent;
            submitBtnMake.innerHTML = '<span class="spinner"></span> Enviando...';
            submitBtnMake.disabled = true;
            formStatusMake.textContent = '';
            formStatusMake.className = 'form-status';

            // Usando FormData para capturar valores
            const formData = new FormData(leadFormMake);
            const data = Object.fromEntries(formData.entries());
            data.fecha = new Date().toISOString();
            data.fuente = 'Landing ErickDDP';

            try {
                if (MAKE_WEBHOOK_URL === 'TU_URL_DE_MAKE_AQUI') {
                    console.warn('⚠️ Webhook de Make no configurado. Reemplaza "TU_URL_DE_MAKE_AQUI" con tu enlace.');
                    // Simulación para probar los estados visuales sin enviar
                    await new Promise(resolve => setTimeout(resolve, 1500));
                } else {
                    // fetch() con el método POST y headers: { 'Content-Type': 'application/json' }
                    const response = await fetch(MAKE_WEBHOOK_URL, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
                }

                // Estado "Éxito" visualmente
                formStatusMake.innerHTML = '✅ ¡Listo! Datos enviados correctamente. Te contactaré pronto.';
                formStatusMake.classList.add('success');
                submitBtnMake.innerHTML = '✅ ¡Éxito!';
                leadFormMake.reset();

                setTimeout(() => {
                    submitBtnMake.textContent = originalBtnText;
                    submitBtnMake.disabled = false;
                    submitBtnMake.classList.add('btn-pulse');
                }, 4000);

            } catch (error) {
                console.error('Error al enviar formulario a Make:', error);
                // Estado "Error" visualmente
                formStatusMake.innerHTML = '❌ Error al enviar el formulario. <a href="https://wa.me/525534806184" target="_blank" style="color: #f87171; text-decoration: underline; font-weight: 600;">Escríbeme por WhatsApp →</a>';
                formStatusMake.classList.add('error');
                submitBtnMake.textContent = originalBtnText;
                submitBtnMake.disabled = false;
            }
        });
    }

    const container = document.getElementById('network-bg');
    if (!container) return;

    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d', { alpha: true });
    container.appendChild(canvas);

    let w = 0, h = 0;
    let particles = [];
    const connDist = 140;

    function resize() {
        w = canvas.width = container.clientWidth;
        h = canvas.height = container.clientHeight;
    }
    window.addEventListener('resize', resize, { passive: true });
    resize();

    class P {
        constructor() {
            this.x = Math.random() * w;
            this.y = Math.random() * h;
            this.vx = (Math.random() - 0.5) * 0.25;
            this.vy = (Math.random() - 0.5) * 0.25;
        }
        u() {
            this.x += this.vx; this.y += this.vy;
            if (this.x <= 0 || this.x >= w) this.vx *= -1;
            if (this.y <= 0 || this.y >= h) this.vy *= -1;
        }
        d() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, 1.2, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(56,189,248,0.35)';
            ctx.fill();
        }
    }

    function init() {
        particles = [];
        const count = window.innerWidth < 768 ? 22 : 44;
        for (let i = 0; i < count; i++) particles.push(new P());
    }
    init();

    function loop() {
        ctx.clearRect(0, 0, w, h);

        for (let i = 0; i < particles.length; i++) {
            const a = particles[i];
            a.u(); a.d();

            for (let j = i + 1; j < particles.length; j++) {
                const b = particles[j];
                const dx = a.x - b.x, dy = a.y - b.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < connDist) {
                    const o = 1 - (dist / connDist);
                    ctx.beginPath();
                    ctx.moveTo(a.x, a.y);
                    ctx.lineTo(b.x, b.y);
                    ctx.strokeStyle = `rgba(56,189,248, ${(o * 0.14).toFixed(2)})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);

    // --- REVEAL & PARALLAX SECCIÓN ECOSISTEMA ---
    const ecoContainer = document.querySelector('.eco-container');
    const ecoSection = document.querySelector('.eco-section');
    if (ecoContainer) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    ecoContainer.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });
        observer.observe(ecoContainer);
    }

    if (ecoSection) {
        ecoSection.addEventListener('mousemove', (e) => {
            if (window.innerWidth > 991) {
                const x = (e.clientX / window.innerWidth - 0.5) * 30;
                const y = (e.clientY / window.innerHeight - 0.5) * 30;
                ecoSection.style.setProperty('--mx', `${x}px`);
                ecoSection.style.setProperty('--my', `${y}px`);
            }
        });
    }

    // ─── BLOG FEED FETCH (JSONP) ────────────────────────────────────────────
    const blogGrid = document.getElementById('blog-grid');
    if (blogGrid) {
        window.blogFeedCallback = function (data) {
            const posts = data.feed.entry || [];
            blogGrid.innerHTML = '';

            if (posts.length === 0) {
                blogGrid.innerHTML = '<p style="color: var(--text-secondary); text-align: center; grid-column: 1/-1;">No hay artículos disponibles en este momento.</p>';
                return;
            }

            posts.forEach((post, index) => {
                const title = post.title.$t;
                let link = '#';
                if (post.link) {
                    for (let i = 0; i < post.link.length; i++) {
                        if (post.link[i].rel === 'alternate') {
                            link = post.link[i].href;
                            break;
                        }
                    }
                }

                const puDate = new Date(post.published.$t);
                const formattedDate = puDate.toLocaleDateString('es-MX', { year: 'numeric', month: 'long', day: 'numeric' });

                let contentHtml = post.content ? post.content.$t : (post.summary ? post.summary.$t : '');
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = contentHtml;
                const textContent = tempDiv.textContent || tempDiv.innerText || '';
                const excerpt = textContent.replace(/\s+/g, ' ').trim().substring(0, 120) + '...';

                let thumbUrl = '';
                if (post.media$thumbnail) {
                    thumbUrl = post.media$thumbnail.url.replace(/\/s[0-9]+(\-c)?\//, '/s600/');
                } else {
                    const imgMatch = contentHtml.match(/<img[^>]+src="([^">]+)"/);
                    if (imgMatch && imgMatch[1]) {
                        thumbUrl = imgMatch[1];
                    }
                }

                const fallbackSvg = '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>';
                const thumbHTML = thumbUrl
                    ? `<img src="${thumbUrl}" alt="${title}" loading="lazy" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                       <div class="blog-thumb-fallback" style="display:none;">${fallbackSvg}</div>`
                    : `<div class="blog-thumb-fallback">${fallbackSvg}</div>`;

                const delay = index * 0.15;
                const cardHTML = `
                    <a href="${link}" target="_blank" rel="noopener" class="blog-card reveal" style="animation-delay: ${delay}s">
                        <div class="blog-thumb">
                            ${thumbHTML}
                        </div>
                        <div class="blog-content">
                            <div class="blog-meta">${formattedDate}</div>
                            <h3 class="blog-title">${title}</h3>
                            <p class="blog-excerpt">${excerpt}</p>
                            <div class="blog-read-more">Leer artículo <span>→</span></div>
                        </div>
                    </a>
                `;
                blogGrid.insertAdjacentHTML('beforeend', cardHTML);
            });

            // Trigger reveal for new cards
            setTimeout(() => {
                document.querySelectorAll('#blog-grid .reveal').forEach(el => {
                    el.classList.add('visible');
                });
            }, 50);
        };

        const script = document.createElement('script');
        script.src = 'https://blog.erickddp.com/feeds/posts/default?alt=json-in-script&max-results=3&callback=blogFeedCallback';
        script.onerror = function () {
            blogGrid.innerHTML = '<p style="color: var(--text-secondary); text-align: center; grid-column: 1/-1;">No se pudieron cargar los artículos. <br><a href="https://blog.erickddp.com" target="_blank" style="color: var(--primary-400);">Visita el blog directamente →</a></p>';
        };
        document.body.appendChild(script);
    }

    // --- ANIMACIONES PORTADA 2: HERO FOTO Y ECO EN PERFIL ---

    // 1. ANIMACIÓN: Hero Background Photo (Portada2.png Transparente)
    const heroBgPhoto = document.getElementById('heroBgPhoto');
    if (heroBgPhoto) {
        // Un leve retraso de 100ms para asegurar renderizado de browser e inferir el efecto popup-out
        setTimeout(() => {
            heroBgPhoto.style.opacity = '0.7';
            heroBgPhoto.style.transform = 'scale(1.0)';
        }, 100);
    }

    // 2. ANIMACIÓN: Profile Background Blur (Sobre-MI Blur Eco)
    const profileBgBlur = document.getElementById('profileBgBlur');
    const sobreMiSection = document.getElementById('sobre-mi');

    if (profileBgBlur && sobreMiSection) {
        const observerProfileBlur = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Cargar opacidad y frenar el observer
                    profileBgBlur.style.opacity = '0.3';
                    observerProfileBlur.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        observerProfileBlur.observe(sobreMiSection);
    }

    // ─── FOOTER LOGO ANIMATION ──────────────────────────────────────────────
    const footerLogo = document.getElementById('footerLogo');
    if (footerLogo) {
        footerLogo.addEventListener('click', () => {
            footerLogo.classList.remove('animate-spin');
            void footerLogo.offsetWidth; // trigger reflow
            footerLogo.classList.add('animate-spin');
        });
    }

});

// --- HIGH END ANIMATIONS PARA CERTIFICACIONES ---
document.addEventListener('DOMContentLoaded', () => {
    // 3D Reveal Logic
    const reveal3d = document.querySelectorAll('.reveal-3d');
    if ('IntersectionObserver' in window) {
        const observer3d = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });

        reveal3d.forEach(el => observer3d.observe(el));
    } else {
        reveal3d.forEach(el => el.classList.add('active'));
    }

    // Magnetic Hover
    const magneticItems = document.querySelectorAll('.cert-magnetic');
    magneticItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            item.style.transform = `translate3d(${x * 0.1}px, ${y * 0.1}px, 0) scale(1.02)`;
            item.style.zIndex = "10";
            item.style.transition = "transform 0.1s ease-out";
        });

        item.addEventListener('mouseleave', () => {
            item.style.transform = '';
            item.style.zIndex = "1";
            item.style.transition = "transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1)";
        });
    });

    // Parallax Mesh & Particles
    const certSection = document.getElementById('certificaciones');
    const certMesh = document.getElementById('certMeshBg');
    const certParticles = document.getElementById('certParticles');

    if (certSection) {
        window.addEventListener('scroll', () => {
            const rect = certSection.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                const scrollFactor = window.scrollY * 0.05;
                if (certMesh) certMesh.style.transform = `translate3d(0, ${scrollFactor}px, 0)`;
            }
        });

        certSection.addEventListener('mousemove', (e) => {
            if (window.innerWidth <= 768) return;
            const x = (e.clientX / window.innerWidth - 0.5) * 20;
            const y = (e.clientY / window.innerHeight - 0.5) * 20;
            if (certParticles) certParticles.style.transform = `translate3d(${x}px, ${y}px, 0)`;
        });
    }

    // ─── PROFILE DYNAMIC EFFECTS (TITLE & TYPEWRITER) ───────────────────────
    const profileContent = document.querySelector('.profile-premium-content');
    const typewriterElem = document.querySelector('.typewriter-js');
    const dynamicTitle = document.querySelector('.profile-dynamic-title');

    function runTypewriter(el) {
        const fullText = el.getAttribute('data-text');
        let currentText = "";
        let index = 0;

        function type() {
            if (index < fullText.length) {
                currentText += fullText[index];
                el.textContent = currentText;
                index++;
                setTimeout(type, 25); // Velocidad de escritura
            }
        }
        type();
    }

    if (profileContent && 'IntersectionObserver' in window) {
        const profileObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // 1. Iniciar Efecto Escritura inmediatamente
                    if (typewriterElem) runTypewriter(typewriterElem);

                    // 2. Colapsar Título después de 2 segundos
                    setTimeout(() => {
                        if (dynamicTitle) dynamicTitle.classList.add('collapsed');
                    }, 5000);

                    profileObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        profileObserver.observe(profileContent);
    }
});

// --- SCRAMBLE EFFECT FOR TITLES ---
document.addEventListener('DOMContentLoaded', () => {
    const chars = '!<>-_\\/[]{}—=+*^?#_';
    const scrambleElements = document.querySelectorAll('.scramble-text');

    const scrambleText = (el) => {
        const originalText = el.getAttribute('data-text');
        if (!originalText) return;

        let iteration = 0;
        clearInterval(el.dataset.scrambleInterval);

        el.dataset.scrambleInterval = setInterval(() => {
            el.innerText = originalText.split('').map((letter, index) => {
                if (index < iteration) {
                    return originalText[index];
                }
                return chars[Math.floor(Math.random() * chars.length)];
            }).join('');

            if (iteration >= originalText.length) {
                clearInterval(el.dataset.scrambleInterval);
                el.innerText = originalText;
            }

            iteration += 1 / 3;
        }, 30);
    };

    if ('IntersectionObserver' in window) {
        const scrambleObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Start scramble effect
                    entry.target.querySelectorAll('.scramble-text').forEach(scrambleText);
                    scrambleObserver.unobserve(entry.target); // decode only once on sight
                }
            });
        }, { threshold: 0.5 });

        const certSection = document.getElementById('certificaciones-overdrive');
        if (certSection) scrambleObserver.observe(certSection);
    }
});
