from estnltk import Text
from estnltk.converters import layer_to_json, json_to_layers


def apply_tagger(data, tagger):
    text = Text(data['text'])
    text.meta = data['meta']
    layers = json_to_layers(text, data['layers'])

    for layer in Text.topological_sort(layers):
        text.add_layer(layer)

    layer = tagger.make_layer(text, layers)
    layer.name = data['output_layer']
    return layer_to_json(layer)
