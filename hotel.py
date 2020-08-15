# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:27:08 2020

@author: Dalia
"""
import indexer
import analyzer

class Hotel:
    def __init__(self, _indexer, _hotelName, _hotelData, _id):
        self.hotelName = _hotelName
        self.analyzed = False
        self.indexer = _indexer
        self.id = _id
        self.data = _hotelData
        
    def Analyze(self):
        if self.analyzed == True:
            return [{"user":review["username"] ,"review": review["text"], "tone": review["tone"]} for review in self.data["reviews"]]
        
        for i, review in enumerate(self.data["reviews"]):
            self.data["reviews"][i]["tone"] = analyzer.GetToneAnalysis(review["text"])

        self.analyzed = True

        return [{"user":review["username"] ,"review": review["text"], "tone": review["tone"]} for review in self.data["reviews"]]

    def Index(self):
        if self.analyzed == False:
            self.Analyze()
        ret = self.indexer.Index(self.id, self.data)
        flag = ret["result"] == "created"
        return flag
        