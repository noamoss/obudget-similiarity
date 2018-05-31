
"""
Methods to tokenie a given Dataframeself.
Usage example: df['tokenized'] = df.apply(tokenize,axis=1)
"""


from settings import ENTITY_TO_EXPLORE
from data_loader import get_data_settings


def tokenize_row(df_row):
    """
    tokenize verbal columns, add meta data columns
    """

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
t
