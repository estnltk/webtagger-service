from estnltk.taggers import VabamorfTagger
from . import apply_tagger

tagger = VabamorfTagger()


def tag(data):
    return apply_tagger.apply_tagger(data, tagger)
