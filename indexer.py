# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:42:46 2020

@author: Dalia
"""
from elasticsearch import Elasticsearch as es
import cfg
import json

class Indexer:
    def __init__(self):
        self.es = es([{'host': cfg.esHost, 'port': cfg.esPortNo}],retry_on_timeout=True)
        if self.es.indices.exists(cfg.indexName) == False:
            requestBody = {"settings" : {"number_of_shards": 1,"number_of_replicas": 0}}
            self.es.indices.create(index = cfg.indexName, body = requestBody)
        
    def Index(self, _id, _document):
        print(_document['name'])
        return self.es.index(index=cfg.indexName, doc_type=_document['name'], id=_id, body=json.dumps(_document))