def create_corpus(df):
    """
    Create a corpus out of the 'tokenized' column in the given dataframe
    """
    import gensim
    import numpy
    gen_docs = [[ word for word in doc.split(", ") if (word!= "" and word!='None')] for doc in df['tokenized']] # split tokenized words list in all dataframe's rows
    dictionary = gensim.corpora.Dictionary(gen_docs)                                                            # turn words list into a a Disctionary class

    print("Number of words in dictionary:",len(dictionary))

    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]                                             # Convert document into the bag-of-words (BoW) format = list of (token_id, token_count).

    return corpus


def corpus_to_tfidf(corpus):
    """
    Transform a corpus (bag of words) into a tfidf model
    """
    import gensim
    return gensim.models.TfidfModel(corpus)                                                                  # transform into tfidf (see https://radimrehurek.com/gensim/models/tfidfmodel.html for details)
