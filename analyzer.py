# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:59:54 2020

@author: Dalia
"""
import cfg
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(cfg.apikey)
tone_analyzer = ToneAnalyzerV3(
    version=cfg.version,
    authenticator=authenticator
)

tone_analyzer.set_service_url(cfg.url)

def __init__():
    pass

def EditJson(text):
    for i in range(len(text)):
        if text[i] == '\"':
            text[i] = '\''
        elif text[i] == '\t' or text[i] == '\b' or text[i] == '\f' or text[i] == '\n' or text[i] == '\r':
            text[i] = ' '
        elif text[i] == '\\' and i < len(text) - 2 and text[i + 1] != 'u':
            text[i] = ' '
        elif text[i] == '\\' and i == len(text) - 1:
            text[i] = ' '
	
    return text

def ExtractToneAnalysis(analysis):
    tonesAnalysis = {}
    
    for sentenceTone in analysis["sentences_tone"]:
        for tone in sentenceTone["tones"]:
            if tone["tone_id"] not in tonesAnalysis:
                tonesAnalysis[tone["tone_id"]] = {"scoreSum":tone["score"],
                                                  "count": 1}
            else:
                 tonesAnalysis[tone["tone_id"]]["scoreSum"] =  tonesAnalysis[tone["tone_id"]]["scoreSum"] + tone["score"]
                 tonesAnalysis[tone["tone_id"]]["count"] = tonesAnalysis[tone["tone_id"]]["count"] + 1
                 
    return tonesAnalysis

def NormalizeTones(tonesAnalysis):
    tonesScore = {}
    for tone in tonesAnalysis:
        tonesScore[tone] = tonesAnalysis[tone]["scoreSum"] / tonesAnalysis[tone]["count"]
        
    return tonesScore

def GetToneAnalysis(text):
    text = EditJson(text)
    analysis = tone_analyzer.tone({'text': text}, content_type='application/json').get_result()
    
    if 'sentences_tone' not in analysis:
        return {}
    
    tonesAnalysis = ExtractToneAnalysis(analysis)
                 
    tonesScore = NormalizeTones(tonesAnalysis)
    
    return tonesScore