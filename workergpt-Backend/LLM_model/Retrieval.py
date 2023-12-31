from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
import os
import chromadb

from . import DocumentLoader
from . import DocumentSpliter

from chromadb import Documents, EmbeddingFunction, Embeddings
import hashlib

class MyEmbeddingFunction(EmbeddingFunction):
	def __call__(self, texts: Documents) -> Embeddings:
		# embed the documents somehow
		embeddings = HuggingFaceBgeEmbeddings(
				model_name=self.model_name, model_kwargs=self.model_kwargs, encode_kwargs=self.encode_kwargs
		)
		return embeddings

def generate_hash(content: str):
		hash_object = hashlib.md5(content.encode())  # 使用MD5哈希算法
		return hash_object.hexdigest()

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
		print(documents)
		ids = [generate_hash(doc.page_content) for doc in documents]

		contents = [doc.page_content for doc in documents]
		metadatas = [doc.metadata for doc in documents]

		# Create a new map using ids as the key and combine documents and metadatas
		new_map = {id: (doc, meta) for id, doc, meta in zip(ids, contents, metadatas)}
		ids = list(new_map.keys())
		values = list(new_map.values())
		contents = [value[0] for value in values]
		metadatas = [value[1] for value in values]

		self.collection.update(ids=ids, documents=contents, metadatas=metadatas)
		
	def query(self, query, top_k=10):
		matched_documents = self.collection.query(query_texts=query, n_results=top_k)
		return matched_documents
	
	def delete(self, username: str, file_name: str):
		file_path = './' + username + '/' + file_name.split(".")[-1] + '/' + file_name
		print(file_path)
		self.collection.delete(where={"source": file_path})