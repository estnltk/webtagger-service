from estnltk.taggers.embeddings.bert.bert_tagger import BertTagger
from . import common


tagger = BertTagger(bert_location='/home/paul/Projects/estnltk/data/estnltk/multi_cased_L-12_H-768_A-12')


def tag(data):
    return common.apply_tagger(data, tagger)
