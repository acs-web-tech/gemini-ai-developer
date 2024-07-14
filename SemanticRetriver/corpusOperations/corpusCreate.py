import google.ai.generativelanguage as glm
def create_corpus(display_name,retriever_service_client,project_name):
    corpus_details = glm.Corpus(display_name=display_name)
    create_corpus_request = glm.CreateCorpusRequest(corpus=corpus_details)
    create_corpus_response = retriever_service_client.create_corpus(create_corpus_request)
    return  create_corpus_response.name
    