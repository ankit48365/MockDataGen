#!/bin/bash

# Run pylint and save the output
uv run pylint myapp > pylint_report.txt || true

# Extract Pylint score
PYLINT_SCORE=$(grep -oP 'rated at \K[0-9.]+' pylint_report.txt)

# Validate Pylint score extraction
if [ -z "$PYLINT_SCORE" ]; then
  echo "Failed to retrieve Pylint score!"
  exit 1
fi

echo "Pylint Score: $PYLINT_SCORE"

# Run pytest with coverage XML report
uv run pytest --cov=myapp --cov-report=xml > /dev/null || true

# Extract test coverage percentage from XML
COVERAGE=$(grep -oP 'line-rate="\K[0-9.]+' coverage.xml | awk 'NR==1 {print $1 * 100}')
# COVERAGE=$(grep -oP 'line-rate="\K[0-9.]+' coverage.xml | awk '{print $1 * 100}')

# Validate Coverage extraction
if [ -z "$COVERAGE" ]; then
  echo "Failed to retrieve coverage percentage!"
  exit 1
fi

echo "Test Coverage: $COVERAGE%"

# Remove old badges from README
sed -i '/!\[pylint\]/d' README.md
sed -i '/!\[coverage\]/d' README.md

# Insert updated badges at the top
echo "![pylint](https://img.shields.io/badge/pylint-$PYLINT_SCORE-green)" | cat - README.md > temp.md && mv temp.md README.md
echo "![coverage](https://img.shields.io/badge/coverage-$COVERAGE%25-blue)" | cat - README.md > temp.md && mv temp.md README.md

# Commit and push the updated badges
git add README.md
git commit -m "Update pylint and coverage badges"
git push origin dev  # Change 'dev' to your branch

echo "Badges updated successfully!"











