def tokenize_text(text):
    """
    tokenize textual string and get rid of non alpha numberics, split to words in selected columns
    """
    import re
    
    regxlst = [re.compile(x) for x in [r'\d+',]]    # regular expressions list for clean ups:
                                                             # 1. only digits
    stringed_text = str(text)
    ignore_signs = ["\,","\:","\;","\.","\&","\$","\-","\=","\(","\)","\d+","\\n"]
    cleaned_1 = re.sub("|".join(ignore_signs),"",stringed_text) # remove non-alphanumberic characters
    cleaned_2 = re.sub("  "," ",cleaned_1)                # no more double spaces
    cleaned_3 = cleaned_2.split()                       # split into separate words list
    cleaned_4 =  [word for regex in regxlst for word in cleaned_3 if not(regex.match(word))] # filter by regular expressions
    cleaned_5 = [word for word in cleaned_4 if word is not None]
    return cleaned_5



def tokenize_row(df_row):
    """
    tokenize verbal columns, add meta data columns
    Methods to tokenize a given Dataframe self.
    Usage example: df['tokenized'] = df.apply(tokenize,axis=1)
    """
    from settings import ENTITY_TO_EXPLORE
    from data_loader import get_data_settings

    data_settings = get_data_settings()
    columns_list = data_settings[ENTITY_TO_EXPLORE]['columns_to_index']
    meta_columns_list = data_settings[ENTITY_TO_EXPLORE]['meta_columns_list']

    # add here the columns you would like to index

    tokenized = []
    for column_name in columns_list:
        tokenized+=tokenize_text(df_row[column_name])
    for meta_column in meta_columns_list:
        tokenized+=[meta_column+": "+str(df_row[meta_column])]
    return ", ".join(tokenized)
