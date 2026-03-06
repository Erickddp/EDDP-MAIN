css_append = """
/* ==========================================================================
   SECCIÓN CONTACTO: HABLAR CONMIGO (NODO)
   ========================================================================== */
.hablar-conmigo-node {
    position: relative;
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--bg-primary);
    overflow: hidden;
    padding: 6rem 0;
}

/* Static Mesh & Radial Focus */
.node-mesh-bg {
    position: absolute;
    inset: 0;
    min-height: 100%;
    background-image: 
        radial-gradient(circle at center, rgba(56, 189, 248, 0.08) 0%, transparent 50%),
        linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
    background-size: 100% 100%, 30px 30px, 30px 30px;
    z-index: 0;
    pointer-events: none;
}

.node-container {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 800px;
}

/* Typography Overrides */
.node-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}

.node-desc {
    color: var(--text-secondary);
    font-size: 1.15rem;
    max-width: 600px;
    margin: 0 auto 4rem;
    line-height: 1.6;
}

/* Identity Grid & Orbital Ring */
.node-identity-grid {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 3rem;
    padding: 3rem;
}

.orbital-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 380px;
    height: 380px;
    margin-top: -190px;
    margin-left: -190px;
    border: 1px dashed rgba(56, 189, 248, 0.15);
    border-radius: 50%;
    z-index: 0;
    pointer-events: none;
    animation: orbitRotate 50s linear infinite; /* 0.02Hz */
}
.orbital-ring::before {
    content: '';
    position: absolute;
    top: -3px; left: 50%;
    width: 6px; height: 6px;
    background: var(--primary-400);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--primary-400);
}
@keyframes orbitRotate {
    100% { transform: rotate(360deg); }
}

/* The Connection Nodes (Links) */
.node-link {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.2rem;
    text-decoration: none;
    z-index: 2;
    group: "node";
}

.node-glass {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.node-icon {
    width: 32px;
    height: 32px;
    color: var(--text-primary);
    transition: color 0.3s ease;
    filter: drop-shadow(0 0 0 transparent);
}

.node-text {
    font-family: var(--font-mono);
    color: var(--text-secondary);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    position: relative;
    padding-bottom: 4px;
    transition: color 0.3s ease;
}

/* Hover Micro-interactions */
.node-link::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: var(--primary-400);
    transform: scaleX(0);
    transform-origin: center;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.node-link:hover .node-glass {
    background: rgba(56, 189, 248, 0.05);
    border-color: rgba(56, 189, 248, 0.3);
    transform: translateY(-8px);
}

.node-link:hover .node-icon {
    color: var(--primary-400);
    filter: drop-shadow(0 0 8px var(--primary-400));
}

.node-link:hover .node-text {
    color: var(--primary-400);
}

.node-link:hover::after {
    transform: scaleX(1);
}

@media (max-width: 768px) {
    .node-identity-grid {
        gap: 2rem;
        padding: 1.5rem;
    }
    .orbital-ring {
        width: 280px;
        height: 280px;
        margin-top: -140px;
        margin-left: -140px;
    }
    .node-glass {
        width: 65px;
        height: 65px;
        border-radius: 16px;
    }
    .node-icon {
        width: 26px;
        height: 26px;
    }
}
"""

with open(r'c:\Users\erick\Desktop\erickddp-main\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("CSS appended.")
