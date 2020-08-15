# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:41:01 2020

@author: Dalia
"""
import pandas as pd
import cfg

def __init__():
	pass

def ExtractHotelData(_record):
    hotelInfo = {}
    
    for key in _record.keys():
        if "reviews" in key:
            continue
        
        hotelInfo[key] = _record[key]
    
    hotelInfo["reviews"] = []
    return hotelInfo

def ExtractReviewInfo(_record):
    review = {}
    startKey = len("reviews.")
    for key in _record.keys():
        if "reviews" not in key:
            continue
        
        review[key[startKey:]] = _record[key]
        
    return review

def GetHotelsNames():
    df = pd.read_csv(cfg.dataPath)

    hotelsNames = set()

    for index, row in df.iterrows():
        if row["categories"] != "Hotels":
            continue
        
        hotelsNames.add(row["name"])

    return list(hotelsNames)

def LoadHotelData(_hotelName):
    df = pd.read_csv(cfg.dataPath)
    
    data = {"reviews":[]}
    
    for index, row in df.iterrows():
        if row["categories"] != "Hotels":
            continue
        
        if row["name"] != _hotelName:
            continue
        
        if len(data["reviews"]) == 0:
            data = ExtractHotelData(data)
            data["reviews"] = []
        
        review = ExtractReviewInfo(row.where(pd.notnull(row), None).to_dict())
        data["reviews"].append(review)
        
    return data

def LoadHotelsData():
    hotelsInfo = {}
    hotelsNames = set()

    df = pd.read_csv(cfg.dataPath, encoding='utf8')

    for index, row in df.iterrows():
        
        if row["categories"] != "Hotels":
            continue

        hotelRecord = row.where(pd.notnull(row), None).to_dict()

        if row["name"] not in hotelsNames:
            hotelsNames.add(row["name"])
            hotelsInfo[row["name"]] = ExtractHotelData(hotelRecord)
            hotelsInfo[row["name"]]["reviews"] = []

        review = ExtractReviewInfo(hotelRecord)
        hotelsInfo[row["name"]]["reviews"].append(review)

    return hotelsInfo