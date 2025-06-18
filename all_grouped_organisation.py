from sema.subyt import Subyt
from sema.subyt.sources import SourceFactory
from pathlib import Path

def json_to_rdf(json_path, template_path, output_path):
    Subyt(
        template_name="template.ttl",
        template_folder=str(Path(template_path).parent),
        sink=str(Path(output_path).resolve()),
        extra_sources={"qres": str(Path(json_path).resolve())},
    ).process()

json_to_rdf(
    json_path="data/v1.66-2025-05-20-ror-data.json",
    template_path="template/template.ttl",
    output_path="rdf/all_organisation.ttl"
)