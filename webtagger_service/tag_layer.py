from estnltk.converters import json_to_text, text_to_json


def tag_layer(layer_names, data):
    text = json_to_text(data)
    text.tag_layer(layer_names.split(','))
    return text_to_json(text)
