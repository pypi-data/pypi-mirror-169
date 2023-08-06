from typing import Dict, List, Optional
from starlette.requests import Request
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import logging

from app.model.request_handler import handle_post_api_call, handle_post_retrain_call, handle_get_api_call, handle_get_visualization_call
from app.spacy_model.interact_with_spacy import spacy_interface
from app.spacy_model.retrain_a_model import model_retrainer
from app.helper.file_helper import file_helper
 
description = """
This Automation Service can **automatically generate a NER model** and offer an endpoint to interact with it.

If **training and testing-data** is provided and no existing model was uploaded, this service will train and use a brand new model for you!
You will be able to send a text to the **\\api endpoint** and receive the NER result for the given text!
You can also send multiple texts and files to that endpoint to have them annotated with the results.
The **\\retrain endpoint** allows you to retrain your model run-time!
"""
tags_metadata = [
    {
        "name": "api",
        "description": "Allows to retrieve NER result of a given input text. Will return the recognized entities and their labels. If larger quantities are uploaded, it allows to annotate an uploaded CSV file/JSON file/ JSON request body with NER results. A CSV file must have texts to identify in the first column whilst a json file must consist of an array where each object has the text to identify with the label \"text\"",
    },
    {
        "name": "retrain",
        "description": "Allows to retrain the NER model based on a given input. The old one will be overwritten."
    }
]

app = FastAPI(
    title="AutomationService",
    description=description,
    version="0.0.1",
)
logging.getLogger().setLevel(logging.INFO)
interface = spacy_interface()
trainer = model_retrainer()
helper = file_helper()

class Input(BaseModel):
    text: str = Field (
        title="A text that should be identified.", example= "I am called Marilyn Monroe."
    )
    language: str = Field (
        default=None, title="A language string.", max_length=2, example="en"
    )
    entities: Dict[str, str] = Field (
        default=None, title="A dictionary of included entities and their labels.", 
        example= {"First_Name": "Marilyn", "Last_Name": "Monroe"}
    )

class Output(Input):
    results: Dict[str, str] = Field (
        default=None, title="A dictionary of recognized entities and their labels.", 
        example= {"FIRST_NAME": "Marilyn", "LAST_NAME": "Monroe"}
    )

    class Config:
        orm_mode=True

class Retraindata (BaseModel):
    testingdata: List[Input] = Field (
        title="A list of objects to test the model with."
    )
    trainingdata: List[Input] = Field (
        title="A list of objects to train the model with."
    )
    entities: List[str] = Field (
        title="A list of all entity-labels that the NER model should learn. "
        + "All entities mentioned within the document must be listed here.", example= ["First_Name", "Middle_Name", "Last_Name"]
    )
    language: str = Field (
        title="The language the new NER model should be based on. ", example= "en"
    )
    modeltype: str = Field (
        title="The base model the new NER model should trained on (currently supporting: 'bert', 'spacy'). ", example= "en"
    )

class SuccessMessage(BaseModel):
    message: str = Field(
        title="A success message.", example= "Successfully updated the spacy model based on your uploaded csv data."
    )

@app.get("/api", 
        tags=["api"],
        summary="Receive a NER result.",
        response_description="The extracted entities.",
        responses={
        200: {
            "description": "An example result",
            "content": {
                "application/json": {
                    "example": {
                        "text": "I am Marilyn Monroe.",
                        "FIRST_NAME": "Marilyn",
                        "LAST_NAME": "Monroe"
                    }
                }
            },
        },
    },
)
def call_recognition(text: str = 'Text to identify'):
    """
    Receive a JSON object containing the indentified entities and their labels. The form depends on your model. 
    With the default example model, a text to identify could be "I am {YOUR NAME}" with or without the optional language string "en".
    """
    result = handle_get_api_call(text, interface)
    return result

@app.post("/api", 
        tags=["api"],
        summary="Receive a NER result.",
        response_description="The extracted entities.",
        openapi_extra={
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "array",
                            "items": Input.schema(ref_template="#/components/schemas/{model}")
                        }
                    }
                }
            }
        },
        responses={
        200: {
            "description": "An example result",
            "content": {
                "application/json": {
                    "schema": {
                            "type": "array",
                            "items": Output.schema(ref_template="#/components/schemas/{model}")
                    }
                }, 
                "text/csv" : {}
            },
        }
    })
async def handle_api_call(req: Request, file_to_identify: Optional[UploadFile] = File(None)):
    """
    Generate a NER result of multiple input texts.
    If you enter a csv file, each line must contain the text that shall be identified in the first column.
    If you enter a json file or json request body, it must contain an array in which each element has the
    text that is supposed to be identified with a "text" label.
    Any other wanted columns / objects can be added and will not be changed or removed by the service.
    The result will be the input file annotated with the results.
    """
    response = await handle_post_api_call(req, interface, helper, file_to_identify)
    return response

@app.post("/retrain", 
        tags=["retrain"],
        summary="Retrain a model.",
        response_description="A success message.",
        openapi_extra={
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema":  Retraindata.schema(ref_template="#/components/schemas/{model}")
                    }
                }
            }
        },
        responses={
        200: {
            "description": "An example success message",
            "content": {
                "application/json": {
                    "schema": SuccessMessage.schema(ref_template="#/components/schemas/{model}")
                }
            },
        }
    })
async def handle_retrain_call(req: Request, trainingdata: Optional[UploadFile] = File(None), testingdata: Optional[UploadFile] = File(None), options: Optional[UploadFile] = File(None)):
    """
    Retrain your model in runtime based on your given input. It needs either two CSV files (trainingdata and testingdata) with an optional JSON file (options, defaults will be set if none given),
    three JSON files (trainingdata, testingdata and options) or a JSON request body containing all three previously
    mentioned files within one. If correctly structured, the data is used to retrain a new model and overwrite the existing one.
    """
    response = await handle_post_retrain_call(req, trainer, interface, trainingdata, testingdata, options)
    return response

@app.get("/visualize", 
        tags=["visualize"],
        summary="Visualize an NER result.",
        response_description="The visualisation as HTML.",
        response_class=HTMLResponse
)
def get_visual(text: str = 'Text to identify'):
    """
    Receive a JSON object containing the indentified entities and their labels. The form depends on your model. 
    With the default example model, a text to identify could be "I am {YOUR NAME}" with or without the optional language string "en".
    """
    result = handle_get_visualization_call(text, interface)
    return result


@app.get("/health",
        tags=["health"],
        summary="Check if the service is running and accessible.",
        response_description="An \"ok\" if all is well.",
        responses={
        200: {
            "description": "Confirmation of service",
            "content": {
                "application/json": {
                    "example": {  
                        "status": "ok"
                        }
                    }
                }
            }
        }
    )
def am_i_ok():
    """
    Check if the service is addressable.
    """
    return {"status":"ok"}
