#!/bin/bash
# Build the static site: generate SVGs, build MkDocs, fix links, make responsive
set -e

echo "Generating SVGs from PlantUML..."
find docs \( -name '*.pu' -o -name '*.puml' \) | xargs java -jar plantuml.jar -tsvg

echo "Building MkDocs site..."
python -m mkdocs build

echo "Fixing SVG links (.md → .html)..."
python build/fix-svg-links.py

echo "Making SVGs responsive..."
python build/make-svg-responsive.py

echo ""
echo "Done! Run: cd site && python -m http.server 8000"
