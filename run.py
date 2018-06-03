## i.e. python run.py "1000621790"


from settings import *
from data_loader.load_data import load_datapackage, get_data_settings
from tokenization.tokenize_df import tokenize_row
from tokenization.tokenize_string import tokenize_text
from tfidf.corpus import create_corpus
from tfidf.tfidf import corpus_to_tfidf
from tfidf.similarities import caluclate_similarities, entity_id_to_df_index, index_to_entity_id, add_id_to_result, find_similiars
import sys


if len(sys.argv) < 2:
    sys.exit('Need an entity id to explore')
else:
    data_settings = get_data_settings()
    ID_FIELD = data_settings[ENTITY_TO_EXPLORE]["entity_id_fieldname"]  # get the entity id field 
    print("Starting to load data, enetity to explore: {} Based on sources file named {}".format(ENTITY_TO_EXPLORE, SOURCES_FILE))
    df = load_datapackage(ENTITY_TO_EXPLORE)
    print("Starting to tokenize dataframe's items (rows)")
    df["tokenized"] = df.apply(tokenize_row, axis=1)
    print("building a corpus")
    corpus, dictionary, num_features = create_corpus(df)
    print("transforming corpus into a tfidf matrix")
    tfidf_matrix = corpus_to_tfidf(corpus)
    print("calculating cosine similarities between the documents based on the given corpus")
    sims = caluclate_similarities(tfidf_matrix=tfidf_matrix, corpus=corpus, num_features=num_features)

    results = find_similiars(ID_FIELD,id=sys.argv[1],df=df,dictionary=dictionary,tfidf=tfidf_matrix,sims=sims)
    print("queried item: \n ----------")
    print(df.iloc[results[0][0]])
    print(" \n ---- similars: ---- \n ")
    for i in range(1, EXPECTED_RESULTS_NUM):
        print(i,":\n")
        print(df.iloc[results[i][0]])
        print("\n")
