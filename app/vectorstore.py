
# import os
# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
# from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
#
# from chunking import split_documents  # Import splitter from chunking module
#
# load_dotenv()
#
# DB_PATH = "./chroma_db"
# DOCS_PATH = "./docs"
#
# def get_vectorstore():
#     """初始化或加载向量库"""
#     embeddings = OpenAIEmbeddings(
#         model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
#         api_key=os.getenv("ARK_API_KEY"),
#         base_url=os.getenv("ARK_BASE_URL")
#     )
#
#     if os.path.exists(DB_PATH):
#         print("加载现有向量库...")
#         return Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
#     else:
#         print("构建新向量库...")
#         loader = DirectoryLoader(
#             DOCS_PATH,
#             glob="**/*.md",
#             loader_cls=UnstructuredMarkdownLoader
#         )
#         documents = loader.load()
#         texts = split_documents(documents)  # Use modular splitting
#         vectorstore = Chroma.from_documents(
#             texts, embeddings, persist_directory=DB_PATH
#         )
#         print(f"已索引 {len(texts)} 个文档块")
#         return vectorstore
#
# def reload_vectorstore():
#     """删除并重新构建向量库"""
#     embeddings = OpenAIEmbeddings(
#         model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
#         api_key=os.getenv("ARK_API_KEY"),
#         base_url=os.getenv("ARK_BASE_URL")
#     )
#     if os.path.exists(DB_PATH):
#         vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
#         vectorstore.delete_collection()
#
#     loader = DirectoryLoader(
#         DOCS_PATH,
#         glob="**/*.md",
#         loader_cls=UnstructuredMarkdownLoader
#     )
#     documents = loader.load()
#     texts = split_documents(documents)
#     Chroma.from_documents(texts, embeddings, persist_directory=DB_PATH)
#     print("向量库已重新构建")


# vectorstore.py
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from chunking import split_documents

load_dotenv()

DB_PATH = "./chroma_db"
DOCS_PATH = "./docs"

# 定义全局私有变量缓存实例
_vectorstore_instance = None


def get_vectorstore():
    """获取向量库单例"""
    global _vectorstore_instance

    # 如果已存在实例，直接返回
    if _vectorstore_instance is not None:
        return _vectorstore_instance

    # 否则初始化
    embeddings = OpenAIEmbeddings(
        model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        api_key=os.getenv("ARK_API_KEY"),
        base_url=os.getenv("ARK_BASE_URL")
    )

    # Chroma 会自动处理目录不存在的情况
    _vectorstore_instance = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    # 如果库里没数据，尝试从 docs 目录加载一次（初始化）
    if _vectorstore_instance._collection.count() == 0 and os.path.exists(DOCS_PATH):
        loader = DirectoryLoader(DOCS_PATH, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
        documents = loader.load()
        if documents:
            texts = split_documents(documents)
            _vectorstore_instance.add_documents(texts)

    return _vectorstore_instance


def reload_vectorstore():
    """彻底重置向量库并重置单例缓存"""
    global _vectorstore_instance
    vs = get_vectorstore()
    vs.delete_collection()  # 清空数据
    _vectorstore_instance = None  # 销毁缓存，下次调用 get_vectorstore 时会重连
    return get_vectorstore()

if __name__ == "__main__":
    # 测试向量库功能
    reload_vectorstore()