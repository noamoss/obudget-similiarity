from settings import EXPECTED_RESULTS_NUM

def caluclate_similarities(tfidf_matrix,corpus,num_features):
    """
    returns a Similiarity class to calculate similarities between the docs in the corpusself.
    This class operates in fixed memory, by splitting the index across multiple files on disk, called shards. See https://radimrehurek.com/gensim/similarities/docsim.html
    The outcome is a Cosine Similarity, see https://en.wikipedia.org/wiki/Cosine_similarity for details,
    """
    import gensim.similarities
    return gensim.similarities.Similarity('',
                                      tfidf_matrix[corpus],
                                      num_features=num_features)

def entity_id_to_df_index(df,column_name, id):
    """
    catch the index number of the desired record by a chosen column (probably 'id')
    """
    return df.index[df[column_name] == id][0]

def index_to_entity_id(df,column_name, row_index):
    """
    catch the entity id (by a chosen column) of a row index
    """
    return df.iloc[row_index][column_name]

def add_id_to_result(df,column_name,result):
    """
    add entity id to a tuple (row index, rank) result --> (row index, id, rank)
    """
    to_list = list(result)
    to_list.insert(1, index_to_entity_id(df,column_name,result[0]))
    return tuple(to_list)

def find_similiars(column_name,id,df,dictionary,tfidf,sims):
    """
    choose a Dataframe row index to query, by entity id
    """
    query_index = entity_id_to_df_index(df,column_name,id)         # transform entity id to DataFrame row index
    print("query_index:", query_index)
    query_doc = df.iloc[query_index]['tokenized'].split(", ")                 # get the queires doc tokenized version
    # print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)               # get the bag of words version of the queried document
    # print(query_doc_bow)
    query_doc_tf_idf = tfidf[query_doc_bow]                    # now put the queried document's bag of words in the general tfidf context
    # print(query_doc_tf_idf)
    results = sims[query_doc_tf_idf]                            # get the similarity ranks from the general similarity matrix
    results = sorted(enumerate(results), key=lambda item: -item[1])[0:EXPECTED_RESULTS_NUM] # sort by relevancy
    results = [add_id_to_result(df,column_name,result) for result in results if result[1] > 0]  # add the result entity id + filter out results with 0 correlation
    print(len(results)," results:\n" )
    
    return results
