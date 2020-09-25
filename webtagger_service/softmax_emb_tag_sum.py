from estnltk.converters import json_to_text, layer_to_json, json_to_layers
from estnltk.taggers.neural_morph.new_neural_morph.neural_morph_tagger import SoftmaxEmbTagSumTagger

tagger = SoftmaxEmbTagSumTagger()


def tag(data):
    text = json_to_text(data['text'])
    layers = json_to_layers(text, data['layers'])

    layer = tagger.make_layer(text, layers)
    layer.name = data['output_layer']
    return layer_to_json(layer)
