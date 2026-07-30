"""Post-build script: rewrite .md links to .html in all SVG and HTML files in site/."""
import os
import re

site_dir = os.path.join(os.path.dirname(__file__), '..', 'site')
fixed_count = 0

for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith('.svg') or f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            # Replace .md" with .html" in href attributes
            new_content = re.sub(r'(href="[^"]*?)\.md"', r'\1.html"', content)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new_content)
                fixed_count += 1

print(f"Fixed {fixed_count} files.")
print("Done.")
