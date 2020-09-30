import json


def test_tag_morph_analysis(client):
    data = {'text': '{"text": "Tere, maailm!", '
                    '"meta": {}, '
                    '"layers": []}',
            'layers': '{"tokens": {"name": "tokens", "attributes": [], "parent": null, "enveloping": null, "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{}]}, {"base_span": [4, 5], "annotations": [{}]}, {"base_span": [6, 12], "annotations": [{}]}, {"base_span": [12, 13], "annotations": [{}]}]}, '
                      '"words": {"name": "words", "attributes": ["normalized_form"], "parent": null, "enveloping": null, "ambiguous": true, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"normalized_form": null}]}, {"base_span": [4, 5], "annotations": [{"normalized_form": null}]}, {"base_span": [6, 12], "annotations": [{"normalized_form": null}]}, {"base_span": [12, 13], "annotations": [{"normalized_form": null}]}]}, '
                      '"compound_tokens": {"name": "compound_tokens", "attributes": ["type", "normalized"], "parent": null, "enveloping": "tokens", "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": []}, '
                      '"sentences": {"name": "sentences", "attributes": [], "parent": null, "enveloping": "words", "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [[0, 4], [4, 5], [6, 12], [12, 13]], "annotations": [{}]}]}}',
            'output_layer': 'morph_analysis'}

    rv = client.post('/tag/morph_analysis', json=data)

    assert rv.status_code == 200
    assert json.loads(rv.data) == {
        'name': 'morph_analysis',
        'attributes': ['normalized_text',
                       'lemma',
                       'root',
                       'root_tokens',
                       'ending',
                       'clitic',
                       'form',
                       'partofspeech'],
        'parent': 'words',
        'enveloping': None,
        'ambiguous': True,
        'serialisation_module': None,
        'meta': {},
        'spans': [{'base_span': [0, 4],
                   'annotations': [{'normalized_text': 'Tere',
                                    'lemma': 'tere',
                                    'root': 'tere',
                                    'root_tokens': ['tere'],
                                    'ending': '0',
                                    'clitic': '',
                                    'form': '',
                                    'partofspeech': 'I'}]},
                  {'base_span': [4, 5],
                   'annotations': [{'normalized_text': ',',
                                    'lemma': ',',
                                    'root': ',',
                                    'root_tokens': [','],
                                    'ending': '',
                                    'clitic': '',
                                    'form': '',
                                    'partofspeech': 'Z'}]},
                  {'base_span': [6, 12],
                   'annotations': [{'normalized_text': 'maailm',
                                    'lemma': 'maailm',
                                    'root': 'maa_ilm',
                                    'root_tokens': ['maa', 'ilm'],
                                    'ending': '0',
                                    'clitic': '',
                                    'form': 'sg n',
                                    'partofspeech': 'S'}]},
                  {'base_span': [12, 13],
                   'annotations': [{'normalized_text': '!',
                                    'lemma': '!',
                                    'root': '!',
                                    'root_tokens': ['!'],
                                    'ending': '',
                                    'clitic': '',
                                    'form': '',
                                    'partofspeech': 'Z'}]}]
    }


def test_tag_softmax_emb_tag_sum(client):
    data = {'text': '{"text": "Tere, maailm!",'
                    '"meta": {}, '
                    '"layers": [{"name": "words", "attributes": ["normalized_form"], "parent": null, "enveloping": null, "ambiguous": true, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"normalized_form": null}]}, {"base_span": [4, 5], "annotations": [{"normalized_form": null}]}, {"base_span": [6, 12], "annotations": [{"normalized_form": null}]}, {"base_span": [12, 13], "annotations": [{"normalized_form": null}]}]}, {"name": "morph_analysis", "attributes": ["normalized_text", "lemma", "root", "root_tokens", "ending", "clitic", "form", "partofspeech"], "parent": "words", "enveloping": null, "ambiguous": true, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"normalized_text": "Tere", "lemma": "tere", "root": "tere", "root_tokens": ["tere"], "ending": "0", "clitic": "", "form": "", "partofspeech": "I"}]}, {"base_span": [4, 5], "annotations": [{"normalized_text": ",", "lemma": ",", "root": ",", "root_tokens": [","], "ending": "", "clitic": "", "form": "", "partofspeech": "Z"}]}, {"base_span": [6, 12], "annotations": [{"normalized_text": "maailm", "lemma": "maailm", "root": "maa_ilm", "root_tokens": ["maa", "ilm"], "ending": "0", "clitic": "", "form": "sg n", "partofspeech": "S"}]}, {"base_span": [12, 13], "annotations": [{"normalized_text": "!", "lemma": "!", "root": "!", "root_tokens": ["!"], "ending": "", "clitic": "", "form": "", "partofspeech": "Z"}]}]}, {"name": "neural_morph_analysis", "attributes": ["morphtag", "pos", "form"], "parent": "words", "enveloping": null, "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"morphtag": "POS=I", "pos": "I", "form": ""}]}, {"base_span": [4, 5], "annotations": [{"morphtag": "POS=Z|PUNCT_TYPE=Com", "pos": "Z", "form": ""}]}, {"base_span": [6, 12], "annotations": [{"morphtag": "POS=S|NOUN_TYPE=com|NUMBER=sg|CASE=nom", "pos": "S", "form": "sg n"}]}, {"base_span": [12, 13], "annotations": [{"morphtag": "POS=Z|PUNCT_TYPE=Exc", "pos": "Z", "form": ""}]}]}, {"name": "sentences", "attributes": [], "parent": null, "enveloping": "words", "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [[0, 4], [4, 5], [6, 12], [12, 13]], "annotations": [{}]}]}]}',
            'layers': '{"morph_analysis": {"name": "morph_analysis", "attributes": ["normalized_text", "lemma", "root", "root_tokens", "ending", "clitic", "form", "partofspeech"], "parent": "words", "enveloping": null, "ambiguous": true, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"normalized_text": "Tere", "lemma": "tere", "root": "tere", "root_tokens": ["tere"], "ending": "0", "clitic": "", "form": "", "partofspeech": "I"}]}, {"base_span": [4, 5], "annotations": [{"normalized_text": ",", "lemma": ",", "root": ",", "root_tokens": [","], "ending": "", "clitic": "", "form": "", "partofspeech": "Z"}]}, {"base_span": [6, 12], "annotations": [{"normalized_text": "maailm", "lemma": "maailm", "root": "maa_ilm", "root_tokens": ["maa", "ilm"], "ending": "0", "clitic": "", "form": "sg n", "partofspeech": "S"}]}, {"base_span": [12, 13], "annotations": [{"normalized_text": "!", "lemma": "!", "root": "!", "root_tokens": ["!"], "ending": "", "clitic": "", "form": "", "partofspeech": "Z"}]}]}, "sentences": {"name": "sentences", "attributes": [], "parent": null, "enveloping": "words", "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [[0, 4], [4, 5], [6, 12], [12, 13]], "annotations": [{}]}]}, "words": {"name": "words", "attributes": ["normalized_form"], "parent": null, "enveloping": null, "ambiguous": true, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"normalized_form": null}]}, {"base_span": [4, 5], "annotations": [{"normalized_form": null}]}, {"base_span": [6, 12], "annotations": [{"normalized_form": null}]}, {"base_span": [12, 13], "annotations": [{"normalized_form": null}]}]}, "neural_morph_analysis": {"name": "neural_morph_analysis", "attributes": ["morphtag", "pos", "form"], "parent": "words", "enveloping": null, "ambiguous": false, "serialisation_module": null, "meta": {}, "spans": [{"base_span": [0, 4], "annotations": [{"morphtag": "POS=I", "pos": "I", "form": ""}]}, {"base_span": [4, 5], "annotations": [{"morphtag": "POS=Z|PUNCT_TYPE=Com", "pos": "Z", "form": ""}]}, {"base_span": [6, 12], "annotations": [{"morphtag": "POS=S|NOUN_TYPE=com|NUMBER=sg|CASE=nom", "pos": "S", "form": "sg n"}]}, {"base_span": [12, 13], "annotations": [{"morphtag": "POS=Z|PUNCT_TYPE=Exc", "pos": "Z", "form": ""}]}]}}',
            'output_layer': 'neural_morph_analysis'}

    rv = client.post('/1.6.7beta/tag/morph_softmax_emb_tag_sum', json=data)

    assert json.loads(rv.data) == {
        'name': 'neural_morph_analysis',
        'attributes': ['morphtag', 'pos', 'form'],
        'parent': 'words',
        'enveloping': None,
        'ambiguous': False,
        'serialisation_module': None,
        'meta': {},
        'spans': [{'base_span': [0, 4],
                   'annotations': [{'morphtag': 'POS=I', 'pos': 'I', 'form': ''}]},
                  {'base_span': [4, 5],
                   'annotations': [{'morphtag': 'POS=Z|PUNCT_TYPE=Com',
                                    'pos': 'Z',
                                    'form': ''}]},
                  {'base_span': [6, 12],
                   'annotations': [{'morphtag': 'POS=S|NOUN_TYPE=com|NUMBER=sg|CASE=nom',
                                    'pos': 'S',
                                    'form': 'sg n'}]},
                  {'base_span': [12, 13],
                   'annotations': [{'morphtag': 'POS=Z|PUNCT_TYPE=Exc',
                                    'pos': 'Z',
                                    'form': ''}]}]
    }
