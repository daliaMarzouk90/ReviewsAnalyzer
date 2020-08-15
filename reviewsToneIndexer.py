# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:45:04 2020

@author: Dalia
"""
import loader
import analyzer
import indexer

def __init__():
    pass

def index():
    Indexer = indexer.Indexer()
    
    for review in loader.LoadDataSeq():
        toneScore = analyzer.GetToneAnalysis(review["reviews.text"])
        review["toneScore"] = toneScore
        Indexer.Index(_id,review )