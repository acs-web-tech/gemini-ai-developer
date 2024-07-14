import google.ai.generativelanguage as glm
from main import retriever_service_client
def queryCorpus(corpus_resource_name,user_query):
     results_count = 5
     request = glm.QueryCorpusRequest(name=corpus_resource_name,
                                 query=user_query,
                                 results_count=results_count)
     query_corpus_response = retriever_service_client.query_corpus(request)
     return query_corpus_response