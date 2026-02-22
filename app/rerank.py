import requests
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

def rerank_documents(query: str, docs: List, top_k: int = 4) -> List:
    """
    调用 SiliconFlow 的 rerank API 对文档重排序
    返回排序后的前 top_k 个 Document
    """
    if not docs:
        return []

    # 准备 payload 中的 documents（取 page_content）
    documents = [doc.page_content for doc in docs]

    payload = {
        "model": "BAAI/bge-reranker-v2-m3",
        "query": query,
        "documents": documents
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('ARK_API_KEY')}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            os.getenv("ARK_BASE_URL") + "/rerank",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        result = response.json()

        # SiliconFlow rerank 返回的 results 是按分数降序排列的列表
        # 每个元素有 index（原始顺序）和 relevance_score
        ranked_results = result.get("results", [])

        # 根据 index 重新排序原始 docs
        sorted_docs = []
        seen_indices = set()
        for item in ranked_results:
            idx = item["index"]
            if idx < len(docs) and idx not in seen_indices:
                sorted_docs.append(docs[idx])
                seen_indices.add(idx)

        # 如果结果不够 top_k，补上剩下的（理论上不会）
        if len(sorted_docs) < top_k:
            for i, doc in enumerate(docs):
                if i not in seen_indices:
                    sorted_docs.append(doc)
                    if len(sorted_docs) >= top_k:
                        break

        return sorted_docs[:top_k]

    except Exception as e:
        print(f"Rerank 失败: {e}")
        # 失败时返回原始顺序（降级策略）
        return docs[:top_k]