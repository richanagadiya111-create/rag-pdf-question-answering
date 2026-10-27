# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import CharacterTextSplitter


# data=PyPDFLoader("docloaders/python_rag_practice.pdf")

# docs=data.load()

# text_splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=0)
# chunks = text_splitter.split_documents(docs)

# print(len(chunks))


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data=PyPDFLoader("oop.pdf")
docs=data.load()

splitter=TokenTextSplitter(chunk_size=100,chunk_overlap=1)
chunk=splitter.split_documents(docs)
print(len(chunk))


