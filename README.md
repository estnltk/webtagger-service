# Webservice for EstNLTK web-taggers

## Install
1. Set up a Python environment with [EstNLTK 1.6](https://github.com/estnltk/estnltk/tree/devel_1.6) (`version>=1.6.7b`). 
2. Set up [Neural morphological taggers](https://github.com/estnltk/estnltk/blob/devel_1.6/tutorials/taggers/neural_morph_tagger_new.ipynb) and [BertTagger](https://github.com/estnltk/estnltk/blob/devel_1.6/tutorials/taggers/embeddings_tagger.ipynb).
3. Clone this repository
4. Install
    ```
    pip install webtagger-service
    ```

## Run
    cd webtagger-service
    python server.py
This will run the server at http://127.0.0.1:5000.    

## Existing endpoints

http://127.0.0.1:5000/1.6.7beta/tag/bert_embeddings

http://127.0.0.1:5000/1.6.7beta/tag/morph_softmax_emb_tag_sum

These endpoints are used by the EstNLTK web-taggers. About web-taggers see
https://github.com/estnltk/estnltk/tree/devel_1.6/estnltk/taggers/web_taggers and https://github.com/estnltk/estnltk/blob/devel_1.6/tutorials/taggers/web_taggers.ipynb.

## Create a new endpoint

To create a new endpoint
1. create a new service (see [morph_analysis](webtagger_service/morph_analysis.py) as an example),
2. create a new endpoint (see [endpoints](webtagger_service/endpoints.py) for examples),
3. write [tests](tests).

Also, you probably want to create a new web-tagger that uses the endpoint.
See https://github.com/estnltk/estnltk/tree/devel_1.6/estnltk/taggers/web_taggers.
