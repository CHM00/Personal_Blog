
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
from rank_bm25 import BM25Okapi
import jieba

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


def hybrid_retrieval(query: str, k: int = 10):
    """
    实现混合检索：向量检索 + BM25 关键词检索
    """
    vs = get_vectorstore()

    # 1. 语义检索 (Vector Search)
    vector_docs = vs.similarity_search(query, k=k)

    # 2. 关键词检索 (BM25)
    # 获取库中所有文档作为语料库
    all_content = vs._collection.get()
    documents_content = all_content['documents']
    metadatas = all_content['metadatas']

    if not documents_content:
        return vector_docs

    # 对语料和查询进行分词
    tokenized_corpus = [list(jieba.cut(doc)) for doc in documents_content]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = list(jieba.cut(query))

    # 获取 BM25 评分前 k 的文档索引
    bm25_scores = bm25.get_scores(tokenized_query)
    top_n_indices = sorted(range(len(bm25_scores)), key=lambda i: bm25_scores[i], reverse=True)[:k]

    # 构建 BM25 结果 Document 对象
    from langchain_core.documents import Document
    bm25_docs = [
        Document(page_content=documents_content[i], metadata=metadatas[i])
        for i in top_n_indices if bm25_scores[i] > 0
    ]

    # 3. 合并去重
    combined_dict = {doc.page_content: doc for doc in (vector_docs + bm25_docs)}
    return list(combined_dict.values())

if __name__ == "__main__":
    # 测试向量库功能
    reload_vectorstore()