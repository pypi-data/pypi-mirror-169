from spacy.cli.train import train
from spacy.cli import download
import spacy
import logging
from dotenv import load_dotenv
import os.path

from .my_exceptions import FailedDocBinException, FailedTrainingException
from .generate_spacy_data import data_generator

class model_helper():
    '''
    Class that is used for direct interaction with spaCy concerning training new models
    '''

    load_dotenv()
    generator = data_generator()

    def generate_docbins(self, inputpath: str, outputpath: str):
        '''
        Generate spaCy docbins used to train a spaCy model
        '''
        try:
            self.generator.generate_doc_bins(inputpath + 'train.csv', outputpath + 'train.spacy')
            self.generator.generate_doc_bins(inputpath + 'test.csv', outputpath + 'test.spacy')
        except:
            raise FailedDocBinException()

    def get_and_control_config(self, lang: str, modeltype: str):
        logging.info('Language: ' + lang)
        logging.info('Modeltype: ' + modeltype)
        model_name = (modeltype + '_' + lang).upper()
        config_name = (model_name + '_CONFIG')
        if model_name in os.environ and config_name in os.environ:
            model = os.getenv(model_name)
            config = os.getenv(config_name)
        else:
            logging.warning('No modeltype or config found for modeltype: \"' + modeltype + '\" and \"' + lang + '\"')
            logging.warning('Using default model (english, empty base)')
            config = os.getenv('DEFAULTCONFIG')
            return config

        try:
            try:
                spacy.load(model)
            except:
                download(model)
        except:
            logging.error('No downloadable model found for the modeltype and language, using default (english, empty base)')
            config = os.getenv('DEFAULTCONFIG')

        return config

    def train_model(self, output_dir: str, training_docbin_file: str, testing_docbin_file: str, lang: str = "", modeltype:str = ""):
        '''
        Trigger a model training
        '''
        config_file = self.get_and_control_config(lang, modeltype)
        logging.info('Using config: ' + config_file)
        gpu = -1
        if spacy.prefer_gpu() and modeltype.lower() == "bert":
            print("\n\033[92m" + "✔ Using GPU" + "\033[0m\n")
            gpu = 0
            try:
                train(config_file, output_dir, use_gpu=gpu,overrides={"paths.train": training_docbin_file, "paths.dev": testing_docbin_file})
            except:
                raise FailedTrainingException()
        else:
            print("\n\033[91m" + "✘ NOT Using GPU!" + "\033[0m\n")
            try:
                train(config_file, output_dir, overrides={"paths.train": training_docbin_file, "paths.dev": testing_docbin_file})
            except:
                raise FailedTrainingException()