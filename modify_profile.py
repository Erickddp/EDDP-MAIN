import sys

css_code = """
/* ==========================================================================
   SECCIÓN 6: PERFIL PROFESIONAL (SOBRE MÍ)
   ========================================================================== */
.profile-premium {
    padding: 8rem 0;
    min-height: 100vh;
    min-height: 100svh;
    background-color: var(--bg-primary);
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
}

.profile-premium-container {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 5rem;
    align-items: center;
}

/* LEFT COLUMN - CONTENT */
.profile-premium-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.profile-subtitle {
    color: var(--text-secondary);
    font-size: 1.25rem;
    font-weight: 500;
    margin-top: -0.5rem;
    margin-bottom: 2rem;
    font-family: var(--font-mono);
}

.profile-narrative {
    color: var(--text-secondary);
    font-size: 1.15rem;
    line-height: 1.8;
    margin-bottom: 3.5rem;
    max-width: 90%;
}

/* DASHBOARD METRICS */
.profile-metrics {
    display: flex;
    gap: 3rem;
    background: rgba(15, 23, 42, 0.4);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 3.5rem;
}

.metric-item {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.metric-value {
    color: var(--primary-400);
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1;
    font-variant-numeric: tabular-nums;
}

.metric-label {
    color: var(--text-tertiary);
    font-family: var(--font-mono);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* LINK ARROW */
.profile-link-arrow {
    display: inline-flex;
    align-items: center;
    color: var(--text-primary);
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-decoration: none;
    transition: all 0.3s ease;
    width: max-content;
}

.profile-link-arrow:hover {
    color: var(--primary-400);
    transform: translateX(5px);
}

/* RIGHT COLUMN - VISUAL */
.profile-premium-visual {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    padding: 2rem;
}

/* AVATAR & GLOW */
.profile-avatar-container {
    position: relative;
    width: 320px;
    height: 320px;
    border-radius: 50%;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-avatar-glow {
    position: absolute;
    inset: -15px;
    border-radius: 50%;
    border: 2px dashed rgba(56, 189, 248, 0.3);
    animation: profileGlowBreathe 6s ease-in-out infinite alternate, profileGlowSpin 30s linear infinite;
    z-index: 0;
}

@keyframes profileGlowBreathe {
    0% { box-shadow: 0 0 10px rgba(56, 189, 248, 0.1), inset 0 0 10px rgba(56, 189, 248, 0.05); border-color: rgba(56, 189, 248, 0.2); transform: scale(0.98); }
    100% { box-shadow: 0 0 30px rgba(56, 189, 248, 0.4), inset 0 0 20px rgba(56, 189, 248, 0.2); border-color: rgba(56, 189, 248, 0.6); transform: scale(1.02); }
}

@keyframes profileGlowSpin {
    100% { transform: rotate(360deg); }
}

.profile-avatar-container::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(5px);
    z-index: 1;
}

.profile-avatar-img {
    position: relative;
    z-index: 2;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    mask-image: radial-gradient(circle, black 60%, transparent 100%);
    -webkit-mask-image: radial-gradient(circle, black 60%, transparent 100%);
}

.profile-signature {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.8rem;
    font-weight: 300;
    color: var(--text-primary);
    opacity: 0.9;
    letter-spacing: -0.5px;
    position: relative;
}

/* RESPONSIVE */
@media (max-width: 991px) {
    .profile-premium-container {
        grid-template-columns: 1fr;
        gap: 3rem;
    }

    /* Invert ordering for Mobile (Image first) */
    .profile-premium-visual {
        grid-row: 1;
        padding: 0;
    }

    .profile-premium-content {
        grid-row: 2;
        text-align: center;
        align-items: center;
    }
    
    .profile-subtitle {
        margin-bottom: 2rem;
    }

    .profile-narrative {
        max-width: 100%;
    }

    .profile-metrics {
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 2rem;
        padding: 1.5rem;
    }

    .metric-value {
        font-size: 2rem;
    }
    
    .profile-avatar-container {
        width: 260px;
        height: 260px;
    }
}
"""

with open(r'c:\Users\erick\Desktop\erickddp-main\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
print("CSS injected")
