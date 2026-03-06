import sys
import re

html_replacement = '''    <!-- 4. SECCIÓN CURSOS Y CERTIFICACIONES -->
    <section id="certificaciones-overdrive" class="cert-overdrive-section">
        <div class="cert-bg-grid"></div>
        <div class="cert-laser-scan"></div>
        
        <div class="container" style="position: relative; z-index: 2; text-align: center; margin-bottom: 3rem;">
            <h2 class="section-title reveal"><span class="scramble-text" data-text="Cursos y ">Cursos y </span><span style="color: var(--primary-400);" class="scramble-text" data-text="Certificaciones">Certificaciones</span></h2>
            <p class="cert-desc reveal">Formación continua en tecnología, finanzas e IA aplicada para la resolución de problemas complejos</p>
        </div>

        <div class="marquee-wrapper reveal-3d">
            <!-- Fila 1: Derecha a Izquierda -->
            <div class="marquee-container">
                <div class="marquee-track track-left">
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">44</span> Curso</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">35</span> Certificación</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">30</span> Platzi</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">12</span> Ciberseguridad</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">7</span> Inteligencia Artificial</div>
                    
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">44</span> Curso</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">35</span> Certificación</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">30</span> Platzi</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">12</span> Ciberseguridad</div>
                    <div class="cert-badge premium-badge"><span class="cert-cat-num">7</span> Inteligencia Artificial</div>
                </div>
            </div>

            <!-- Fila 2: Izquierda a Derecha -->
            <div class="marquee-container reverse-mask">
                <div class="marquee-track track-right">
                    <div class="cert-badge premium-badge">SQL / DATA</div>
                    <div class="cert-badge premium-badge">Business Intelligence</div>
                    <div class="cert-badge premium-badge">Python</div>
                    <div class="cert-badge premium-badge">Automatización</div>
                    <div class="cert-badge premium-badge">Seguridad Ofensiva</div>
                    
                    <div class="cert-badge premium-badge">SQL / DATA</div>
                    <div class="cert-badge premium-badge">Business Intelligence</div>
                    <div class="cert-badge premium-badge">Python</div>
                    <div class="cert-badge premium-badge">Automatización</div>
                    <div class="cert-badge premium-badge">Seguridad Ofensiva</div>
                </div>
            </div>
        </div>

        <div class="container" style="position: relative; z-index: 2; text-align: center; margin-top: 4rem;">
            <a href="https://nsl-reconocimientos.blogspot.com/" target="_blank" class="btn-glow-extreme reveal">
                VER TODAS MIS CREDENCIALES (+50 CERTIFICACIONES)
            </a>
        </div>
    </section>'''

html_path = r'c:\Users\erick\Desktop\erickddp-main\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'<!-- 4\. SECCIÓN CURSOS Y CERTIFICACIONES -->[\s\S]*?</section>')
html = pattern.sub(html_replacement, html, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML updated for certificaciones-overdrive.')

css_overdrive = """
/* ==========================================================================
   SECCIÓN CERTIFICACIONES OVERDRIVE (DOBLE CINTA + GLOW + SCRAMBLE)
   ========================================================================== */
.cert-overdrive-section {
    position: relative;
    padding: 8rem 0;
    overflow: hidden;
    background-color: var(--bg-primary);
}

/* Digital Grid */
.cert-bg-grid {
    position: absolute;
    inset: 0;
    background-image: 
        linear-gradient(rgba(56, 189, 248, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56, 189, 248, 0.05) 1px, transparent 1px);
    background-size: 40px 40px;
    background-position: center center;
    z-index: 0;
    opacity: 0.3;
}

/* Laser Scan Line */
.cert-laser-scan {
    position: absolute;
    top: -10px;
    left: 0;
    width: 100%;
    height: 4px;
    background: rgba(56, 189, 248, 0.5);
    box-shadow: 0 0 20px 2px rgba(56, 189, 248, 0.6);
    z-index: 1;
    animation: laserScan 8s linear infinite;
    pointer-events: none;
    opacity: 0.7;
}
@keyframes laserScan {
    0% { transform: translateY(-100px); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(800px); opacity: 0; }
}

.cert-desc {
    color: var(--text-secondary);
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0.5rem auto 0;
    letter-spacing: 0.5px;
}

/* Double Marquee */
.marquee-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin: 2rem 0;
    position: relative;
    z-index: 2;
}

.marquee-container {
    width: 100%;
    overflow: hidden;
    padding: 1rem 0;
    -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
    mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}
.reverse-mask {
    -webkit-mask-image: linear-gradient(to left, transparent, black 15%, black 85%, transparent);
    mask-image: linear-gradient(to left, transparent, black 15%, black 85%, transparent);
}

.marquee-track {
    display: flex;
    gap: 2rem;
    width: max-content;
    will-change: transform;
}

.track-left {
    animation: marqueeLeft 20s linear infinite;
}
.track-right {
    animation: marqueeRight 20s linear infinite;
    transform: translate3d(calc(-50% - 1rem), 0, 0); 
}

/* Pause on hover on both tracks */
.marquee-wrapper:hover .marquee-track {
    animation-play-state: paused;
}

@keyframes marqueeLeft {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(calc(-50% - 1rem), 0, 0); }
}
@keyframes marqueeRight {
    0% { transform: translate3d(calc(-50% - 1rem), 0, 0); }
    100% { transform: translate3d(0, 0, 0); }
}

/* Glass Pills Premium */
.premium-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.8rem;
    padding: 1rem 2rem;
    background: rgba(15, 23, 42, 0.4);
    border-radius: 50px; /* Pill shape */
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(56, 189, 248, 0.2);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    color: var(--text-primary);
    font-size: 1.1rem;
    font-weight: 600;
    white-space: nowrap;
    transition: all 0.3s ease;
    cursor: default;
}
.premium-badge:hover {
    border-color: var(--primary-400);
    background: rgba(56, 189, 248, 0.1);
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
    transform: scale(1.05);
}

.cert-cat-num {
    background: var(--primary-400);
    color: #0f172a;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.9rem;
    font-weight: 700;
}

/* CTA Botón Extremo */
.btn-glow-extreme {
    display: inline-block;
    padding: 1.2rem 2.8rem;
    background: transparent;
    border: 2px solid var(--primary-400);
    color: var(--primary-400);
    font-weight: 700;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 50px;
    position: relative;
    z-index: 10;
    text-decoration: none;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.2), inset 0 0 10px rgba(56, 189, 248, 0.1);
    animation: btnPulseExtreme 3s infinite;
}

.btn-glow-extreme::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(120deg, transparent, rgba(56,189,248,0.4), transparent);
    transition: all 0.6s;
    z-index: -1;
}

.btn-glow-extreme:hover {
    background: var(--primary-400);
    color: #0f172a;
    box-shadow: 0 0 30px rgba(56, 189, 248, 0.6), inset 0 0 20px rgba(255, 255, 255, 0.5);
    transform: scale(1.05);
}

.btn-glow-extreme:hover::before {
    left: 100%;
}

@keyframes btnPulseExtreme {
    0% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2), inset 0 0 10px rgba(56, 189, 248, 0.1); }
    50% { box-shadow: 0 0 30px rgba(56, 189, 248, 0.5), inset 0 0 15px rgba(56, 189, 248, 0.2); }
    100% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2), inset 0 0 10px rgba(56, 189, 248, 0.1); }
}
"""

css_path = r'c:\Users\erick\Desktop\erickddp-main\styles.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_overdrive)
print('CSS appended.')

js_overdrive = """
// --- SCRAMBLE EFFECT FOR TITLES ---
document.addEventListener('DOMContentLoaded', () => {
    const chars = '!<>-_\\\\/[]{}—=+*^?#_';
    const scrambleElements = document.querySelectorAll('.scramble-text');

    const scrambleText = (el) => {
        const originalText = el.getAttribute('data-text');
        if(!originalText) return;
        
        let iteration = 0;
        clearInterval(el.dataset.scrambleInterval);
        
        el.dataset.scrambleInterval = setInterval(() => {
            el.innerText = originalText.split('').map((letter, index) => {
                if(index < iteration) {
                    return originalText[index];
                }
                return chars[Math.floor(Math.random() * chars.length)];
            }).join('');
            
            if(iteration >= originalText.length) {
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
        if(certSection) scrambleObserver.observe(certSection);
    }
});
"""

js_path = r'c:\Users\erick\Desktop\erickddp-main\script.js'
with open(js_path, 'a', encoding='utf-8') as f:
    f.write(js_overdrive)
print('JS appended.')
