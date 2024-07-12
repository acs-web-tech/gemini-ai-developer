import google.ai.generativelanguage as glm
from main import retriever_service_client
def create_corpus(display_name,project_name=None):
    corpus_details = glm.Corpus(display_name=display_name)
    create_corpus_response = retriever_service_client.create_corpus(corpus_details)
    return  create_corpus_response.name
    