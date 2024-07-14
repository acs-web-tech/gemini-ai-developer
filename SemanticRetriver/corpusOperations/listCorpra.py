import google.ai.generativelanguage as glm
def list_corpora(retriever_service_client):
    corpora_list_request = glm.ListCorporaRequest()
    corpora_list_response = retriever_service_client.list_corpora(corpora_list_request)
    return corpora_list_response.corpora