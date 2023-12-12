from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
import os
import chromadb

from DocumentLoader import DocumentLoader
from DocumentSpliter import DocumentSpliter

from chromadb import Documents, EmbeddingFunction, Embeddings

class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        # embed the documents somehow
        embeddings = HuggingFaceBgeEmbeddings(
				model_name=self.model_name, model_kwargs=self.model_kwargs, encode_kwargs=self.encode_kwargs
		)
        return embeddings

class VectorDB:
	model_name = "BAAI/bge-small-zh"
	model_kwargs = {"device": "cuda"}
	encode_kwargs = {"normalize_embeddings": True}

	def __init__(self, db_path, embeddings=None, documents=None):
		if embeddings is None:
			embeddings = HuggingFaceBgeEmbeddings(
				model_name=self.model_name, model_kwargs=self.model_kwargs, encode_kwargs=self.encode_kwargs
			)
		self.embeddings = embeddings
		user_name = db_path.split("/")[-1]
		self.chroma_client = chromadb.PersistentClient(db_path)
		self.db_path = db_path
		self.db = Chroma(client=self.chroma_client, collection_name=user_name, embedding_function = self.embeddings)
		self.collection = self.chroma_client.get_collection(user_name)
		
		if documents is not None:
			self.add(documents)
	
	def add(self, documents):
		ids=[str(hash(doc.page_content)) for doc in documents]
		metadatas = [doc.metadata for doc in documents]
		documents = [doc.page_content for doc in documents]
		self.collection.add(ids=ids, documents=documents, metadatas=metadatas)
		
	def query(self, query):
		matched_documents = self.collection.query(query_texts=query)
		return matched_documents
	

db = VectorDB("./db/admin")
document_loader = DocumentLoader()
document_spliter = DocumentSpliter()
db.add(document_spliter.split_document(document_loader.load_directory("admin")))
        
print(db.query("hello world!"))