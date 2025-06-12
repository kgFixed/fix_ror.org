import os

# utilisation de sema.subyt
from sema.subyt import (
    Generator,
    GeneratorSettings,
    Sink,
    Source,
    SinkFactory,
    SourceFactory,
    JinjaBasedGenerator,
)

def json_to_rdf(path_json_file, template_name, template_directory, ouput_directory):
    input_json = f"{path_json_file}"

    output_ttl = f"{ouput_directory}/all_grouped_organisation.ttl"
    template_file = f"{template_name}.ttl"
    template_path = os.path.join(os.path.dirname(__file__), f"{template_directory}")

    # Initialisation
    generator = JinjaBasedGenerator(template_path)
    sink = SinkFactory.make_sink(output_ttl, False)
    inputs = {"qres": SourceFactory.make_source(input_json)}

    # Génération
    generator.process(template_file, inputs, GeneratorSettings(), sink, {})

# Appel de la fonction
json_to_rdf("data/v1.66-2025-05-20-ror-data.json", "template", "template", "rdf")