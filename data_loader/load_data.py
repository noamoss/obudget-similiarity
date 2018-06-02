import datapackage, json
import pandas as pd
from settings import SOURCES_FILE, ENTITY_TO_EXPLORE

def load_datapackage(entity=ENTITY_TO_EXPLORE):
    """
    data_loader.load_datapackage(source_file_path, entity)
    Loads a json file from the source_file_path, and parse the relevant path for the entityself into a returned dataframe of raw_data
    source_file json file should include entity as key, and a datapackage_path as a key in a sub-dictionary
    """
    get_data_settings()
    datapacakge_path = data_settings[entity]["datapackage_path"]
    package=datapackage.Package(datapacakge_path)
    response = package.resources[0]
    iterator = response.iter(keyed=True)

    df=pd.DataFrame()

    items = []
    counter = 0
    for row in iterator:
        for column_name in list(row.keys()):
            if column_name not in df.columns:
                df.insert(column=column_name,loc=len(df.columns),value=None)
        items.append(row)
        counter+=1
        if counter % 10000 == 0:
            print("downloaded: ",counter," items")
    print("downloaded: ",counter," items")

    df = pd.DataFrame(items)
    # add a row index to df
    df['doc_index'] = df.index

    return df


def get_data_settings():
    """
    load the customized data source settings
    """
    global data_settings
    with open(SOURCES_FILE) as f:
        data_settings = json.loads(f.read())
    return data_settings
