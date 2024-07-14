import google.ai.generativelanguage as glm
def create_document(display_name,retriever_service_client,corpus_resource_name):
   document = glm.Document(display_name=display_name)
   create_document_request = glm.CreateDocumentRequest(parent=corpus_resource_name, document=document)
   create_document_response = retriever_service_client.create_document(create_document_request)
   return create_document_response.name
