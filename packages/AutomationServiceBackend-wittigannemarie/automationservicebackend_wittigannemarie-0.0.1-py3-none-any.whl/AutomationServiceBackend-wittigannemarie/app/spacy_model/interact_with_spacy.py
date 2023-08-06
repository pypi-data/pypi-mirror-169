import json
import spacy 
import logging
import pandas as pd
import os
from spacy import displacy
from io import StringIO
from fastapi import UploadFile
from datetime import datetime
from dotenv import load_dotenv

class spacy_interface():

    load_dotenv()
    model_location = os.getenv('MODELLOCATION')
    results = os.getenv('RESULTLOCATION')

    nlp = spacy.load(model_location)

    def __init__(self):
        logging.info("Spacy parser initialized")

    def initialize_empty_result_object(self):
        result = {}
        for entity in self.nlp.get_pipe('ner').labels:
            result[entity] = ""
        return result


    def get_nlp (self, text):
        '''
        Generate a NER result based on a given input string
        '''
        doc = self.nlp(text)
        results = {}
        result_object = self.initialize_empty_result_object()
        results['text']=text
        result_list=[]
        for entity in doc.ents:
            label = entity.label_
            content = entity.text
            if (result_object[label] == ""):
                result_object[label] = content
            else:
                result_list.append(result_object)
                result_object = self.initialize_empty_result_object()
                result_object[label] = content
        
        result_list.append(result_object)
        results['result'] = result_list
        
        return results

    def get_visualisation(self, text):
        doc2 = self.nlp(text)
        html = displacy.render([doc2], style="dep", page=True)
        html = html + displacy.render([doc2], style="ent", page=True)
        return html

    def reload_nlp(self):
        '''
        Attempt to reload the NER model and replace the current one if the reload is successfull
        '''
        new_nlp = spacy.load("./app/spacy_model/output/model-best")
        self.nlp = new_nlp


    def append_entity_dolumns (self, dataframe: pd.DataFrame):
        for entity in self.nlp.get_pipe('ner').labels:
            dataframe[entity] = ""
        return dataframe

    def bulk_recognization_csv_file (self, uploadfile: UploadFile):
        '''
        Run each line of an input CSV file through NER and annotate it with the results
        '''
        csv_df = pd.read_csv(StringIO(str(uploadfile.file.read(), 'utf-8')), encoding='utf-8', dtype=object)
        identify_df = self.append_entity_dolumns(csv_df)
        identifying_data = identify_df[csv_df.columns[0]]
        no_trainingdata = len(identifying_data)

        for i in range(no_trainingdata):
            doc = self.nlp(identifying_data.iloc[i])
            for entity in doc.ents:
                identify_df[entity.label_][i] = entity.text

        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        identify_df.to_csv(self.results + 'identified-' + date_time + '.csv', sep=',', encoding='utf-8')

        return identify_df
        
    def bulk_recognization_json_file (self, jsonfile: json):
        '''
        Run each object of an input JSON through NER and annotate it with the results
        '''
        for entry in jsonfile:
            entry['results'] = {}
            doc = self.get_nlp(entry['text'])
            entry['results'] = doc['result']

        path = self.results + 'identified-' + datetime.now().strftime("%m-%d-%Y_%H-%M-%S") + '.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(jsonfile, f, ensure_ascii=False, indent=4)

        return jsonfile
        