# Scrum Automation

This repository contains Playwright + Pytest UI automation tests.

## What we changed

- Test report output was moved to docs/report.html in pytest.ini.
- A GitHub Pages workflow was added at .github/workflows/deploy-pages.yml.
- A simple Pages landing file was added at docs/index.html.
- docs/.nojekyll was added for static Pages hosting.
- Current report file was copied to docs/report.html.

## How to generate report

1. Run tests.
2. Pytest creates the HTML report at docs/report.html.

## GitHub Pages

- The workflow deploys the docs folder on push to main.
- Open the deployed page and click the report link from docs/index.html.
