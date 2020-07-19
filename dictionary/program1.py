# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:19:23 2020

@author: tapierolandia
"""

import json

data =json.load(open("data.json"))

def traslate(word):
    
    word=word.lower()
    if word in data:
        
        return(data[word])
    else:
        return "word doesn't fine in the diccionary"
        


word=input("Ingress a word :")

print(traslate(word))
