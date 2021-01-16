# **********************************************************************
# * Changelog										
# * All notable changes to this project will be documented in this file.	
# **********************************************************************
# *
# * Author				: Akash Singh
# *
# * Date created		: 11/01/2021
# *
# * Purpose			    : English Flair NLP Extraction Script
# *
# * Revision History	:
# *
# * Date			Author			    Jira			Functionality 
# * 
# **********************************************************************
#
#Importing Flair Dependencies & Segtok Segmenter
from flair.data import Sentence
from flair.models import SequenceTagger
from segtok.segmenter import split_single
#Loading Flair "ner-ontonotes-fast" Model
tagger = SequenceTagger.load('ner-ontonotes-fast')

# Definition for NER Extraction
def ner(para):
    #Passing text to Sentence
    sentence = Sentence(para)

    # Run NER on sentence to identify Entities
    tagger.predict(sentence)

    #Initialising the default entities variables
    org=''
    money =0
    location=''
    product=''

    #Fetching the named entitites 
    for span in sentence.get_spans():
        entities = span.to_dict()
        for labl in entities['labels']:
            if labl.value == 'MONEY':
                money=entities['text']
            elif labl.value == 'ORG':
                org=org + entities['text'] + " "
            elif labl.value == 'PRODUCT':
                product=product + entities['text'] + " "
            elif labl.value == 'GPE':
                location=location + entities['text'] + " "

    #Creating a JSON response
    entity_json = {
        "money" : money,
        "location" : location,
        "details" : org + product
    }
    print(entity_json)
    #Sending back the resoponse
    return entity_json