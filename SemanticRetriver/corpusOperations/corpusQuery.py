import google.ai.generativelanguage as glm
def queryCorpus(resource_name,query,generative_service_client):
    answer_style = "ABSTRACTIVE" # Or VERBOSE, EXTRACTIVE
    MODEL_NAME = "models/aqa"
    content = glm.Content(parts=[glm.Part(text=query)])
    retriever_config = glm.SemanticRetrieverConfig(source=resource_name, query=content)
    req = glm.GenerateAnswerRequest(model=MODEL_NAME,
                                contents=[content],
                                semantic_retriever=retriever_config,
                                answer_style=answer_style)
    aqa_response = generative_service_client.generate_answer(req)
    print(aqa_response)