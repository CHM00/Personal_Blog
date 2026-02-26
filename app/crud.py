import os
from langchain_core.documents import Document
from vectorstore import get_vectorstore
from chunking import split_documents

DOCS_PATH = "./docs"


def add_document(filename: str, content: str):
    """添加新文档并同步到向量库"""
    filepath = os.path.join(DOCS_PATH, filename)
    if os.path.exists(filepath):
        raise ValueError(f"文档 {filename} 已存在")

    # 写入文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    # 同步到向量库
    vectorstore = get_vectorstore()
    # 创建一个 LangChain 文档对象
    new_doc = Document(page_content=content, metadata={"source": filename})
    # 使用你刚才优化的 Markdown 标题切分逻辑
    chunks = split_documents([new_doc])
    # 将切分后的块添加到 Chroma
    vectorstore.add_documents(chunks)

    print(f"文档 {filename} 已成功添加到磁盘和向量库 (共 {len(chunks)} 个块)")


def delete_document(filename: str):
    """删除文档并从向量库中移除"""
    filepath = os.path.join(DOCS_PATH, filename)
    if os.path.exists(filepath):
        os.remove(filepath)

    # 从 Chroma 中删除 (根据 metadata 中的 source 过滤)
    vectorstore = get_vectorstore()
    vectorstore.delete(where={"source": filename})
    print(f"文档 {filename} 已从磁盘和向量库中删除")


def update_document(filename: str, content: str):
    """更新文档：先删后加"""
    # Chroma 的更新通常建议先根据 source 删除旧块，再添加新块
    try:
        delete_document(filename)
    except:
        pass
    add_document(filename, content)

def get_document_count(path: str = DOCS_PATH) -> int:
    """获取文档数量"""
    return len([f for f in os.listdir(path) if f.endswith('.md')])