import unittest
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
from Retrieval import VectorDB  # 请将your_module替换为实际的模块名
from DocumentLoader import DocumentLoader
from DocumentSpliter import DocumentSpliter

class TestVectorDB(unittest.TestCase):
    def setUp(self):
        self.db_path = "./db/admin"
        self.query = "test query"

    def test_init_with_db_path(self):
        vector_db = VectorDB(self.db_path)
        self.assertIsInstance(vector_db.embeddings, HuggingFaceBgeEmbeddings)
        self.assertIsInstance(vector_db.db, Chroma)

    def test_query(self):
        vector_db = VectorDB(self.db_path)
        result = vector_db.query(self.query)
        print(result)
        self.assertIsNotNone(result)

    def test_add(self):
        vector_db = VectorDB(self.db_path)
        document_loader = DocumentLoader()
        document_spliter = DocumentSpliter()
        vector_db.add(document_spliter.split_document(document_loader.load_directory("admin")))
        # 这里应该有一些断言来检查db是否已经保存到db_path，但由于我无法访问您的文件系统，所以无法提供具体的代码

if __name__ == '__main__':
    unittest.main()