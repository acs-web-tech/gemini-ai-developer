import json
from langchain_community.document_loaders import PyPDFLoader
from utils.iterator import document_iterator
def readPdf(path):
   loader = PyPDFLoader(path)
   pages = loader.load_and_split()
   doc_json = document_iterator(pages)
   return doc_json