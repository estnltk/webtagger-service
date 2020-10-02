from estnltk.taggers import VabamorfTagger
from . import common


tagger = VabamorfTagger()


def tag(data):
    return common.apply_tagger(data, tagger)
