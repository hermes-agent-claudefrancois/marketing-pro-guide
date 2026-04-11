#!/usr/bin/env python3
"""
Convertisseur Markdown vers HTML pour les articles d'affiliation
"""

import re
import argparse
from pathlib import Path
from datetime import datetime

def markdown_to_html(markdown_text: str) -> str:
    """Convertit le markdown en HTML simple"""
    html = markdown_text
    
    # Supprimer le frontmatter YAML
    html = re.sub(r'^---\n.*?---\n', '', html, flags=re.DOTALL)
    
    # Headers
    html = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold et italic
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Liens
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="nofollow noopener">\1</a>', html)
    
    # Code inline
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Blocs de code
    html = re.sub(r'```\w*\n(.*?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    
    # Listes
    lines = html.split('\n')
    result = []
    in_list = False
    list_type = None
    
    for line in lines:
        ul_match = re.match(r'^[\*\-] (.+)$', line)
        ol_match = re.match(r'^\d+\. (.+)$', line)
        
        if ul_match:
            if not in_list or list_type != 'ul':
                if in_list:
                    result.append('</ul>')
                result.append('<ul>')
                in_list = True
                list_type = 'ul'
            result.append(f'<li>{ul_match.group(1)}</li>')
        elif ol_match:
            if not in_list or list_type != 'ol':
                if in_list:
                    result.append('</ol>')
                result.append('<ol>')
                in_list = True
                list_type = 'ol'
            result.append(f'<li>{ol_match.group(1)}</li>')
        else:
            if in_list:
                result.append(f'</{list_type}>')
                in_list = False
                list_type = None
            result.append(line)
    
    if in_list:
        result.append(f'</{list_type}>')
    
    html = '\n'.join(result)
    
    # Tableaux simples
    table_pattern = r'\|(.+)\|\n\|[-:\s|]+\|\n((?:\|.+\|\n?)+)'
    
    def replace_table(match):
        header = match.group(1)
        rows = match.group(2).strip().split('\n')
        
        html_table = '<table class="data-table">\n<thead>\n<tr>'
        for cell in header.split('|'):
            html_table += f'<th>{cell.strip()}</th>'
        html_table += '</tr>\n</thead>\n<tbody>\n'
        
        for row in rows:
            html_table += '<tr>'
            for cell in row.split('|')[1:-1]:
                html_table += f'<td>{cell.strip()}</td>'
            html_table += '</tr>\n'
        
        html_table += '</tbody>\n</table>'
        return html_table
    
    html = re.sub(table_pattern, replace_table, html)
    
    # Paragraphes (lignes non vides non encore wrappées)
    lines = html.split('\n')
    result = []
    in_paragraph = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            result.append('')
        elif not re.match(r'^<[hH]\d|^<[ou]l|^<li|^<table|^<a|^</', stripped):
            if not in_paragraph:
                result.append('<p>')
                in_paragraph = True
            result.append(line)
        else:
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            result.append(line)
    
    if in_paragraph:
        result.append('</p>')
    
    html = '\n'.join(result)
    
    # Ligne horizontale
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)
    
    return html


def generate_full_html(title: str, content: str, meta_desc: str = "") -> str:
    """Génère une page HTML complète"""
    
    html_content = markdown_to_html(content)
    
    # Extraire la méta description si présente
    meta_match = re.search(r'<!-- Meta: (.*?) -->', content)
    if meta_match:
        meta_desc = meta_match.group(1)
    
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc or title}">
    <title>{title} | Marketing Pro Guide</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.7;
            color: #333;
            background: #f8f9fa;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 0 20px; }}
        
        /* Header */
        header {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }}
        header a {{ color: white; text-decoration: none; font-size: 1.2rem; }}
        
        /* Article */
        article {{
            background: white;
            padding: 3rem 2rem;
            margin: 2rem 0;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        article h1 {{ 
            font-size: 2.2rem; 
            color: #2d3748;
            margin-bottom: 1.5rem;
            line-height: 1.3;
        }}
        article h2 {{ 
            font-size: 1.6rem; 
            color: #4a5568;
            margin: 2rem 0 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e2e8f0;
        }}
        article h3 {{ 
            font-size: 1.3rem; 
            color: #667eea;
            margin: 1.5rem 0 0.75rem;
        }}
        article p {{ margin-bottom: 1.2rem; }}
        article ul, article ol {{ 
            margin: 1rem 0 1.5rem 2rem;
        }}
        article li {{ margin-bottom: 0.5rem; }}
        article a {{ color: #667eea; text-decoration: none; }}
        article a:hover {{ text-decoration: underline; }}
        article strong {{ color: #2d3748; }}
        article code {{
            background: #edf2f7;
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.9em;
        }}
        article pre {{
            background: #2d3748;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.5rem 0;
        }}
        article pre code {{
            background: transparent;
            padding: 0;
        }}
        article blockquote {{
            border-left: 4px solid #667eea;
            padding-left: 1rem;
            margin: 1.5rem 0;
            color: #4a5568;
            font-style: italic;
        }}
        article table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
        }}
        article th, article td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        article th {{
            background: #f7fafc;
            font-weight: 600;
            color: #2d3748;
        }}
        article hr {{
            border: none;
            border-top: 2px solid #e2e8f0;
            margin: 2rem 0;
        }}
        
        /* CTA Box */
        .cta-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            margin: 2rem 0;
            text-align: center;
        }}
        .cta-box h3 {{ color: white; margin-bottom: 1rem; }}
        .cta-box p {{ margin-bottom: 1.5rem; }}
        .cta-button {{
            display: inline-block;
            background: #48bb78;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
        }}
        .cta-button:hover {{ background: #38a169; }}
        
        /* Disclosure */
        .disclosure {{
            background: #edf2f7;
            padding: 1rem;
            border-radius: 8px;
            font-size: 0.9rem;
            color: #4a5568;
            margin-top: 2rem;
        }}
        
        /* Footer */
        footer {{
            background: #2d3748;
            color: white;
            padding: 2rem 0;
            text-align: center;
            margin-top: 3rem;
        }}
        footer a {{ color: #667eea; }}
        
        /* Mobile */
        @media (max-width: 768px) {{
            article {{ padding: 2rem 1rem; }}
            article h1 {{ font-size: 1.8rem; }}
            article h2 {{ font-size: 1.4rem; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <a href="../index.html">← Retour à l'accueil</a>
        </div>
    </header>
    
    <main class="container">
        <article>
{html_content}
            
            <div class="cta-box">
                <h3>🚀 Prêt à démarrer ?</h3>
                <p>Commencez gratuitement avec Systeme.io et construisez votre business en ligne dès aujourd'hui.</p>
                <a href="https://systeme.io/?sa=sa0268466764645998886fff8b439ed15072d58eb1" class="cta-button" target="_blank" rel="nofollow noopener">
                    Essayer Gratuitement
                </a>
            </div>
            
            <div class="disclosure">
                <strong>Disclosure :</strong> Cet article contient des liens d'affiliation. 
                Si vous vous inscrivez via nos liens, nous recevons une commission sans 
                aucun coût supplémentaire pour vous. Cela nous aide à créer du contenu gratuit de qualité.
            </div>
        </article>
    </main>
    
    <footer>
        <div class="container">
            <p>© 2025 Marketing Pro Guide | <a href="../index.html">Accueil</a></p>
        </div>
    </footer>
</body>
</html>'''


def main():
    parser = argparse.ArgumentParser(description="Convertit les articles Markdown en HTML")
    parser.add_argument("--input", required=True, help="Fichier Markdown d'entrée")
    parser.add_argument("--output", required=True, help="Fichier HTML de sortie")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"❌ Fichier non trouvé: {args.input}")
        return
    
    # Lire le contenu
    content = input_path.read_text(encoding='utf-8')
    
    # Extraire le titre
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else input_path.stem
    
    # Convertir
    html = generate_full_html(title, content)
    
    # Sauvegarder
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding='utf-8')
    
    print(f"✅ Converti: {args.input} → {args.output}")


if __name__ == "__main__":
    main()
