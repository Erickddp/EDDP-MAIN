import sys
import re

html_path = r'c:\Users\erick\Desktop\erickddp-main\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# heading
html = re.sub(
    r'(<section id="educacion" class="edu-section">)',
    r'\1\n        <div class="edu-heading container">\n            <h2 class="section-title reveal">Formación <span style="color: var(--primary-400);">Profesional</span></h2>\n        </div>',
    html
)

# glows
html = re.sub(
    r'(<div class="edu-card-content">\s*<img src="__LOGO_CONTADURIA__")',
    r'<div class="edu-card-glow"></div>\n                \1',
    html
)

html = re.sub(
    r'(<div class="edu-card-content">\s*<img src="__LOGO_IA__")',
    r'<div class="edu-card-glow edu-glow-active"></div>\n                \1',
    html
)

# timelines
html = re.sub(
    r'(<div class="edu-line-dashed"></div>)\s*(<div class="edu-node edu-node-active"></div>)',
    r'<div class="edu-line-dashed-container">\n                                \1\n                            </div>\n                            <div class="edu-node edu-node-active">\n                                <div class="node-pulse"></div>\n                            </div>',
    html
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML done")

css_path = r'c:\Users\erick\Desktop\erickddp-main\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# display: flex => block in edu-section
css = re.sub(
    r'(\.edu-section\s*\{[^}]*?)display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*center;\s*background-color:\s*var\(--bg-primary\);',
    r'\1display: block;\n    background-color: var(--bg-primary);',
    css
)

css += '''
.edu-heading {
    margin-bottom: 3rem;
    text-align: center;
}

.edu-heading .section-title {
    margin-bottom: 0;
}

.edu-card-glow {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 70%);
    opacity: 0.5;
    z-index: 1;
    transition: opacity 0.5s ease;
}

.edu-glow-active {
    background: radial-gradient(circle at 100% 100%, rgba(56, 189, 248, 0.15) 0%, transparent 60%);
    animation: eduGlowBreathe 4s ease-in-out infinite alternate;
}

@keyframes eduGlowBreathe {
    0% { opacity: 0.4; }
    100% { opacity: 1; }
}

.edu-line-dashed-container {
    flex-grow: 1;
    height: 1px;
    margin: 0 0.5rem;
    position: relative;
    overflow: hidden;
    background: transparent;
    border-top: 1px dashed rgba(56, 189, 248, 0.2);
}

.edu-line-dashed-container .edu-line-dashed {
    position: absolute;
    top: -1px;
    left: 0;
    width: 200%;
    height: 100%;
    margin: 0;
    border-top: 1px dashed rgba(56, 189, 248, 0.8);
    animation: eduLineSlide 5s linear infinite;
}

@keyframes eduLineSlide {
    0% { transform: translateX(-50%); }
    100% { transform: translateX(0%); }
}

.node-pulse {
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 1px solid var(--primary-400);
    opacity: 0;
    animation: nodePulseAnim 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes nodePulseAnim {
    0% { transform: scale(0.5); opacity: 1; }
    100% { transform: scale(3.5); opacity: 0; }
}
'''

# We also need to remove .edu-line-dashed from the flex-grow block, since we added it to the container instead.
# Actually, we can just leave it or overwrite it specifically. I created `.edu-line-dashed-container .edu-line-dashed` which will take precedence.

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS done")
