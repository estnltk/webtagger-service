from estnltk.converters import json_to_text, layer_to_json, json_to_layers
from estnltk.taggers.embeddings.bert.bert_tagger import BertTagger


tagger = BertTagger(bert_location='/home/paul/Projects/estnltk/data/estnltk/multi_cased_L-12_H-768_A-12')


def tag(data):
    text = json_to_text(data['text'])
    layers = json_to_layers(text, data['layers'])

    layer = tagger.make_layer(text, layers)
    layer.name = data['output_layer']
    return layer_to_json(layer)
