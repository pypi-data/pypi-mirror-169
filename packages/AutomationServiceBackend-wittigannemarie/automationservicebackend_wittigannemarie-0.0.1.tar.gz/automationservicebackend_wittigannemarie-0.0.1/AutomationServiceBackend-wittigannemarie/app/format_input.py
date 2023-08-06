import sys
import os.path
import logging
import sys
from dotenv import load_dotenv
from helper.file_helper import file_helper

def validate_file(dir_path, file_name, new_name, helper: file_helper):
    if (not helper.check_file_size(dir_path + file_name)):
        logging.warning(file_name + " is either not a file or emtpy, it cannot be used.")
    else:
        os.rename(dir_path + file_name, dir_path + new_name)

load_dotenv()
helper = file_helper()

training_data_path = os.getenv('TRAININGLOCATION')
numberofarguments = len(sys.argv[1:])

if (numberofarguments == 0):
    logging.info("No filenames were given. If you want a new model trained, you must enter the names of your .csv files in the .env file.")
    sys.exit(0)

elif (numberofarguments == 1):
    logging.warning("There is a training or testingfile missing. You must enter both names into the .env file for initializing training.")
    sys.exit(0)

else:
    training = sys.argv[1].replace("\"", "")
    testing = sys.argv[2].replace("\"", "")
    logging.info("Checking the files: " + training + " for training and " + testing + " for testing.")
    validate_file(training_data_path, training, "train.csv", helper)
    validate_file(training_data_path, testing, "test.csv", helper)
    


