from langchain.text_splitter import RecursiveCharacterTextSplitter
from app import app

class DocumentSpliter:
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    def __init__(self):
        pass

    def split_document(self, documents):
        texts = self.text_splitter.split_documents(documents)
        app.logger.info("len texts: " + str(len(texts)))
        return texts
