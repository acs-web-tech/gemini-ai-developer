import sys
sys.path.insert(0,r"C:\Users\ganes\OneDrive\Documents\eng services llm\gemini-ai-developer\loaders")
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"\assests\elecdesignbasis.pdf")
pages = loader.load_and_split()
print(pages)