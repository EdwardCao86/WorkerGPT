import logging
import os

from app import app
from langchain.document_loaders import TextLoader, CSVLoader, PyPDFLoader, \
    DirectoryLoader, JSONLoader, BSHTMLLoader, UnstructuredMarkdownLoader


def get_fileloader(filetype: str):
    if filetype == 'txt':
        return TextLoader
    elif filetype == 'csv':
        return CSVLoader
    elif filetype == 'json':
        return JSONLoader
    elif filetype == 'html':
        return BSHTMLLoader
    elif filetype == 'md':
        return UnstructuredMarkdownLoader
    elif filetype == 'pdf':
        return PyPDFLoader
    else:
        return None


class DocumentLoader:
    username = None

    def __init__(self):
        pass

    def load_directory(self, username: str):
        self.username = username
        documents = list()
        for item in os.listdir('../' + username):
            item_path = os.path.join('../' + username, item)
            if os.path.isdir(item_path):
                documents.extend(self._load_directory(item))
        return documents

    def _load_directory(self, filetype: str):
        glob_path = '../' + self.username + '/' + filetype + '/'
        app.logger.info('glob_path: ' + glob_path)
        text_loader_kwargs = {'autodetect_encoding': True}
        directory_loader = DirectoryLoader(glob_path, use_multithreading=True, loader_cls=get_fileloader(filetype),
                                           silent_errors=True, loader_kwargs=text_loader_kwargs)
        return directory_loader.load()
