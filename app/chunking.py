# from typing import List
# from langchain_core.documents import Document
# from langchain_text_splitters import CharacterTextSplitter
#
# def split_documents(documents: List[Document]) -> List[Document]:
#     """Split documents into chunks, 基于固定大小切分存在问题"""
#     text_splitter = CharacterTextSplitter(
#         chunk_size=400,
#         chunk_overlap=150
#     )
#     return text_splitter.split_documents(documents)


# 按 Markdown 标题层级切分
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


def split_documents(documents: List[Document]) -> List[Document]:
    """
    按 Markdown 标题切分文档。
    1. 首先识别 #, ##, ### 标题并进行物理切分。
    2. 如果切分后的块依然超过阈值，再进行递归字符切分。
    """
    # 定义需要识别的标题层级
    headers_to_split_on = [
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3"),
    ]

    # 配置markdown切分器
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False  # 保留标题在正文中，增强检索时的文本匹配度
    )

    final_chunks = []

    for doc in documents:
        # MarkdownHeaderTextSplitter 接收的是字符串文本
        header_splits = markdown_splitter.split_text(doc.page_content)

        # 进一步对过大的块进行切分，防止超出 LLM 上下文限制, 配置如何对文本进行进一步细分原则
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", "。", "！", "？"]
        )

        for split in header_splits:
            # 继承原始文档的元数据，并合并标题信息
            new_metadata = doc.metadata.copy()
            new_metadata.update(split.metadata)

            # 执行二次切分
            secondary_splits = text_splitter.split_text(split.page_content)
            for text in secondary_splits:
                final_chunks.append(Document(page_content=text, metadata=new_metadata))

    return final_chunks


if __name__ == "__main__":
    # 测试切分功能
    sample_doc = Document(
        page_content="""
        ## 1、TCP/IP模型和OSI模型分别是什么？它们之间有什么区别？

首先OSI模型是ISO组织提出的用于计算机通信互联的标准体系，分为七层，自下而上，分别是物理层，数据链路层，网络层，传输层，会话层，表示层、应用层。虽然OSI模型在理论上更加全面，但是在实际的应用中更常见的是TCP/IP的四层模型，自下而上分别是网络接口层，网络层、传输层、应用层。

其中TCP/IP的**应用层**对应于OSI模型的**会话层、表示层以及应用层**，主要提供与用户应用程序交互的接口，例如http，电子邮件等；

**传输层**对应于OSI模型的传输层，**负责端到端的通信，即进程到进程的通信**，提供面向连接的**可靠TCP通信服务**和无连接的不可靠的UDP通信服务。都具备差错检测的能力，TCP检错之后通知发送方重传，而UDP直接丢弃且不通知发送方。TCP确保数据正确完整，但是开销大，实时性差，传文件用**TCP**，UDP数据可能存在错误或者丢失。

### 追问：传输层有哪些协议？

**传输层最核心的协议是TCP和UDP**，解释TCP和UDP的区别和联系

> **TCP的三次的握手和四次挥手**
>
> ==**三次握手(建立连接)**==
>
> **客户端向服务器**发送 `SYN` 包(同步请求)  --> SYN的同步标志
>
> 服务器回应 `SYN`+`ACK` 包(确认收到请求)  -->ACK的确认标志
>
> 客户端再发送 `ACK` 包(确认响应)，连接建立
>
> ==**四次挥手(断开连接)**==
>
> 客户端向服务器发送`FIN`包(请求结束)
>
> 服务器向客户端回应`ACK`包(确认收到请求)
>
> 服务器向客户端发送`FIN`包(结束连接请求)
>
> 客户端向服务器发送`ACK`包,连接关闭

**网络层**对应于OSI模型的网络层，主要负责**主机到主机的通信**，主要的协议**是IP协议**。主要的功能分为三块：第一是**异构网络互连**，就是把不同类型的主机，不同结构的网络都连接起来。第二是**路由和转发**，路由就是不同路由器之间相互配合，规划IP数据报的最佳路径；转发就是路由器根据自己的转发表，把IP数据报从合适的接口发出去。第三是**拥塞控制**，也就是当网络上正在传输的IP数据报过多，导致网络性能下降时进行调控。

### 追问：网络层的协议有哪些？

在网络层最核心的协议是**IP协议**，它的作用是负责**逻辑寻址** (**给每台机器一个IP地址**) 和**路由选择**（**决定数据包走哪条路**），**IPv4**是32位地址，点分十进制表示。 **IPv6**是**128位地址**，用**冒号十六进制**表示。

其次还有**ICMP协议（诊断与控制协议）**，它的作用是: 用于在**IP主机和路由器**之间传递控制信息，**如果数据包发不出去、网络堵了、或者主机不可达**，路由器会用**ICMP**告诉**==发送方==**。 `ping`的底层原理就是**发送ICMP请求，并等待ICMP响应**。

**ARP (地址解析协议)**：连接**网络层（IP）和物理链路层（MAC）**的桥梁，它的作用是**将IP地址解析为MAC地址**。

### 追问：`ping`的原理是什么？

`ping`的底层是**通过ICMP协议**实现的，**通过发送ICMP请求并接收ICMP响应实现的**。

**网络层 = IP（核心） + ICMP（查错） + ARP（找物理地址） + 路由协议（找路）**

**网络接口层**对应于OSI模型的物理层和数据链路层，负责相邻节点之间的通信。它把数据封装成帧，在物理介质上传输，并提供错误检测和纠正的功能。



## 2、从输入URL到页面展示到底发生了什么？

从输入URL到页面展示发生的过程主要从以下几个方面进行阐述：

1、**URL是统一资源定位符**，即我们在浏览器页面输入的网址，浏览器会解析网址，并判断网址是否合法和完整；同时会检查浏览器缓存中是否有缓存该资源，如果有直接返回，如果没有则进行**网络请求**

2、**DNS域名解析**：在进行网络请求前，我们需要将用户输入的域名解析为IP地址，**因为用户往往输入的是域名**，比较容易记住，比如，baidu, 而主机之间的通信是**通过IP协议进行**的。DNS解析会按照本地浏览器缓存，本地host文件，路由器缓存，DNS服务器，根DNS服务器的顺序查询域名对应IP地址。

3、**TCP三次握手建立连接**：浏览器使用DNS解析后的IP地址，与服务器通过三次握手建立连接，如果是**==Https==**的话，还涉及到**TLS/SSL**加密过程。

4、**浏览器向客户端发送Http请求**：连接建立后，浏览器会构建**请求行、请求头**等信息，**向服务器发送请求信息，请求特定的资源**，比如HTML网页、图像等。① 这些请求**在应用层**生成，往下经过**传输层加TCP头**，**网络层加IP头**，**数据链路层加MAC层**。

5、**服务器处理请求和响应**：Http请求**通常先到达Nginx**反向代理服务器，Nginx进行解密、负载均衡之后发送到一台服务器，服务器接收浏览器发送的请求信息，通过对请求信息进行解析和处理，将处理之后的结果封装到**HTTP响应**中，发送给浏览器

6、**浏览器解析响应**：浏览器接收到HTTP响应，解析其中的内容，如果响应中包含HTML，浏览器会解析HTML以构建DOM（文档对象类型），如果HTML中引用了其他资源，如CSS，图像等，浏览器会发送额外的请求获取资源。**如果响应的响应头状态码为301，302会重定向到新地址**

7、TCP四次挥手断开连接：**浏览器与服务器断开TCP连接**。



## 3、HTTP请求报文和响应报文是怎样的？包含哪些常见字段

**==HTTP请求报文==**主要由**请求行**、**请求头**、**空行**、**请求体**构成。

**请求行**主要包含：

1. 请求的方法，Get或者Post等；
2. 请求的资源：URL；
3. HTTP版本号，HTTP 1.1或者HTTP 2.0

请求头（header）主要包含：

1. **请求服务器的域名,host；**
2. 请求体的数据类型，Content-Type, 在中控实习定义的接口一般使用 **json** 格式传输; 
3. 请求体的长度，Content-Length；
4. 存储在客户端的cookie数据

空行是**请求头和请求体**之间的空行，用于分割**请求头和请求体**

请求体通常用于post请求，包含发送给服务器的数据

```http
GET \ POST /login HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

username=test&password=123
```



**==HTTP响应报文==**主要由状态行，响应头，空行、响应体构成

状态行包含：

1. HTTP版本号，http1.1或者http2.0；
2. 状态码，常见的状态码有200，表示成功；301，302表示重定向；404表示客户端错误，请求资源不存在； 500表示服务器异常
3. 状态描述，对状态码的描述

响应头，以键值对的形式提供额外信息，主要包含：

1. 响应体的数据类型：content-type;
2. 响应体的长度：content-length;
3. 重定向时的指定新资源的位置：Location;

空行是**状态行和响应头**之间的空行，表示响应头的结束

响应体是服务器端传递给客户端的实际数据

```http
 HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Server: nginx

<html>...</html>
```



## 4、HTTP有哪些请求方式

**get请求，用于获取指定资源**

**post请求，向指定资源提交数据，服务器接收数据以处理请求**

**put请求, 更新指定资源**

**Delete请求，删除指定资源**

**head请求**，获取报文的首部，只需要获取部分信息，不需要知道具体内容

**options请求**，查询服务器支持的请求方法

**patch请求**，对资源进行部分更新，这里只修改一部分""",
        metadata={"source": "interview_notes.md"}
    )

    chunks = split_documents([sample_doc])
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk.page_content}\n---\n")