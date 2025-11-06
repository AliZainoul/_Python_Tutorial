#!/bin/bash
# Setup script for actuarial_analysis project structure

set -e  # Exit on error

echo "🚀 Creating actuarial_analysis project structure..."

# Create all directories
mkdir -p actuarial_analysis/{config,src/{models,database,services,utils}}

# Navigate to project root
cd actuarial_analysis

# Create all __init__.py files
touch config/__init__.py
touch src/__init__.py
touch src/models/__init__.py
touch src/database/__init__.py
touch src/services/__init__.py
touch src/utils/__init__.py

# Create config files
touch config/settings.py

# Create model files
touch src/models/base.py
touch src/models/client.py
touch src/models/contract.py
touch src/models/prime.py
touch src/models/claim.py

# Create database files
touch src/database/connection.py
touch src/database/setup.py

# Create service files
touch src/services/data_generator.py
touch src/services/analytics.py

# Create utility files
touch src/utils/date_helpers.py

# Create root files
touch main.py
touch requirements.txt
touch README.md

echo ""
echo "✅ Project structure created successfully!"
echo ""
echo "📁 Project structure:"
echo ""

# Display tree structure
if command -v tree &> /dev/null; then
    tree -L 3
else
    find . -type f -o -type d | sed 's|[^/]*/| |g'
fi

echo ""
echo "📝 Next steps:"
echo "   1. cd actuarial_analysis"
echo "   2. Copy the code into respective files"
echo "   3. pip install -r requirements.txt"
echo "   4. python main.py"