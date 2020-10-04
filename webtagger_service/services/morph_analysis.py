from estnltk.taggers import VabamorfTagger
from webtagger_service.services import common

tagger = VabamorfTagger()


def tag(data):
    return common.apply_tagger(data, tagger)
