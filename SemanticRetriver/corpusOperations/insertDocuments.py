import google.ai.generativelanguage as glm
def insertDocuments(retriever_service_client,document_resource_name,chunks):
    create_chunk_requests = []
    data = []
    for chunk in chunks:
         create_chunk_requests.append(glm.CreateChunkRequest(parent=document_resource_name, chunk=glm.Chunk(data={"string_value":chunk["data"]})))
    request = glm.BatchCreateChunksRequest(parent=document_resource_name, requests=create_chunk_requests)
    response = retriever_service_client.batch_create_chunks(request)
    return response
