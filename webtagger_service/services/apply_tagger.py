from estnltk import Text
from estnltk.converters import layer_to_json, json_to_layers


class TextMock:
    __slots__ = ['__dict__']

    def __init__(self, layers: dict):
        self.__dict__ = layers


def apply_tagger(data, tagger):
    text = Text(data['text'])
    text.meta = data['meta']
    layers = json_to_layers(text, data['layers'])

    for layer in Text.list_layers(TextMock(layers)):
        text.add_layer(layer)

    layer = tagger.make_layer(text, layers)
    layer.name = data['output_layer']
    return layer_to_json(layer)
