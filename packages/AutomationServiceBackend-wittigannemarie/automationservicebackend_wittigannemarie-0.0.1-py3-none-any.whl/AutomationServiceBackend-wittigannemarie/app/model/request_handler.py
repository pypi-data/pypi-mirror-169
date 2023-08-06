import logging
from typing import Optional
from starlette.requests import Request
from fastapi import UploadFile, File
from fastapi.encoders import jsonable_encoder
import json

def valid_accept_header (accept):
    if (accept == "application/json" or accept == "text/csv"):
        return True
    else:
        return False

def get_accept_header (req: Request, file: UploadFile):
    if (req.headers["Accept"] is not None and valid_accept_header(req.headers["Accept"])):
        return req.headers["Accept"]
    elif (file is not None and valid_accept_header(file.content_type)):
        logging.warning("No valid Accept-Header was set, using the content-type of the uploadfile.")
        return file.content_type
    elif (valid_accept_header(req.headers["content-type"])):
        logging.warning("No valid Accept-Header was set, using the content-type of the request.")
        return req.headers["content-type"]
    else:
        raise ValueError("Please place an Accept Header with either application/json or text/csv as value.")

def read_optional_json_value(value: str, json: json):
    if json is not None and value in json:
        return json[value]
    else:
        return ""

async def handle_post_retrain_call(req: Request, trainer, interface, trainingdata: Optional[UploadFile] = File(None), testingdata: Optional[UploadFile] = File(None), options: Optional[UploadFile] = File(None)):
    success = False
    successmessage = ""
    if (trainingdata is not None and trainingdata.content_type == 'text/csv') and (testingdata is not None and testingdata.content_type == 'text/csv'):
        options_json = None
        if (options is not None and options.content_type == 'application/json'):
            options_json = json.load(options.file)
        language = read_optional_json_value('language', options_json)
        modeltype = read_optional_json_value('modeltype', options_json)
        
        success = trainer.handle_csv_upload(trainingdata, testingdata, language, modeltype)
        successmessage = "Successfully updated the spacy model based on your uploaded csv data."
        trainingdata.file.close()
        testingdata.file.close()

    elif (trainingdata is not None and trainingdata.content_type == 'application/json') and (testingdata is not None and testingdata.content_type == 'application/json') and (options is not None and testingdata.content_type == 'application/json'):
        training_json = json.load(trainingdata.file)
        testing_json = json.load(testingdata.file)
        options_json = json.load(options.file)

        success = trainer.handle_json_upload(training_json["trainingdata"], testing_json["testingdata"], options_json["entities"], read_optional_json_value("language", options_json), read_optional_json_value("modeltype", options_json))
        successmessage = "Successfully updated the spacy model based on your uploaded json files."

        trainingdata.file.close()
        testingdata.file.close()
        options.file.close()

    elif (req.headers["content-type"] == "application/json"):
        data = await req.json()
        success = trainer.handle_json_upload(data['trainingdata'], data['testingdata'], data['entities'], data['language'], data['modeltype'])
        successmessage = "Successfully updated the spacy model based on your request json body."

    else:
        return {"Error": "No supported content is given for retraining the model. The original model remains."}

    if (success):
        try:
            interface.reload_nlp()
            return {"message": successmessage}    
        except:
            logging.error('Could not reload the model. Maybe the files were not moved properly?')
            return {"Error": "Could not reload the model, it will not be uploaded."}
    else:
        return {"Error": "The model could not be updated."}

async def handle_post_api_call(req: Request, interface, helper, file_to_identify: Optional[UploadFile] = File(None)):
    accept = get_accept_header(req, file_to_identify)
    if file_to_identify is not None and file_to_identify.content_type == 'text/csv' :
        df = interface.bulk_recognization_csv_file(file_to_identify)
        response = helper.save_generated_csv_dataframe(df, accept)
        file_to_identify.file.close()
        return response
    elif (file_to_identify is not None and file_to_identify.content_type == 'application/json'):
        json_to_identify = json.load(file_to_identify.file)
        jsonfile = interface.bulk_recognization_json_file(json_to_identify)
        return helper.save_generated_json(jsonfile, accept)
    elif (req.headers["content-type"] == "application/json"):
        json_to_identify = await req.json()
        result = interface.bulk_recognization_json_file(jsonable_encoder(json_to_identify))
        return helper.save_generated_json(result, accept)
    else:
        return {"Error": "No supported content is given to identify. Request[content-type]: " + req.headers["content-type"]} 

def handle_get_api_call (text: str, interface):
    result = interface.get_nlp(text)
    return result

def handle_get_visualization_call(text: str, interface):
    result = interface.get_visualisation(text)
    return result