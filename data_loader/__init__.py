def load_datapackage(source_file_path, entity):
    """
    data_loader.load_datapackage(source_file_path, entity)
    Loads a json file from the source_file_path, and parse the relevant path for the entityself into a returned dataframe of raw_data
    source_file json file should include entity as key, and a datapackage_path as a key in a sub-dictionary
    """

    import datapackage, json
    import pandas as pd

    with open(source_file_path) as f:
        settings_data = json.loads(f.read())
        datapacakge_path = settings_data[entity]["datapackage_path"]

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
