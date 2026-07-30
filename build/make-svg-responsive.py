"""Make PlantUML SVGs responsive by removing fixed dimensions.

PlantUML generates SVGs with inline style="width:Xpx;height:Ypx" and
width/height attributes. This prevents them from scaling in the browser.

This script:
1. Removes the inline width/height style
2. Removes width/height attributes from <svg>
3. Keeps the viewBox (which enables proper scaling)
4. Sets preserveAspectRatio to scale properly
"""
import os
import re

site_dir = os.path.join(os.path.dirname(__file__), '..', 'site')
fixed_count = 0

for root, dirs, files in os.walk(site_dir):
    for f in files:
        if not f.endswith('.svg'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()

        original = content

        # Remove inline style with fixed dimensions: style="width:XXXpx;height:YYYpx;..."
        # Replace with style that allows full scaling
        content = re.sub(
            r'style="width:\d+px;height:\d+px;(background:#[A-Fa-f0-9]+;)"',
            r'style="width:100%;height:auto;\1"',
            content
        )

        # Remove fixed width="XXXpx" and height="XXXpx" attributes
        content = re.sub(r'\s+width="\d+px"', '', content)
        content = re.sub(r'\s+height="\d+px"', '', content)

        # Change preserveAspectRatio to scale proportionally (fill width)
        content = content.replace(
            'preserveAspectRatio="none"',
            'preserveAspectRatio="xMidYMin meet"'
        )

        if content != original:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            fixed_count += 1

print(f"Made {fixed_count} SVGs responsive.")
