# ***************************************************************************************************************
# * Changelog										
# * All notable changes to this project will be documented in this file.	
# ***************************************************************************************************************
# *
# * Author				: Akash Singh
# *
# * Date created		: 11/01/2021
# *
# * Purpose			    : English Flair NLP API
# *
# * Revision History	:
# *
# * Date			Author			    Jira			Functionality 
# * 12/01/2021     Akash Singh         EC-583          Added Status Codes & Try-Except for Error Handling
# ***************************************************************************************************************
#
#Importing koalanlp function from Korean Prediction Script
from predict import korNLP
#Importing KobertModelLoader function from Korean Prediction Script
from predict import KobertModelLoader
#Importing english NLP function from engNLP
from engNLP import ner
# Importing Flask for creating a python server
from flask import Flask, request, abort
app = Flask(__name__)

# API for NLP Server
@app.route('/nlp/ko', methods=['POST'])
def koreanExtract():
    # Request Received
    print("Request Received")
    # Message for Named Entity Recognition
    text_for_NER = request.get_json()["messages"]
    if text_for_NER == "":
        #Creating a JSON response
        json_response = {
            "money" : "",
            "location" : "",
            "details" : ""
        }
        return json_response
    else:
        # Calling Extraction Script for Performing NER
        json_response = korNLP(text_for_NER)
        # Returning Response for API
        return json_response


@app.route('/nlp/en', methods=['POST'])
def englishExtract():
    # Request Received
    print("Request Received")
    # Message for Named Entity Recognition
    text_for_NER = request.get_json()["messages"]
    # Calling Extraction Script for Performing NER
    json_response = ner(text_for_NER)
    # Returning Response for API
    return json_response


if __name__ == '__main__':
    KobertModelLoader()
    from waitress import serve
    serve(app,port=30080)