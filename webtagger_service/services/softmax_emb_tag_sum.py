from estnltk.taggers.neural_morph.new_neural_morph.neural_morph_tagger import SoftmaxEmbTagSumTagger
from webtagger_service.services import common

tagger = SoftmaxEmbTagSumTagger()


def tag(data):
    return common.apply_tagger(data, tagger)