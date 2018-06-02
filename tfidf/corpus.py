import gensim
import numpy

def create_corpus(df):
    """
    Create a corpus out of the 'tokenized' column in the given dataframe, reutrn the (corpus, num_features)
    """
    gen_docs = [[ word for word in doc.split(", ") if (word!= "" and word!='None')] for doc in df['tokenized']] # split tokenized words list in all dataframe's rows
    dictionary = gensim.corpora.Dictionary(gen_docs)                                                            # turn words list into a a Disctionary class
    num_features = len(dictionary)
    print("Number of words in dictionary:",num_features)

    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]                                             # Convert document into the bag-of-words (BoW) format = list of (token_id, token_count).
    result = (corpus, dictionary, num_features)
    return result
