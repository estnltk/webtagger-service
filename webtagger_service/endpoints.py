from flask import Flask, request

from webtagger_service.services.tag_layer import tag_layer
from .services import bert_embeddings, morph_analysis, softmax_emb_tag_sum

estntk_v16_service = Flask(__name__, static_folder=None, template_folder=None)


# tag_layer


@estntk_v16_service.route('/tag_layer', methods=['POST'])
def tag_layer_endpoint():
    return tag_layer(request.json)


@estntk_v16_service.route('/tag_layer/about', methods=['GET'])
def tag_layer_about_endpoint():
    return 'Tags layers using EstNLTK 1.6.7beta webservice.'


@estntk_v16_service.route('/tag_layer/status', methods=['GET'])
def tag_layer_status_endpoint():
    return 'OK'


# tag_morph_analysis


@estntk_v16_service.route('/tag/morph_analysis', methods=['POST'])
def tag_morph_analysis_endpoint():
    return morph_analysis.tag(request.json)


@estntk_v16_service.route('/tag/morph_analysis/about', methods=['GET'])
def tag_morph_analysis_about_endpoint():
    return 'Tags morphological analysis using EstNLTK 1.6.7beta webservice.'


@estntk_v16_service.route('/tag/morph_analysis/status', methods=['GET'])
def tag_morph_analysis_status_endpoint():
    return 'OK'


# tag_bert_embeddings


@estntk_v16_service.route('/tag/bert_embeddings', methods=['POST'])
def tag_bert_embeddings_endpoint():
    return bert_embeddings.tag(request.json)


@estntk_v16_service.route('/tag/bert_embeddings/about', methods=['GET'])
def tag_bert_embeddings_about_endpoint():
    return 'Tags BERT embeddings using EstNLTK 1.6.7beta webservice.'


@estntk_v16_service.route('/tag/bert_embeddings/status', methods=['GET'])
def tag_bert_embeddings_status_endpoint():
    return 'OK'


# tag_morph_softmax_emb_tag_sum


@estntk_v16_service.route('/tag/morph_softmax_emb_tag_sum', methods=['POST'])
def tag_morph_softmax_emb_tag_sum_endpoint():
    return softmax_emb_tag_sum.tag(request.json)


@estntk_v16_service.route('/tag/morph_softmax_emb_tag_sum/about', methods=['GET'])
def tag_morph_softmax_emb_tag_sum_about_endpoint():
    return 'Performs neural morphological tagging using EstNLTK 1.6.7beta webservice.'


@estntk_v16_service.route('/tag/morph_softmax_emb_tag_sum/status', methods=['GET'])
def tag_morph_softmax_emb_tag_sum_status_endpoint():
    return 'OK'
