from estnltk.taggers.neural_morph.new_neural_morph.neural_morph_tagger import SoftmaxEmbTagSumTagger
from . import apply_tagger

tagger = SoftmaxEmbTagSumTagger()


def tag(data):
    return apply_tagger.apply_tagger(data, tagger)
