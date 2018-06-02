import json
from settings import SOURCES_FILE

def get_data_settings():
    """
    load the customized data source settings
    """
    global data_settings
    with open(SOURCES_FILE) as f:
        data_settings = json.loads(f.read())
    return data_settings
