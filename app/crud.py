# crud.py - Handles CRUD operations for documents
# Includes adding, deleting, updating documents and counting files.

import os

DOCS_PATH = "./docs"

# 示例文件创建（如果目录为空时初始化）
def initialize_sample_if_empty():
    if len(os.listdir(DOCS_PATH)) == 0:
        sample_content = """
# 面试心得

## TCP 三次握手
TCP三次握手的核心是确保双方收发能力正常：
1. SYN：客户端发送 SYN 包，等待服务器确认
2. SYN+ACK：服务器回复 SYN+ACK，确认收到客户端请求
3. ACK：客户端回复 ACK，确认收到服务器响应

三次握手确保了双向通信可靠，避免了半连接问题。

## 数据库索引
B+树索引适合范围查询，叶子节点存储数据。
哈希索引适合等值查询，不支持范围。

## 系统设计要点
高可用：负载均衡 + 数据库主从复制
高性能：缓存 Redis + CDN
## 更多内容...
"""
        add_document("interview_notes.md", sample_content)

def add_document(filename: str, content: str):
    """添加新文档"""
    filepath = os.path.join(DOCS_PATH, filename)
    if os.path.exists(filepath):
        raise ValueError(f"文档 {filename} 已存在")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"添加文档: {filename}")

def delete_document(filename: str):
    """删除文档"""
    filepath = os.path.join(DOCS_PATH, filename)
    if not os.path.exists(filepath):
        raise ValueError(f"文档 {filename} 不存在")
    os.remove(filepath)
    print(f"删除文档: {filename}")

def update_document(filename: str, content: str):
    """更新文档"""
    filepath = os.path.join(DOCS_PATH, filename)
    if not os.path.exists(filepath):
        raise ValueError(f"文档 {filename} 不存在")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"更新文档: {filename}")

def get_document_count(path: str = DOCS_PATH) -> int:
    """获取文档数量"""
    return len([f for f in os.listdir(path) if f.endswith('.md')])

# 初始化示例（如果需要，在 app.py 中调用）
initialize_sample_if_empty()