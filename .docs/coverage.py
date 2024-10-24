import json

# Lire les données de couverture
with open("../reports/coverage.json", "r") as f:
    data = json.load(f)

# Calculer la couverture totale
total_coverage = data["totals"]["percent_covered"]

# Lire le contenu actuel de index.md
with open("docs/index.md", "r") as f:
    index_content = f.read()

# Définir la section Coverage avec la couverture totale
coverage_content = f"\nhttps://img.shields.io/badge/coverage-{total_coverage}%25-brightgreen\n"

# Ajouter la section Coverage à une section existante de index.md
section_header = "## Coverage"  # Assurez-vous que ce titre correspond à celui de votre section existante
if section_header in index_content:
    new_index_content = index_content.replace(section_header, coverage_content)
else:
    new_index_content = index_content + coverage_content

# Écrire le nouveau contenu dans index.md
with open("docs/index.md", "w") as f:
    f.write(new_index_content)
