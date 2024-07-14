import google.ai.generativelanguage as glm
def deleteCorpra(display_name,retriever_service_client,corpus_resource_name=""):
    req = glm.DeleteCorpusRequest(name=corpus_resource_name,force=True)
    delete_corpus_response = retriever_service_client.delete_corpus(req)
    print("Successfully deleted corpus: " )