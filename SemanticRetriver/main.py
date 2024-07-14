from oAuth import init_Oauth
from corpusOperations.corpusCreate import create_corpus
from corpusOperations.corpusCreateDocument import create_document
from corpusOperations.deleteCorpra import deleteCorpra
from corpusOperations.listCorpra import list_corpora
from corpusOperations.insertDocuments import insertDocuments
from corpusOperations.corpusQuery import queryCorpus
from loaders.pdf_2_json import readPdf
from scopes import CORPRA_NAME,CORPUS_DEFAULT_NAME
generative_service_client,retriever_service_client,_= init_Oauth()
# create_corpus("gemini",retriever_service_client,CORPUS_DEFAULT_NAME)
# doc = create_document("gem doc",retriever_service_client,CORPRA_NAME)
# print(doc)
# json = readPdf("SemanticRetriver/loaders/assests/elecdesignbasis.pdf")
# print(json)
# response = insertDocuments(retriever_service_client,doc,json)
# print(response)
queryCorpus(CORPRA_NAME,"havells india",generative_service_client)
# deleteCorpra("gemini",retriever_service_client,"gemini")
#print(list_corpora(retriever_service_client))
