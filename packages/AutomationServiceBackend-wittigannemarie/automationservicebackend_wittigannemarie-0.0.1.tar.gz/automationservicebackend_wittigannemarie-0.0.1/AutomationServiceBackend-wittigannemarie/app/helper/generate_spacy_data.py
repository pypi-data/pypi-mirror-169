import spacy
from spacy.tokens import DocBin
import pandas as pd
import re

class data_generator():
    pd.set_option('display.max_colwidth', None)

    def __init__(self):
        print("Data Generator initialized")

    def massage_data(self, name):
        #Pre process name string to remove new line characters, add comma punctuations etc.
        cleansed_name1=re.sub(r'(,)(?!\s)',', ',name)
        cleansed_name2=re.sub(r'(\\n)',', ',cleansed_name1)
        cleansed_name3=re.sub(r'(?!\s)(-)(?!\s)',' - ',cleansed_name2)
        return cleansed_name3

    def get_entity_span(self, entity=None,entity_component=None,label=None):
        '''Search for specified name component and get the span.'''
        if pd.isna(entity_component) or str(entity_component)=='nan':
            pass
        else:
            entity_component1=re.sub('\.','',entity_component)
            entity_component2=re.sub(r'(?!\s)(-)(?!\s)',' - ',entity_component1)
            span=re.search('\\b(?:'+entity_component2+')\\b',entity)
            try:
                return (span.start(),span.end(),label)
            except:
                print('no span for ')
                print(entity)
                print('and')
                print(entity_component)

    def extend_list(self, entity_list,entity):
        if pd.isna(entity):
            return entity_list
        else:
            entity_list.append(entity)
            return entity_list

    def remove_special_characters(self, text):
        return text.replace("_", "").replace("(", "").replace(")", "").replace("-", "")

    #Name,First_Name,Middle_Name,Last_Name
    def create_entity_spans(self, df,entity_list, first_column):
        '''Create entity spans for training/test datasets'''
        df[first_column]=df[first_column].apply(lambda x: self.massage_data(x))
        tag_list = []
        for tag in entity_list:
            tag_name = self.remove_special_characters(tag) + 'Tag'
            tag_list.append(tag_name)
            label = tag.upper()
            df[tag_name]=df.apply(lambda row:self.get_entity_span(entity=row[first_column],entity_component=row[tag],label=label),axis=1)

        df['EmptySpan']=df.apply(lambda x: [], axis=1)
     
        for i in tag_list:
            df['EntitySpans']=df.apply(lambda row: self.extend_list(row['EmptySpan'],row[i]),axis=1)
            df['EntitySpans']=df[['EntitySpans',first_column]].apply(lambda x: (x[1], x[0]),axis=1)

        return df['EntitySpans']

    #https://spacy.io/usage/training#training-data
    def get_doc_bin(self, training_data,nlp):
        '''Create DocBin object for building training/test corpus'''
        # the DocBin will store the example documents
        db = DocBin()
        for text, annotations in training_data:
            doc = nlp(text) #Construct a Doc object
            ents = []
            for start, end, label in annotations:
                span = doc.char_span(start, end, label=label)
                ents.append(span)
            if(None in ents):
                print('None Type detected in:')
                print(text)
                print('with annotations')
                print(annotations)  
                print('creates entitites:')
                print(ents)
                continue
            doc.ents = ents
            db.add(doc)
        return db

    def generate_entity_list (self, dataframe_columns):
        entity_list = []
        for i in range(0, len(dataframe_columns)):
            if (i == 0):
                continue
            entity_list.append(dataframe_columns[i])
        return entity_list


    def generate_doc_bins (self, input_path, output_path):
        #Load blank English model. This is needed for initializing a Document object for our training/test set.
        nlp = spacy.blank("en")

        ###### Training dataset prep ###########
        # Read the training dataset into pandas
        df_train=pd.read_csv(filepath_or_buffer=input_path,sep=",",dtype=str)
        
        # Get entity tag list
        entity_list = self.generate_entity_list(df_train.columns)

        # Get first column name
        first_column = df_train.columns[0]

        # Get entity spans
        df_entity_spans= self.create_entity_spans(df_train.astype(str),entity_list, first_column)
        training_data= df_entity_spans.values.tolist()

        # Get & Persist DocBin to disk./corpus/spacy-docbins
        doc_bin_train= self.get_doc_bin(training_data,nlp)
        doc_bin_train.to_disk(output_path)
        ######################################