from settings import *
from data_loader import load_datapackage
from tokenize_df import tokenize_row


print("Starting to load data, enetity to explore: {} Based on sources file named {}".format(ENTITY_TO_EXPLORE, SOURCES_FILE))
df = load_datapackage(ENTITY_TO_EXPLORE)
print("Starting to tokenize to tokenize dataframe's items")
df["tokenized"] = df.apply(tokenize_row, axis=1)
