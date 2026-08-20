#!/bin/bash
# Projekt-miljö för migration_pact
# Användning: source .gitenv.sh
#
# Lägger till Python, pip, Java och mkdocs i PATH så att
# build.sh och scripts/ fungerar direkt.

# Python 3.14
export PYTHON_HOME="/c/Users/christerhe/AppData/Local/Python/bin"
export PYTHON_SCRIPTS="/c/Users/christerhe/AppData/Local/Python/pythoncore-3.14-64/Scripts"

# Java (PlantUML)
export JAVA_HOME="/c/repo/jdk-25.0.2"

# Bygg PATH
export PATH="$PYTHON_HOME:$PYTHON_SCRIPTS:$JAVA_HOME/bin:$PATH"

# pip som alias (pip.exe saknas ofta i nyare Python på Windows)
alias pip='python -m pip'

# Bekräfta
echo "migration_pact miljö laddad:"
echo "  python : $(python --version 2>&1)"
echo "  pip    : $(python -m pip --version 2>&1 | head -1)"
echo "  java   : $(java -version 2>&1 | head -1)"
echo ""
echo "Kör 'pip install pymupdf' för PDF-konvertering"
echo "Kör './build.sh' för att bygga sajten"
