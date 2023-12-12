from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings

from DocumentLoader import DocumentLoader

from DocumentSpliter import DocumentSpliter


class VectorDB:
    model_name = "BAAI/bge-small-zh"
    model_kwargs = {"device": "cuda"}
    encode_kwargs = {"normalize_embeddings": True}

    def __init__(self, documents):
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name=self.model_name, model_kwargs=self.model_kwargs, encode_kwargs=self.encode_kwargs
        )
        self.db = Chroma.from_documents(documents, self.embeddings)

    def query(self, documents, query):
        doc_result = self.embeddings.embed_documents(documents)
        query_result = self.embeddings.embed_query(query)
        print(doc_result)
        return query_result
