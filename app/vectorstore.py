# vectorstore.py - Handles Chroma vectorstore initialization and reloading

import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader

from chunking import split_documents  # Import splitter from chunking module

load_dotenv()

DB_PATH = "./chroma_db"
DOCS_PATH = "./docs"

def get_vectorstore():
    """初始化或加载向量库"""
    embeddings = OpenAIEmbeddings(
        model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        api_key=os.getenv("ARK_API_KEY"),
        base_url=os.getenv("ARK_BASE_URL")
    )

    if os.path.exists(DB_PATH):
        print("加载现有向量库...")
        return Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    else:
        print("构建新向量库...")
        loader = DirectoryLoader(
            DOCS_PATH,
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader
        )
        documents = loader.load()
        texts = split_documents(documents)  # Use modular splitting
        vectorstore = Chroma.from_documents(
            texts, embeddings, persist_directory=DB_PATH
        )
        print(f"已索引 {len(texts)} 个文档块")
        return vectorstore

def reload_vectorstore():
    """删除并重新构建向量库"""
    embeddings = OpenAIEmbeddings(
        model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        api_key=os.getenv("ARK_API_KEY"),
        base_url=os.getenv("ARK_BASE_URL")
    )
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    vectorstore.delete_collection()
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader
    )
    documents = loader.load()
    texts = split_documents(documents)
    Chroma.from_documents(texts, embeddings, persist_directory=DB_PATH)
    print("向量库已重新构建")