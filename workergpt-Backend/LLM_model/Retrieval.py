from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings

from chromadb import Documents, EmbeddingFunction, Embeddings, PersistentClient
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
		self.chroma_client = PersistentClient(db_path)
		self.db_path = db_path
		self.db = Chroma(client=self.chroma_client, collection_name=user_name, embedding_function = self.embeddings)
		self.collection = self.chroma_client.get_collection(user_name)
		
		if documents is not None:
			self.add(documents)
	
	def add(self, documents):
		print(documents)
		ids = []
		contents = []
		metadatas = []

		for doc in documents:
			doc_id = generate_hash(doc.page_content)
			if doc_id not in ids:
				ids.append(doc_id)
				contents.append(doc.page_content)
				metadatas.append(doc.metadata)

		self.collection.add(ids=ids, documents=contents, metadatas=metadatas)

		return self.collection.count()
		
	def query(self, query, top_k=10):
		matched_documents = self.collection.query(query_texts=query, n_results=top_k)
		return matched_documents
	
	def delete(self, username: str, file_name: str):
		file_path = './' + username + '/' + file_name.split(".")[-1] + '/' + file_name
		print(file_path)
		self.collection.delete(where={"source": file_path})
		return self.collection.count()

	def count(self):
		return self.collection.count()