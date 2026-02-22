# chunking.py - Handles document splitting/chunking operations

from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

def split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into chunks"""
    text_splitter = CharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=150
    )
    return text_splitter.split_documents(documents)