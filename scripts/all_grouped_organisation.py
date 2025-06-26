from sema.subyt import Subyt
from pathlib import Path

def json_to_rdf(template_name, json_path, template_path, output_path):
    Subyt(
        template_name=f'{template_name}.ttl',
        template_folder=str(Path(template_path).parent),
        sink=str(Path(output_path).resolve()),
        extra_sources={"qres": str(Path(json_path).resolve())},
    ).process()

template_name = "template_1_0"
json_to_rdf(
    json_path="../ror_dump_json/v1.66-2025-05-20-ror-data.json",
    template_path=f"../template/{template_name}.ttl",
    output_path="../output_rdf/all_organisation.ttl",
    template_name= template_name
)