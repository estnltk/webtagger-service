from estnltk.converters import json_to_text, layer_to_json, json_to_layers
from estnltk.taggers import VabamorfTagger

morph_analysis_tagger = VabamorfTagger()


def tag_morph_analysis(data):
    text = json_to_text(data['text'])
    layers = json_to_layers(text, data['layers'])

    layer = morph_analysis_tagger.make_layer(text, layers)
    layer.name = data['output_layer']
    return layer_to_json(layer)
