import os
from typing import Dict
from fastapi import FastAPI, Body
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Import modular components
from vectorstore import get_vectorstore, reload_vectorstore, hybrid_retrieval
from crud import add_document, delete_document, update_document, get_document_count
from chunking import split_documents
from fastapi.middleware.cors import CORSMiddleware
from rerank import rerank_documents

import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from typing import List

import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# 配置 JWT 密钥和管理员账号
SECRET_KEY = os.getenv("SECRET_KEY", "chm_super_secret_key_2026")
ALGORITHM = "HS256"
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "123456")  # 你可以自己改成复杂的密码

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


# SQLite 数据库配置
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

load_dotenv()

app = FastAPI(title="面试心得 RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://150.158.123.242", "http://localhost:8080", "*"],  # 允许的前端来源，* 为允许所有（开发用）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 配置路径
DB_PATH = "./chroma_db"
DOCS_PATH = "./docs"

# 创建 docs 目录（示例文件移到 crud.py 中的初始化逻辑，如果需要）
if not os.path.exists(DOCS_PATH):
    os.makedirs(DOCS_PATH)

# 初始化向量库和检索器
print("初始化向量数据库...")
vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 40})
print("向量库文档总数:", vectorstore._collection.count())

# 初始化 LLM（支持 OpenAI 兼容端点）
llm = ChatOpenAI(
    model=os.getenv("MODEL", "deepseek-chat"),
    temperature=0.1,
    api_key=os.getenv("ARK_API_KEY") or os.getenv("ARK_API_KEY"),
    base_url=os.getenv("ARK_BASE_URL") or os.getenv("ARK_BASE_URL"),
)

# RAG 提示模板
system_prompt = """你是一个专业的面试官助手。根据以下提供的面试心得内容回答问题。
严格基于上下文回答，如果上下文没有相关信息，请说"上下文不足，无法准确回答"。
回答简洁、专业，用中文，5-10 句话即可。

上下文信息：
{context}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{question}"),
])

from langchain_core.runnables import RunnableParallel, RunnableLambda

def debug_context(docs):
    print("\n" + "="*70)
    print(f"【检索到的文档数量】: {len(docs)}")
    if not docs:
        print("【严重警告】检索结果为空 → 向量库无匹配或完全没数据")
    for i, doc in enumerate(docs, 1):
        content_len = len(doc.page_content)
        preview = doc.page_content[:220].replace("\n", " ").strip() + "..." if content_len > 220 else doc.page_content
        print(f"  Doc {i:2d} | {content_len:4d} 字符 | source: {doc.metadata.get('source','未知')}")
        print(f"       {preview}")
    print("="*70 + "\n")
    return docs

# 格式化上下文（过滤空内容 + 加入分隔符）
def format_context(docs):
    contents = [
        doc.page_content.strip()
        for doc in docs
        if hasattr(doc, 'page_content') and doc.page_content.strip()
    ]
    context_str = "\n\n───\n\n".join(contents)
    print(f"最终传入 LLM 的 context 长度: {len(context_str)} 字符")
    if len(context_str) < 20:
        print("context 几乎为空，LLM 很可能回答'上下文不足'")
    return context_str


class DBArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(String)
    tags = Column(String)
    summary = Column(Text)
    content = Column(Text)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ================= 2. Pydantic 数据模型 =================
class ArticleCreate(BaseModel):
    title: str
    tags: List[str]
    summary: str
    content: str


class ArticleResponse(BaseModel):
    id: int
    title: str
    date: str
    tags: List[str]
    summary: str
    content: str


# 登录获取 Token 接口
@app.post("/api/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 校验账号密码
    if form_data.username != ADMIN_USERNAME or form_data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=400, detail="账号或密码错误")

    # 签发 Token，有效期设为 24 小时
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode = {"sub": form_data.username, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": encoded_jwt, "token_type": "bearer"}


# 4. 新增：校验 Token 的依赖函数
def get_current_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username != ADMIN_USERNAME:
            raise HTTPException(status_code=401, detail="无效的管理员")
    except Exception:
        raise HTTPException(status_code=401, detail="登录已过期，请重新登录")
    return username


# 博客文章 API 接口
@app.post("/api/articles", response_model=ArticleResponse)
def create_article(article: ArticleCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_admin)):
    """前端发布新文章接口"""
    date_str = datetime.now().strftime("%Y-%m-%d")

    # 存入 SQLite 数据库 (用于前端页面展示)
    db_article = DBArticle(
        title=article.title,
        date=date_str,
        tags=json.dumps(article.tags),
        summary=article.summary,
        content=article.content
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    # 同步保存为 md 文件，供 AI 面试助手 RAG 使用
    try:
        filename = f"article_{db_article.id}.md"
        # 拼接一个适合 AI 阅读的文档格式
        md_content = f"# {article.title}\n\n{article.content}"
        add_document(filename, md_content)
    except Exception as e:
        print(f"警告: 同步至本地知识库失败: {e}")

    return {
        "id": db_article.id, "title": db_article.title, "date": db_article.date,
        "tags": json.loads(db_article.tags), "summary": db_article.summary, "content": db_article.content
    }


@app.get("/api/articles", response_model=List[ArticleResponse])
def get_articles(db: Session = Depends(get_db)):
    """获取文章列表"""
    articles = db.query(DBArticle).order_by(DBArticle.id.desc()).all()
    return [{"id": a.id, "title": a.title, "date": a.date, "tags": json.loads(a.tags) if a.tags else [],
             "summary": a.summary, "content": a.content} for a in articles]


@app.get("/api/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    """获取单篇文章"""
    a = db.query(DBArticle).filter(DBArticle.id == article_id).first()
    if not a:
        raise HTTPException(status_code=404, detail="文章不存在")
    return {"id": a.id, "title": a.title, "date": a.date, "tags": json.loads(a.tags) if a.tags else [],
            "summary": a.summary, "content": a.content}


from langchain_core.runnables import RunnableLambda

def rerank_step(x):
    """RunnableLambda 包装 rerank 函数"""
    question = x["question"]
    docs = x["docs"]
    reranked = rerank_documents(question, docs, top_k=5)
    return {
        "question": question,
        "docs": reranked
    }

rag_chain = (
    RunnableParallel(
        question=RunnablePassthrough(),
        docs=RunnableLambda(lambda q: hybrid_retrieval(q, k=10))
        # docs=retriever | RunnableLambda(debug_context)
    )
    | RunnableLambda(rerank_step)
    | RunnableLambda(lambda x: {
        "question": x["question"],
        "context": format_context(x["docs"])
    })
    | RunnableLambda(lambda inputs: print("\n=== 实际送进 LLM 的完整 Prompt ===\n")
                     or print(prompt.invoke(inputs).to_string())
                     or print("====================================\n")
                     or inputs)
    | prompt
    | llm
    | StrOutputParser()
)

# 完整 RAG 链
rag_chain = rag_chain  # Simplified since retriever is now in stuff_chain

@app.post("/api/ask")
async def ask_question(question: str = Body(..., embed=True)):
    """提问接口"""
    try:
        answer = rag_chain.invoke(question)
        return {
            "answer": answer,
            "status": "success",
            "sources": len(retriever.invoke(question))  # 检索文档数
        }
    except Exception as e:
        return {
            "answer": f"错误：{str(e)}",
            "status": "error"
        }

@app.get("/api/health")
async def health_check():
    doc_count = get_document_count(DOCS_PATH)
    collection_count = vectorstore._collection.count()
    return {
        "status": "healthy",
        "docs_path": DOCS_PATH,
        "db_path": DB_PATH,
        "local_files": doc_count,
        "vector_count": collection_count,
        "embedding_model": os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    }

@app.post("/api/reload")
async def reload_db():
    """重新加载文档（开发用）"""
    global vectorstore, retriever
    reload_vectorstore()
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    return {"status": "reloaded", "message": "向量库已重新构建"}

# 新增 CRUD API 端点
@app.post("/api/add_document")
async def api_add_document(filename: str = Body(...), content: str = Body(...)):
    """添加新文档"""
    try:
        add_document(filename, content)
        return {"status": "success", "message": f"文档 {filename} 已添加"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/update_document")
async def api_update_document(filename: str = Body(...), content: str = Body(...)):
    """更新文档"""
    try:
        update_document(filename, content)
        return {"status": "success", "message": f"文档 {filename} 已更新"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.delete("/api/articles/{article_id}")
def delete_article_api(article_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    """管理员专用：删除文章并清理 RAG 向量库"""
    # 1. 从数据库查找
    db_article = db.query(DBArticle).filter(DBArticle.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="文章不存在")

    # 2. 调用 crud.py 同步删除向量库和 MD 文件
    try:
        # 假设你的文件名遵循 article_ID.md 格式
        delete_document(f"article_{article_id}.md")
    except Exception as e:
        print(f"向量库同步清理失败: {e}")

    # 3. 从数据库删除
    db.delete(db_article)
    db.commit()
    return {"status": "success", "message": "文章已彻底移除"}

@app.post("/api/delete_document")
async def api_delete_document(filename: str = Body(...)):
    """删除文档"""
    try:
        delete_document(filename)
        return {"status": "success", "message": f"文档 {filename} 已删除"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    print("启动 RAG API 服务...")
    print(f"向量库路径: {DB_PATH}")
    print(f"文档路径: {DOCS_PATH}")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)