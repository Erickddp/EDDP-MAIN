import sys

file_path = r'c:\Users\erick\Desktop\erickddp-main\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace missing edu-heading
if 'class="edu-heading container"' not in content:
    content = content.replace(
        '<section id="educacion" class="edu-section">',
        '<section id="educacion" class="edu-section">\n        <div class="edu-heading container">\n            <h2 class="section-title reveal">Formación <span style="color: var(--primary-400);">Profesional</span></h2>\n        </div>'
    )

# Add glow 1
if 'class="edu-card-glow"' not in content:
    content = content.replace(
        '<div class="edu-card-content">\n                    <img src="__LOGO_CONTADURIA__"',
        '<div class="edu-card-glow"></div>\n                <div class="edu-card-content">\n                    <img src="__LOGO_CONTADURIA__"'
    )
    
# Add glow 2
if 'class="edu-card-glow edu-glow-active"' not in content:
    content = content.replace(
        '<div class="edu-card-content">\n                    <img src="__LOGO_IA__"',
        '<div class="edu-card-glow edu-glow-active"></div>\n                <div class="edu-card-content">\n                    <img src="__LOGO_IA__"'
    )

# Replace dashed line
content = content.replace(
    '<div class="edu-line-dashed"></div>\n                            <div class="edu-node edu-node-active"></div>',
    '<div class="edu-line-dashed-container">\n                                <div class="edu-line-dashed"></div>\n                            </div>\n                            <div class="edu-node edu-node-active">\n                                <div class="node-pulse"></div>\n                            </div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html')
