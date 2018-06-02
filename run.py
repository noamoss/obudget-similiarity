from settings import *
from data_loader.load_data import load_datapackage
from data_loader.get_settings import get_data_settings
from tokenization.tokenize_df import tokenize_row
from tokenization.tokenize_string import tokenize_text
from tfidf.corpus import create_corpus
from tfidf.tfidf import corpus_to_tfidf

print("Starting to load data, enetity to explore: {} Based on sources file named {}".format(ENTITY_TO_EXPLORE, SOURCES_FILE))
df = load_datapackage(ENTITY_TO_EXPLORE)
print("Starting to tokenize to tokenize dataframe's items (rows)")
df["tokenized"] = df.apply(tokenize_row, axis=1)
print("building a corpus")
corpus = create_corpus(df)
print("transforming corpus into a tfidf matrix")
tfidf_matrix = corpus_to_tfidf(corpus)
