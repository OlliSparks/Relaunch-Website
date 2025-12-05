import glob
import re

# Find all HTML files
html_files = glob.glob('*.html')

# Old footer patterns that need to be updated to include all 5 links
old_footer_patterns = [
    # Pattern 1: Only has Impressum, Datenschutzhinweise, Kontakt
    r'<footer class="footer" style="background: #0a0e1a; padding: 2rem; text-align: center;">\s*<a href="impressum\.html"[^>]*>Impressum</a>\s*<a href="datenschutzhinweise\.html"[^>]*>Datenschutzhinweise</a>\s*<a href="kontakt\.html"[^>]*>Kontakt</a>\s*</footer>',
    # Pattern 2: Has Impressum, Datenschutz (old name), Kontakt
    r'<footer class="footer" style="background: #0a0e1a; padding: 2rem; text-align: center;">\s*<a href="impressum\.html"[^>]*>Impressum</a>\s*<a href="datenschutz\.html"[^>]*>Datenschutz</a>\s*<a href="kontakt\.html"[^>]*>Kontakt</a>\s*</footer>',
]

# New footer with all 5 links
new_footer = '''<footer class="footer" style="background: #0a0e1a; padding: 2rem; text-align: center;">
        <a href="impressum.html" style="color: white; text-decoration: none; margin: 0 1rem;">Impressum</a>
        <a href="datenschutzhinweise.html" style="color: white; text-decoration: none; margin: 0 1rem;">Datenschutzhinweise</a>
        <a href="datenschutzerklaerung.html" style="color: white; text-decoration: none; margin: 0 1rem;">Datenschutzerklärung</a>
        <a href="nutzungsbedingungen.html" style="color: white; text-decoration: none; margin: 0 1rem;">Nutzungsbedingungen</a>
        <a href="kontakt.html" style="color: white; text-decoration: none; margin: 0 1rem;">Kontakt</a>
    </footer>'''

updated_files = []

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Check if this file already has all 5 footer links
        if 'datenschutzerklaerung.html' in content and 'nutzungsbedingungen.html' in content:
            print(f"SKIP (already updated): {file}")
            continue

        # Check if file has a footer to update
        if '<footer class="footer"' in content:
            # Replace the footer section with new footer
            # Match any footer and replace it
            footer_pattern = r'<footer class="footer"[^>]*>.*?</footer>'
            if re.search(footer_pattern, content, re.DOTALL):
                content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files.append(file)
            print(f"UPDATED: {file}")
        else:
            print(f"NO CHANGE: {file}")

    except Exception as e:
        print(f"ERROR {file}: {e}")

print(f"\nTotal files updated: {len(updated_files)}")
