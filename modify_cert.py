import sys

css_code = """
/* ==========================================================================
   SECCIÓN CERTIFICACIONES (HIGH-END)
   ========================================================================== */
.marquee-overdrive {
    position: relative;
    padding: 8rem 0;
    overflow: hidden;
    background-color: var(--bg-primary);
}

/* Fixed Mesh Gradient */
.cert-mesh-bg {
    position: absolute;
    inset: -50%;
    background: 
        radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 80% 20%, rgba(239, 68, 68, 0.03) 0%, transparent 30%),
        radial-gradient(circle at 20% 80%, rgba(234, 179, 8, 0.03) 0%, transparent 30%);
    background-size: 100% 100%;
    z-index: 0;
    pointer-events: none;
    transition: transform 0.1s linear;
    will-change: transform;
}

/* Local Particles */
.cert-particles {
    position: absolute;
    inset: -10%;
    background-image: radial-gradient(rgba(255,255,255,0.15) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 1;
    pointer-events: none;
    transition: transform 0.1s ease-out;
    will-change: transform;
}

/* Marquee Container Mask */
.marquee-container {
    width: 100%;
    overflow: hidden;
    padding: 2rem 0;
    -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
    mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}

.marquee-track {
    display: flex;
    gap: 2rem;
    width: max-content;
    animation: marqueeScroll 25s linear infinite;
    will-change: transform;
}

.marquee-track:hover {
    animation-play-state: paused;
}

@keyframes marqueeScroll {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(calc(-50% - 1rem), 0, 0); }
}

/* 3D Fold Entrance */
.reveal-3d {
    opacity: 0;
    transform: perspective(1000px) rotateX(90deg) translateY(50px);
    transform-origin: top center;
    transition: transform 1.2s cubic-bezier(0.68, -0.55, 0.27, 1.55), opacity 0.8s ease-out;
}

.reveal-3d.active {
    opacity: 1;
    transform: perspective(1000px) rotateX(0deg) translateY(0);
}

/* Cert Badges */
.cert-badge {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    padding: 1.2rem 1.8rem;
    background: rgba(15, 23, 42, 0.4);
    border-radius: 20px;
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    animation: floatCert 6s ease-in-out infinite;
    will-change: transform;
    transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.1s;
    cursor: default;
    min-width: 380px;
}

@keyframes floatCert {
    0%, 100% { transform: translate3d(0, 0, 0); }
    50% { transform: translate3d(0, -10px, 0); }
}

/* Category Colors */
.cat-ai { border-left: 4px solid #38bdf8; }         /* Cyan */
.cat-data { border-left: 4px solid #eab308; }       /* Gold */
.cat-security { border-left: 4px solid #ef4444; }   /* Red */
.cat-tech { border-left: 4px solid #a855f7; }       /* Purple */
.cat-pro { border-left: 4px solid #10b981; }        /* Green */

.cat-ai:hover { border-color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.2); }
.cat-data:hover { border-color: #eab308; box-shadow: 0 0 20px rgba(234, 179, 8, 0.2); }
.cat-security:hover { border-color: #ef4444; box-shadow: 0 0 20px rgba(239, 68, 68, 0.2); }
.cat-tech:hover { border-color: #a855f7; box-shadow: 0 0 20px rgba(168, 85, 247, 0.2); }
.cat-pro:hover { border-color: #10b981; box-shadow: 0 0 20px rgba(16, 185, 129, 0.2); }

.cert-icon {
    font-size: 2rem;
    background: rgba(255,255,255,0.05);
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
}

.cert-cat {
    display: block;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-tertiary);
    font-family: var(--font-mono);
}

.cert-info h4 {
    margin: 0.2rem 0 0;
    font-size: 1.1rem;
    color: var(--text-primary);
    font-weight: 600;
}

@media (max-width: 768px) {
    .cert-badge {
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        min-width: 300px;
    }
    .cert-particles {
        display: none;
    }
}
"""

js_code = """
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

    if(certSection) {
        window.addEventListener('scroll', () => {
            const rect = certSection.getBoundingClientRect();
            if(rect.top < window.innerHeight && rect.bottom > 0) {
                const scrollFactor = window.scrollY * 0.05;
                if(certMesh) certMesh.style.transform = `translate3d(0, ${scrollFactor}px, 0)`;
            }
        });

        certSection.addEventListener('mousemove', (e) => {
            if (window.innerWidth <= 768) return;
            const x = (e.clientX / window.innerWidth - 0.5) * 20;
            const y = (e.clientY / window.innerHeight - 0.5) * 20;
            if(certParticles) certParticles.style.transform = `translate3d(${x}px, ${y}px, 0)`;
        });
    }
});
"""

css_path = r'c:\Users\erick\Desktop\erickddp-main\styles.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_code)

js_path = r'c:\Users\erick\Desktop\erickddp-main\script.js'
with open(js_path, 'a', encoding='utf-8') as f:
    f.write(js_code)
