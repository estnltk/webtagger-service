from estnltk import Text
from estnltk.converters import text_to_json, json_to_layers


def tag_layer(data):
    text = Text(data['text'])
    text.meta = data['meta']
    layers = json_to_layers(text, data['layers'])

    for layer in Text.topological_sort(layers):
        text.add_layer(layer)

    text.tag_layer(layer_names=data['parameters']['layer_names'])
    return text_to_json(text)
