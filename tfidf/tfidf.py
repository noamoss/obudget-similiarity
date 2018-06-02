def corpus_to_tfidf(corpus):
    """
    Transform a corpus (bag of words) into a tfidf model
    """
    import gensim
    tfidf_matrix = gensim.models.TfidfModel(corpus)                                                             # transform into tfidf (see https://radimrehurek.com/gensim/models/tfidfmodel.html for details)
    print(tfidf_matrix)
    return tfidf_matrix
