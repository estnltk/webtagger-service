from flask import Flask, request

from .morph_analysis import tag_morph_analysis
from . import softmax_emb_tag_sum
from .tag_layer import tag_layer


app = Flask(__name__, static_folder=None, template_folder=None)


@app.route('/tag_layer/<layer_names>', methods=['POST'])
def tag_layer_endpoint(layer_names):
    return tag_layer(layer_names, request.json)


@app.route('/tag/morph_analysis', methods=['POST'])
def tag_morph_analysis_endpoint():
    return tag_morph_analysis(request.json)


@app.route('/tag/morph_softmax_emb_tag_sum', methods=['POST'])
def tag_morph_softmax_emb_tag_sum_endpoint():
    return softmax_emb_tag_sum.tag(request.json)
