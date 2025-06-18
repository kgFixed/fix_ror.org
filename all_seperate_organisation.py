import json
from pathlib import Path
import tempfile
from sema.subyt import Subyt

def json_to_individual_rdf(json_path, template_path, output_dir):
    output_dir = Path(output_dir) / "organisations"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(json_path, encoding='utf-8') as f:
        for org in json.load(f):
            ror_id = org['id'].split('/')[-1]
            
            # Créez un fichier JSON temporaire
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as tmp:
                json.dump({"sets": {"qres": [org]}}, tmp, ensure_ascii=False, indent=2)
                tmp_path = tmp.name
            
            try:
                # Utilisez le fichier comme source
                Subyt(
                    template_name=Path(template_path).name,
                    template_folder=str(Path(template_path).parent),
                    extra_sources={"qres": str(Path(tmp_path).resolve())},
                    sink=str(output_dir / f"{ror_id}.ttl"),
                    overwrite_sink=True,
                    conditional=False
                ).process()
            finally:
                Path(tmp_path).unlink()  # Nettoyage

# Exemple d'utilisation
json_to_individual_rdf(
    json_path="data/v1.66-2025-05-20-ror-data.json",
    template_path="template/template.ttl",
    output_dir="rdf"
)