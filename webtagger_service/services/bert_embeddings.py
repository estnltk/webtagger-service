from estnltk.taggers.embeddings.bert.bert_tagger import BertTagger
from . import apply_tagger

tagger = BertTagger(bert_location='/home/paul/Projects/estnltk/data/estnltk/multi_cased_L-12_H-768_A-12')


def tag(data):
    return apply_tagger.apply_tagger(data, tagger)
