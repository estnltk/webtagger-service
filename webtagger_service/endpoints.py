from flask import Flask, request

from webtagger_service.services.tag_layer import tag_layer
from .services import bert_embeddings, morph_analysis, softmax_emb_tag_sum

app = Flask(__name__, static_folder=None, template_folder=None)


@app.route('/tag_layer/<layer_names>', methods=['POST'])
def tag_layer_endpoint(layer_names):
    return tag_layer(layer_names, request.json)


@app.route('/tag/morph_analysis', methods=['POST'])
def tag_morph_analysis_endpoint():
    return morph_analysis.tag(request.json)


@app.route('/tag/bert_embeddings', methods=['POST'])
def tag_bert_embeddings_endpoint():
    return bert_embeddings.tag(request.json)


@app.route('/tag/morph_softmax_emb_tag_sum', methods=['POST'])
def tag_morph_softmax_emb_tag_sum_endpoint():
    return softmax_emb_tag_sum.tag(request.json)
